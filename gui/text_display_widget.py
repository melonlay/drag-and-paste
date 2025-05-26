# -*- coding: utf-8 -*-
import tkinter as tk
from tkinter import ttk, messagebox
import pyperclip
from typing import Callable, Optional
from utils.i18n import i18n


class TextDisplayWidget:
    """文字顯示元件"""
    
    def __init__(self, parent):
        self.parent = parent
        
        # 創建主框架
        self.frame = ttk.LabelFrame(parent, text=i18n.get_text("text_content_title"), padding="5")
        
        # 創建文字區域框架
        text_frame = ttk.Frame(self.frame)
        text_frame.pack(fill=tk.BOTH, expand=True)
        
        # 創建文字框和滾動條
        self.text_widget = tk.Text(
            text_frame, 
            wrap=tk.WORD, 
            state=tk.DISABLED,
            font=('Consolas', 10),
            bg='white',
            fg='black'
        )
        
        # 垂直滾動條
        v_scrollbar = ttk.Scrollbar(text_frame, orient=tk.VERTICAL, command=self.text_widget.yview)
        self.text_widget.configure(yscrollcommand=v_scrollbar.set)
        
        # 水平滾動條
        h_scrollbar = ttk.Scrollbar(text_frame, orient=tk.HORIZONTAL, command=self.text_widget.xview)
        self.text_widget.configure(xscrollcommand=h_scrollbar.set)
        
        # 佈局文字框和滾動條
        self.text_widget.grid(row=0, column=0, sticky='nsew')
        v_scrollbar.grid(row=0, column=1, sticky='ns')
        h_scrollbar.grid(row=1, column=0, sticky='ew')
        
        # 設定grid權重
        text_frame.grid_rowconfigure(0, weight=1)
        text_frame.grid_columnconfigure(0, weight=1)
        
        # 創建按鈕框架
        button_frame = ttk.Frame(self.frame)
        button_frame.pack(fill=tk.X, pady=(5, 0))
        
        # 創建複製按鈕
        self.copy_btn = ttk.Button(
            button_frame, 
            text=i18n.get_text("copy_content"), 
            command=self._on_copy_clicked
        )
        self.copy_btn.pack(side=tk.LEFT)
        
        # 創建清空按鈕
        self.clear_btn = ttk.Button(
            button_frame, 
            text=i18n.get_text("clear_content"), 
            command=self._on_clear_clicked
        )
        self.clear_btn.pack(side=tk.LEFT, padx=(5, 0))
        
        # 狀態標籤
        self.status_label = ttk.Label(button_frame, text="")
        self.status_label.pack(side=tk.RIGHT)
        
        # 回調函數
        self.on_clear_callback = None
        
        # 註冊為觀察者
        i18n.add_observer(self)
    
    def pack(self, **kwargs):
        """包裝pack方法"""
        self.frame.pack(**kwargs)
    
    def grid(self, **kwargs):
        """包裝grid方法"""
        self.frame.grid(**kwargs)
    
    def set_content(self, content: str):
        """
        設定文字內容
        
        Args:
            content (str): 要顯示的文字內容
        """
        self.text_widget.config(state=tk.NORMAL)
        self.text_widget.delete(1.0, tk.END)
        self.text_widget.insert(1.0, content)
        self.text_widget.config(state=tk.DISABLED)
        
        # 更新狀態
        lines = content.count('\n') + 1 if content else 0
        chars = len(content)
        self.status_label.config(text=i18n.get_text("lines_chars", lines, chars))
    
    def get_content(self) -> str:
        """
        取得文字內容
        
        Returns:
            str: 文字內容
        """
        return self.text_widget.get(1.0, tk.END).rstrip('\n')
    
    def clear_content(self):
        """清空文字內容"""
        self.text_widget.config(state=tk.NORMAL)
        self.text_widget.delete(1.0, tk.END)
        self.text_widget.config(state=tk.DISABLED)
        self.status_label.config(text="")
    
    def append_content(self, content: str):
        """
        追加文字內容
        
        Args:
            content (str): 要追加的文字內容
        """
        self.text_widget.config(state=tk.NORMAL)
        if self.text_widget.get(1.0, tk.END).strip():
            self.text_widget.insert(tk.END, "\n\n")
        self.text_widget.insert(tk.END, content)
        self.text_widget.config(state=tk.DISABLED)
        
        # 自動滾動到底部
        self.text_widget.see(tk.END)
        
        # 更新狀態
        full_content = self.get_content()
        lines = full_content.count('\n') + 1 if full_content else 0
        chars = len(full_content)
        self.status_label.config(text=i18n.get_text("lines_chars", lines, chars))
    
    def set_clear_callback(self, callback: Callable):
        """設定清空回調函數"""
        self.on_clear_callback = callback
    
    def _on_copy_clicked(self):
        """複製按鈕點擊事件"""
        content = self.get_content()
        if content.strip():
            try:
                pyperclip.copy(content)
                messagebox.showinfo(
                    i18n.get_text("success"), 
                    i18n.get_text("content_copied")
                )
            except Exception as e:
                messagebox.showerror(
                    i18n.get_text("error"), 
                    i18n.get_text("copy_failed", str(e))
                )
        else:
            messagebox.showwarning(
                i18n.get_text("warning"), 
                i18n.get_text("no_content_to_copy")
            )
    
    def _on_clear_clicked(self):
        """清空按鈕點擊事件"""
        if self.get_content().strip():
            result = messagebox.askyesno(
                i18n.get_text("confirm"), 
                i18n.get_text("confirm_clear_content")
            )
            if result:
                if self.on_clear_callback:
                    self.on_clear_callback()
                else:
                    self.clear_content()
    
    def on_language_changed(self):
        """語言變更通知（觀察者模式）"""
        # 更新框架標題
        self.frame.config(text=i18n.get_text("text_content_title"))
        
        # 更新按鈕文字
        self.copy_btn.config(text=i18n.get_text("copy_content"))
        self.clear_btn.config(text=i18n.get_text("clear_content"))
        
        # 更新狀態標籤（如果有內容的話）
        content = self.get_content()
        if content:
            lines = content.count('\n') + 1
            chars = len(content)
            self.status_label.config(text=i18n.get_text("lines_chars", lines, chars))
    
    def destroy(self):
        """銷毀元件時移除觀察者"""
        i18n.remove_observer(self)
        self.frame.destroy() 