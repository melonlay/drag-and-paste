#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
文字檔案拖拽工具
支援拖拽文字檔案到程式中，顯示檔案列表和內容
"""

import sys
import os

# 將當前目錄加入Python路徑
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from gui.main_window import MainWindow


def main():
    """主程式入口"""
    try:
        # 創建並執行主視窗
        app = MainWindow()
        app.run()
    except KeyboardInterrupt:
        print("\n程式被使用者中斷")
    except Exception as e:
        print(f"程式執行錯誤: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    main() 