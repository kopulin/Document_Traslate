import { defineConfig } from 'vitepress'

const CH = '/atp-4-02.11/'

export default defineConfig({
  lang: 'zh-TW',
  title: 'ATP 4-02.11 繁體中文譯本',
  description:
    'ATP 4-02.11《傷患處置：戰術戰傷救護與急救》2026 年 3 月版逐章繁體中文翻譯，僅供訓練參考。',

  base: '/Document_Traslate/',
  cleanUrls: true,
  lastUpdated: true,

  head: [
    ['link', { rel: 'preconnect', href: 'https://fonts.googleapis.com' }],
    ['link', { rel: 'preconnect', href: 'https://fonts.gstatic.com', crossorigin: '' }],
    ['link', {
      href: 'https://fonts.googleapis.com/css2?family=IBM+Plex+Sans:wght@300;400;600&family=IBM+Plex+Mono:wght@400;600&display=swap',
      rel: 'stylesheet'
    }]
  ],

  themeConfig: {
    siteTitle: 'ATP 4-02.11 中譯本',
    nav: [
      { text: '首頁', link: '/' },
      { text: '第 1 章', link: `${CH}01-casualty-response` },
      { text: '原文勘誤', link: '/errata' }
    ],

    sidebar: [
      {
        text: 'PART ONE — 傷患處置',
        collapsed: false,
        items: [
          { text: '01｜傷患處置', link: `${CH}01-casualty-response` },
          { text: '02｜傷患脫離與搬運', link: `${CH}02-extraction-movement` }
        ]
      },
      {
        text: 'PART TWO — 戰術戰傷救護',
        collapsed: false,
        items: [
          { text: '03｜戰術戰傷救護基礎', link: `${CH}03-tccc-fundamentals` },
          { text: '04｜大量出血控制（M）', link: `${CH}04-massive-bleeding` },
          { text: '05｜呼吸道控制（A）', link: `${CH}05-airway` },
          { text: '06｜呼吸與換氣控制（R）', link: `${CH}06-respiration-ventilation` },
          { text: '07｜循環控制（C）', link: `${CH}07-circulation` },
          { text: '08｜低體溫控制（H）', link: `${CH}08-hypothermia` },
          { text: '09｜二次傷勢評估', link: `${CH}09-secondary-assessment` },
          { text: '10｜眼部創傷', link: `${CH}10-eye-trauma` },
          { text: '11｜頭部傷勢', link: `${CH}11-head-injury` },
          { text: '12｜燒傷', link: `${CH}12-burns` },
          { text: '13｜骨折與固定', link: `${CH}13-fractures-splinting` },
          { text: '14｜其他二次傷勢的應急技術', link: `${CH}14-other-field-techniques` },
          { text: '15｜傷患監測與後送準備', link: `${CH}15-monitoring-evac-prep` }
        ]
      },
      {
        text: 'PART THREE — 特定傷病照護',
        collapsed: false,
        items: [
          { text: '16｜叮咬與螫傷', link: `${CH}16-bites-stings` },
          { text: '17｜氣候與環境傷害', link: `${CH}17-environmental-injuries` },
          { text: '18｜鐮刀型血球特徵', link: `${CH}18-sickle-cell-trait` },
          { text: '19｜CBRN 環境急救', link: `${CH}19-cbrn-first-aid` },
          { text: '20｜戰鬥與作戰壓力控制', link: `${CH}20-combat-operational-stress` }
        ]
      },
      {
        text: '附錄',
        collapsed: false,
        items: [
          { text: 'A｜急救包與核定醫材清單', link: `${CH}app-a-aid-kits-amal` },
          { text: 'B｜救援裝備', link: `${CH}app-b-rescue-equipment` }
        ]
      },
      {
        text: '其他',
        collapsed: false,
        items: [
          { text: '原文勘誤彙整', link: '/errata' }
        ]
      }
    ],

    search: {
      provider: 'local',
      options: {
        locales: {
          root: {
            translations: {
              button: { buttonText: '搜尋', buttonAriaLabel: '搜尋' },
              modal: {
                displayDetails: '顯示詳情',
                noResultsText: '找不到相關內容',
                resetButtonTitle: '清除查詢',
                footer: { selectText: '選擇', navigateText: '切換', closeText: '關閉' }
              }
            }
          }
        }
      }
    },

    outline: { label: '本頁目錄', level: [2, 3] },
    docFooter: { prev: '上一章', next: '下一章' },
    darkModeSwitchLabel: '深色模式',
    lightModeSwitchTitle: '切換至淺色模式',
    darkModeSwitchTitle: '切換至深色模式',
    returnToTopLabel: '回到頂部',
    sidebarMenuLabel: '選單',
    lastUpdatedText: '最後更新',

    footer: {
      message:
        '原文為美國陸軍公開刊物（ATP 4-02.11，U.S. Government work，公有領域）。本站僅提供非官方繁體中文翻譯，僅供訓練參考，實際操作一律以英文原文為準。',
      copyright: '譯文 © 2026 kopulin｜依原文授權以公有領域方式釋出'
    }
  },

  markdown: {
    lineNumbers: false
  }
})
