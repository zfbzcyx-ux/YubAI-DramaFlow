const { contextBridge, ipcRenderer } = require('electron');

// Expose protected methods to the renderer process
contextBridge.exposeInMainWorld('electronAPI', {
  // App info
  getAppVersion: () => ipcRenderer.invoke('get-app-version'),
  checkForUpdates: () => ipcRenderer.invoke('check-for-updates'),

  // Shell
  openExternal: (url) => ipcRenderer.invoke('open-external', url),

  // Dialogs
  showSaveDialog: (options) => ipcRenderer.invoke('show-save-dialog', options),
  showOpenDialog: (options) => ipcRenderer.invoke('show-open-dialog', options),

  // Storage (local encrypted store)
  storeGet: (key) => {
    try {
      const val = localStorage.getItem('yubai_' + key);
      return val ? JSON.parse(val) : null;
    } catch { return null; }
  },
  storeSet: (key, value) => {
    localStorage.setItem('yubai_' + key, JSON.stringify(value));
  },
  storeRemove: (key) => {
    localStorage.removeItem('yubai_' + key);
  },

  // Update events
  onUpdateProgress: (callback) => {
    ipcRenderer.on('update-progress', (event, percent) => callback(percent));
  },
});
