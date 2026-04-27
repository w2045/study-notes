# 基础工具 · 第五章 · VS Code 高效技巧

← 前置: [04 — Git 版本控制基础](../04-Git版本控制基础/notes.md)
→ 延伸: [06 — 命令行基础](../06-命令行基础/notes.md)

---

## 1. 为什么花时间学编辑器？

你每天花在编辑器里的时间比任何其他工具都多。花 30 分钟学快捷键和技巧，之后每天能省下大量时间。VS Code 是目前最流行的代码/文档编辑器，免费、跨平台、插件丰富。

---

## 2. 命令面板 — 一切操作的入口

| 平台 | 快捷键 |
|------|--------|
| macOS | `Cmd + Shift + P` |
| Ubuntu / Windows | `Ctrl + Shift + P` |

命令面板可以搜索并执行 **所有** VS Code 操作——不用记菜单位置，只需要记住这一个快捷键。输入关键字即可：`theme`、`format`、`terminal`、`zoom`。

---

## 3. 编辑快捷键

### 3.1 光标操作

| 操作 | macOS | Ubuntu / Windows |
|------|-------|-------------------|
| 行首/行尾 | `Cmd + ←/→` | `Home / End` |
| 按词跳转 | `Alt + ←/→` | `Ctrl + ←/→` |
| 选中整行 | `Cmd + L` | `Ctrl + L` |
| 向上/下复制行 | `Alt + Shift + ↑/↓` | `Alt + Shift + ↑/↓` |
| 删除整行 | `Cmd + Shift + K` | `Ctrl + Shift + K` |
| 移动行 | `Alt + ↑/↓` | `Alt + ↑/↓` |

### 3.2 多光标（最强大的功能）

| 操作 | 快捷键 |
|------|--------|
| 在任意位置加光标 | `Alt + Click` |
| 向上/下加光标 | `Cmd + Alt + ↑/↓`（macOS）`Ctrl + Alt + ↑/↓`（Win/Linux） |
| 选中所有相同词 | `Cmd + D` 逐个添加 |
| 选中文件中全部相同词 | `Cmd + Shift + L` |

**典型场景**：你有 10 个变量 `old_name`，要全部改成 `new_name`。选中第一个 → `Cmd+Shift+L` 全选 → 直接打字替换。1 秒搞定。

### 3.3 查找与替换

| 操作 | macOS | Ubuntu / Windows |
|------|-------|-------------------|
| 文件内查找 | `Cmd + F` | `Ctrl + F` |
| 文件内替换 | `Cmd + Alt + F` | `Ctrl + H` |
| 全局搜索 | `Cmd + Shift + F` | `Ctrl + Shift + F` |
| 跳转到文件 | `Cmd + P` | `Ctrl + P` |
| 跳转到符号 | `Cmd + Shift + O` | `Ctrl + Shift + O` |

---

## 4. 文件与标签页

| 操作 | macOS | Ubuntu / Windows |
|------|-------|-------------------|
| 快速打开文件 | `Cmd + P` | `Ctrl + P` |
| 关闭当前标签 | `Cmd + W` | `Ctrl + W` |
| 切换标签 | `Cmd + Tab`（按编号） | `Ctrl + Tab` |
| 侧边栏开关 | `Cmd + B` | `Ctrl + B` |
| 终端开关 | `` Ctrl + ` `` | `` Ctrl + ` `` |
| 分屏 | `Cmd + \` | `Ctrl + \` |

`Cmd + P` 是最常用的快捷键之一——输入文件名模糊匹配，直接跳转，比在侧边栏翻找快得多。

---

## 5. 终端集成

VS Code 内置终端，不用切换窗口。终端默认使用你的系统 Shell（macOS = zsh，Ubuntu = bash）。

| 操作 | 快捷键 |
|------|--------|
| 打开/关闭终端 | `` Ctrl + ` ``（所有平台） |
| 新建终端 | `` Ctrl + Shift + ` `` |
| 在终端中运行选中文本 | `Cmd + Shift + Enter` |

**典型使用**：编辑器在左边，终端在下面——写完代码立刻在终端跑测试。

---

## 6. Markdown 专属技巧

| 操作 | 快捷键 |
|------|--------|
| 预览（内置） | `Cmd/Ctrl + Shift + V` |
| 预览（支持 LaTeX） | `Cmd/Ctrl + K V` |
| 加粗 | `Cmd/Ctrl + B` |
| 斜体 | `Cmd/Ctrl + I` |
| 切换编辑/预览 | `Cmd/Ctrl + Shift + V` |

---

## 7. LaTeX 专属技巧

| 操作 | 快捷键 |
|------|--------|
| 编译 | 保存即编译（`Cmd/Ctrl + S`） |
| 查看 PDF | `Cmd/Ctrl + Alt + V` |
| 正向搜索（源码→PDF） | `Cmd/Ctrl + Alt + J` |
| 反向搜索（PDF→源码） | `Cmd/Ctrl + Click` PDF 中 |

更多设置在 VS Code 中搜 `latex-workshop` 扩展设置。

---

## 8. 推荐设置

在 `settings.json` 中调整这些（直接打开 `Cmd+Shift+P` → `Preferences: Open Settings (JSON)`）：

```json
{
    "editor.fontSize": 18,           // 字体大小
    "editor.minimap.enabled": false,  // 关掉缩略图（省空间）
    "editor.renderWhitespace": "none",
    "files.autoSave": "onFocusChange" // 失焦自动保存
}
```

---

## 9. 推荐扩展

| 扩展 | 用途 |
|------|------|
| Markdown Preview Enhanced | 渲染 LaTeX 公式的 Markdown 预览 |
| LaTeX Workshop | LaTeX 编译 + PDF 预览 |
| Python (Microsoft) | Python 语法高亮、补全 |
| GitLens | 增强 Git 功能（看每行是谁改的） |
| Git Graph | Git 历史可视化 |

安装：`Cmd/Ctrl + Shift + P` → `Extensions: Install Extensions` → 搜索扩展名。

---

## 本章核心概念速查

| 功能 | 快捷键 |
|------|--------|
| 命令面板 | `Cmd/Ctrl + Shift + P` |
| 快速打开文件 | `Cmd/Ctrl + P` |
| 全局搜索 | `Cmd/Ctrl + Shift + F` |
| 多光标 | `Alt + Click` / `Cmd/Ctrl + D` |
| 终端 | `` Ctrl + ` `` |
| Markdown 预览 | `Cmd/Ctrl + K V` |
| LaTeX 预览 | `Cmd/Ctrl + Alt + V` |
