# AGENTS.md — Document_Traslate

軍事／技術文件翻譯專案。任何 agent 接手前先讀完本文件。
完整規則見 [`CLAUDE.md`](CLAUDE.md)，父層共用規則見 [`/Projects/CLAUDE.md`](../CLAUDE.md)；衝突時以 `CLAUDE.md` >父層為準。

---

## 專案定位

**產品：** 把英文原版文件（PDF）逐章翻譯成繁體中文 Markdown，並保留原書的圖片與版面對應關係。
**範圍：** 本 repo 只放翻譯內容（PDF、`.md` 譯文、圖片、術語表）。未來對外發佈的 HTML／網站程式碼放另一個獨立 repo，本 repo 是內容的單一事實來源。
**Git Remote：** `https://github.com/kopulin/Document_Traslate.git`（repo 名沿用 GitHub 上的既有拼寫，勿改）
**語言：** 所有回覆與交付文件使用繁體中文，專有名詞、軍語、藥名保留英文原文並在首次出現時加註中文。

---

## 目前進度

| 文件 | 位置 | 狀態 |
|------|------|------|
| ATP 4-02.11《Casualty Response (TCCC and First Aid)》 | [`ATP_4-02.11/`](ATP_4-02.11/) | 翻譯中 |
| TC 3-21.76《Ranger Handbook》 | [`TC_3-21.76/`](TC_3-21.76/) | 翻譯中（Ch01–Ch14） |

ATP 4-02.11 章節：

| 章 | 檔案 | 狀態 |
|----|------|------|
| Ch01 | Casualty Response（印刷頁 1–22） | **未翻譯** |
| Ch02 | Casualty Extraction and Movement（印刷頁 23–26） | **未翻譯** |
| Ch03 | Fundamentals of TCCC（印刷頁 27–42） | **未翻譯｜優先補譯** |
| Ch04 | `ATP_4-02.11_Ch04_大量出血控制_zh-TW.md` | 已翻譯 |
| Ch05 | `ATP_4-02.11_Ch05_呼吸道控制_zh-TW.md` | 已翻譯 |
| Ch06 | `ATP_4-02.11_Ch06_呼吸與換氣控制_zh-TW.md` | 已翻譯 |
| Ch07 | `ATP_4-02.11_Ch07_循環控制_zh-TW.md` | 已翻譯 |
| Ch08 | `ATP_4-02.11_Ch08_低體溫控制_zh-TW.md` | 已翻譯 |
| Ch09 | `ATP_4-02.11_Ch09_二次傷勢評估_zh-TW.md` | 已翻譯 |
| Ch10 | `ATP_4-02.11_Ch10_眼部創傷_zh-TW.md` | 已翻譯 |
| Ch11 | `ATP_4-02.11_Ch11_頭部傷勢_zh-TW.md` | 已翻譯 |
| Ch12 | `ATP_4-02.11_Ch12_燒傷_zh-TW.md` | 已翻譯 |
| Ch13 | `ATP_4-02.11_Ch13_骨折與固定_zh-TW.md` | 已翻譯 |
| Ch14 | `ATP_4-02.11_Ch14_其他二次傷勢的應急技術_zh-TW.md` | 已翻譯 |
| Ch15 | `ATP_4-02.11_Ch15_傷患監測與後送準備_zh-TW.md` | 已翻譯 |
| Ch16 | `ATP_4-02.11_Ch16_叮咬與螫傷_zh-TW.md` | 已翻譯 |
| Ch17 | `ATP_4-02.11_Ch17_氣候與環境傷害_zh-TW.md` | 已翻譯 |
| Ch18 | `ATP_4-02.11_Ch18_鐮刀型血球特徵_zh-TW.md` | 已翻譯 |
| Ch19 | `ATP_4-02.11_Ch19_CBRN環境急救_zh-TW.md` | 已翻譯 |
| Ch20 | `ATP_4-02.11_Ch20_戰鬥與作戰壓力控制_zh-TW.md` | 已翻譯 |
| 附錄 A | 急救包內容清單（印刷頁 217–223） | **未翻譯** |
| 附錄 B | 救援裝備（印刷頁 224–226） | **未翻譯** |

> **進度：17／20 章 + 0／2 附錄　｜　累計約 19.2 萬字**
> ⚠️ **Ch01–Ch03 從未翻譯**（翻譯自 Ch04 起跳），Ch03 為 TCCC 基礎章，後續各章大量引用，建議優先補譯。

原始 PDF：`ATP_4-02.11/ATP_4-02.11_Casualty_Response_TCCC_and_First_Aid_March_2026.pdf`
圖片抽取測試：`ATP_4-02.11/_圖片測試/`

TC 3-21.76 章節（2025 年 9 月 19 日版，共 380 頁；PDF 頁為檔案實際頁碼）：

| 章 | 原書章名 | PDF 頁 | 狀態 |
|----|---------|--------|------|
| 前言 | Preface／Introduction | 17–24 | **未翻譯** |
| Ch01 | Leadership → `TC_3-21.76_Ch01_領導_zh-TW.md` | 25–34 | 已翻譯（術語已驗收） |
| Ch02 | Operations → `TC_3-21.76_Ch02_作戰_zh-TW.md` | 35–80 | 已翻譯，待驗收 |
| Ch03 | Fire Support → `TC_3-21.76_Ch03_火力支援_zh-TW.md` | 81–100 | 已翻譯，待驗收 |
| Ch04 | Communications → `TC_3-21.76_Ch04_通訊_zh-TW.md` | 101–108 | 已翻譯，待驗收 |
| Ch05 | Demolitions → `TC_3-21.76_Ch05_爆破_zh-TW.md` | 109–118 | 已翻譯（特殊處理），待驗收 |
| Ch06 | Movement → `TC_3-21.76_Ch06_行進_zh-TW.md` | 119–136 | 已翻譯，待驗收 |
| Ch07 | Patrols → `TC_3-21.76_Ch07_巡邏_zh-TW.md` | 137–168 | 已翻譯，待驗收 |
| Ch08 | Battle Drills → `TC_3-21.76_Ch08_戰鬥演練_zh-TW.md` | 169–202 | 已翻譯，待驗收 |
| Ch09 | Military Mountaineering → `TC_3-21.76_Ch09_軍事登山_zh-TW.md` | 203–232 | 已翻譯，待驗收 |
| Ch10 | Machine Gun Employment → `TC_3-21.76_Ch10_機槍運用_zh-TW.md` | 233–248 | 已翻譯，待驗收 |
| Ch11 | Urban Operations → `TC_3-21.76_Ch11_城鎮作戰_zh-TW.md` | 249–258 | 已翻譯，待驗收 |
| Ch12 | Waterborne Operations → `TC_3-21.76_Ch12_水上作戰_zh-TW.md` | 259–280 | 已翻譯，待驗收 |
| Ch13 | Mounted Patrol Operations → `TC_3-21.76_Ch13_車載巡邏_zh-TW.md` | 281–296 | 已翻譯，待驗收 |
| Ch14 | Aviation → `TC_3-21.76_Ch14_航空_zh-TW.md` | 297–310 | 已翻譯，待驗收 |
| Ch15 | Tactical Combat Casualty Care | 311–324 | **未翻譯** |
| 附錄 A | Resources | 325–354 | **未翻譯** |
| 附錄 B | Quick Reference Cards | 355–362 | **未翻譯** |
| 書末 | Glossary（詞彙表） | 365–368 | **未翻譯** |
| 書末 | Source Notes／References／Index | 363–364、369–380 | **不翻譯**（保留英文原文） |

> **TC 3-21.76 專屬規則：**
> - **Ch05 爆破**：章節結構、術語、安全注意事項、概念說明照常翻譯；裝藥量公式、起爆系統組裝步驟、爆破操作程序改寫成摘要，並標註原文頁碼供對照。
> - **Ch15 TCCC**：術語沿用 ATP 4-02.11 已拍板的譯法（見 `DEVLOG.md` 2026-08-28 設計師決策 1）。
> - **章末術語表格式（2026-09-18）**：欄位為 `| 原文 | 譯文 | 說明 |`。說明欄只填「使用者指定或修正過的術語」與譯名易誤解者，其餘留空；外部連結另行統一處理，翻譯階段先不加。
> - **職稱與編組（使用者指定）**：platoon sergeant＝**排士官長**、team leader＝**伍長**、fire team＝**火力伍**、medic＝**醫務兵**、range card＝**射界卡**；cloverleaf method＝**四葉草環繞法**；slough＝**盲汊**；long count／short count＝**單人報數／雙人報數**；combat lifesaver (CLS)＝**戰鬥救護員**（階層低於 CMC＝combat medic＝醫務兵；ATP 4-02.11 共 13 處已於 2026-09-18 一併改為此譯名）；machine gun team＝**機槍組**、aid and litter team＝**救護擔架組**（team 只有指步兵火力伍時才譯「伍」）。其餘術語見各章末術語表。

原始 PDF：`TC_3-21.76/TC_3-21.76_Ranger_Handbook_September_2025.pdf`

---

## 檔案與命名慣例

- 每份文件一個資料夾，資料夾名＝文件編號（例：`ATP_4-02.11/`）。
- 譯文檔名：`<文件編號>_Ch<章號>_<章名中文>_zh-TW.md`。
- 原始 PDF 與圖片素材放同一資料夾內；圖片子資料夾用 `_` 前綴（不進最終交付）。
- 章名中文取原書章標題的通用譯法，跨章保持一致。

---

## 翻譯規則

1. **忠實原文**：不增刪內容、不改寫語氣、不加入原文沒有的臨床建議。
2. **軍語與術語**：TCCC、MARCH、TQ、NPA 等縮寫保留英文，首次出現時括號註中文全稱。已拍板的譯法（見 `DEVLOG.md` 2026-08-28 設計師決策 1，例：`Soldier`＝官兵、`Service member`＝服役人員）所有文件共用。
3. **藥名、劑量、單位**：
   - **藥名與藥品劑量**：完全照原文，不換算。
   - **英制單位**（長度、距離、重量、溫度等）：保留原數值，括號內加註公制換算，例：「2 英寸（約 5 公分）」「華氏 104 度（攝氏 40 度）」。
   - 章首譯註須說明「實際操作請以原文數值為準」。
4. **結構對齊**：保留原書的標題階層、編號、表格、警告框（WARNING / CAUTION / NOTE）。
5. **圖片**：原圖保留英文不重繪，圖下補中文圖說，並標注原書頁碼（如 `（原書 p.60）`）。分兩階段——
   - **翻譯階段**：圖片尚未抽出，以文字佔位：`> ［圖 X-X．中文圖說］　原文圖說：Figure X-X. ...`
   - **抽圖階段**（全部文字翻完後統一處理）：以 PyMuPDF 依版面範圍重新渲染（200 dpi PNG），再把佔位改為 `![中文圖說](相對路徑)`＋原書頁碼。
6. **不確定處**：術語或語意有疑義時停下來問使用者，不自行假設。

---

## Agent 工作規則

- 執行任何 git 指令前先 `pwd` 確認在本資料夾，`git remote -v` 尾段必須是 `Document_Traslate.git`。
- 一次處理一章，翻完等使用者驗收再繼續下一章。
- 每次收工前更新本檔的「目前進度」表，或寫入 `DEVLOG.md`。
- 不修改父層 `/Projects/` 的制度檔與 skill。
