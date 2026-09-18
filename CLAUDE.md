# CLAUDE.md — Document_Traslate

這是 Claude 的 agent 指令檔。父層共用規則見 [`/Projects/CLAUDE.md`](../CLAUDE.md)，本檔補充本專案專屬規則。
Codex／其他 agent 讀 [`AGENTS.md`](AGENTS.md)，兩份以本檔為準。

---

## 專案定位

**用途：** 存放翻譯文件，並把譯文發佈為線上可查閱的靜態網站。把英文原版文件（PDF）逐章翻譯成繁體中文（交付格式 Markdown），再以 VitePress 打包成網站，部署到 GitHub Pages。
**Git Remote：** `https://github.com/kopulin/Document_Traslate.git`（repo 名沿用 GitHub 既有拼寫，勿改）

### 範圍邊界

| 屬於本 repo | 不屬於本 repo |
|---|---|
| 原始 PDF、逐章 `.md` 譯文、圖片素材、翻譯術語表 | 非本專案要翻譯的其他文件 |
| 翻譯流程與品質規則 | 後端服務、資料庫、任何動態功能 |
| VitePress 網站程式（`docs/`、主題、`package.json`、部署 workflow） | |

**發佈方式（2026-08-29 決策，取代舊「發佈拆分／另開 repo」規則）：**
譯文網站與翻譯內容**放同一個 repo**，比照 [`/Projects/tccc-notes/`](../tccc-notes/) 的 VitePress 架構：

- `docs/` 為 VitePress 根；`docs/atp-4-02.11/*.md` 為逐章譯文的 canonical 位置
- `docs/public/images/` 放圖，`docs/.vitepress/` 放設定與主題（IBM Carbon 風格，直接沿用 tccc-notes 的 `custom.css`）
- 原始 PDF 留在 `ATP_4-02.11/`，**不進 `docs/`**（不打包進網站）
- GitHub Actions 自動 build 並部署到 GitHub Pages（沿用 `deploy-to-github-pages` skill）

單一事實來源（source of truth）＝`docs/` 內的 Markdown 與圖片。

---

## 主要文件

| 文件 | 用途 |
|------|------|
| [AGENTS.md](AGENTS.md) | 逐章進度表、命名慣例、翻譯規則（給所有 agent） |
| [DEVLOG.md](DEVLOG.md) | 開發紀錄，接手時先讀最新一則 |

---

## 專案結構（發佈架構定案後）

```
Document_Traslate/
├─ ATP_4-02.11/…_March_2026.pdf        原始 PDF（source，不進網站）
├─ docs/                               VitePress 根
│  ├─ index.md                         首頁（hero + 章節卡片 + 版本免責橫幅）
│  ├─ atp-4-02.11/                     逐章譯文 .md（canonical，slug 檔名）
│  ├─ public/images/atp-4-02.11/       圖檔（fig-<章>-<序>.png）
│  └─ .vitepress/
│     ├─ config.ts                     側欄、local 中文搜尋、base 路徑
│     └─ theme/{index.ts,custom.css}   IBM Carbon 主題
├─ .github/workflows/deploy.yml        GitHub Pages 自動部署
└─ package.json                        vitepress 依賴
```

**狀態（2026-08-29 第七場）：** 逐章 `.md` 已全數搬入 `docs/atp-4-02.11/`（slug 檔名 + frontmatter），VitePress 網站已架好（`config.ts`／`index.md`／主題／`deploy.yml`／`package.json`），`npm run docs:build` 通過。過渡期結束，canonical 位置即 `docs/`。剩 GitHub Pages 首次啟用與 P3（術語表、逐章驗收）。

---

## Claude 的工作規則

1. 執行任何 git 指令前先 `pwd` 確認在本資料夾，`git remote -v` 尾段須為 `Document_Traslate.git`。
2. 一次處理一章，翻完等使用者驗收再繼續。
3. 每次收工前更新 [AGENTS.md](AGENTS.md) 進度表與 [DEVLOG.md](DEVLOG.md)。
4. 術語或語意有疑義時停下來問，不自行假設。
5. 網站程式（VitePress／`docs/`／部署設定）比照 [`/Projects/tccc-notes/`](../tccc-notes/)；改動前先看該專案作法與 `deploy-to-github-pages` skill。
6. 一次只推進一個階段（翻譯／圖片工序／架站／驗收），做完等使用者驗收再進下一階段。
