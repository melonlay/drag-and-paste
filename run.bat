@echo off
chcp 65001 >nul
echo Starting Text File Drag and Drop Tool...
echo 啟動文字檔案拖拽工具...
echo.

REM Check if Python is installed
REM 檢查Python是否已安裝
python --version >nul 2>&1
if errorlevel 1 (
    echo Error: Python not found, please install Python first
    echo 錯誤：未找到Python，請先安裝Python
    pause
    exit /b 1
)

REM Start the program
REM 啟動程式
python main.py

REM If program exits with error, show error message
REM 如果程式異常退出，顯示錯誤訊息
if errorlevel 1 (
    echo.
    echo An error occurred while running the program
    echo 程式執行時發生錯誤
    echo Please check if required dependencies are installed
    echo 請檢查是否已安裝所需的依賴套件
    echo You can run install.bat to install dependencies
    echo 可以執行 install.bat 來安裝依賴
    echo.
    pause
) 