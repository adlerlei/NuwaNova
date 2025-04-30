# NuwaNōva 專案結構說明

本文件說明 NuwaNōva 專案各資料夾與檔案的用途與邏輯結構。

## 📁 根目錄（NuwaNova）

- `.gitignore`：Git 忽略設定
- `LICENSE`：專案授權條款
- `README.md`：專案簡介
- `memo.md`：開發備忘與筆記
- `.vscode/`：本地開發環境設定（如自動格式化等）
- `docs/`：官方說明文件區（語法、規格、Roadmap 等）
- `nuwanova_language/`：語言核心解析與範例
- `nuwanova_weave/`：伺服器實作與測試用語法執行環境

## 📁 docs/

- `NUWANOVA_SYNTAX.md`：NuwaNōva 語法規範 v0.1
- `README.md`：此文件夾的簡介說明
- `PROJECT_STRUCTURE.md`：你正在看的這份，整體架構與用途說明

## 📁 nuwanova_language/

- `parser.py`：語法解析邏輯（待擴充）
- `examples/weave.nuwa`：語法設計範例

## 📁 nuwanova_weave/

- `server.py`：用於執行 `.nuwa` 腳本的簡易 HTTP 伺服器
- `weave.nuwa`：實際執行測試用的 Nuwa 語法腳本
- `templates/index.html`：靜態 HTML 頁面（透過 `show` 指令載入）

---
此結構設計目的是讓語言核心、教學範例與伺服器實作彼此分離，方便維護與擴充。

# NuwaNōva - `anima/` 靜態資源命名結構說明

`anima/` 是 NuwaNōva 專案中的靜態資源資料夾，  
它象徵網頁的「靈魂容器」，承載視覺、行為與形象的核心能量。

## 📁 anima/Inksoul

- **用途**：放置 CSS 樣式表
- **語意**：「墨魂」——如墨在宣紙上留下的痕跡，為網頁增添風格與詩意
- **代表**：頁面的氣質、色彩、排版與節奏

## 📁 anima/Pulse

- **用途**：放置 JavaScript 腳本
- **語意**：「脈動」——賦予頁面生命與互動的節奏律動
- **代表**：按鈕反應、滾動特效、互動邏輯等

## 📁 anima/TrueShape

- **用途**：放置圖片與圖像素材（如 .png, .jpg, .svg 等）
- **語意**：「真形」——靈魂可視化後顯現的形體
- **代表**：圖標、背景圖、Logo、插圖等視覺實體

---

每個命名都承載著 NuwaNōva 的語言美學與宇宙觀，  
這不僅是檔案分類，更是一種世界觀的編碼。