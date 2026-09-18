# 術語總表（跨文件）

> **涵蓋文件**：
> - **TC** — TC 3-21.76《遊騎兵手冊》（Ranger Handbook，2025 年 9 月版）
> - **ATP** — ATP 4-02.11《戰術戰傷救護與急救》（2026 年 3 月版）
>
> **條目數**：1238 條，由兩份譯稿的**章末術語對照表自動彙整**（TC 另含書末詞彙表）。
> **排序**：依原文英文字母（縮寫依字首）。**出處**欄標示文件與章節。
> **產生方式**：`python3 tools/gen_glossary.py`。章末術語表為主檔、本表為產生結果——改譯名請先改章末表再重新產生。
> **單一文件檢視**：TC 3-21.76 另有 `TC_3-21.76/TC_3-21.76_全書術語總表_zh-TW.md`。

---

## 跨文件譯名差異（已處理）

彙整時比對兩份文件的全部術語，共 6 組原文出現不同譯文，處理如下：

| 原文 | 統一譯文 | 原本的另一譯法 | 處理 |
|---|---|---|---|
| CBRN | 化學、生物、**輻射**與核 | 化學、生物、放射性與核 | 使用者指定，TC 附錄 B 與詞彙表共 4 處已改 |
| space blanket | **保暖毯** | 太空毯 | 使用者指定，ATP Ch08 共 2 處已改 |
| acclimatization | 高度（環境）適應／熱適應 | — | 語境不同並存：TC Ch09 登山為高度適應、ATP Ch17 熱傷害為熱適應 |
| DD Form 1380 | DD Form 1380（戰傷救護卡） | 戰術戰傷救護卡（TCCC 卡） | 同義，表單全稱寫法不同，不強制統一 |
| rescue breathing | 人工呼吸 | 人工呼吸（人工換氣） | 同義，括號補充 |
| contusion | 挫傷 | 挫傷（瘀青） | 同義，括號補充 |

---

## 一詞多義與易混淆

| 原文 | 出處 | 譯文 | 說明 |
|---|---|---|---|
| TQ | TC Ch11 | 戰術詢問（tactical questioning） | TC 詞彙表只收錄此義 |
| TQ | TC Ch15、ATP | 止血帶（tourniquet） | 兩份文件的醫療章節同此用法 |
| TQ | TC 附A | 戰術詢問員（tactical questioner） | 執行戰術詢問的人員 |
| cloverleaf | TC Ch07 | 四葉草環繞法 | 偵察技巧（使用者指定譯名） |
| cloverleaf | TC Ch13 | 苜蓿葉型交流道 | 道路工程用語，與上者無關 |
| high carry／low carry | TC Ch11／Ch12 | 高姿／低姿持槍／搬運 | 前者為持槍姿勢，後者為小艇搬運 |
| slough／dead water | TC Ch12 | 盲汊／靜水區 | 前者為盲端支汊，後者為主河道上的無流段 |
| SE | TC Ch07、附A／詞彙表 | 敏感地點蒐證／地點蒐證 | 正文與原文詞彙表全稱不一致 |
| CLS／CMC | TC、ATP | 戰鬥救護員／醫務兵 | CLS 階層低於 CMC（combat medic） |

---

## A

| 原文 | 譯文 | 說明 | 出處 |
|---|---|---|---|
| AA (avenue of approach) | 接近路線 |  | TC Ch2 |
| AAR (after action review) | 行動後檢討 |  | TC Ch11 |
| AAS | 先進抗痙攣系統 | 藥物為咪達唑侖；**不可自行施打** | ATP Ch19 |
| AATFC (air assault task force commander) | 空中突擊特遣部隊指揮官 | 空中突擊作戰的總指揮，統合空中與地面兩方 | TC Ch14 |
| abdominal thrust / Heimlich maneuver | 腹部推擠法 / 哈姆立克法 |  | ATP Ch5 |
| abdominal wound | 腹部傷口 | 傷患採仰臥屈膝姿勢 | ATP Ch14 |
| abrasion | 擦傷 |  | ATP Ch11 |
| abrasion / road rash | 擦傷 / 路面磨擦傷 |  | ATP Ch9 |
| accessory cord | 輔助繩 |  | TC Ch9 |
| acclimatization | 高度（環境）適應 | 預防策略之一 | TC Ch9｜ATP Ch17 |
| ACE (Acknowledge, Care, Escort) | 察覺、關懷、陪同 | 處理 COSR 的三步驟策略 | ATP Ch20 |
| acetaminophen | 乙醯胺酚 | 500 mg × 2，緩釋劑型 | ATP Ch9 |
| acetic / chromic / hydrofluoric acid | 醋酸 / 鉻酸 / 氫氟酸 |  | ATP Ch10 |
| actions on contact | 接觸時的行動 |  | TC Ch6 |
| actions on the objective | 目標區行動 |  | TC Ch1 |
| active warming | 主動保溫 | 具外部熱源 | ATP Ch8 |
| active／passive security | 主動／被動警戒 |  | TC Ch6 |
| adjust fire／fire for effect | 試射／效力射 |  | TC Ch3 |
| ADP (Army doctrine publication) | 陸軍準則出版品 | 僅見於書末詞彙表 | TC 詞彙表 |
| advanced rifle marksmanship | 進階步槍射擊 |  | TC Ch11 |
| after action review (AAR) | 事後檢討 | 72 小時內完成 | ATP Ch15 |
| afterdrop | 後續降溫 | 復溫過程中深部體溫仍持續下降 | ATP Ch17 |
| aggressor | 假想敵 |  | TC Ch2 |
| air assault task force | 空中突擊特遣部隊 | 本章主題 | TC Ch14 |
| air exchange | 氣體交換 |  | ATP Ch5 |
| air guard | 對空監視哨 |  | TC Ch2 |
| air liaison officer | 空軍聯絡官 |  | TC Ch3 |
| air movement plan | 空中運動計畫 |  | TC Ch14 |
| airway obstruction | 呼吸道阻塞 | 分部分／完全 | ATP Ch5 |
| ALARACT 094/2020 | 全陸軍活動通報 094/2020 | 陸軍全員 SCT 篩檢的實施依據 | ATP Ch18 |
| alkali / acid | 鹼 / 酸 | 鹼灼傷更危險，需沖洗 20 分鐘 | ATP Ch10 |
| ALL CLEAR | 安全 | 信號 | TC Ch6 |
| allowable combat load | 允許戰鬥載重 |  | TC Ch13 |
| altitude sickness | 高山症 |  | ATP Ch17 |
| ambient temperature | 環境溫度 |  | ATP Ch12 |
| ambulance exchange point | 救護車交接點 | 第 2 章作「傷患交接點（CXP）」 | TC Ch15 |
| ambulatory / non-ambulatory lane | 可行走 / 不可行走除污通道 |  | ATP Ch19 |
| ambush | 伏擊 |  | TC Ch7 |
| AMC (air mission commander) | 空中任務指揮官 | 兩架以上航空器共同執行任務時設置，通常由任務中的**資深飛行員**擔任，是**依任務指派的戰術指揮職**（非固定職缺）。大型作戰（如空中突擊）中，與 AATFC、GTC 並列為三大核心角色 | TC Ch14 |
| amputation stump | 截肢殘端 |  | ATP Ch9 |
| analgesia | 止痛 |  | ATP Ch12 |
| analgesic | 止痛藥 |  | ATP Ch9 |
| anaphylactic shock / anaphylaxis | 過敏性休克 |  | ATP Ch7 |
| anatomical splint | 解剖式夾板 | 以未受傷的腿當夾板 | ATP Ch13 |
| anchor | 固定點 | 人工／天然；多點 | TC Ch9 |
| anemone | 海葵 | 刺絲胞螫傷 | ATP Ch16 |
| Angle-T | T 角 | 觀測員—目標線與砲目線夾角 | TC Ch3 |
| anterior axillary line | 腋前線 | NDC 部位二 | ATP Ch6 |
| anthrax / smallpox / Ebola | 炭疽 / 天花 / 伊波拉 | CDC A 類 | ATP Ch19 |
| anti-venom | 抗蛇毒血清 |  | ATP Ch16 |
| antihistamine | 抗組織胺 | 口服或外用 | ATP Ch16 |
| AO (area of operations) | 作戰地區 |  | TC Ch2 |
| AOO (actions on objective) | 目標區行動 | 同第 1 章 actions on the objective | TC Ch2 |
| apathetic | 冷漠 |  | ATP Ch20 |
| apathetic / lethargic | 淡漠 / 倦怠 | 低體溫早期徵象 | ATP Ch8 |
| apex (of bandage) | 頂角 | 三角巾的尖端 | ATP Ch14 |
| AR (Army regulation) | 陸軍規則 | 僅見於書末詞彙表 | TC 詞彙表 |
| AR 40-66 / ATP 4-02.2 | 陸軍規則 40-66 / ATP 4-02.2 | DD Form 1380 與 MEDEVAC 的參考文件 | ATP Ch15 |
| arachnid | 蛛形綱 | 蜘蛛、蠍、蜱、蟎 | ATP Ch16 |
| area of interest | 關注地區 |  | TC Ch2 |
| area／zone reconnaissance | 地區偵察／區域偵察 |  | TC Ch7 |
| armed escort | 武裝護航 | 第 6 線代碼 X | TC 附B |
| Army attack aviation | 陸軍攻擊航空 |  | TC Ch3 |
| Army leader | 陸軍領導者 |  | TC Ch1 |
| Army Medical Protection System | 陸軍醫療防護系統 | 篩檢結果登錄處 | ATP Ch18 |
| Army Training Network | 陸軍訓練網 | 美軍線上訓練資源平台 | TC 附B |
| Army values | 陸軍價值觀 |  | TC Ch1 |
| around-the-waist bowline／end-of-rope bowline | 腰間稱人結／繩端稱人結 |  | TC Ch12 |
| arthropod | 節肢動物 | 昆蟲、蛛形綱、蜈蚣、馬陸 | ATP Ch16 |
| artificial tears | 人工淚液 |  | ATP Ch17 |
| ASCOPE | 地區、建築、能力、組織、人員、事件 | 原文未寫縮寫，為列舉項目 | TC Ch11 |
| ASIP (advanced system improvement program) | 先進系統改良計畫 | 型號名稱保留 | TC Ch4 |
| ASOC／DASC | 空中支援作戰中心／直接空中支援中心 |  | TC Ch13 |
| assault climbing／assault climber | 突擊攀登／突擊攀登手 |  | TC Ch9 |
| assault team | 突擊伍 |  | TC Ch8 |
| assault／security／support element | 突擊組／警戒組／支援組 |  | TC Ch7 |
| assistant patrol leader | 副巡邏隊長 |  | TC Ch2 |
| ASSLT (assault) | 突擊 | 表 A-1、A-3 的分隊代號 | TC 附A |
| assumption of command | 接掌指揮 |  | TC Ch1 |
| asymptomatic | 無症狀 |  | ATP Ch18 |
| AT MY COMMAND | 聽我口令射擊 |  | TC Ch3 |
| AT4 | AT4 反裝甲武器 |  | TC 附A |
| ATC (Air Traffic Controller) | ATC 確保器 | 管狀確保器通稱 | TC Ch9 |
| ATL／BTL | A 伍伍長／B 伍伍長 |  | TC Ch2 |
| ATNAA | 神經毒劑解毒自動注射器 | 含阿托品＋氯化解磷定，**最多 3 支** | ATP Ch19 |
| ATP (Army techniques publication) | 陸軍技術出版品 | 僅見於書末詞彙表 | TC 詞彙表 |
| ATPIAL | 先進目標指示／照明／瞄準雷射 | AN/PEQ-15，武器用雷射指示器 | TC 附A |
| atropine | 阿托品 | 2.1 mg／支 | ATP Ch19 |
| atropinization | 阿托品化 | 心率>90、分泌物與唾液減少 | ATP Ch19 |
| attrition approach | 消耗戰方式 |  | TC Ch11 |
| auto-injector | 自動注射器 |  | ATP Ch7 |
| automated net control device | 自動化網路管制裝置 |  | TC Ch4 |
| avalanche / rockfall | 雪崩 / 落石 |  | ATP Ch17 |
| avalanche transceiver | 雪崩訊號器 |  | TC Ch9 |
| AVPU (alert, verbal, pain, unresponsive) | 清醒／語音／疼痛／無反應 | 意識程度評估法，字母保留原文 | ATP Ch11 |
| avulsed tissue | 撕脫組織 | 以浸生理食鹽水的無菌紗布保存待移植 | ATP Ch10 |
| avulsion | 撕脫傷 | 組織被扯離 | ATP Ch11 |
| axial / appendicular bones | 中軸骨 / 附肢骨 | 80 塊 / 126 塊，共 206 塊 | ATP Ch13 |
| axillary / inguinal | 腋窩 / 腹股溝 |  | ATP Ch4 |

## B

| 原文 | 譯文 | 說明 | 出處 |
|---|---|---|---|
| babesiosis | 巴貝斯蟲症 |  | ATP Ch16 |
| back blow | 拍背 | 腹部推擠前先施五次 | ATP Ch5 |
| backbrief | 回報簡報 |  | TC Ch2 |
| backbrief／confirmation brief | 回報簡報／確認簡報 |  | TC Ch13 |
| Bark scorpion | 樹皮蠍 | 含亞利桑那樹皮蠍 | ATP Ch16 |
| barracuda | 梭魚 | 少數會主動攻擊者之一 | ATP Ch16 |
| base maneuver element | 基準機動組 |  | TC Ch8 |
| base of fire | 火力基礎 | 沿用第 8 章 | TC Ch8、Ch13 |
| base squad | 基準班 |  | TC Ch7 |
| base-of-fire element | 火力基礎組 |  | TC Ch2 |
| basic load | 基本攜行量 |  | TC Ch2 |
| basilar skull fracture | 顱底骨折 | NPA 使用禁忌 | ATP Ch5 |
| basket-type litter | 籃式擔架 |  | TC Ch9 |
| battery | 砲兵連 |  | TC Ch3 |
| battle buddy | 戰鬥夥伴 | 初期回應的核心 | ATP Ch20 |
| battle drill | 戰鬥演練 | 第 8 章詳述 | TC Ch2、Ch8 |
| battle roster # | 戰鬥名冊編號 | 名首字母＋姓首字母＋識別碼末四碼 | ATP Ch15 |
| battlespace owner | 戰場空間責任單位 |  | TC Ch11 |
| BDO / JSLIST | 戰鬥服外罩 / 聯合部隊輕型整合防護衣 | 用過的注射器別於其口袋蓋 | ATP Ch19 |
| beach landing site | 登岸灘頭 |  | TC Ch12 |
| beaching | 搶灘 |  | TC Ch12 |
| bean bag light | 豆袋燈 | 可貼地放置、光束朝上的小型標示燈 | TC Ch14 |
| beaten zone | 彈著區 | 沿用第 8 章 | TC Ch8、Ch10 |
| belay/rappel device | 確保／垂降器 |  | TC Ch9 |
| belay／belayer | 確保／確保者 |  | TC Ch9 |
| bend／reach | 河彎／直河段 |  | TC Ch12 |
| bight／loop | 繩耳／繩圈 |  | TC Ch9 |
| biometrics | 生物特徵資料 | 指紋、虹膜掃描與照片 | TC 附A |
| bipod／tripod | 兩腳架／三腳架 |  | TC Ch10 |
| Black Widow Spider | 黑寡婦蜘蛛 | 雌蛛腹部紅色沙漏斑 | ATP Ch16 |
| Blacklegged “Deer” tick | 黑腳蜱（鹿蜱） | 萊姆病病媒 | ATP Ch16 |
| blackout (headlights) | 燈火管制 |  | TC Ch13 |
| blank firing adapter | 空包彈助退器 |  | TC Ch14 |
| blast injury | 爆震傷 |  | ATP Ch6 |
| blasting cap | 雷管 |  | TC Ch5 |
| blister agent (vesicant) | 糜爛性毒劑（起泡劑） |  | ATP Ch19 |
| blister pack | 鋁箔泡殼包裝 |  | ATP Ch9 |
| blood sweep | 掃血 | 頭到腳目視＋觸診 | ATP Ch4 |
| bloodshot | 充血 |  | ATP Ch10 |
| BMNT／EENT | 航海晨光始／航海昏影終 |  | TC Ch2 |
| boat commander | 艇長 |  | TC Ch12 |
| body belay | 身體確保 |  | TC Ch9 |
| body rappel | 身體垂降 | 僅限中等坡度 | TC Ch9 |
| body substance isolation | 體液隔離防護 |  | ATP Ch4 |
| booby trap | 詭雷 |  | TC Ch11 |
| bottom-fed intelligence | 由下而上的情報發展 |  | TC Ch11 |
| bounding overwatch | 躍進監視 | 預期接觸 | TC Ch6 |
| bounding rappel／walk down rappel | 跳躍式垂降／步行式垂降 | 禁止跳躍式 | TC Ch9 |
| bounding／overwatch element | 躍進組／監視組 |  | TC Ch6 |
| bowel / intestines | 腸道 / 腸子 |  | ATP Ch14 |
| bowline | 稱人結 |  | TC Ch9 |
| bowline (boat line) | 艏纜 | 注意與稱人結同字 | TC Ch12 |
| bow／stern | 艇首／艇尾 |  | TC Ch12 |
| bracketing fire | 夾叉射擊 |  | TC Ch2 |
| bracketing／creeping method | 夾叉法／漸近法 | 危險近距只能用漸近法 | TC Ch3 |
| Bradley Fighting Vehicle／Stryker／HMMWV | 布萊德雷戰鬥車／史崔克／高機動多用途輪型車 |  | TC Ch8 |
| brake hand | 制動手 |  | TC Ch9 |
| branch／sequel | 分支／後續 | 計畫的應變與後續階段 | TC Ch2 |
| Brazilian Wandering Spider | 巴西遊走蛛 | 世界毒性最強蜘蛛之一 | ATP Ch16 |
| breach element | 破障組 |  | TC Ch7 |
| breach point／entry point | 破障點／進入點 |  | TC Ch11 |
| break | break（分段） | 通聯中用以分隔不同類別的口令，保留原文 | TC 附B |
| break contact | 脫離接觸 | 沿用第 2 章 | TC Ch2、Ch8、Ch13 |
| breaks in contact | 脫節 | 隊伍前後失去聯繫 | TC Ch1 |
| breastbone | 胸骨 |  | ATP Ch5 |
| bronchial tree | 支氣管樹 |  | ATP Ch5 |
| Brown Recluse Spider | 棕色遁蛛 | 造成組織壞死 | ATP Ch16 |
| BTC (bridge team commander) | 架橋組長 |  | TC Ch9 |
| buddy team | 雙人夥伴組 |  | TC Ch7 |
| bump card／battle roster number | 號牌卡／戰鬥名冊編號 | 便於清點傷者與已後送人員 | TC Ch15 |
| bump plan | 遞補計畫 | 搭載人員因故無法上車（機）時的替補安排 | TC Ch2 |
| bumping and blocking technique | 推擠與阻擋技術 | 以車身推擠、阻擋威脅車輛，維持車隊持續運動 | TC Ch13 |
| buoyancy tube | 浮力管 |  | TC Ch12 |
| burp (the chest seal) | 排氣 | 掀開胸封貼釋放困住的空氣 | TC Ch15 |
| burping (the chest seal) | 排氣 | 掀開胸封貼釋放困住的空氣 | ATP Ch6 |
| burrowing asp | 穴蝰類 | 匕首蛇、鼴蝰 | ATP Ch16 |
| burst of fire | 連發 |  | TC Ch10 |
| buttoned up | 關閉艙蓋 |  | TC Ch10 |
| BVM (bag valve mask) | 甦醒球面罩 | 又稱袋瓣罩甦醒器 | ATP Ch5 |
| bypass | 繞越 |  | TC Ch8 |
| BZ / anticholinergic | 畢茲毒劑 / 抗膽鹼 | **給水須極為節制** | ATP Ch19 |

## C

| 原文 | 譯文 | 說明 | 出處 |
|---|---|---|---|
| C-spine | 頸椎 |  | ATP Ch15 |
| calamine lotion | 爐甘石洗劑 |  | ATP Ch16 |
| call for fire | 請求射擊 |  | TC Ch3 |
| call sign | 呼號 |  | ATP Ch15 |
| CANA | 神經毒劑抗痙攣解毒劑 | 藥物為地西泮；**不可自行施打** | ATP Ch19 |
| capillary refill | 微血管再充填 |  | ATP Ch13 |
| caplet | 膠囊狀錠劑 |  | ATP Ch9 |
| capsize drill | 翻艇演練 |  | TC Ch12 |
| capsize line | 翻艇繩 |  | TC Ch12 |
| carabiner | 鉤環 | 鎖定式／非鎖定式 | TC Ch9 |
| carabiner wrap | 鉤環纏繞 |  | TC Ch9 |
| carbon dioxide inflatable life preserver | 二氧化碳充氣式救生衣 | 偵察泳者背心 | TC Ch12 |
| cardiac tamponade | 心包填塞 |  | ATP Ch6 |
| carotid / femoral / radial / posterior tibial | 頸動脈 / 股動脈 / 橈動脈 / 脛後動脈 |  | ATP Ch4 |
| CARRO | 近接空中支援、火砲／迫擊砲、增援、預備隊、其他 | 縮寫保留不譯 | TC Ch2 |
| cartilage / ligament / tendon | 軟骨 / 韌帶 / 肌腱 | 韌帶連骨與骨；肌腱連肌肉與骨 | ATP Ch13 |
| CAS (close air support) | 近接空中支援 |  | TC Ch3 |
| CASEVAC | 傷患後送 | MEDEVAC 無法取得時才用 | ATP Ch7 |
| CASEVAC (casualty evacuation) | 傷患後送 | 沿用 ATP 4-02.11 | TC Ch1 |
| casualty | 傷患 |  | ATP Ch4 |
| casualty handoff | 傷患交接 |  | ATP Ch9 |
| casualty packaging | 傷患整備 | 固定所有鬆脫端 | ATP Ch15 |
| casualty staging | 傷患集結 | 最重者最後裝載、最先卸載 | ATP Ch15 |
| catheter-over-needle device | 套管針 | 10 號、14 號或 3¼ 英寸 | ATP Ch6 |
| CBRN | 化學、生物、輻射與核 | 沿用 ATP 4-02.11 | TC 附B｜ATP Ch6、Ch19 |
| CCP (casualty collection point) | 傷患集中點 | 沿用 ATP 4-02.11 | TC Ch1、Ch15 |
| CEASE LOADING | 停止裝填 |  | TC Ch3 |
| centerline | 中央繩 |  | TC Ch12 |
| centipede / millipede | 蜈蚣 / 馬陸 | 蜈蚣有毒鉤、馬陸無 | ATP Ch16 |
| centralized／decentralized | 集中式／分散式 | 工作優先順序掌控方式 | TC Ch7 |
| cephalothorax | 頭胸部 |  | ATP Ch16 |
| cerebral contusion | 腦挫傷 |  | ATP Ch11 |
| cerebrospinal fluid (CSF) | 腦脊髓液 | 自鼻耳滲出即屬急症 | ATP Ch11 |
| chafing | 磨擦 | 手指、腳趾間須以吸水材料隔開 | ATP Ch14 |
| chalk | 分載梯次 | 沿用第 13 章 | TC Ch14 |
| chalk／chalk leader | 分載梯次／梯次長 | 沿用第 2 章「梯次」用法 | TC Ch13 |
| challenge／password | 問令／答令 |  | TC Ch7 |
| chance contact | 意外接觸 |  | TC Ch6 |
| chaplain | 隨軍牧師 | ACE 中「陪同」的轉介對象之一 | ATP Ch20 |
| CHECK FIRING | 暫停射擊 |  | TC Ch3 |
| checkpoint／blocking position | 檢查哨／阻絕陣地 |  | TC Ch11 |
| chelicerae / pedipalp / spinneret | 螯肢 / 觸肢 / 紡器 |  | ATP Ch16 |
| chemical burn | 化學灼傷 | **不可浸水** | ATP Ch12 |
| chest recoil | 胸壁回彈 |  | ATP Ch6 |
| chest seal | 胸封貼 | 分附閥式（vented，首選）／無閥式 | ATP Ch6 |
| chest thrust | 胸部推擠法 | 孕婦、肥胖、腹部傷口時改用 | ATP Ch5 |
| chest tube | 胸管 |  | ATP Ch15 |
| chilblains (pernio) | 凍瘡 | 非凍結性；50–32°F 經 1–5 小時，無長期後遺症 | ATP Ch17 |
| chin-lift／jaw thrust | 抬下巴法／提下顎法 | ATP 4-02.11 作「壓額抬下巴法（head-tilt/chin-lift）」與「提下顎法」 | TC Ch15 |
| chlorine (Cl) / chloropicrin (PS) | 氯氣 / 氯化苦 |  | ATP Ch19 |
| chock pick | 岩楔取出器 |  | TC Ch9 |
| choking agent (lung-damaging) | 窒息性毒劑（肺損傷劑） | 造成肺水腫 | ATP Ch19 |
| cipher text | 密語 | 對應第 2 章 plain text（明語） | TC Ch4 |
| civil affairs | 民事 |  | TC Ch11 |
| civil disturbance | 民眾騷亂 |  | TC Ch11 |
| CL V (Class V) | 第五類補給品 | 彈藥與爆破器材 | TC Ch13 |
| clammy | 濕冷 | 出汗但皮膚冰冷 | TC Ch15 |
| clammy skin | 濕冷皮膚 | 休克徵象 | ATP Ch7 |
| Class I／III／V／VII／VIII／IX | 第一／三／五／七／八／九類補給品 | 口糧／油料／彈藥／主要成品／醫療／零件 | TC Ch2 |
| Class VIII | 第八類補給品（醫療物資） |  | TC Ch1 |
| Claymore mine | 闊刀地雷 |  | TC Ch1 |
| CLEAR | 清除完畢 | 喊話保留英文 | TC Ch8 |
| CLEARED DANGER CLOSE | 許可危險近距 |  | TC Ch3 |
| clearing team | 清除組 |  | TC Ch8 |
| climbing commands | 攀登口令 | 保留英文，見表 9-2 | TC Ch9 |
| clock direction | 時鐘方位 |  | TC Ch13 |
| close terrain | 近距地形 |  | TC Ch7 |
| closed / open fracture | 閉鎖性 / 開放性骨折 | 開放性常有骨頭突出，**不可推回** | ATP Ch13 |
| closed bolt／open bolt | 閉膛待擊／開膛待擊 |  | TC Ch7 |
| clove hitch | 雙套結 | 繩端／繩中 | TC Ch9 |
| cloverleaf interchange | 苜蓿葉型交流道 | 道路工程用語，與第 7 章 cloverleaf method（四葉草環繞法）無關 | TC Ch13 |
| cloverleaf method | 四葉草環繞法 | 以目標為中心，像四片葉子般依序繞到各側觀察 | TC Ch7 |
| CLS (combat lifesaver) | 戰鬥救護員 | 使用者指定譯名。受過進階戰傷急救訓練的一般官兵，階層低於 CMC（combat medic，醫務兵） | TC Ch1、Ch13 |
| CLS (Combat Lifesaver) | 戰鬥救護員 | Tier 2 人員 | ATP Ch4 |
| COA (course of action) | 行動方案 |  | TC Ch2 |
| cobra / krait / mamba | 眼鏡蛇 / 環蛇 / 曼巴蛇 |  | ATP Ch16 |
| cobra head connector | 眼鏡蛇頭接頭 |  | TC Ch4 |
| cold burn / frostbite | 冷灼傷 / 凍傷 |  | ATP Ch12 |
| cold compress | 冷敷 |  | ATP Ch10 |
| collarbone (clavicle) | 鎖骨 |  | ATP Ch13 |
| collateral damage | 附帶損害 |  | TC Ch8 |
| colubrid | 游蛇類 | 最大的蛇科，多無毒 | ATP Ch16 |
| combat communications | 戰鬥通信 |  | TC Ch4 |
| combat gauze | 止血紗布 | 沿用 ATP 4-02.11（hemostatic gauze） | TC Ch15 |
| combat pill pack | 戰傷用藥包 | 即第 9 章的 CWMP | ATP Ch10 |
| combat wound medication pack | 戰傷藥包 | 內含口服止痛藥與抗生素 | TC Ch15 |
| combined arms team | 諸兵種聯合團隊 |  | TC Ch11 |
| command-detonated | 命令起爆 |  | TC Ch7 |
| commander's critical information requirement (CCIR) | 指揮官重要情報需求 |  | TC Ch2 |
| commando crawl | 突擊隊爬行法 |  | TC Ch9 |
| communication window | 通信時窗 |  | TC Ch4 |
| communications security fill | 通信保密金鑰 |  | TC Ch1 |
| compartmentalized／canalized terrain | 分隔化／導引性地形 |  | TC Ch9 |
| compass Soldier／pace Soldier | 方位手／步測手 |  | TC Ch6 |
| Composition C-4 | C-4 混合炸藥 |  | TC Ch5 |
| compressed gauze | 壓縮紗布 | 六層無菌棉質 | ATP Ch12 |
| compromise and contingency plan | 洩密應處與應變計畫 |  | TC Ch13 |
| COMSEC | 通信保密 |  | TC Ch3 |
| concussion | 腦震盪 | 最常見的閉鎖性頭部傷勢；多數不伴隨意識喪失 | ATP Ch11 |
| Conditions／Standards／Cue／Task Steps | 條件／標準／啟動信號／任務步驟 | 演練格式 | TC Ch8 |
| cone of fire | 射彈散布錐 |  | TC Ch10 |
| conenose beetle (kissing bug) | 錐鼻蟲（接吻蟲） |  | ATP Ch16 |
| confirmation brief | 確認簡報 |  | TC Ch2 |
| consolidation and reorganization | 鞏固與重整 |  | TC Ch1 |
| constrained planning model | 受限計畫模式 |  | TC Ch2 |
| constrictor | 絞殺類蛇 | 蚺、蟒、森蚺 | ATP Ch16 |
| contact team | 聯絡小組 |  | TC Ch7 |
| contingency planning | 應變計畫 |  | TC Ch7 |
| contour | 沿周邊繞行 |  | TC Ch6 |
| contraband | 違禁品 |  | TC Ch7 |
| contraindicated | 禁忌（禁用） |  | ATP Ch8 |
| controlled occupation／withdrawal | 有掌控地進占／撤離 |  | TC Ch10 |
| contusion | 挫傷 |  | ATP Ch6、Ch11 |
| convulsion / seizure | 抽搐 / 癲癇發作 | 不可強行壓制手腳或撬開牙關 | ATP Ch11 |
| cook off／milk (grenade) | 延時投擲／預放握柄 | 危險，禁止 | TC Ch8 |
| copperhead | 銅頭蝮 |  | ATP Ch16 |
| coral snake | 珊瑚蛇 | 紅接黃有毒、紅接黑無毒（僅適用美國） | ATP Ch16 |
| cordon and search | 封鎖與搜索 |  | TC Ch7 |
| core temperature | 核心體溫 | 須以直腸測量 | ATP Ch8 |
| cornea | 角膜 |  | ATP Ch17 |
| corneal erosion | 角膜糜爛 | 化學灼傷症狀 | ATP Ch10 |
| corpsman | （海軍）醫務兵 |  | ATP Ch18 |
| COSC (combat and operational stress control) | 戰鬥與作戰壓力控制 | 本章主題 | ATP Ch20 |
| COSR (combat and operational stress reaction) | 戰鬥與作戰壓力反應 |  | ATP Ch20 |
| CoTCCC | 戰術戰傷救護委員會 | 器材建議標準的權威來源 | ATP Ch4 |
| cottonmouth / water moccasin | 棉口蛇 / 食魚蝮 | 半水生、具攻擊性 | ATP Ch16 |
| counterassault element | 反突擊分隊 |  | TC Ch13 |
| coup-contrecoup injury | 對衝傷 | 撞擊處（coup）＋對側（contrecoup） | ATP Ch11 |
| cover and concealment | 掩蔽與隱蔽 | cover 防彈、concealment 防視 | TC Ch2 |
| cover fire zone | 掩護射擊區域 |  | TC Ch10 |
| covering fire | 掩護火力 |  | TC Ch10 |
| covert gap crossing | 隱密渡越間隙 | 沿用第 2 章 | TC Ch2、Ch12 |
| coxswain | 舵手 | 沿用第 2 章 | TC Ch2、Ch12 |
| CPG (clinical practice guideline) | 臨床實務指引 |  | ATP Ch19 |
| CPR (cardiopulmonary resuscitation) | 心肺復甦術 | 戰鬥傷患罕用 | ATP Ch6 |
| CQC (close quarters combat) | 近距離戰鬥 |  | TC Ch11 |
| crampons／ice axe | 冰爪／冰斧 |  | TC Ch9 |
| cravat | 三角巾 |  | ATP Ch4 |
| crepitus | 捻髮音／骨摩擦感 | 可觸摸或聽見 | ATP Ch6、Ch13 |
| CRESS | 意識、呼吸、瞳孔、分泌物、皮膚 | 快速辨識化學戰劑暴露類型 | ATP Ch19 |
| crew-served weapons | 班組操作武器 | 需兩人以上操作的武器，如機槍 | TC Ch1 |
| CRIC (cricothyrotomy) | 環甲膜切開術 |  | ATP Ch15 |
| cross-loading | 分散搭載 | 關鍵人員與武器分散於不同航空器，與第 13 章 tactical cross-load 同理 | TC Ch14 |
| crossed-finger method | 交叉手指法 |  | ATP Ch5 |
| CRRC (combat rubber raiding craft) | 戰鬥橡皮突擊艇 |  | TC Ch12 |
| crypto fill | 密鑰 |  | TC Ch4 |
| CSW (crew-served weapon) | 班組操作武器 | 沿用第 1 章 | TC Ch13 |
| CUF (care under fire) | 火力下救護 | TCCC 第一階段，沿用 ATP 4-02.11 | TC Ch15 |
| CUF (Care Under Fire) | 火力下救護 | TCCC 第一階段 | ATP Ch4 |
| current velocity | 水流流速 |  | TC Ch12 |
| curvature of the Earth | 地球曲率 |  | TC Ch4 |
| CWMP (combat wound medication pack) | 戰傷用藥包 | 涵蓋 PAWS 的 P 與 A | ATP Ch9 |
| CXP (casualty exchange point) | 傷患交接點 |  | TC Ch2 |
| cyanogen (blood) agent | 氰化物（血液性）毒劑 | 干擾氧氣利用 | ATP Ch19 |
| cyanogen chloride | 氯化氰 |  | ATP Ch19 |
| cyanosis | 發紺 | 皮膚呈藍色調 | ATP Ch18 |

## D

| 原文 | 譯文 | 說明 | 出處 |
|---|---|---|---|
| D-ring | D 形環 |  | TC Ch12 |
| DA Form 1156 (Casualty Feeder Card) | 傷亡回報卡 | 表單編號保留 | TC Ch1 |
| DA Form 2028 | DA Form 2028 | 出版品修改建議表，表單編號保留原文 | TC 前言 |
| DA Form 5517 | DA Form 5517（標準射界卡） | 表單編號保留原文；射界卡沿用第 2 章（使用者指定譯名） | TC 附B |
| DA Pam (Department of the Army pamphlet) | 陸軍部手冊 | 僅見於書末詞彙表 | TC 詞彙表 |
| DAGR (defense advanced GPS receiver) | 國防先進 GPS 接收機 |  | TC Ch4 |
| danger area | 危險地區 | 第 6 章詳述 | TC Ch1、Ch6 |
| DANGER CLOSE | 危險近距 | 迫擊砲、砲兵 600 公尺內 | TC Ch3 |
| danger space | 危險空間 |  | TC Ch10 |
| data link | 資料鏈路 |  | TC Ch3 |
| datum | 大地基準 |  | TC Ch2 |
| DD Form 1380 | DD Form 1380（戰傷救護卡） | 表單編號保留原文，沿用 ATP 4-02.11 | TC Ch15｜ATP Ch4、Ch15 |
| DD Form 3019 | 復甦紀錄 | 較高照護層級接手後改用 | ATP Ch15 |
| dead space | 死角 | 沿用第 1 章 | TC Ch1、Ch4 |
| dead water | 靜水區 |  | TC Ch12 |
| Deathstalker scorpion | 死亡追蹤者蠍 | 北非與中東 | ATP Ch16 |
| debriefing | 任務歸詢 |  | TC Ch2 |
| decisive action | 決定性行動 | 攻擊、防禦、穩定作戰的持續組合 | TC Ch11 |
| decisive engagement | 決定性交戰 |  | TC Ch6 |
| decisive point | 決勝點 |  | TC Ch1 |
| decisive／shaping／sustaining operation | 決定性作戰／塑造作戰／持續作戰 |  | TC Ch2 |
| decontamination | 除污 | 本身即屬醫療介入 | ATP Ch19 |
| DEET | 敵避（N,N-二乙基間甲苯醯胺） | 驅蟲劑活性成分 | ATP Ch16 |
| defense support of civil authorities | 國防支援民政機關 |  | TC Ch11 |
| deliberate TQ | 精確式止血帶 | 用於 TFC，傷口上方 2–3 吋 | ATP Ch4 |
| demolition team | 爆破組 |  | TC Ch7 |
| demolitions | 爆破 | 本章主題 | TC Ch5 |
| demolitions effects simulator | 爆破效果模擬器 | 遊騎兵學校唯一製作的裝藥 | TC Ch5 |
| designated marksman | 指定射手 |  | TC Ch13 |
| det cord (detonating cord) | 導爆索 |  | TC Ch5 |
| detachment | 分遣隊 |  | TC Ch7 |
| detainee | 被拘留者 | 沿用第 11 章 | TC Ch8、附A |
| detonation (firing) system | 引爆（發火）系統 |  | TC Ch5 |
| detonation velocity | 爆速 |  | TC Ch5 |
| detour bypass method | 繞道迂迴法 |  | TC Ch6 |
| dexamethasone | 地塞米松 | HACE 用藥 | ATP Ch17 |
| DHA-PI 6025.14 / DODI 6465.01 | （國防衛生局與國防部規範編號） | SCT 與 G6PD 篩檢的法源 | ATP Ch18 |
| diaphragm | 橫膈膜 |  | ATP Ch5 |
| diazepam / midazolam | 地西泮 / 咪達唑侖 | 最多共 3 支（30 mg） | ATP Ch19 |
| diffuse axonal injury | 瀰漫性軸突損傷 |  | ATP Ch11 |
| dip can | 無煙菸草罐 | 應急護眼罩材料 | ATP Ch10 |
| Diplopoda | 倍足綱 | 馬陸所屬 | ATP Ch16 |
| dirty pit／clean pit | 髒區／淨區 | 對應第 11 章的「髒房／淨房」，此處為集結待命區內的兩個區位 | TC 附A |
| dirty room／clean room | 髒房／淨房 | 未搜查／已搜查人員區 | TC Ch11 |
| disabled vehicle | 故障車輛 | 含受損無法自行運動者 | TC Ch13 |
| disease and nonbattle injury (DNBI) | 疾病與非戰鬥傷害 | 良好衛生可預防 | ATP Ch20 |
| disengagement criteria | 脫離交戰準則 |  | TC Ch8 |
| dislocation | 脫臼 |  | ATP Ch13 |
| disorientation | 定向感喪失 | 重度低體溫徵象 | ATP Ch8 |
| distal | 遠端 | 距身體中心或傷處較遠的一側 | ATP Ch14 |
| distal pulse | 遠端脈搏 | 止血帶／繃帶以下的脈搏 | ATP Ch4 |
| DOD Trauma Registry | 國防部創傷登錄 |  | ATP Ch15 |
| DODI 6490.11 | 國防部指令 6490.11 | 腦震盪通報與處置的法源 | ATP Ch11 |
| double figure eight knot | 雙八字結 |  | TC Ch9 |
| doxycycline / ciprofloxacin | 多西環素 / 環丙沙星 | 生物戰劑暴露用藥 | ATP Ch19 |
| DPICM | 雙用途改良傳統彈藥 |  | TC Ch3 |
| DRAW-D | 防禦、增援、攻擊、撤退、遲滯 | 研判敵軍行動方案的記憶口訣 | TC Ch13 |
| dress (a knot) | 整理繩結 |  | TC Ch9 |
| dual initiating system | 雙重起爆系統 |  | TC Ch5 |
| DX (direct exchange) | 直接交換 |  | TC Ch2 |

## 數字與符號

| 原文 | 譯文 | 說明 | 出處 |
|---|---|---|---|
| “E-C” holding technique | E-C 夾持法 | BVM 面罩握持 | ATP Ch5 |
| (MARCHE)² | MARCHE 平方 | TCCC MARCH 與 CBRN 考量的整合 | ATP Ch19 |
| # (number) | 數量、編號 | 僅見於書末詞彙表 | TC 詞彙表 |
| (+) (–) | （加強）（減編） | 原文以符號表示編制增減 | TC 附A |
| 1/3::2/3 rule | 1/3：2/3 原則 | 領導者用三分之一時間，下級用三分之二 | TC Ch2 |
| 100 mph tape | 百哩膠帶 | 高強度布基膠帶 | TC Ch5 |
| 2-by-2 (box) formation | 2×2（方箱）隊形 |  | TC 附A |
| 5-S rule | 5-S 原則 | 搜索、禁聲、隔離、看管、迅速後送 | TC Ch2 |
| 6-ply | 六層 |  | ATP Ch12 |
| 9-line MEDEVAC request | 九線後送申請 | 沿用 ATP 4-02.11 | TC Ch15｜ATP Ch9 |

## E

| 原文 | 譯文 | 說明 | 出處 |
|---|---|---|---|
| ECAST (exercise collapse associated with sickle cell trait) | 鐮刀型血球特徵相關運動性昏厥 | 本章核心概念 | ATP Ch18 |
| EEFI (essential elements of friendly information) | 友軍資訊基本要項 |  | TC Ch2 |
| egress | 脫離 |  | TC Ch3 |
| egress procedures | 脫離程序 | 緊急狀況下離開航空器的程序 | TC Ch14 |
| elapid | 蝙蝠蛇科 | 固定式前溝牙、神經毒 | ATP Ch16 |
| electrical burn | 電燒傷 | 不可徒手接觸 | ATP Ch12 |
| electrolyte | 電解質 |  | ATP Ch17 |
| enabler | 賦能單位 |  | TC Ch2 |
| enabling operations | 賦能作戰 |  | TC Ch2 |
| enemy-prepared kill zone | 敵軍預設的殺傷區 |  | TC Ch8 |
| enfilade／frontal／flanking／oblique fire | 縱射／正面射擊／側射／斜射 | 相對於目標 | TC Ch10 |
| engagement／disengagement criteria | 交戰／脫離交戰準則 |  | TC Ch7 |
| entry point | 進入點 |  | TC Ch8 |
| envenomation | 中毒（毒液注入） |  | ATP Ch16 |
| environmental hypothermia | 環境性低體溫 |  | ATP Ch8 |
| EOD (explosive ordnance disposal) | 爆炸物處理 |  | TC Ch13 |
| epinephrine (adrenaline) | 腎上腺素 | 兒童 0.15 mg／成人 0.3 mg | ATP Ch7 |
| EPW (enemy prisoner of war) | 敵俘 |  | TC Ch2 |
| EPW and search team | 敵俘與搜索組 |  | TC Ch7 |
| EPW exchange point | 敵俘交接點 |  | TC Ch7 |
| erythrocyte | 紅血球 |  | ATP Ch18 |
| esprit de corps | 團隊精神 | 沿用 ATP 4-02.11 Ch20 | TC Ch1｜ATP Ch20 |
| ET tube (endotracheal tube) | 氣管內管 |  | ATP Ch15 |
| evacuation precedence | 後送優先順序 | 緊急／緊急手術／優先／例行／便利 | TC Ch15｜ATP Ch15 |
| evidence placement point | 證物放置點 | 分「各房間」與「集中」兩級 | TC 附A |
| exercise-induced asthma | 運動誘發型氣喘 | ECAST 風險因子 | ATP Ch18 |
| exertional heat illness | 運動性熱疾病 | 產熱與散熱失衡 | ATP Ch17 |
| expectant (triage category) | 期待（傷檢分類） | 資源有限時的分類 | ATP Ch5 |
| expedient technique | 應急技術 |  | ATP Ch4 |
| extended bandage | 延長繃帶 | 兩條三角巾接合而成 | ATP Ch14 |
| extended-release | 緩釋（劑型） |  | ATP Ch9 |
| extraction equipment | 脫困器材 | 將傷患自受困處救出的器材 | TC 附B |
| extruded polystyrene (foam) | 保麗龍（發泡聚苯乙烯） | 應急護眼罩材料 | ATP Ch10 |
| extrusion (of the eye) | 眼球脫出 | 眼球離開眼窩 | ATP Ch10 |
| eye socket / orbit | 眼窩 / 眼眶 | 眼眶傷勢可輕度加壓，眼球本身不可 | ATP Ch10 |

## F

| 原文 | 譯文 | 說明 | 出處 |
|---|---|---|---|
| fan／converging routes／box method | 扇形法／會合路線法／方框法 | 區域偵察方法 | TC Ch7 |
| fast-roping | 快速垂降 | 脊椎傷勢的高風險情境 | ATP Ch15 |
| fatal funnel | 致命漏斗 | 門口、樓梯等使人員被迫集中通過的位置 | TC 附A |
| FDC (fire direction center) | 射擊指揮所 |  | TC Ch3 |
| Fer-De-Lance / Bushmaster | 矛頭蝮 / 巨蝮 | 熱帶中美洲 | ATP Ch16 |
| ferry flight | 渡場飛行 | 不執行任務、單純將航空器飛渡至他處 | TC Ch14 |
| field artillery | 野戰砲兵 |  | TC Ch3 |
| field load carrier | 野戰攜行具 |  | TC Ch12 |
| field-expedient antenna | 野戰應急天線 |  | TC Ch4 |
| fight through | 戰鬥穿越 |  | TC Ch8 |
| figure eight descender | 八字下降器 |  | TC Ch9 |
| figure eight slipknot | 八字活結 |  | TC Ch9 |
| final protective fire | 最後防護射擊 |  | TC Ch2 |
| final protective line | 最終保護線 | 沿用第 10 章 | TC 附B |
| finger sweep | 手指清掃 | 僅限可見異物，禁止盲目清掃 | ATP Ch5 |
| fire and movement | 射擊與運動 |  | TC Ch6 |
| fire ant | 火蟻 | 群體同時攻擊 | ATP Ch16 |
| fire superiority | 火力優勢 |  | TC Ch7 |
| fire support | 火力支援 | 本章主題 | TC Ch3 |
| fire support officer | 火力支援官 |  | TC Ch2 |
| fire team | 火力伍 | 使用者指定：team 指步兵編組時譯「伍」，對應國軍「伍」的編制 | TC Ch1 |
| five-point contingency plan | 五要點應變計畫 | 即 GOTWA | TC Ch7 |
| fixed rope | 固定繩 |  | TC Ch9 |
| fixed／traverse／search fire | 定點射擊／橫移射擊／縱深射擊 | 相對於機槍 | TC Ch10 |
| flagging | 亮槍 | 在轉角露出槍口 | TC Ch11 |
| flanking／enfilading fire | 側射／縱射火力 |  | TC Ch7 |
| flex cuffs | 束帶 | 一次性拘束帶 | TC 附A |
| FLOT (forward line of own troops) | 友軍前緣 |  | TC Ch2 |
| flow technique | 流動技術 | 上下樓梯的清除法，分 2 人、3 人、4 人版本 | TC 附A |
| fluid replacement | 水分補充 |  | ATP Ch17 |
| FM (field manual; frequency modulation) | 野戰教範；調頻 | 僅見於書末詞彙表 | TC 詞彙表 |
| FO (forward observer) | 前進觀測官 |  | TC Ch1 |
| foot march／motor (road) march | 徒步行軍／摩托化（道路）行軍 |  | TC Ch6 |
| footgear | 鞋具 |  | ATP Ch13 |
| foothold | 立足點 |  | TC Ch7 |
| force-on-force | 對抗演練 |  | TC Ch2 |
| forced stop | 被迫停車 |  | TC Ch13 |
| FPF (final protective fire) | 最後防護射擊 | 沿用第 2 章 | TC Ch10 |
| FPL (final protective line) | 最後防護線 |  | TC Ch10 |
| FRAG OUT／STUN OUT | 破片彈出手／震撼彈出手 | 喊話保留英文 | TC Ch8 |
| fragmentation／concussion grenade | 破片手榴彈／震撼手榴彈 |  | TC Ch8 |
| FRAGORD (fragmentary order) | 部分命令 |  | TC Ch1 |
| fratricide | 誤擊友軍 |  | TC Ch1 |
| free gun | 自由射擊 |  | TC Ch10 |
| freezing under fire | 火力下僵住 | 嚴重壓力反應徵象 | ATP Ch20 |
| frequency hopping | 跳頻 |  | TC Ch3 |
| friction burn | 摩擦燒傷 | 含 road rash、地毯、繩索、滑行燒傷 | ATP Ch12 |
| friction hitch | 摩擦結 |  | TC Ch9 |
| FRIES／SPIES | 快速繩降插入與撤出系統／特種巡邏插入與撤出系統 | 以繩索自懸停直升機進出的兩種系統 | TC Ch14 |
| frostbite | 凍傷 | 年度數量最多的冷傷害；<32°F／0°C | ATP Ch17 |
| full thickness / third degree burn | 全厚度 / 三度燒傷 | 可能無痛覺，常需植皮 | ATP Ch12 |
| full thickness burn (3rd degree) | 全厚度燒傷（三度） |  | ATP Ch7 |
| fume toxicity／water resistance | 煙霧毒性／抗水性 |  | TC Ch5 |
| fuze igniter | 導火索點火器 |  | TC Ch5 |

## G

| 原文 | 譯文 | 說明 | 出處 |
|---|---|---|---|
| G6PD (glucose-6-phosphate dehydrogenase) deficiency | 葡萄糖六磷酸鹽脫氫酶缺乏症 | 台灣俗稱「蠶豆症」；與 SCT 同時篩檢 | ATP Ch18 |
| gag reflex | 嘔吐反射 |  | ATP Ch5 |
| gangrene | 壞疽 | 重度凍傷 | ATP Ch17 |
| garrison environment | 駐地環境 | 相對於戰鬥情境 | ATP Ch14 |
| gas-operated／recoil-operated／blowback-operated | 氣動式／後座作用式／反衝作用 |  | TC Ch10 |
| GEAR | 評量、評估、分析、減少 | 官兵負重管理架構 | TC Ch2 |
| Geneva Conventions | 日內瓦公約 | MEDEVAC 受保護、CASEVAC 不受保護 | ATP Ch15 |
| GIVE WAY TOGETHER | 齊划前進 | 口令保留英文 | TC Ch12 |
| globe (of the eye) | 眼球 |  | ATP Ch10 |
| gooseneck | 鵝頸管 |  | TC Ch4 |
| GOTWA | 去處、同行人員、時間、若未返回、接敵行動 | 縮寫保留不譯 | TC Ch7 |
| go／slow go／no go | 可通行／緩行／不可通行 |  | TC Ch11 |
| grazing fire／plunging fire | 掠射／俯射 | 相對於地面 | TC Ch10 |
| grenade launcher (GL) | 榴彈發射器 |  | TC Ch10 |
| grenade sump | 手榴彈坑 |  | TC Ch7 |
| ground guide | 地面引導員 |  | TC Ch14 |
| ground movement plan | 地面運動計畫 |  | TC Ch13 |
| ground plane | 地網 |  | TC Ch4 |
| ground tactical plan | 地面戰術計畫 | 沿用第 13 章 | TC Ch13、Ch14 |
| GTC (ground tactical commander) | 地面戰術指揮官 | 負責地面戰術計畫與目標區行動 | TC Ch14 |
| gunner／assistant gunner／ammunition bearer | 射手／副射手／彈藥手 |  | TC Ch10 |

## H

| 原文 | 譯文 | 說明 | 出處 |
|---|---|---|---|
| H-hour | H 時 |  | TC Ch2 |
| HACE (high-altitude cerebral edema) | 高海拔腦水腫 | >3,000 公尺／9,800 英尺 | ATP Ch17 |
| half hitch | 半結 |  | TC Ch9 |
| hand and arm signals | 手臂信號 |  | TC Ch6 |
| handset | 送受話器 |  | TC Ch4 |
| HAPE (high-altitude pulmonary edema) | 高海拔肺水腫 | >2,500 公尺／8,200 英尺 | ATP Ch17 |
| hard time | 硬性時間 | 不可變動的時間節點 | TC Ch2 |
| hard／soft compromise | 確定暴露／疑似暴露 |  | TC Ch2 |
| harness | 吊帶 |  | TC Ch9 |
| hasty hookup | 應急掛結 | 迅速完成拖救連結，不求完整程序 | TC Ch13 |
| hasty TQ | 應急式止血帶 | 用於 CUF，「high and tight」 | ATP Ch4 |
| hasty／deliberate ambush | 倉促伏擊／審慎伏擊 |  | TC Ch7 |
| hasty／deliberate attack | 倉促攻擊／審慎攻擊 |  | TC Ch3 |
| haul line | 拖拉繩 |  | TC Ch12 |
| head-tilt/chin-lift | 壓額抬下巴法 |  | ATP Ch5 |
| heat cramps | 熱痙攣 | 熱衰竭的前兆 | ATP Ch17 |
| heat exhaustion | 熱衰竭 | 大量出汗、皮膚蒼白濕冷 | ATP Ch17 |
| heat reflective shell | 反射熱外殼 | 附頭罩與側邊魔鬼氈開口 | ATP Ch8 |
| Heat Reflective Shield | 反射熱護罩 | 燒傷超過 20% 時使用 | ATP Ch12 |
| heat stroke | 中暑 | **皮膚灼熱乾燥、不出汗**；>104°F／40°C | ATP Ch17 |
| heavy left／heavy right | 左重／右重 | 空中突擊隊形 | TC Ch14 |
| HEDP (high explosive dual purpose) | 高爆兩用彈 |  | TC Ch2 |
| hemoglobin / hemoglobin S | 血紅素 / 血紅素 S | 血紅素 S 使紅血球呈鐮刀狀 | ATP Ch18 |
| hemorrhagic shock | 出血性休克 | 戰場休克的預設成因 | TC Ch15｜ATP Ch7 |
| hemostatic dressing | 止血敷料 |  | ATP Ch4 |
| hemothorax | 血胸 |  | ATP Ch6 |
| hemotoxin / neurotoxin | 血液毒素 / 神經毒素 | 頰窩蝮蛇 / 蝙蝠蛇科 | ATP Ch16 |
| HE／WP／Illum | 高爆彈／白磷彈／照明彈 |  | TC Ch3 |
| HF／VHF／UHF | 高頻／特高頻／超高頻 |  | TC Ch4 |
| high and tight | 保留原文不譯 |  | ATP Ch4 |
| high carry／low carry (boat) | 高姿／低姿搬運 | 與第 11 章持槍姿勢同字 | TC Ch12 |
| high crawl／low crawl | 高姿匍匐／低姿匍匐 |  | TC Ch6 |
| high-payoff target | 高報償目標 |  | TC Ch3 |
| high-value target | 高價值目標 |  | TC Ch11 |
| histamine | 組織胺 |  | ATP Ch7 |
| hives | 蕁麻疹 |  | ATP Ch7 |
| HLZ (helicopter landing zone) | 直升機降落區 | 沿用第 2 章 | TC Ch2、Ch14 |
| hoist | 吊掛絞車 | 直升機自地面吊升傷患的絞車 | TC 附B |
| HOLD／BACKPADDLE／REST PADDLES | 停槳／倒划／收槳 | 口令保留英文 | TC Ch12 |
| Holistic Health and Fitness | 全人健康與體能 | 症狀回報對象之一 | ATP Ch18 |
| hollow between thumb and palm | 虎口 | 手掌包紮的穿繞位置 | ATP Ch14 |
| horizontal／vertical lift | 水平／垂直吊升 |  | TC Ch9 |
| host-nation | 駐在國 |  | TC 前言 |
| hot lead | 饋電線 |  | TC Ch4 |
| HQ (headquarters) | 指揮部 |  | TC Ch1 |
| hydrocortisone | 氫化可體松 | 外用止癢 | ATP Ch16 |
| hydrogen cyanide (AC) | 氰化氫 | 氣味似苦杏仁；**數秒內即失能** | ATP Ch19 |
| hyperthermia | 高體溫症 | 主動保溫的禁忌症 | ATP Ch8 |
| hyponatremia (water intoxication) | 低血鈉症（水中毒） | **易與中暑混淆，處置相反：不可再給水** | ATP Ch17 |
| hypothermia | 低體溫症 | MARCH-PAWS 的「H」 | ATP Ch8 |
| hypothermia prevention and management kit | 低體溫預防與處置套組 | 沿用 ATP 4-02.11 | TC Ch15｜ATP Ch8 |
| hypovolemia | 低血容 |  | ATP Ch7 |
| hypovolemic shock | 低血容性休克 |  | ATP Ch7 |
| hypoxia | 缺氧 | 嘴唇或指尖發紫 | ATP Ch17 |
| hysterical outburst | 歇斯底里發作 |  | ATP Ch20 |

## I

| 原文 | 譯文 | 說明 | 出處 |
|---|---|---|---|
| I.E.D. checklist (injury/evaluation/distance) | 傷害／評估／距離檢核表 | 評估欄助記字為 HEADS | ATP Ch11 |
| IAW (in accordance with) | 依據 |  | ATP Ch6 |
| ibuprofen / naproxen / aspirin | 布洛芬 / 萘普生 / 阿斯匹靈 | 戰傷傷患應避免，會增加出血風險 | ATP Ch9 |
| IED (improvised explosive device) | 簡易爆炸裝置 |  | TC Ch11 |
| IFAK / JFAK | 個人急救包 / 聯合急救包 |  | ATP Ch4 |
| immediate action | 立即處置 | 武器故障排除 | TC Ch11 |
| immediate／delayed／minimal／expectant | 立即／延遲／輕微／期待 | 四種檢傷分類類別 | TC Ch15 |
| impaled object | 插入異物 | 不可拔除 | ATP Ch9 |
| impalement injury | 插入傷 |  | ATP Ch14 |
| impending doom | 瀕死感 | 過敏性休克症狀 | ATP Ch7 |
| in-line (neutral) stabilization | 中立軸線固定 | 四人搬運時二號的職責 | ATP Ch13 |
| incapacitating agent | 失能性毒劑 | 效果持續數小時至數天 | ATP Ch19 |
| incendiary | 燃燒劑 |  | ATP Ch19 |
| INCOMING | 砲擊來襲 | 喊話保留英文 | TC Ch8 |
| indelible marker | 不褪色麥克筆 | 書寫 TCCC 卡用 | ATP Ch15 |
| index marks | 定位標記 |  | TC Ch3 |
| INFIL／EXFIL | 滲透／撤出 |  | TC Ch2 |
| information requirement | 情報需求 |  | TC Ch7 |
| inhalation injury | 吸入性傷害 | **有此徵象者禁用 NPA** | ATP Ch12 |
| initial contact report | 初步接觸報告 |  | TC Ch7 |
| initiating (priming) system | 起爆系統 |  | TC Ch5 |
| installation team | 架設組 |  | TC Ch9 |
| insulator | 絕緣體 |  | TC Ch4 |
| intercostal space | 肋間隙 |  | ATP Ch6 |
| interdiction | 遮斷 | 限制、轉移、擾亂、遲滯、摧毀、損傷 | TC Ch3 |
| interim pace count | 臨時步測計數 |  | TC Ch6 |
| intracranial hemorrhage | 顱內出血 |  | ATP Ch11 |
| iodine tablets | 碘錠 | 2% 碘酊 5 滴＝1 錠 | TC Ch15 |
| IOT (in order to) | 以便 |  | TC Ch2 |
| IP (initial point) | 起始點 | CAS 用語；圖 3-2 的 IP 為滲透點 | TC Ch3 |
| irrigation | 沖洗 |  | ATP Ch10 |
| IV (intravenous) | 靜脈輸液 |  | ATP Ch8 |

## J

| 原文 | 譯文 | 說明 | 出處 |
|---|---|---|---|
| jaw-thrust | 提下顎法 | 疑似頸傷時的首選 | ATP Ch5 |
| JFAK (joint first aid kit) | 聯合急救包 | 沿用 ATP 4-02.11 | TC Ch15 |
| joint, interagency, and multinational | 聯合、跨部會與多國 |  | TC Ch11 |
| JSTARS | 聯合監視目標攻擊雷達系統 |  | TC Ch13 |
| JTAC (joint terminal attack controller) | 聯合終端攻擊管制員 |  | TC Ch3 |
| JTS (Joint Trauma System) | 聯合創傷系統 | 維護國防部創傷登錄 | ATP Ch15 |
| junctional area | 交界部位 | 頸、腋窩、腹股溝 | ATP Ch4 |

## K

| 原文 | 譯文 | 說明 | 出處 |
|---|---|---|---|
| kapok | 木棉救生衣 |  | TC Ch12 |
| KDDTMK | 關鍵行動、距離、方向、運動時間、運動方式、關鍵位置 | 縮寫保留不譯 | TC Ch2 |
| kernmantle rope | 包芯繩 |  | TC Ch9 |
| key terrain／decisive terrain | 要域／決定性地形 |  | TC Ch2 |
| KIA (killed in action) | 陣亡 | 沿用第 1 章 | TC Ch1、Ch15 |
| kill zone | 殺傷區 | 沿用第 8 章 | TC Ch2、Ch13 |
| kneecap (patella) | 膝蓋骨 | 疑似骨折時不可彎膝 | ATP Ch14 |
| knot | 節 | 每小時 1 浬（1.852 公里），依原文照列不換算 | TC Ch14 |
| knot (speed) | 節 |  | TC Ch12 |
| knotted hand line | 打結手持繩 |  | TC Ch12 |

## L

| 原文 | 譯文 | 說明 | 出處 |
|---|---|---|---|
| laager site | 待命區 | 飛機暫停待命地點 | TC Ch2 |
| LACE | 液體、彈藥、傷亡、裝備（報告） | 縮寫保留不譯 | TC Ch1 |
| laceration | 撕裂傷 |  | ATP Ch9、Ch10 |
| landing plan | 著陸計畫 |  | TC Ch14 |
| landing point | 降落點 | 單機接地位置，與整個降落區不同 | TC Ch14 |
| lateral／range／vertical shift | 左右／距離／高低修正 |  | TC Ch3 |
| law of armed conflict | 武裝衝突法 |  | TC 前言 |
| lead safety swimmer | 領頭安全泳者 |  | TC Ch12 |
| lead-in | 引入線 |  | TC Ch4 |
| leader performance step | 領導者執行步驟 | 以「\*」標示 | TC Ch8 |
| leadership requirements model | 領導要求模式 | 出自 ADP 6-22 | TC Ch1 |
| left-handed firing method | 左手持槍射擊法 | 清除右手邊轉角時減少暴露 | TC 附A |
| lethargy | 嗜睡／倦怠 |  | ATP Ch7 |
| lewisite | 路易氏劑 | 接觸即劇痛 | ATP Ch19 |
| lift | 架次 | 沿用第 2 章 | TC Ch14 |
| lift or shift fires | 停止或轉移火力 |  | TC Ch7 |
| lightweight flexible stretcher | 輕量軟式擔架 | 可一人拖行 | ATP Ch15 |
| limiting stakes／aiming stakes | 射界限制樁／瞄準樁 |  | TC Ch7 |
| line of deployment | 展開線 |  | TC Ch7 |
| line of sight | 瞄準線 |  | TC Ch10 |
| linear danger area | 線狀危險地區 |  | TC Ch6 |
| linear／L-shaped formation | 線形／L 形隊形 |  | TC Ch7 |
| lines of communication | 交通線 |  | TC Ch11 |
| line／vee／echelon／diamond／wedge／file | 橫隊／V 字形／梯形／菱形／楔形／縱隊 |  | TC Ch6 |
| linkup | 會合 |  | TC Ch7 |
| linkup rally point | 會合集合點 |  | TC Ch7 |
| listening post | 聽音哨 |  | TC Ch1 |
| litter | 擔架 |  | ATP Ch13 |
| litter casualty / ambulatory casualty | 擔架傷患 / 可行走傷患 | 不必要遮蔽雙眼會使後者變成前者 | ATP Ch10 |
| litter discipline | 垃圾紀律 | 此處 litter 指垃圾，非擔架 | TC Ch6 |
| litter／ambulatory | 擔架／可行走 | 第 5 線的兩種傷患類型 | TC 附B |
| live training environment | 實彈訓練環境 |  | TC Ch8 |
| LOA (limit of advance) | 推進限制線 | 沿用第 2 章 | TC Ch2、Ch7 |
| loading plan／staging plan | 裝載計畫／整備集結計畫 | 沿用第 13 章 | TC Ch14 |
| loading plan／unloading plan | 裝載計畫／下車計畫 |  | TC Ch13 |
| lock down a room | 鎖定房間 |  | TC Ch11 |
| locking bar | 鎖定橫桿 |  | TC Ch9 |
| logroll method／slide method | 滾木法／滑入法 | 傷患上擔架方式 | TC Ch9 |
| long count／short count | 單人報數／雙人報數 | 使用者指定譯名。兼指上下艇方式與報數方式：long count 乘員逐一從艇首上下艇、逐一報數（水深、無法從兩側下艇時使用）；short count 乘員兩兩一組從艇側上下艇、兩兩報數（淺水區快速離艇，搶灘與突擊作戰常用） | TC Ch12 |
| long-range penetration | 長程滲透 | 梅里爾突擊隊的叢林戰術 | TC 前言 |
| long-range reconnaissance patrol | 長程偵察巡邏 | 越戰時期的遊騎兵連前身 | TC 前言 |
| long-range／short-range surveillance | 遠距／近距監視 |  | TC Ch7 |
| LOS (line of sight) | 視距 |  | TC Ch4 |
| low angle／high angle | 低射界／高射界 |  | TC Ch3 |
| low carry／high carry | 低姿持槍／高姿持槍 |  | TC Ch11 |
| low explosive／high explosive (HE) | 低爆炸藥／高爆炸藥 | 推擠效果／碎裂效果 | TC Ch5 |
| low-range thermometer | 低溫域體溫計 | 寒冷環境中口溫、耳溫不準 | ATP Ch8 |
| LSS／RSS | 左側警戒／右側警戒 | 伏擊時兩側的警戒組 | TC 附A |
| lumbar region | 腰部（下背部） |  | ATP Ch13 |
| luminescent tape | 夜光膠帶 |  | TC Ch6 |
| lye | 鹼液（氫氧化鈉） |  | ATP Ch10 |
| Lyme disease | 萊姆病 |  | ATP Ch16 |
| LZ (landing zone) | 降落區 |  | ATP Ch15 |
| LZ rush | 降落區疾進 | 離機後迅速脫離降落區的動作 | TC Ch14 |

## M

| 原文 | 譯文 | 說明 | 出處 |
|---|---|---|---|
| M18A1 claymore mine | M18A1 闊刀地雷 |  | TC 附A |
| MACE 2 | 軍用急性腦震盪評估卡第 2 版 | 見第 10 章 | ATP Ch11 |
| MACE 2 (Military Acute Concussion Evaluation 2) | 軍用急性腦震盪評估卡第 2 版 | 評估平衡、視覺與動作 | ATP Ch10 |
| machine gun employment | 機槍運用 | 本章主題 | TC Ch10 |
| main effort | 主力 |  | TC Ch1 |
| malaise | 倦怠 | 輻射疾病初期症狀 | ATP Ch19 |
| mandible | 下顎骨 | **骨折者不可平躺仰臥** | ATP Ch13 |
| Maneuver Center of Excellence | 機動卓越中心 | 本書主管機關 | TC 前言 |
| manifest | 載運清冊 | 沿用第 13 章 | TC Ch14 |
| manpack radio | 背負式無線電機 |  | TC Ch4 |
| MARCH PAWS | （保留原文） | 處置優先順序助記碼，沿用 ATP 4-02.11 | TC Ch15 |
| MARCH-PAWS | （保留原文） | 處置優先順序助記碼 | ATP Ch4 |
| marshalling area | 集結待命區 | 集中管控被拘留者之處 | TC 附A |
| mass casualty | 大量傷患 |  | TC Ch2 |
| mass casualty incident | 大量傷患事件 | 傷患人數超過建制醫療資源所能處理 | TC Ch15｜ATP Ch9 |
| Massasauga | 侏儒響尾蛇 |  | ATP Ch16 |
| masthead | 天線頂座 |  | TC Ch4 |
| maximum ordinate | 最大彈道高 | 約在距離三分之二處 | TC Ch10 |
| maximum range／maximum effective range | 最大射程／最大有效射程 |  | TC Ch10 |
| MCO (Marine Corps order) | 陸戰隊命令 | 僅見於書末詞彙表 | TC 詞彙表 |
| MCRP (Marine Corps reference publication) | 陸戰隊參考出版品 | 僅見於書末詞彙表 | TC 詞彙表 |
| MDI (modernized demolition initiator) | 現代化爆破起爆器 |  | TC Ch5 |
| meat tenderizer / talcum powder | 嫩肉粉 / 滑石粉 | 水母螫傷處置 | ATP Ch16 |
| mechanical advantage | 機械利益 |  | TC Ch9 |
| mechanical ascender | 機械式上升器 |  | TC Ch9 |
| Medal of Honor | 榮譽勳章 | 美軍最高榮譽 | TC 前言 |
| MEDEVAC | 醫療後送 | 優先使用 | ATP Ch7 |
| MEDEVAC (medical evacuation) | 醫療後送 | 與 CASEVAC（傷患後送）區分 | TC Ch6 |
| MEDEVAC／CASEVAC | 傷患醫療後送／傷患後送 | 沿用第 2 章 | TC Ch13 |
| medic | 醫務兵 | 使用者指定譯名 | TC Ch1 |
| medical logistics | 醫療後勤 |  | ATP Ch9 |
| medical officer (physician) | 醫官（醫師） | 僅其可取出嵌入眼球的異物 | ATP Ch10 |
| medical regulating | 醫療調度 | CASEVAC 不經此程序 | ATP Ch15 |
| meloxicam | 美洛昔康 | 15 mg × 1，不影響血小板功能 | ATP Ch9 |
| meninges | 腦膜 | 腦部的保護層 | ATP Ch11 |
| Merrill's Marauders | 梅里爾突擊隊 | 第 5307 混合部隊（臨時編組） | TC 前言 |
| METT-TC (I) | 任務、敵情、地形與天候、可用兵力與支援、可用時間、民事考量、資訊考量 | 縮寫保留不譯 | TC Ch1 |
| MGRS (military grid reference system) | 軍用方格參考系統 |  | TC 附B |
| mid-clavicular line | 鎖骨中線 | NDC 部位一 | ATP Ch6 |
| midface | 顏面中段 |  | ATP Ch5 |
| military information support operations | 軍事資訊支援作戰 |  | TC Ch11 |
| military mountaineering | 軍事登山 | 本章主題 | TC Ch9 |
| military working dog | 軍犬 |  | TC Ch11 |
| military-aged males | 役齡男性 |  | TC Ch11 |
| milk snake / scarlet kingsnake | 牛奶蛇 / 猩紅王蛇 | 與珊瑚蛇斑紋相似的無毒蛇 | ATP Ch16 |
| milliradian (mil) | 密位 |  | TC Ch3 |
| minimum force／time available | 最低兵力／可用時間 | 集合點行動技巧 | TC Ch6 |
| minimum safe distance | 最小安全距離 | 適用訓練 | TC Ch3、Ch8 |
| misconduct stress behavior | 失當壓力行為 | 可能需紀律處分而非醫療處置 | ATP Ch20 |
| misfire | 啞火 |  | TC Ch5 |
| mission-essential task | 任務必要任務 |  | TC Ch2 |
| MIST | 傷害機轉、傷勢類型、徵象與症狀、處置 | 傷患交接的結構化通報格式 | ATP Ch9 |
| MIST report | MIST 報告 | 傷害機轉、傷勢類型、徵象與症狀、處置 | TC Ch15 |
| mm (millimeter) | 公釐 | 僅見於書末詞彙表 | TC 詞彙表 |
| moldable splint | 可塑形夾板 |  | ATP Ch13 |
| monkey crawl | 猴子爬行法 |  | TC Ch9 |
| MOPP | 任務導向防護態勢 |  | ATP Ch19 |
| MOPP (mission-oriented protective posture) | 任務導向防護態勢 |  | TC Ch2 |
| MOPP 4 | 任務導向防護態勢第 4 級 | 最高防護等級 | TC Ch8 |
| moray eel | 海鱔 |  | ATP Ch16 |
| mounted avenue of approach | 乘車接近路線 |  | TC Ch10 |
| mounted patrol operations | 車載巡邏作戰 | 本章主題 | TC Ch13 |
| mousehole | 鼠洞 | 在牆上打穿、供人員通行的洞口 | TC 附A |
| movement formation | 運動隊形 |  | TC Ch6 |
| movement technique | 運動技術 |  | TC Ch6 |
| movement to contact | 接敵運動 |  | TC Ch7 |
| moxifloxacin | 莫西沙星 | 400 mg × 1，穿刺傷專用抗生素 | ATP Ch9 |
| MPCOA／MDCOA | 最可能行動方案／最危險行動方案 |  | TC Ch2 |
| MRE (meal, ready to eat) | 野戰口糧 |  | TC Ch2 |
| MTF (medical treatment facility) | 醫療處置設施 |  | ATP Ch6 |
| Munter hitch | 義大利半扣 |  | TC Ch9 |
| Munter mule knot | 義大利半扣騾結 |  | TC Ch9 |
| musculoskeletal system | 肌肉骨骼系統 |  | ATP Ch13 |
| mustard / nitrogen mustard | 芥子氣 / 氮芥 | **接觸當下不痛，具欺騙性** | ATP Ch19 |
| muzzle awareness | 槍口意識 |  | TC Ch11 |

## N

| 原文 | 譯文 | 說明 | 出處 |
|---|---|---|---|
| nail bed | 甲床 | 觀察缺氧的部位之一 | ATP Ch11 |
| napalm | 凝固汽油 |  | ATP Ch19 |
| NAPP | 神經毒劑吡啶斯的明前置治療 | 須於暴露前 8 小時內服用 | ATP Ch19 |
| nasopharynx | 鼻咽 |  | ATP Ch5 |
| National Command Authority | 國家指揮當局 |  | TC Ch11 |
| NATO (North Atlantic Treaty Organization) | 北大西洋公約組織 | 僅見於書末詞彙表 | TC 詞彙表 |
| natural lines of drift | 天然移動路線 | 人員自然傾向行走的路線 | TC Ch7 |
| navigator observer method | 導航員—觀測員法 |  | TC Ch12 |
| navigator／observer | 導航員／觀測員 |  | TC Ch12 |
| NDC (needle decompression of the chest) | 胸腔針刺減壓 |  | ATP Ch6 |
| near ambush／far ambush | 近距伏擊／遠距伏擊 | 以手榴彈投擲距離區分 | TC Ch8 |
| near flank | 近側翼 |  | TC Ch8 |
| near side／far side lifeguard | 近側／遠側救生員 |  | TC Ch12 |
| near side／far side rally point | 近側／遠側集合點 |  | TC Ch6 |
| necrosis | 壞死 | 棕色遁蛛咬傷 | ATP Ch16 |
| Needle-D | 針刺減壓 | 即 NDC | ATP Ch15 |
| net control device | 網路管制裝置 |  | TC 附B |
| nifedipine / sildenafil | 硝苯地平 / 西地那非 | HAPE 用藥 | ATP Ch17 |
| Nipah virus / hantavirus | 立百病毒 / 漢他病毒 | CDC C 類 | ATP Ch19 |
| NKDA (no known drug allergies) | 無已知藥物過敏 |  | ATP Ch15 |
| NLT (not later than) | 不遲於 |  | TC Ch2 |
| NO CHANGE | 無變更 |  | TC Ch2 |
| no-fire area／restrictive fire area | 禁止射擊區／限制射擊區 |  | TC Ch2 |
| noise and light discipline | 噪音與燈火管制 |  | TC Ch1 |
| noncombatant | 非戰鬥人員 |  | TC Ch8 |
| nonconductive material | 非導電材料 | 繩索、衣物、乾木 | ATP Ch12 |
| noncontact side／safe side | 非接觸側／安全側 |  | TC Ch13 |
| nonfreezing cold injury | 非凍結性冷傷害 |  | ATP Ch17 |
| noninflatable life preserver | 非充氣式救生衣 | 工作背心 | TC Ch12 |
| northing／easting | 北距／東距 |  | TC Ch2 |
| NPA (nasopharyngeal airway) | 鼻咽呼吸道 | JFAK 配發 32 Fr 一種尺寸 | ATP Ch5 |
| NSAID (nonsteroidal anti-inflammatory drug) | 非類固醇消炎止痛藥 |  | ATP Ch9 |
| number combination | 數字組合 |  | TC Ch2 |
| NVD (night-vision device) | 夜視裝置 | AN/PVS-14 | TC Ch6、附A |

## O

| 原文 | 譯文 | 說明 | 出處 |
|---|---|---|---|
| OAKOC | 觀測與射界、接近路線、要域、障礙、掩蔽與隱蔽 | 縮寫保留不譯 | TC Ch2 |
| obscurants | 遮蔽物 |  | TC Ch11 |
| obscuration | 遮蔽（發煙） |  | TC Ch13 |
| obstacle clearance ratio | 障礙淨空比 | 進離場所需水平距離與障礙高度之比，10 比 1 | TC Ch14 |
| occlusive dressing | 密封敷料 |  | ATP Ch12 |
| occlusive material | 密封（氣密）材料 |  | ATP Ch6 |
| odd number system | 奇數系統 | 口令系統 | TC Ch7 |
| one-rope bridge | 單繩橋 |  | TC Ch12 |
| OOM (order of march) | 行軍序列 |  | TC Ch2 |
| OP (observation post) | 觀測哨 |  | TC Ch1 |
| OPCON (operational control) | 作戰管制 |  | TC Ch13 |
| open / closed head injury | 開放性 / 閉鎖性頭部傷勢 |  | ATP Ch11 |
| open pneumothorax | 開放性氣胸 |  | ATP Ch6 |
| open spacing／close interval | 疏開車距／密集車距 |  | TC Ch13 |
| Operation Enduring Freedom | 持久自由行動 | 阿富汗戰爭代號 | ATP Ch9 |
| OPORD (operation order) | 作戰命令 |  | TC Ch1 |
| OPSKED (operation schedule) | 作戰時程 |  | TC Ch2 |
| order of march | 行軍序列 | 沿用第 2 章 | TC Ch13 |
| organic unit | 建制單位 |  | TC Ch7 |
| organophosphorus | 有機磷 |  | ATP Ch19 |
| oropharynx | 口咽 |  | ATP Ch6 |
| ORP (objective rally point) | 目標集合點 |  | TC Ch1 |
| OTSG | 軍醫署 | 部分藥品須其授權才配發 | ATP Ch19 |
| outer／inner cordon | 外圍／內圍封鎖 |  | TC Ch7 |
| over-the-counter pain reliever | 非處方止痛藥 |  | ATP Ch12 |
| overhand knot | 單結 |  | TC Ch9 |
| overlapping and interlocking fires | 重疊與交叉火力 |  | TC Ch10 |
| overwatch | 掩護監視 | 沿用第 8 章 | TC 附A |
| OVER／OUT／SHOT／SPLASH | 完畢／通話結束／已發射／彈著前通知 | 通話範例保留英文 | TC Ch3 |

## P

| 原文 | 譯文 | 說明 | 出處 |
|---|---|---|---|
| PACE | 主要、預備、應變、緊急 | 縮寫保留不譯 | TC Ch2 |
| paddler | 划槳手 |  | TC Ch12 |
| pain scale (0–10) | 疼痛量表 | 0 不痛，10 最痛 | ATP Ch15 |
| parallel planning | 平行計畫 |  | TC Ch2 |
| partial thickness / second degree burn | 部分厚度 / 二度燒傷 | 起水泡 | ATP Ch12 |
| partial thickness burn (2nd degree) | 部分厚度燒傷（二度） |  | ATP Ch7 |
| partisan linkup | 游擊隊會合 |  | TC Ch12 |
| partisans | 游擊隊 | 沿用第 12 章 | TC 前言 |
| passage of lines | 超越通過 |  | TC Ch2 |
| passive (clandestine) PB | 被動（隱密）巡邏基地 |  | TC Ch7 |
| passive warming | 被動保溫 | 僅保留自身體熱 | ATP Ch8 |
| patent airway | 通暢的呼吸道 |  | ATP Ch11 |
| path of least resistance | 阻力最小的路徑 |  | TC Ch8 |
| Pathfinder | 先導隊 | 先期進入並開設、管制降落區的專業人員 | TC Ch14 |
| Patient Evacuation Coordination Cell | 傷患後送協調中心 |  | ATP Ch15 |
| patrol | 巡邏隊 | 指編組時；指行動時譯「巡邏」 | TC Ch1 |
| patrol leader | 巡邏隊長 | 原文 1-6、1-8 段與 PL（排長）混用，譯文依原文區分 | TC Ch1 |
| PAWS | 疼痛、抗生素、傷口、固定 | MARCH-PAWS 的後半段，縮寫保留原文 | ATP Ch9 |
| PB (patrol base) | 巡邏基地 | 不超過 24 小時；不重複使用 | TC Ch1、Ch7 |
| PDD (pressure delivery device) | 加壓裝置 | 就地取材製作 | ATP Ch4 |
| PDF (principal direction of fire) | 主射向 | 沿用第 1 章 | TC Ch10 |
| PD／VT／MT／ET／MTSQ | 著發／近發／機械時間／電子時間／機械時間兼瞬發引信 |  | TC Ch3 |
| pelvic fracture | 骨盆骨折 | 大量內出血成因 | ATP Ch7 |
| perfusion | 灌流 |  | ATP Ch7 |
| pericardial tamponade | 心包填塞 | 阻塞性休克成因 | ATP Ch7 |
| permeability | 通透性 |  | ATP Ch7 |
| persistent / nonpersistent agent | 持久性 / 非持久性戰劑 | >24 小時 / 10–15 分鐘 | ATP Ch19 |
| PETN／RDX／TNT | 季戊四醇四硝酸酯／旋風炸藥／三硝基甲苯 |  | TC Ch5 |
| PGK (precision guidance kit) | 精準導引套件 |  | TC Ch3 |
| phase line | 階段線 |  | TC Ch2 |
| phonetic alphabet | 通話字母表 |  | ATP Ch15 |
| phosgene / diphosgene (DP) | 光氣 / 雙光氣 | 光氣最危險；氣味似新割乾草 | ATP Ch19 |
| phosgene oxime | 光氣肟 | 接觸即劇痛 | ATP Ch19 |
| photo map | 影像地圖 |  | TC Ch12 |
| PI (probability of incapacitation) | 失能機率 |  | TC Ch3 |
| pigtail | 繩尾 |  | TC Ch9 |
| PIR (priority intelligence requirement) | 優先情報需求 | 沿用第 2 章 | TC Ch1、附A |
| PIR／FFIR | 優先情報需求／友軍情資需求 |  | TC Ch2 |
| pitch | 繩距 |  | TC Ch9 |
| PL (platoon leader) | 排長 |  | TC Ch1 |
| planned／immediate CAS | 計畫性／立即性近接空中支援 |  | TC Ch3 |
| plastic wrapper | 塑膠外包裝 | 敷料不夠大時可先覆蓋傷口 | ATP Ch14 |
| platelet function | 血小板功能 |  | ATP Ch9 |
| pleat | 摺層 | 手部／足部包紮時塞入多餘材料 | ATP Ch14 |
| pleural space | 肋膜腔（胸膜腔） | 肺臟與胸壁之間 | ATP Ch6 |
| PLT-D (platoon drill) | 排級演練 | 僅見於書末詞彙表 | TC 詞彙表 |
| PMESII-PT | 政治、軍事、經濟、社會、資訊、基礎設施、實體環境、時間 | 原文未寫縮寫，為列舉項目 | TC Ch11 |
| point of domination | 控制位置 | 沿用第 8 章 | TC Ch8、附A |
| point person | 尖兵 | 不兼任方位手、步測手 | TC Ch6 |
| point-blank range | 近距直射距離 |  | TC Ch10 |
| point／area target | 點目標／面積目標 | 沿用第 3 章 | TC Ch10 |
| point／area／antiarmor ambush | 點伏擊／地區伏擊／反裝甲伏擊 |  | TC Ch7 |
| poison | 毒物 | 食入／吸入／經皮吸收才致害 | ATP Ch16 |
| polar plot | 極座標法 |  | TC Ch3 |
| poncho liner | 雨衣內襯 | 被動保溫替代品 | ATP Ch8 |
| poncho raft | 雨衣筏 | 以雨衣包裹裝備綁成防水浮包，人在水中推行渡越 | TC Ch12 |
| port／starboard | 左舷／右舷 |  | TC Ch12 |
| position of comfort | 舒適姿勢 | 讓傷患自行選擇 | ATP Ch5 |
| position of function | 功能位置 |  | ATP Ch13 |
| positive flotation device | 正浮力漂浮器材 |  | TC Ch12 |
| positive pressure ventilation | 正壓換氣 |  | ATP Ch6 |
| post-concussion syndrome | 腦震盪後症候群 |  | ATP Ch11 |
| potassium iodide (KI) | 碘化鉀 | **僅輻射暴露前後 4 小時內有效** | ATP Ch19 |
| power of hydrogen (pH) | 酸鹼值 |  | ATP Ch10 |
| pralidoxime chloride | 氯化解磷定 | 600 mg／支 | ATP Ch19 |
| pre-equalized anchor | 預先均力固定點 |  | TC Ch9 |
| precision fire／area fire | 精確射擊／面積射擊 |  | TC Ch3 |
| precombat checks and inspections | 戰鬥前查核與檢查 |  | TC Ch2 |
| precombat inspection | 戰前檢查 |  | TC Ch13 |
| pressure bar | 加壓桿 | 急救繃帶上的構件 | ATP Ch4 |
| pressure dressing | 加壓敷料 |  | TC Ch15 |
| pressure dressing / bandage | 加壓敷料 / 加壓繃帶 |  | ATP Ch4 |
| pressure patch | 加壓貼片 | **眼傷禁用** | ATP Ch10 |
| pressure relief valve | 洩壓閥 |  | TC Ch12 |
| preventive maintenance checks and services | 預防保養檢查與勤務 |  | TC Ch13 |
| priapism | 陰莖持續勃起 | 巴西遊走蛛咬傷 | ATP Ch16 |
| primary／alternate／supplementary position | 主要／預備／補助陣地 |  | TC Ch10 |
| primary／secondary sector of fire | 主要／次要射界 |  | TC Ch10 |
| principal direction of fire | 主射向 |  | TC Ch1 |
| priority of fires | 火力優先權 |  | TC Ch2 |
| priority of work | 工作優先順序 |  | TC Ch1 |
| probable error in range | 距離公算偏差 |  | TC Ch3 |
| profession of arms | 軍人專業 |  | TC 前言 |
| progress capture device | 防逆裝置 |  | TC Ch9 |
| prone position | 俯臥 |  | ATP Ch5 |
| prophylaxis | 預防性投藥 |  | ATP Ch16 |
| proponent | 主管機關 | 負責某準則或術語的權責單位 | TC 前言 |
| protection | 保護支點 |  | TC Ch9 |
| protruding organs | 突出的器官 | **不可推回體內、不可徒手碰觸、須保持濕潤** | ATP Ch14 |
| Prusik knot | 普魯士結 |  | TC Ch9 |
| PSG (platoon sergeant) | 排士官長 | 國軍編制稱「排副」，本書採「排士官長」 | TC Ch1 |
| psychological first aid | 心理急救 | 與生理急救並行 | ATP Ch20 |
| PTSD (post-traumatic stress disorder) | 創傷後壓力症候群 | 例行心理急救可降低其發生 | ATP Ch20 |
| pubic area / buttocks | 陰部 / 臀部 | 九則律各佔 1% | ATP Ch12 |
| pyridostigmine bromide | 溴化吡啶斯的明 | **僅供暴露前預防**，30 mg×21 錠／7 天 | ATP Ch19 |
| pyrotechnic signals | 煙火信號 | 信號彈、發煙罐等 | TC Ch13 |
| PZ (pickup zone)／LZ (landing zone) | 搭機區／降落區 | 沿用第 2 章 | TC Ch14 |
| PZ／LZ | 搭機區／降落區 |  | TC Ch2 |

## Q

| 原文 | 譯文 | 說明 | 出處 |
|---|---|---|---|
| Q fever / Brucellosis / ricin | Q 熱 / 布氏桿菌病 / 蓖麻毒素 | CDC B 類 | ATP Ch19 |
| QRF (quick reaction force) | 快速反應部隊 |  | TC Ch2 |
| quad-folding litter | 四折式擔架 | 適合長距離搬運 | ATP Ch15 |
| quartering party | 宿營先遣組 |  | TC Ch1 |
| quick fire plan | 快速火力計畫 |  | TC Ch8 |
| quick reference card | 速查卡 | 本附錄主題 | TC 附B |
| quick release | 快速解脫結 |  | TC Ch12 |

## R

| 原文 | 譯文 | 說明 | 出處 |
|---|---|---|---|
| R&S (reconnaissance and surveillance) team | 偵察與監視小組 |  | TC Ch7 |
| rabies | 狂犬病 | 動物咬傷的首要顧慮 | ATP Ch16 |
| radiating element | 輻射元件 |  | TC Ch4 |
| radiation burn | 輻射燒傷 | 曬傷、X 光、放射治療 | ATP Ch12 |
| radio operator | 無線電兵 |  | TC Ch1 |
| radio-listening silence | 無線電靜聽 |  | TC Ch6 |
| raid | 突襲 |  | TC Ch7 |
| rally point | 集合點 | 起始、途中、目標、近側、遠側 | TC Ch7 |
| ramming technique | 衝撞技術 |  | TC Ch13 |
| range card | 射界卡 | 使用者指定譯名（非「射程卡」）；記錄武器射界、目標參考點與射擊諸元的卡片 | TC Ch1 |
| Ranger | 遊騎兵 | 書名譯為《遊騎兵手冊》 | TC Ch1 |
| Ranger Creed | 遊騎兵信條 | 六段首字拼成 RANGER | TC 前言 |
| Ranger tab | 遊騎兵臂章 | 完成遊騎兵學校者佩戴 | TC 前言 |
| Rangers lead the way! | 遊騎兵，開路先鋒！ | 官方格言，源自諾曼第登陸日 | TC 前言 |
| RAP (rocket assisted projectile) | 火箭增程彈 |  | TC Ch3 |
| rappel seat | 垂降座繩 |  | TC Ch9 |
| rappelling | 垂降 |  | TC Ch9 |
| ratchet | 棘輪 |  | ATP Ch4 |
| rate of march | 行軍速度 |  | TC Ch6 |
| rattlesnake | 響尾蛇 |  | ATP Ch16 |
| RE (relative effectiveness) factor | 相對效能係數 | 以 TNT＝1.00 為基準 | TC Ch5 |
| ready-heat blanket | 速熱毯 | 需氧氣進行化學反應，高海拔可能失效 | ATP Ch8 |
| rear ramp off-load | 後艙門卸載 |  | TC Ch14 |
| rear-fanged snake | 後溝牙蛇類 | 非洲樹蛇、紅樹林蛇、藤蛇 | ATP Ch16 |
| RECON/REORG | 偵察／重編 |  | TC 附A |
| reconnaissance patrol／combat patrol | 偵察巡邏／戰鬥巡邏 |  | TC Ch7 |
| recovery operations | 車輛回收作業 |  | TC Ch13 |
| recovery position | 復甦姿勢 |  | ATP Ch5 |
| RED (risk estimate distance) | 風險評估距離 | 僅適用實戰 | TC Ch3 |
| red medical warning tag | 紅色醫療警示牌 | SCT 陽性者須配戴 | ATP Ch18 |
| reflexive fire | 反射射擊 |  | TC Ch11 |
| reflexive sight | 反射式瞄準鏡 |  | TC Ch10 |
| rehearsal of concept drill | 概念演練預演 |  | TC Ch2 |
| relay frequency | 中繼頻率 | 第 2 線明定不可填中繼頻率 | TC 附B |
| release point (RP) | 解散點 |  | TC Ch2 |
| rendezvous point | 會合點 |  | TC Ch7 |
| rerouted figure eight knot | 回穿八字結 |  | TC Ch9 |
| rescue breathing | 人工呼吸 |  | ATP Ch5、Ch6 |
| respiratory distress | 呼吸窘迫 |  | ATP Ch6 |
| responder | 施救者 |  | ATP Ch4 |
| restated mission | 重述任務 |  | TC Ch2 |
| restrictive／severely restrictive terrain | 限制性／極度限制性地形 |  | TC Ch7 |
| retrievable rappel | 可回收垂降 |  | TC Ch9 |
| retrograde | 退卻 | 含遲滯、撤離、撤退 | TC Ch2 |
| reverse planning | 逆向規劃 | 從任務時間往回推算 | TC Ch1 |
| reverse planning sequence | 逆向計畫順序 | 自目標區行動往回推的五項計畫 | TC Ch14 |
| RFL (restrictive fire line) | 限制射擊線 |  | TC Ch2 |
| rib cage | 胸廓 |  | ATP Ch5 |
| rigid eye shield | 硬式護眼罩 | 穹頂狀、不施壓；本章核心器材 | ATP Ch10 |
| riot control agent | 鎮暴劑 | 作用短暫，與失能性毒劑不同 | ATP Ch19 |
| Risk Group / Biosafety Level | 風險群組 / 生物安全等級 | 各分 1–4 級 | ATP Ch19 |
| rock drill | 沙盤推演 | 以地面實物模擬推演，沿用第 2 章地形模型預演的概念 | TC 附A |
| Rocky Mountain spotted fever | 洛磯山斑疹熱 |  | ATP Ch16 |
| ROE (rules of engagement) | 交戰準則 | 沿用第 2 章 | TC Ch8 |
| Role 2／Role 3 | Role 2／Role 3 | 北約醫療設施層級，代號保留原文 | TC Ch15 |
| roll bypass | 越級後送 | 跳過能力不足的醫療設施，直接送往具備處置能力者 | TC Ch15 |
| rolling-T technique | 滾動 T 字技術 | V 字形隊形的變化型，用於寬走廊 | TC 附A |
| rope bridge | 繩橋 |  | TC Ch9 |
| rope installation | 繩索設施 |  | TC Ch9 |
| rope puller | 拉繩手 |  | TC Ch12 |
| rope swimmer | 拖繩泳者 |  | TC Ch12 |
| rotor wash | 旋翼下洗氣流 |  | TC Ch14 |
| rotor wash / propeller wash | 旋翼下洗氣流 / 螺旋槳氣流 |  | ATP Ch15 |
| round turn with two half hitches | 繞一圈半加兩個半結 |  | TC Ch9 |
| route classification | 路線分級 |  | TC Ch9 |
| routing buckle | 穿繞扣 |  | ATP Ch4 |
| RPG (rocket-propelled grenade) | 火箭推進榴彈 |  | TC Ch13 |
| RSDL | 反應性皮膚除污乳液 | 首選除污方式，2 分鐘內中和 | ATP Ch19 |
| RT (radio transmitter) | 無線電發射機 | 原文展開；一般指收發機 | TC Ch4 |
| RTO (radio-telephone operator) | 無線電話務員 | 與第 1 章 radio operator（無線電兵）區分 | TC Ch2 |
| Rule of Nines | 九則律 | 燒傷面積估算法 | ATP Ch12 |
| rules of engagement | 交戰準則 |  | TC Ch2 |
| running (working) end／standing end | 動端／靜端 |  | TC Ch9 |
| running password | 跑步口令 |  | TC Ch2 |
| rush | 躍進 | 3 至 5 秒 | TC Ch6 |

## S

| 原文 | 譯文 | 說明 | 出處 |
|---|---|---|---|
| S-2／S-3／S-4 | 營或旅情報／作戰／後勤參謀官 |  | TC Ch2 |
| S-3 Air | S-3 航空官 |  | TC Ch2 |
| SA (situational awareness) | 狀況覺知 |  | TC Ch4 |
| safety pin | 安全別針 | 固定延長繃帶重疊處 | ATP Ch14 |
| saline | 生理食鹽水 |  | ATP Ch10 |
| SALUTE | 規模、活動、位置、單位、時間、裝備（報告格式） | 縮寫保留不譯 | TC Ch1 |
| sandbar／tributary | 沙洲／支流 |  | TC Ch12 |
| SC/PT (single channel/plain text) | 單頻道／明語 |  | TC Ch2 |
| SCATMINE | 撒布地雷 |  | TC Ch3 |
| scout swimmer | 偵察泳者 |  | TC Ch12 |
| screening smoke | 遮蔽煙幕 |  | TC Ch8 |
| SE (sensitive site exploitation) | 敏感地點蒐證 | 沿用第 7 章 | TC Ch11、附A |
| sea snake | 海蛇 | 毒液極強但毒牙僅 ¼ 英寸 | ATP Ch16 |
| search and attack | 搜索與攻擊 |  | TC Ch7 |
| seat hip rappel | 座式髖部垂降 |  | TC Ch9 |
| secondary entry team | 次要進入小組 |  | TC Ch11 |
| section | 分隊 | 車輛分隊等 | TC Ch8 |
| sector of fire | 射界 |  | TC Ch1 |
| sector sketch | 區域要圖 |  | TC Ch1 |
| security halt | 警戒停止 |  | TC Ch7 |
| security squad／assault squad | 警戒班／突擊班 |  | TC Ch6 |
| semi-rigid splint | 半硬式夾板 | 36 英寸鋁材外覆泡棉 | ATP Ch13 |
| septum (nasal) | 鼻中隔 |  | ATP Ch6 |
| serial | 梯次 |  | TC Ch13 |
| serpentine technique | 蛇形技術 | 菱形隊形的變化型，用於狹窄走廊 | TC 附A |
| Service member | 服役人員 |  | ATP Ch4 |
| SGA (supraglottic airway) | 聲門上呼吸道 |  | ATP Ch15 |
| shallow wedge | 淺楔形隊形 |  | TC Ch7 |
| sheaf | 彈著分佈 | 多門砲同時射擊時彈著點的排列形狀；集中、特種、開放、平行 | TC Ch3 |
| shelter half | 帳篷布 | 襯墊／吊帶材料 | ATP Ch13 |
| shift from a known point | 自已知點移位法 |  | TC Ch3 |
| shock recovery position | 休克復甦姿勢 | 仰臥、雙腳略高於心臟 | ATP Ch7 |
| shock tube | 導爆管 |  | TC Ch5 |
| short halt／long halt | 短停／長停 |  | TC Ch6 |
| SHORT ROOM | 淺房 | 喊話保留英文 | TC Ch8 |
| shrapnel | 彈片 |  | ATP Ch9 |
| sickle cell disease (SCD) | 鐮刀型血球疾病 | 繼承兩份鐮刀型基因 | ATP Ch18 |
| sickle cell trait (SCT) | 鐮刀型血球特徵 | 帶一份鐮刀型基因＋一份正常基因，通常無症狀 | ATP Ch18 |
| Sidewinder | 角響尾蛇 |  | ATP Ch16 |
| signature | 特徵訊號 | 車輛在戰場上易被偵知的聲、光、塵、熱等徵候 | TC Ch13 |
| significant activities report | 重要活動報告 | 爆炸相關事件須提報 | ATP Ch11 |
| single channel (SC)／frequency hop (FH) | 單頻道／跳頻 |  | TC Ch4 |
| SITREP (situation report) | 狀況報告 |  | TC Ch8 |
| skeletal / cardiac / smooth muscle | 骨骼肌 / 心肌 / 平滑肌 |  | ATP Ch13 |
| skin graft | 植皮 |  | ATP Ch12 |
| SL (squad leader) | 班長 |  | TC Ch1 |
| SLCD (spring-loaded camming device) | 彈簧凸輪 |  | TC Ch9 |
| sling | 吊帶 | 手高於肘、手指外露 | ATP Ch13 |
| sling load | 吊掛載重 | 掛在機腹下方以纜索吊運的載重 | TC Ch14 |
| sling rope／cordelette | 繩環／輔助繩環 |  | TC Ch9 |
| sling／runner | 扁帶環 |  | TC Ch9 |
| slit trench | 散兵坑式廁所 |  | TC Ch7 |
| slough | 盲汊 | 使用者指定譯名（原譯「死水汊」）。河流的盲端支汊，深且無水流，夜航易誤入；與 dead water（靜水區，位於主河道上）不同 | TC Ch12 |
| slurred speech | 口齒不清 |  | ATP Ch8 |
| snap link | 扣環 |  | TC Ch12 |
| snow blindness / photokeratitis | 雪盲 / 光角膜炎 | 角膜的暫時性曬傷；3–5 小時後加劇 | ATP Ch17 |
| SOF (special operations forces) | 特種作戰部隊 |  | TC Ch13 |
| SOI (signal operating instructions) | 通信作業指示 |  | TC Ch2 |
| Soldier | 官兵 | 原文專指陸軍；與泛指各軍種的 Service member（服役人員）刻意區分 | ATP Ch8 |
| Soldier load | 官兵負重 |  | TC Ch2 |
| SOP (standard operating procedure) | 標準作業程序 |  | TC Ch1 |
| space blanket | 保暖毯 | 應急保溫材料 | TC Ch9｜ATP Ch8 |
| spare barrel | 備用槍管 |  | TC Ch10 |
| specified task／implied task | 明示任務／隱含任務 |  | TC Ch2 |
| spinal column / spinal cord | 脊柱 / 脊髓 |  | ATP Ch13 |
| spiral motion | 螺旋方式 | 腿部包紮手法 | ATP Ch14 |
| spoiling attack | 破壞性攻擊 |  | TC Ch2 |
| spot report | 即時報告 |  | TC Ch7 |
| sprain / strain | 扭傷 / 拉傷 |  | ATP Ch17 |
| SQD-D (squad drill) | 班級演練 | 僅見於書末詞彙表 | TC 詞彙表 |
| square knot | 平結 | 結打在夾板遠離身體側 | TC Ch9｜ATP Ch13 |
| squelch (SQ) | 靜噪 |  | TC Ch4 |
| stability operations | 穩定作戰 |  | TC Ch11 |
| staging plan | 整備集結計畫 |  | TC Ch13 |
| STANAG | 北約標準化協定 | 沿用第 15 章 | TC 前言、Ch15 |
| stance | 站姿 |  | TC Ch11 |
| stand-to | 全員戒備 |  | TC Ch7 |
| standard fire command | 標準射擊口令 | 初始與補充 | TC Ch8 |
| Standing Orders | 常備命令 | 羅傑斯遊騎兵的 19 條守則 | TC 前言 |
| standoff | 遠距 |  | TC Ch10 |
| start point (SP)／release point (RP) | 起點／解散點 |  | TC Ch6 |
| starter belt | 起始彈鏈 |  | TC Ch10 |
| static／dynamic rope | 靜力繩／動力繩 |  | TC Ch9 |
| stationary assault line | 固定突擊線 |  | TC Ch7 |
| stationary unit／moving unit | 固定單位／運動單位 |  | TC Ch7 |
| sterile／nonsterile overlay | 保密版／非保密版透明圖 |  | TC Ch3 |
| sterilize | 清除痕跡 |  | TC Ch6 |
| stigma | 汙名 | 尋求心理健康支持的障礙 | ATP Ch20 |
| stingray / cone shell / sea urchin | 魟魚 / 芋螺 / 海膽 | 熱水浸泡 30–60 分鐘去活性 | ATP Ch16 |
| stoma / tracheostomy | 造口 / 氣管造口術 |  | ATP Ch6 |
| stopper／chock | 岩楔 |  | TC Ch9 |
| STP (Soldier training publication) | 官兵訓練出版品 | 僅見於書末詞彙表 | TC 詞彙表 |
| straddle trench | 跨坐式壕溝 | 野戰廁所，原文另有 saddle trench 拼寫不一致 | TC Ch15 |
| stragglers | 脫隊人員 |  | TC Ch6 |
| stretcher bearer | 擔架手 |  | ATP Ch18 |
| strip map | 帶狀路線圖 | 沿用第 12 章 | TC Ch6、Ch13 |
| structural brain injury detection device | 結構性腦損傷偵測裝置 |  | ATP Ch11 |
| stun grenade | 閃光震撼手榴彈 |  | TC Ch8 |
| subterranean complex | 地下設施 |  | TC Ch11 |
| successive／alternating bounds | 連續躍進／交互躍進 |  | TC Ch6 |
| sucking chest wound | 吸吮性胸傷 | 開放性氣胸的別稱 | ATP Ch6 |
| sulfuric / hydrochloric / nitric acid | 硫酸 / 鹽酸 / 硝酸 |  | ATP Ch10 |
| superficial / first degree burn | 淺層 / 一度燒傷 | 不列入燒傷百分比計算 | ATP Ch12 |
| supine | 仰臥 |  | ATP Ch7 |
| support by fire team | 火力支援伍 |  | TC Ch8 |
| suppress | 制壓 | 表 2-25 戰術任務譯「壓制」，火力任務類型採砲兵用語「制壓」 | TC Ch3 |
| suppressive fire | 壓制射擊 |  | TC Ch8 |
| surf operations | 碎浪區作業 |  | TC Ch12 |
| surface danger zone | 地面危險區 |  | TC Ch10 |
| sustained operations | 持續性作戰 | 展開前應先睡飽 | ATP Ch20 |
| sustained／rapid／cyclic rate of fire | 持續射速／快速射速／循環射速 |  | TC Ch10 |
| SW (surface warfare) | 水面作戰 | 僅見於書末詞彙表 | TC 詞彙表 |
| swathe | 束縛帶 | 綁在骨折處上方或下方，不可正上方 | ATP Ch13 |
| swimmer safety line | 泳者安全繩 |  | TC Ch12 |
| swimmer's position | 泳者姿勢 | 側臥 | ATP Ch19 |
| swinging traverse | 擺動橫移射擊 |  | TC Ch10 |
| swollen neck veins | 頸靜脈怒張 | 張力性氣胸晚期徵象 | ATP Ch6 |
| Sydney Funnel-web Spider | 雪梨漏斗網蜘蛛 | 澳洲，具攻擊性 | ATP Ch16 |

## T

| 原文 | 譯文 | 說明 | 出處 |
|---|---|---|---|
| T-2 mycotoxin / yellow rain | T-2 黴菌毒素 / 黃雨 | 具出血性症狀 | ATP Ch19 |
| T/C/S | 任務、條件、標準 |  | TC Ch2 |
| T/F (test fire) | 試射 |  | TC Ch2 |
| TACSAT (tactical satellite) | 戰術衛星 |  | TC Ch4 |
| tactical assault panel | 戰術突擊胸掛 |  | TC Ch12 |
| tactical call out | 戰術喊話勸出 |  | TC Ch11 |
| tactical cross-load | 戰術分載 | 關鍵人員與武器分散搭載於不同車輛 | TC Ch13 |
| tactical evacuation care | 戰術後送救護 | TCCC 第三階段 | TC Ch15 |
| Tactical Evacuation Care | 戰術後送照護 | TCCC 第三階段 | ATP Ch15 |
| tactical eyewear / ballistic glasses | 戰術眼鏡 / 防彈眼鏡 | 護眼罩的替代品 | ATP Ch10 |
| tactical march | 戰術行軍 |  | TC Ch6 |
| tactical mission task | 戰術任務 | 表 2-25 各項譯名見該表 | TC Ch2 |
| tactical patience | 戰術耐心 |  | TC Ch11 |
| tactical／protective obstacles | 戰術障礙／防護障礙 |  | TC Ch10 |
| tagline | 控制繩 |  | TC Ch9 |
| tarantula | 捕鳥蛛 |  | ATP Ch16 |
| targeting／decide／detect | 目標選定／決定／偵獲 |  | TC Ch3 |
| TB MED 507 / TC 4-02.3 | （軍用技術公報與訓練通報編號） | 熱與冷傷害預防的參考文件 | ATP Ch17 |
| TBI (traumatic brain injury) | 創傷性腦損傷 |  | ATP Ch5、Ch11 |
| TCCC (tactical combat casualty care) | 戰術戰傷救護 | 本章主題，沿用 ATP 4-02.11 | TC Ch15 |
| TCCC (Tactical Combat Casualty Care) | 戰術戰傷救護 | 全書核心概念 | ATP Ch4 |
| TCCC card | TCCC 卡 | 即 DD Form 1380 | ATP Ch11 |
| templated position | 判定位置 |  | TC Ch6 |
| ten-print card | 十指指紋卡 |  | TC 附A |
| tensile strength | 拉伸強度 |  | TC Ch9 |
| tension pneumothorax | 張力性氣胸 | 沿用 ATP 4-02.11 | TC Ch15｜ATP Ch6 |
| tensionless anchor | 無張力固定點 |  | TC Ch9 |
| terrain model | 地形模型 |  | TC Ch2 |
| tetanus (lockjaw) | 破傷風（牙關緊閉症） | 所有蛇咬皆須考量 | ATP Ch16 |
| TFC (tactical field care) | 戰術戰場救護 | TCCC 第二階段，沿用 ATP 4-02.11 | TC Ch15 |
| TFC (Tactical Field Care) | 戰術戰場救護 | TCCC 第二階段 | ATP Ch4 |
| TH (time hack) | 對時 |  | TC Ch2 |
| theater commander | 戰區指揮官 |  | ATP Ch9 |
| thermal burn | 熱燒傷 |  | ATP Ch12 |
| thermite / magnesium | 鋁熱劑 / 鎂 | 金屬燃燒劑 | ATP Ch19 |
| thousand-yard stare | 千碼凝視 | 失神空洞的凝視；輕度壓力反應徵象 | ATP Ch20 |
| three-dimensional fight | 三維戰鬥 | 含天花板與上下樓層 | TC Ch11 |
| tick / mite | 蜱（壁蝨）/ 蟎 |  | ATP Ch16 |
| time fuze | 定時導火索 |  | TC Ch5 |
| TIME ON TARGET (TOT) | 同時彈著／目標時間 | 請求射擊譯「同時彈著」，CAS 表單譯「目標時間」 | TC Ch3 |
| TL (team leader) | 伍長 | 對應國軍「伍」的編組 | TC Ch1 |
| TLP (troop leading procedures) | 部隊領導程序 | 本章主題之一，共 8 步驟 | TC Ch2 |
| TM (technical manual) | 技術手冊 | 僅見於書末詞彙表 | TC 詞彙表 |
| TO (technical order) | 技術命令 | 僅見於書末詞彙表 | TC 詞彙表 |
| TOC (tactical operations center) | 戰術作戰中心 |  | TC Ch2 |
| tongue-jaw lift | 舌顎上提法 |  | ATP Ch5 |
| total body surface area (TBSA) | 全身體表面積 | 手掌約 1% | ATP Ch12 |
| TQ (tactical questioner) | 戰術詢問員 | 第 11 章 TQ 為戰術詢問（行為），第 15 章 TQ 為止血帶 | TC 附A |
| TQ (tactical questioning) | 戰術詢問 | 注意與 tourniquet（止血帶）縮寫相同 | TC Ch11 |
| TQ (tourniquet) | 止血帶 | ⚠️ 本章 TQ 為止血帶，第 11 章 TQ 為戰術詢問（tactical questioning） | TC Ch15 |
| TQ (Tourniquet) | 止血帶 | 原文全篇縮寫為 TQ | ATP Ch4 |
| tracer | 曳光彈 |  | TC Ch8 |
| tracer burnout | 曳光彈燃盡距離 |  | TC Ch10 |
| tracheal deviation | 氣管偏移 | 張力性氣胸晚期徵象 | ATP Ch6 |
| trail team | 殿後伍 |  | TC Ch6 |
| trail／staggered trail | 縱列／交錯縱列 | 空中突擊隊形 | TC Ch14 |
| training board | 訓練圖板 | 課目要點圖卡，圖 A-1～A-14 皆屬此類 | TC 附A |
| trains | 後勤梯隊 |  | TC Ch2 |
| trajectory | 彈道 |  | TC Ch10 |
| transmission line | 傳輸線 |  | TC Ch4 |
| transmission line／branch line | 傳爆線／分支線 |  | TC Ch5 |
| transport-tightening system／transport knot | 運輸收緊系統／運輸結 |  | TC Ch9 |
| traveling | 行進 | 不太可能接觸 | TC Ch6 |
| traveling overwatch | 行進監視 | 可能接觸；最常用 | TC Ch6 |
| traverse and elevation mechanism (T&E) | 方向與高低機 |  | TC Ch10 |
| traverse and search | 橫移縱深射擊 |  | TC Ch10 |
| traversing slide lock lever | 橫移滑軌鎖定桿 |  | TC Ch10 |
| trench foot / immersion foot | 壕溝足 / 浸泡足 | 非凍結性；32–60°F 超過 12 小時 | ATP Ch17 |
| triage | 檢傷分類 | 沿用第 7 章 | TC Ch15 |
| triage triangle | 檢傷三角形 | 開設傷患集中點的一種編排方式 | TC Ch15 |
| TRP (target reference point) | 目標參考點 |  | TC Ch2 |
| TTLODAC | 目標、觸發條件、位置、觀測員、投射系統、攻擊指導、通信網路 | 縮寫保留不譯 | TC Ch2、Ch3 |
| TTT (time to target) | 至目標時間 |  | TC Ch3 |
| turn／round turn | 繞圈／繞一圈半 |  | TC Ch9 |
| two-Ranger search technique | 雙人搜索技巧 |  | TC Ch7 |
| Tyrolean traverse | 泰洛林橫渡法 |  | TC Ch9 |

## U

| 原文 | 譯文 | 說明 | 出處 |
|---|---|---|---|
| U.S. Army Ranger School | 美國陸軍遊騎兵學校 | 本書的主要使用對象 | TC 前言 |
| UAS (unmanned aircraft system) | 無人機系統 |  | TC Ch3 |
| unbloused (pant leg) | 褲管不紮入靴 |  | TC Ch12 |
| unequal pupils | 瞳孔不等大 | 頭部傷勢徵象 | ATP Ch11 |
| unexploded explosive ordnance | 未爆彈藥 |  | TC 附B |
| universal sign for choking | 哽塞通用手勢 |  | ATP Ch5 |
| urban operations | 城鎮作戰 | 本章主題 | TC Ch11 |
| urticating caterpillar | 刺毛毛蟲 |  | ATP Ch16 |

## V

| 原文 | 譯文 | 說明 | 出處 |
|---|---|---|---|
| vasodilation | 血管擴張 |  | ATP Ch7 |
| VCS (vehicle control system) | 車輛管制系統 | 原文展開如此，但列於職責分工，語意存疑（見譯註） | TC Ch13 |
| vector | 病媒 | 蜱、蚤、蚊 | ATP Ch19 |
| vehicle commander／truck commander | 車長 |  | TC Ch13 |
| venom | 毒液 | 主動注入體內 | ATP Ch16 |
| vented / non-vented | 附閥式 / 無閥式 |  | ATP Ch6 |
| vented chest seal | 附閥式胸封貼 | 沿用 ATP 4-02.11 | TC Ch15 |
| ventilation | 宣洩（傾訴） | 讓當事人反覆談論其經歷 | ATP Ch20 |
| ventilator | 呼吸器 |  | TC 附B |
| vertical obstacle | 垂直障礙 |  | TC Ch9 |
| violence of action | 猛烈行動 |  | TC Ch7 |
| viper / pit viper | 蝰蛇類 / 頰窩蝮蛇 | 三角頭、熱感應頰窩、長中空活動毒牙 | ATP Ch16 |
| visual acuity | 視力 | Tier 2 快速野戰測試 | ATP Ch10 |
| visual signal | 目視信號 |  | TC Ch6 |
| vital signs | 生命徵象 |  | ATP Ch7 |
| VS-17 signal panel | VS-17 信號布板 | 沿用第 4 章 | TC Ch14 |

## W

| 原文 | 譯文 | 說明 | 出處 |
|---|---|---|---|
| wadding | 填塞物 | 腋下需足量填塞 | ATP Ch14 |
| walking wounded / ambulatory | 可行走傷患 | 可協助搬運擔架或警戒 | ATP Ch15 |
| warfighting function | 作戰功能 |  | TC Ch2 |
| WARNORD (warning order) | 預令 |  | TC Ch1 |
| Warrior ethos | 戰士精神 |  | TC Ch1 |
| water discipline | 飲水紀律 |  | TC Ch6 |
| water submersion chart | 浸水時間表 |  | TC Ch12 |
| water-gel／slurry explosive | 水膠炸藥／漿狀炸藥 |  | TC Ch5 |
| waterborne operations | 水上作戰 | 本章主題 | TC Ch12 |
| waterborne uniform | 水上服裝 |  | TC Ch12 |
| watercraft | 小艇 |  | TC Ch12 |
| watering party | 取水組 |  | TC Ch7 |
| wavelength | 波長 | 1/4、1/2、全波長 | TC Ch4 |
| well-aimed fire | 精準瞄準射擊 |  | TC Ch8 |
| wet／dry crossing | 濕式／乾式渡越 |  | TC Ch9 |
| wheel bug | 輪獵蝽 |  | ATP Ch16 |
| whip antenna | 鞭狀天線 |  | TC Ch4 |
| white phosphorus (WP) | 白磷 | **可溶於油，不可用油脂滅火** | ATP Ch19 |
| wind chill | 風寒效應 |  | ATP Ch17 |
| wind sprints | 折返衝刺 | 高風險訓練型態 | ATP Ch18 |
| windlass | 絞棒 | 扭轉收緊的桿件 | ATP Ch4 |
| windpipe | 氣管 |  | ATP Ch5 |
| wound packing | 傷口填塞 |  | ATP Ch4 |
| WSL (weapons squad leader) | 武器班班長 |  | TC Ch1 |

## Z

| 原文 | 譯文 | 說明 | 出處 |
|---|---|---|---|
| Z-pulley system | Z 形滑輪系統 | 3 比 1 機械利益 | TC Ch9 |
| zero (iron sights) | 歸零（機械瞄具） |  | TC Ch10 |
| Zulu (Z) / Local (L) time | 祖魯時間 / 當地時間 | 24 小時制 | ATP Ch15 |
| Zulu time | 祖魯時間 | 格林威治標準時間 | TC Ch2 |

---

*自章末術語對照表彙整，共 1238 條；其中 4 條在不同章節有不同譯文寫法（見上方說明）。*
