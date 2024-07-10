@ECHO OFF
::SET /A postgres_service=postgresql-x64-16
::net stop %postgres_service%
SET "pg_version=15"
SET "pg_folder_path=C:\Program Files\PostgreSQL"
SET "pg_data_path=%pg_folder_path%\%pg_version%\data"

ECHO All Postgres Versions:
setlocal enabledelayedexpansion
CD %pg_folder_path%
for /d %%i in ("%pg_folder_path%\*") do (
    SET "folderName=%%~nxi"
    ECHO !folderName!
)
endlocal
ECHO Current Path:
ECHO %pg_data_path%
pg_ctl -D %pg_data_path% pause

PAUSE
