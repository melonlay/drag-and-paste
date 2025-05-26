@echo off
chcp 65001 >nul
echo Installing dependencies for Text File Drag and Drop Tool...
echo 正在安裝文字檔案拖拽工具的依賴套件...
echo.

REM Check if Python is installed
REM 檢查Python是否已安裝
python --version >nul 2>&1
if errorlevel 1 (
    echo Error: Python not found, please install Python 3.7 or higher
    echo 錯誤：未找到Python，請先安裝Python 3.7或更高版本
    echo Download: https://www.python.org/downloads/
    echo 下載地址：https://www.python.org/downloads/
    pause
    exit /b 1
)

echo Python version / Python版本：
python --version
echo.

REM Upgrade pip
REM 升級pip
echo Upgrading pip... / 正在升級pip...
python -m pip install --upgrade pip

REM Install dependencies
REM 安裝依賴套件
echo Installing dependencies... / 正在安裝依賴套件...
pip install -r requirements.txt

if errorlevel 1 (
    echo.
    echo Installation failed, please check network connection or install manually:
    echo 安裝失敗，請檢查網路連線或手動安裝：
    echo pip install tkinterdnd2==0.3.0
    echo pip install pyperclip==1.8.2
    pause
    exit /b 1
)

echo.
echo Installation completed! / 安裝完成！
echo You can now run: python main.py
echo 現在可以執行：python main.py
echo.
pause 