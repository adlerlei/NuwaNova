

# NuwaNōva 開發日誌

---

## 2025-04-30

### ✅ 完成事項
- 設定 `anima/` 靜態資源結構：
  - `Inksoul/`：CSS
  - `Pulse/`：JavaScript
  - `TrueShape/`：圖像資源
- `server.py` 支援 `/anima/` 資源讀取與傳送
- 加入 MIME 類型自動判斷功能，讓 CSS/JS/圖片能被瀏覽器正確識別
- 寫入 `ANIMA_STRUCTURE.md` 靜態資源命名說明

### 🛠️ 修改檔案
- `server.py`
- `docs/ANIMA_STRUCTURE.md`
- `docs/PROJECT_STRUCTURE.md`
- `memo.md`

---

## 2025-04-29

### ✅ 完成事項
- 定義 NuwaNōva 基礎語法（url / say / show）
- 實作 `.nuwa` 語法解析並建立基礎路由功能
- 建立範例腳本 `weave.nuwa`
- 完成基本伺服器程式 `server.py` 測試通過
- 建立語法說明與專案結構文件

### 🛠️ 修改檔案
- `server.py`
- `weave.nuwa`
- `docs/NUWANOVA_SYNTAX.md`
- `docs/PROJECT_STRUCTURE.md`
- `memo.md`