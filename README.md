# YubAI DramaFlow

AI漫剧生成客户端 - 基于 Electron 的跨平台桌面应用

## 功能特性

- 🎬 **6阶段AI漫剧工作流**：剧本改写 → 风格定义 → 人物设计 → 场景设计 → 分镜生成 → 视频提示词
- 🤖 **多AI工具支持**：MiniMax（文本生成）+ 火山引擎即梦/小云雀（图片/视频）
- 💰 **平台费抽成**：成本 × 1.3 倍，自动余额扣费
- 🔄 **自动更新**：支持 electron-updater 热更新
- 🌙 **Dark主题UI**：深色护眼设计

## 技术栈

- **Electron 33** - 跨平台桌面框架
- **MiniMax API** - 文本生成（剧本/风格/分镜等）
- **Volcengine 火山引擎** - 即梦图片生成 + 小云雀视频生成
- **FastAPI 后端** - 认证/余额/用量记录

## 开发

```bash
# 安装依赖
npm install

# 开发模式运行
npm start

# 构建安装包
npm run dist          # 全平台
npm run dist -- --linux   # 仅 Linux
npm run dist -- --win     # 仅 Windows
npm run dist -- --mac     # 仅 macOS
```

## 构建产物

| 平台 | 文件 |
|------|------|
| Linux | `YubAI-DramaFlow-x.x.x.AppImage` |
| Windows | `YubAI-DramaFlow-Setup-x.x.x.exe` |
| macOS | `YubAI-DramaFlow-x.x.x.dmg` |

## 配置说明

首次使用需要配置以下 API Key（在客户端设置界面输入）：

1. **MiniMax API Key** - 用于文本生成
   - 获取地址：https://www.minimax.chat/
2. **火山引擎 AK/SK** - 用于图片和视频生成
   - 获取地址：https://console.volcengine.com/

## 客户端下载

- Linux: http://39.107.251.193:8000/client/YubAI-DramaFlow-1.0.0.AppImage
- Windows/macOS: 请从 [Releases](https://github.com/zfbzcyx-ux/YubAI-DramaFlow/releases) 下载

## 管理后台

http://39.107.251.193:8000/admin

账号：`admin` 密码：`admin123`

## 许可证

MIT
