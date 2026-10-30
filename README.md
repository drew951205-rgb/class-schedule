# 個人課表維護功能

使用 Python、Django 和 SQLite 建立的個人課表。支援星期一至星期日、第 1 至第 9 節的課程管理。

## 功能

- 新增、查看、修改與刪除課程。
- 一次選擇開始與結束節次，課表自動顯示連續課程。
- 檢查節次衝突，顯示星期、時間與教室。
- 點選課程卡片查看老師等詳細資料。

## Windows 現場演示

需要已安裝 Python（此專案曾以 Python 3.13 測試）、Git，並可連線下載 Python 套件。開啟 PowerShell 後依序執行：

```powershell
git clone https://github.com/drew951205-rgb/class-schedule.git
cd class-schedule
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe manage.py migrate
.\.venv\Scripts\python.exe manage.py load_demo
.\.venv\Scripts\python.exe manage.py runserver
```

用瀏覽器開啟 http://127.0.0.1:8000/ 。執行 `load_demo` 可以在空白課表建立虛構的示範課程；若已有課程，此指令不會新增、刪除或覆蓋資料。按 `Ctrl + C` 可停止伺服器。

資料保存在專案資料夾的 `db.sqlite3`，不會上傳至 GitHub。換電腦或重新下載專案後需要重新建立資料庫及示範資料。請勿在公開網路環境使用本地開發設定。

## 檢查與測試

```powershell
.\.venv\Scripts\python.exe manage.py check
.\.venv\Scripts\python.exe manage.py test
```

若遇到問題，先確認目前位於專案資料夾、套件安裝成功且已執行 `migrate`，再查看執行伺服器的終端機錯誤訊息。

## 10 分鐘內演示建議

1. 簡介專案用途、Django 與 SQLite。
2. 顯示週課表及午餐時間，點選課程查看詳細資料。
3. 新增課程，展示連續節次；嘗試新增重疊課程，展示衝突提示。
4. 修改、刪除課程，說明刪除前的確認。
5. 關閉並重新啟動程式，說明資料保存在本機資料庫。
