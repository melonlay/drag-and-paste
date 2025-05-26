# -*- coding: utf-8 -*-
"""
語言選擇元件
提供語言切換下拉選單
"""

import tkinter as tk
from tkinter import ttk
from utils.i18n import i18n


class LanguageSelector:
    """語言選擇器元件"""
    
    def __init__(self, parent):
        self.parent = parent
        
        # 創建框架
        self.frame = ttk.Frame(parent)
        
        # 創建標籤
        self.label = ttk.Label(self.frame, text=i18n.get_text("language"))
        self.label.pack(side=tk.LEFT, padx=(0, 5))
        
        # 創建下拉選單
        self.language_var = tk.StringVar()
        self.combobox = ttk.Combobox(
            self.frame,
            textvariable=self.language_var,
            state="readonly",
            width=10
        )
        self.combobox.pack(side=tk.LEFT)
        
        # 設定語言選項
        self._update_language_options()
        
        # 設定當前語言
        current_lang = i18n.get_current_language()
        self.language_var.set(i18n.get_text("chinese" if current_lang == "zh_TW" else "english"))
        
        # 綁定選擇事件
        self.combobox.bind('<<ComboboxSelected>>', self._on_language_changed)
        
        # 註冊為觀察者
        i18n.add_observer(self)
    
    def pack(self, **kwargs):
        """包裝pack方法"""
        self.frame.pack(**kwargs)
    
    def grid(self, **kwargs):
        """包裝grid方法"""
        self.frame.grid(**kwargs)
    
    def _update_language_options(self):
        """更新語言選項"""
        languages = i18n.get_available_languages()
        self.combobox['values'] = list(languages.values())
    
    def _on_language_changed(self, event=None):
        """語言選擇變更事件"""
        selected_text = self.language_var.get()
        
        # 根據選擇的文字確定語言代碼
        if "中文" in selected_text:
            i18n.set_language("zh_TW")
        else:
            i18n.set_language("en_US")
    
    def on_language_changed(self):
        """語言變更通知（觀察者模式）"""
        # 更新標籤文字
        self.label.config(text=i18n.get_text("language"))
        
        # 更新下拉選單選項
        self._update_language_options()
        
        # 更新當前選擇
        current_lang = i18n.get_current_language()
        self.language_var.set(i18n.get_text("chinese" if current_lang == "zh_TW" else "english"))
    
    def destroy(self):
        """銷毀元件時移除觀察者"""
        i18n.remove_observer(self)
        self.frame.destroy() 