#!/usr/bin/env python3
"""Upload Electron artifacts to GitHub Release."""
import json
import os
import urllib.parse
import urllib.request

GITHUB_TOKEN = os.environ.get('GITHUB_TOKEN', '')
REPO = os.environ.get('GITHUB_REPOSITORY', '')
VERSION = os.environ.get('VERSION', '')
RELEASE_ID = os.environ.get('RELEASE_ID', '')

def gh_api(method, path, data=None):
    url = f'https://api.github.com{path}'
    headers = {
        'Authorization': f'token {GITHUB_TOKEN}',
        'Accept': 'application/vnd.github.v3+json',
        'User-Agent': 'YubAI-Release/1.0',
    }
    req = urllib.request.Request(url, method=method, headers=headers)
    if data:
        req.add_header('Content-Type', 'application/json')
        req.data = json.dumps(data).encode()
    with urllib.request.urlopen(req, timeout=60) as r:
        return json.loads(r.read())

def upload_asset(release_id, filepath):
    filename = os.path.basename(filepath)
    filesize = os.path.getsize(filepath)
    print(f"Uploading {filename} ({filesize//1024//1024}MB)...")

    encoded_name = urllib.parse.quote(filename)
    url = f'https://uploads.github.com/repos/{REPO}/releases/{release_id}/assets?name={encoded_name}'
    headers = {
        'Authorization': f'token {GITHUB_TOKEN}',
        'Content-Type': 'application/octet-stream',
        'Content-Length': str(filesize),
    }

    with open(filepath, 'rb') as f:
        data = f.read()

    req = urllib.request.Request(url, method='POST', headers=headers, data=data)
    with urllib.request.urlopen(req, timeout=300) as r:
        result = json.loads(r.read())
        print(f"  OK {filename}")

# Find all installer files (skip blockmap)
extensions = ['.AppImage', '.exe', '.dmg']
found = []
for root, dirs, files in os.walk('artifacts'):
    for file in files:
        if any(file.endswith(ext) for ext in extensions):
            found.append(os.path.join(root, file))

print(f"Found {len(found)} installer files:")
for f in found:
    size = os.path.getsize(f) // 1024 // 1024
    print(f"  {f} ({size}MB)")

# Find or create release
if not RELEASE_ID:
    releases = gh_api('GET', f'/repos/{REPO}/releases')
    existing = [r for r in releases if r['tag_name'] == VERSION]
    if existing:
        RELEASE_ID = existing[0]['id']
        print(f"Found existing release {RELEASE_ID}")
    else:
        release = gh_api('POST', f'/repos/{REPO}/releases', {
            'tag_name': VERSION,
            'name': f'YubAI DramaFlow {VERSION}',
            'draft': False,
            'prerelease': False,
        })
        RELEASE_ID = release['id']
        print(f"Created release {RELEASE_ID}")

print(f"Uploading to release ID: {RELEASE_ID}")

# Upload all found files
for filepath in found:
    try:
        upload_asset(RELEASE_ID, filepath)
    except Exception as e:
        print(f"  FAIL {os.path.basename(filepath)}: {e}")

print("\nDone!")
