#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
這是一個測試用的Python檔案
用於測試拖拽功能是否正常工作
"""

def hello_world():
    """簡單的Hello World函數"""
    print("Hello, World!")
    print("這是一個測試檔案")
    return "Success"

def calculate_sum(a, b):
    """計算兩個數字的和"""
    result = a + b
    print(f"{a} + {b} = {result}")
    return result

if __name__ == "__main__":
    hello_world()
    calculate_sum(10, 20)
    
    # 測試中文字元
    print("測試中文字元顯示")
    print("這個檔案可以用來測試拖拽功能") 