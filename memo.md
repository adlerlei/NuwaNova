

# NuwaNōva 備忘錄（截至 2025/04/29）

---

## 目前完成的進度

- 建立了 GitHub 倉庫 NuwaNova
- 撰寫並上傳 README.md（以英文為主，繁體中文、簡體中文、日文輔助）
- 確立專案風格：簡潔、乾淨、極簡主義

---

## NuwaNōva Weave（Web伺服器環境）

- 完成 server.py，具備以下功能：
  - 啟動本地 HTTP 伺服器（使用 Python http.server）
  - 讀取 weave.nuwa 腳本
  - 解析 route 與 respond 指令
  - 根據網址路徑回應對應文字
  - 未定義路徑則回應 404

- weave.nuwa 目前內容：
  ```
  route '/'
  respond '這是首頁'

  route '/about'
  respond '這是關於頁面'

  route '/contact'
  respond '這是聯絡頁面'
  ```

- 本地測試流程：
  ```
  cd nuwanova_weave
  python server.py
  ```
  然後在瀏覽器打開 http://localhost:8000 測試路由功能

---

## 下一步可接續項目

- 增加 HTML 回應支援
- 支援 URL 查詢參數（如 /hello?name=小明）
- 設計並實作互動指令（input, save 等）
- 規劃並撰寫 NuwaNōva Language 的正式語法規範
- 長期目標：拓展至前端互動、行動 App、遊戲開發引擎等領域

---

## 備註

此備忘錄將作為未來開新視窗時的接續依據。  
NuwaNōva 的創世之路，從這裡開始。