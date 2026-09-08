# Debugging and Testing

Use the project virtual environment from the repository root:

```powershell
Set-Location 'G:\Projects\Python_Projects\Learning_Log'
& '.\.pwsh\Scripts\Activate.ps1'
Set-Location '.\ll_project'
```

Run Django's configuration checks:

```powershell
python manage.py check
python manage.py makemigrations --check --dry-run
```

Run all tests:

```powershell
python manage.py test -v 2
```

Run only one app:

```powershell
python manage.py test learning_logs -v 2
python manage.py test accounts -v 2
```

Run one test method:

```powershell
python manage.py test learning_logs.tests.LearningLogsViewTests.test_owner_can_create_entry -v 2
```

Start the local development server:

```powershell
python manage.py runserver
```

Open `http://127.0.0.1:8000/` in a browser. Django is configured with `DEBUG = True`, so unhandled development errors include a detailed traceback.

For a terminal breakpoint, add `breakpoint()` to a view, start the server, and visit its URL. Useful debugger commands are `p variable`, `n`, `s`, `c`, and `q`.

For VS Code, open the repository root and press `F5`. Select either `Django: Debug server` or `Django: Run tests`. The debug configuration uses `.pwsh\Scripts\python.exe`; `--noreload` prevents the Django auto-reloader from creating a second process that can bypass breakpoints.
