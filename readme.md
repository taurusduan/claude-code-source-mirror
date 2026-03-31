# Claude Code 泄露完整版客户端源码镜像

<div align="center">

**🔍 深入理解 AI 编程工具的完整客户端实现**

一份从公开 npm 包恢复的 Claude Code 完整源码 · 51 万行代码 · 可运行 · 适合学习

> 本仓库的所有文档均由 Claude Code 生成 —— 我在分析我自己的源码 😄

</div>

---

> **⚠️ 重要声明**
>
> 非官方、无官方支持，仅供研究、文档整理与学习参考。
>
> 本仓库与 Anthropic 无关。若你要正常使用 Claude Code，请优先参考官方产品、官方文档和官方仓库。

## 🌟 为什么要看这个仓库

- **完整性**：51 万行真实生产代码，覆盖 CLI、工具系统、MCP、Bridge、权限、UI 等完整客户端
- **可运行**：已补齐依赖和配置，可以真正启动和调试
- **中文友好**：面向中文开发者的详细文档和学习路径
- **学习价值**：罕见的头部 AI 编程产品完整客户端实现样本

## 📚 文档导航

| 文档                                             | 适合谁         | 内容                           |
| ------------------------------------------------ | -------------- | ------------------------------ |
| [RUNNING_SETUP.md](./RUNNING_SETUP.md)           | 想把项目跑起来 | 依赖补齐、兼容修复、启动方式   |
| [SOURCE_STUDY_GUIDE.md](./SOURCE_STUDY_GUIDE.md) | 想系统学习源码 | 架构总览、核心子系统、阅读路径 |
| [LEARNING_PATH.md](./LEARNING_PATH.md)           | 想要学习路线图 | 入门/进阶/专题路径、检查清单   |
| [EVENT_STORY.md](./EVENT_STORY.md)               | 想了解事件背景 | 时间线、传播过程、社区讨论     |
| [FAQ.md](./FAQ.md)                               | 遇到问题       | 常见问题解答                   |

---

### 目录

- [项目定位](#项目定位)
- [适合谁阅读](#适合谁阅读)
- [文档导航](#文档导航)
- [快速事实](#快速事实)
- [如何运行项目](#如何运行项目)
- [如何阅读这个仓库](#如何阅读这个仓库)
- [相关公开资料](#相关公开资料)
- [免责声明](#免责声明)

## 📦 项目定位

这是一份从公开 npm 包 `@anthropic-ai/claude-code@2.1.88` 的 source map 恢复的**完整客户端源码镜像**。

**来源验证：**

- npm 包中包含 59.8MB 的 `cli.js.map`
- 包含 4756 个源文件的完整 `sourcesContent`
- 已补齐依赖和配置，可直接运行

**包含内容：**

- ✅ 完整客户端源码（CLI、工具、UI、MCP、Bridge 等）
- ✅ 可运行的开发环境配置
- ✅ 详细的中文学习文档

**不包含内容：**

- ❌ Claude 模型权重和训练数据
- ❌ Anthropic 后端服务代码
- ❌ 官方支持和更新

## 🎯 两条路径

### 路径 1：快速上手（10 分钟）

1. 阅读本页"快速事实"了解项目规模
2. 跳转 [RUNNING_SETUP.md](./RUNNING_SETUP.md) 查看三行命令启动
3. 运行 `bun run start` 体验交互界面

### 路径 2：深入学习（系统性）

1. 阅读 [EVENT_STORY.md](./EVENT_STORY.md) 了解事件背景
2. 阅读 [SOURCE_STUDY_GUIDE.md](./SOURCE_STUDY_GUIDE.md) 理解架构
3. 选择一条学习路径深入源码

---

## 👥 适合谁

**✅ 适合：**

- AI 编程工具开发者和研究者
- 想学习大型 TypeScript/React 项目架构的工程师
- 对 Agent、MCP、工具系统感兴趣的开发者
- 需要参考资料做技术分享或课程的讲师

**❌ 不适合：**

- 寻求官方支持和稳定生产环境的用户
- 期望获得模型权重或训练数据的研究者

## 📊 快速事实

| 维度         | 数据                                             |
| ------------ | ------------------------------------------------ |
| **源码规模** | 512,685 行代码 · 1,884 个 TS/TSX 文件            |
| **来源**     | `@anthropic-ai/claude-code@2.1.88` 的 source map |
| **状态**     | ✅ 可运行 · ✅ 已补齐依赖 · ✅ 中文文档          |
| **核心内容** | CLI · 工具系统 · MCP · Bridge · 权限 · UI        |

## 🚀 快速开始

### 三行命令启动

```bash
cd /Users/tools/Music/cc/claude-codes
bun install
bun run start
```

> 💡 首次启动会显示工作区信任确认，详细说明见 [RUNNING_SETUP.md](./RUNNING_SETUP.md)

### 其他常用命令

```bash
# 查看版本
bun run start --version

# 查看帮助
bun run start --help

# 格式化代码
bun run format
```

## 📖 学习建议

**第一次接触？** 建议顺序：

1. 阅读本页了解项目边界
2. 选择”快速上手”或”深入学习”路径
3. 查看 [EVENT_STORY.md](./EVENT_STORY.md) 了解事件背景（可选）

**有使用经验？** 直接跳转：

- 运行细节 → [RUNNING_SETUP.md](./RUNNING_SETUP.md)
- 源码结构 → [SOURCE_STUDY_GUIDE.md](./SOURCE_STUDY_GUIDE.md)

## 🔗 相关资源

### 官方资源

- [Anthropic 官方产品页](https://www.anthropic.com/claude-code)
- [官方文档](https://docs.anthropic.com/en/docs/agents-and-tools/claude-code/overview)
- [官方 GitHub](https://github.com/anthropics/claude-code)
- [Introducing Claude 4 公告](https://www.anthropic.com/news/claude-4)

### 社区镜像仓库

- [nirholas/claude-code](https://github.com/nirholas/claude-code) - 增强文档版
- [pengchengneo/Claude-Code](https://github.com/pengchengneo/Claude-Code) - 可运行版
- [chatgptprojects/claude-code](https://github.com/chatgptprojects/claude-code) - 提取展示版

### 事件讨论

- [Chaofan Shou on X](https://x.com/Fried_rice/status/2038894956459290963?s=20)
- [Reddit r/ClaudeAI 讨论](https://www.reddit.com/r/ClaudeAI/comments/1s8lkkm/i_dug_through_claude_codes_leaked_source_and/)
- [Reddit r/LocalLLaMA 讨论](https://www.reddit.com/r/LocalLLaMA/comments/1s8ijfb/claude_code_source_code_has_been_leaked_via_a_map/)

## 🆚 本仓库的特色

与其他社区仓库相比，本仓库的独特价值：

| 特点         | 本仓库                      | 其他仓库       |
| ------------ | --------------------------- | -------------- |
| **中文文档** | ✅ 完整的中文学习指南       | 多为英文       |
| **可运行性** | ✅ 已补齐依赖，可直接启动   | 部分仅展示源码 |
| **文档结构** | ✅ 分层清晰：运行/学习/事件 | 单一 README    |
| **学习路径** | ✅ 提供多条阅读路径         | 较少学习指导   |
| **事件背景** | ✅ 详细的事件时间线         | 较少背景说明   |

## 📋 免责声明

本仓库中的代码、命名、提示词、实现细节及相关知识产权归其原始权利人所有。此镜像仓库及 README 仅用于：

- 研究
- 文档整理
- 架构学习
- 安全与产品分析

如果你需要实际使用 Claude Code，请优先选择 Anthropic 的官方产品、官方文档和官方仓库。
