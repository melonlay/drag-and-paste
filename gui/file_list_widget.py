# -*- coding: utf-8 -*-
import tkinter as tk
from tkinter import ttk, messagebox
from typing import Callable, Optional
from utils.i18n import i18n


class FileListWidget:
    """檔案列表元件"""
    
    def __init__(self, parent, on_delete_callback: Optional[Callable] = None):
        self.parent = parent
        self.on_delete_callback = on_delete_callback
        
        # 創建主框架
        self.frame = ttk.LabelFrame(parent, text=i18n.get_text("file_list_title"), padding="5")
        
        # 創建列表框架
        list_frame = ttk.Frame(self.frame)
        list_frame.pack(fill=tk.BOTH, expand=True)
        
        # 創建列表框和滾動條
        self.listbox = tk.Listbox(list_frame, selectmode=tk.SINGLE)
        scrollbar = ttk.Scrollbar(list_frame, orient=tk.VERTICAL, command=self.listbox.yview)
        self.listbox.configure(yscrollcommand=scrollbar.set)
        
        # 佈局列表框和滾動條
        self.listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        # 創建按鈕框架
        button_frame = ttk.Frame(self.frame)
        button_frame.pack(fill=tk.X, pady=(5, 0))
        
        # 創建按鈕
        self.delete_btn = ttk.Button(
            button_frame, 
            text=i18n.get_text("delete_selected"), 
            command=self._on_delete_clicked
        )
        self.delete_btn.pack(side=tk.LEFT, padx=(0, 5))
        
        self.restore_btn = ttk.Button(
            button_frame, 
            text=i18n.get_text("restore"), 
            command=self._on_restore_clicked
        )
        self.restore_btn.pack(side=tk.LEFT, padx=(0, 5))
        
        self.clear_btn = ttk.Button(
            button_frame, 
            text=i18n.get_text("clear"), 
            command=self._on_clear_clicked
        )
        self.clear_btn.pack(side=tk.LEFT)
        
        # 綁定雙擊事件
        self.listbox.bind('<Double-Button-1>', self._on_double_click)
        
        # 回調函數
        self.on_restore_callback = None
        self.on_clear_callback = None
        
        # 註冊為觀察者
        i18n.add_observer(self)
    
    def pack(self, **kwargs):
        """包裝pack方法"""
        self.frame.pack(**kwargs)
    
    def grid(self, **kwargs):
        """包裝grid方法"""
        self.frame.grid(**kwargs)
    
    def add_file(self, filename: str):
        """
        新增檔案到列表
        
        Args:
            filename (str): 檔案名稱
        """
        self.listbox.insert(tk.END, filename)
        # 自動選中最新新增的項目
        self.listbox.selection_clear(0, tk.END)
        self.listbox.selection_set(tk.END)
        self.listbox.see(tk.END)
    
    def remove_selected(self) -> Optional[int]:
        """
        移除選中的檔案
        
        Returns:
            Optional[int]: 被移除項目的索引，如果沒有選中項目則返回None
        """
        selection = self.listbox.curselection()
        if selection:
            index = selection[0]
            self.listbox.delete(index)
            return index
        return None
    
    def clear_all(self):
        """清空所有項目"""
        self.listbox.delete(0, tk.END)
    
    def get_selected_index(self) -> Optional[int]:
        """
        取得選中項目的索引
        
        Returns:
            Optional[int]: 選中項目的索引，如果沒有選中則返回None
        """
        selection = self.listbox.curselection()
        return selection[0] if selection else None
    
    def get_item_count(self) -> int:
        """
        取得項目數量
        
        Returns:
            int: 項目數量
        """
        return self.listbox.size()
    
    def insert_file(self, index: int, filename: str):
        """
        在指定位置插入檔案
        
        Args:
            index (int): 插入位置
            filename (str): 檔案名稱
        """
        self.listbox.insert(index, filename)
    
    def set_restore_callback(self, callback: Callable):
        """設定復原回調函數"""
        self.on_restore_callback = callback
    
    def set_clear_callback(self, callback: Callable):
        """設定清空回調函數"""
        self.on_clear_callback = callback
    
    def _on_delete_clicked(self):
        """刪除按鈕點擊事件"""
        if self.on_delete_callback:
            self.on_delete_callback()
    
    def _on_restore_clicked(self):
        """復原按鈕點擊事件"""
        if self.on_restore_callback:
            self.on_restore_callback()
    
    def _on_clear_clicked(self):
        """清空按鈕點擊事件"""
        if self.get_item_count() > 0:
            result = messagebox.askyesno(
                i18n.get_text("confirm"), 
                i18n.get_text("confirm_clear_files")
            )
            if result and self.on_clear_callback:
                self.on_clear_callback()
    
    def _on_double_click(self, event):
        """雙擊事件處理"""
        # 雙擊時刪除項目
        if self.on_delete_callback:
            self.on_delete_callback()
    
    def on_language_changed(self):
        """語言變更通知（觀察者模式）"""
        # 更新框架標題
        self.frame.config(text=i18n.get_text("file_list_title"))
        
        # 更新按鈕文字
        self.delete_btn.config(text=i18n.get_text("delete_selected"))
        self.restore_btn.config(text=i18n.get_text("restore"))
        self.clear_btn.config(text=i18n.get_text("clear"))
    
    def destroy(self):
        """銷毀元件時移除觀察者"""
        i18n.remove_observer(self)
        self.frame.destroy() 