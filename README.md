# 個人課表

使用 Django 和 SQLite 製作的個人課表。

## 執行方式

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

開啟 http://127.0.0.1:8000/。資料保存在本機 db.sqlite3，不會上傳至 GitHub。此版本供本機個人使用。
