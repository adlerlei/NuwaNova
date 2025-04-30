# NuwaNōva 備忘錄（截至 2025/04/29）

---

## 目前完成的進度

- 建立了 GitHub 倉庫 NuwaNova
- 撰寫並上傳 README.md（以英文為主，繁體中文、簡體中文、日文輔助）
- 確立專案風格：簡潔、乾淨、極簡主義
- 完成 NuwaNōva 語法 v0.1 初版定義（url, say, show）
- 建立語法說明文件：`docs/NUWANOVA_SYNTAX.md`
- 建立專案架構說明文件：`docs/PROJECT_STRUCTURE.md`
- 建立 anima 靜態資源命名結構文件：`docs/ANIMA_STRUCTURE.md`
- 設計並實作 `anima/` 資料夾，細分為：
  - `Inksoul/`：CSS（墨魂）風格樣式表
  - `Pulse/`：JavaScript（脈動）行為邏輯
  - `TrueShape/`：圖片素材（真形）圖像載體

---

## NuwaNōva Weave（Web伺服器環境）

- 完成 server.py，具備以下功能：
  - 啟動本地 HTTP 伺服器（使用 Python http.server）
  - 讀取 weave.nuwa 腳本
  - 解析 `url`、`say`、`show` 指令
  - 根據網址路徑回應純文字或 HTML 頁面
  - 靜態資源支援 `/anima/` 路徑（對應 CSS、JS、圖片）
  - 未定義路徑則回應 404

- weave.nuwa 目前內容：
  ```
  url '/'
  say '這是首頁'

  url '/about'
  show 'about.html'

  url '/contact'
  show 'contact.html'
  ```

- 本地測試流程：
  ```
  cd nuwanova_weave
  python server.py
  ```
  然後在瀏覽器打開 http://localhost:8000 測試路由與靜態資源

---

## 備註

此備忘錄將作為未來開新視窗時的接續依據。  
NuwaNōva 的語言世界、頁面靈魂與邏輯脈動，已正式誕生。

 接下來你可以考慮的下一步方向有三條路：

⸻

① ✨ 語法功能擴展（NuwaNōva Language 層）

增強 .nuwa 腳本語言的能力，例如：
	•	新增 input（接受使用者輸入）
	•	save / load（寫入或讀取伺服器端資料）
	•	支援 URL 參數（如 /hello?name=小明）
	•	建立變數、條件、區塊（未來走向 DSL）

📈 適合你想往「創造語言」核心邏輯邁進

⸻

② 🌐 頁面互動開發（anima 結構發揮）

開始寫：
	•	CSS 動畫效果（Inksoul）
	•	JavaScript DOM 操作（Pulse）
	•	建立互動頁面或小範例（結合 HTML + JS + CSS）

📈 適合你想讓整體 demo 更豐富有「靈魂與表現力」

⸻

③ 📦 進入模板系統（show 的進階版）

設計一套簡單的：
	•	{var} 替換邏輯 → 讓 HTML 可以使用 NuwaNōva 傳遞變數
	•	將 show 升級為 render，可帶入變數
	•	將 server.py 功能逐步模組化

📈 適合你想讓 NuwaNōva 更像一個真正的 backend 框架