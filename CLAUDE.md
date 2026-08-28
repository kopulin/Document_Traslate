# CLAUDE.md — Document_Traslate

這是 Claude 的 agent 指令檔。父層共用規則見 [`/Projects/CLAUDE.md`](../CLAUDE.md)，本檔補充本專案專屬規則。
Codex／其他 agent 讀 [`AGENTS.md`](AGENTS.md)，兩份以本檔為準。

---

## 專案定位

**用途：** 專門存放翻譯文件。把英文原版文件（PDF）逐章翻譯成繁體中文，交付格式為 Markdown。
**Git Remote：** `https://github.com/kopulin/Document_Traslate.git`（repo 名沿用 GitHub 既有拼寫，勿改）

### 範圍邊界

| 屬於本 repo | 不屬於本 repo |
|---|---|
| 原始 PDF、逐章 `.md` 譯文、圖片素材、翻譯術語表 | 對外發佈用的網站程式碼 |
| 翻譯流程與品質規則 | HTML 生成器、樣式、部署設定 |

**發佈拆分：** 未來若把譯文做成 HTML 發佈到網路上，發佈用的程式碼與資產放**另一個獨立 repo**，本 repo 只維護「內容真實來源（source of truth）」的 Markdown。

---

## 主要文件

| 文件 | 用途 |
|------|------|
| [AGENTS.md](AGENTS.md) | 逐章進度表、命名慣例、翻譯規則（給所有 agent） |
| [DEVLOG.md](DEVLOG.md) | 開發紀錄，接手時先讀最新一則 |

---

## Claude 的工作規則

1. 執行任何 git 指令前先 `pwd` 確認在本資料夾，`git remote -v` 尾段須為 `Document_Traslate.git`。
2. 一次處理一章，翻完等使用者驗收再繼續。
3. 每次收工前更新 [AGENTS.md](AGENTS.md) 進度表與 [DEVLOG.md](DEVLOG.md)。
4. 術語或語意有疑義時停下來問，不自行假設。
5. 不在本 repo 加入發佈用的網站程式碼。
