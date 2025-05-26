# -*- coding: utf-8 -*-
import tkinter as tk
from tkinter import ttk, messagebox
import tkinterdnd2 as tkdnd
import os
from typing import List

from core.file_handler import FileHandler
from gui.file_list_widget import FileListWidget
from gui.text_display_widget import TextDisplayWidget
from gui.language_selector import LanguageSelector
from utils.constants import WINDOW_SIZE, WINDOW_MIN_SIZE
from utils.i18n import i18n


class MainWindow:
    """主視窗類別"""
    
    def __init__(self):
        # 初始化檔案處理器
        self.file_handler = FileHandler()
        
        # 創建主視窗
        self.root = tkdnd.Tk()
        self.root.title(i18n.get_text("window_title"))
        self.root.geometry(WINDOW_SIZE)
        self.root.minsize(*WINDOW_MIN_SIZE)
        
        # 設定視窗圖示（如果有的話）
        try:
            self.root.iconbitmap('icon.ico')
        except:
            pass
        
        # 創建頂部框架（語言選擇器）
        self.top_frame = ttk.Frame(self.root, padding="5")
        self.top_frame.pack(fill=tk.X)
        
        # 創建語言選擇器
        self.language_selector = LanguageSelector(self.top_frame)
        self.language_selector.pack(side=tk.RIGHT)
        
        # 創建主框架
        self.main_frame = ttk.Frame(self.root, padding="10")
        self.main_frame.pack(fill=tk.BOTH, expand=True)
        
        # 創建左右分割的PanedWindow
        self.paned_window = ttk.PanedWindow(self.main_frame, orient=tk.HORIZONTAL)
        self.paned_window.pack(fill=tk.BOTH, expand=True)
        
        # 創建左側框架（檔案列表）
        self.left_frame = ttk.Frame(self.paned_window)
        self.paned_window.add(self.left_frame, weight=1)
        
        # 創建右側框架（文字顯示）
        self.right_frame = ttk.Frame(self.paned_window)
        self.paned_window.add(self.right_frame, weight=2)
        
        # 創建檔案列表元件
        self.file_list_widget = FileListWidget(
            self.left_frame, 
            on_delete_callback=self._on_delete_file
        )
        self.file_list_widget.pack(fill=tk.BOTH, expand=True)
        
        # 設定檔案列表的回調函數
        self.file_list_widget.set_restore_callback(self._on_restore_file)
        self.file_list_widget.set_clear_callback(self._on_clear_all_files)
        
        # 創建文字顯示元件
        self.text_display_widget = TextDisplayWidget(self.right_frame)
        self.text_display_widget.pack(fill=tk.BOTH, expand=True)
        
        # 設定文字顯示的回調函數
        self.text_display_widget.set_clear_callback(self._on_clear_text_content)
        
        # 創建狀態列
        self.status_frame = ttk.Frame(self.root)
        self.status_frame.pack(fill=tk.X, side=tk.BOTTOM)
        
        self.status_label = ttk.Label(
            self.status_frame, 
            text=i18n.get_text("drag_files_hint"),
            relief=tk.SUNKEN
        )
        self.status_label.pack(fill=tk.X, padx=5, pady=2)
        
        # 設定拖拽功能
        self._setup_drag_and_drop()
        
        # 綁定視窗關閉事件
        self.root.protocol("WM_DELETE_WINDOW", self._on_closing)
    
    def _setup_drag_and_drop(self):
        """設定拖拽功能"""
        # 註冊拖拽事件
        self.root.drop_target_register(tkdnd.DND_FILES)
        self.root.dnd_bind('<<Drop>>', self._on_drop)
        
        # 為主要元件也註冊拖拽
        self.file_list_widget.listbox.drop_target_register(tkdnd.DND_FILES)
        self.file_list_widget.listbox.dnd_bind('<<Drop>>', self._on_drop)
        
        self.text_display_widget.text_widget.drop_target_register(tkdnd.DND_FILES)
        self.text_display_widget.text_widget.dnd_bind('<<Drop>>', self._on_drop)
    
    def _on_drop(self, event):
        """處理拖拽事件"""
        # 取得拖拽的檔案列表
        files = self._parse_drop_files(event.data)
        
        for file_path in files:
            self._add_file(file_path)
    
    def _parse_drop_files(self, data: str) -> List[str]:
        """
        解析拖拽的檔案資料
        
        Args:
            data (str): 拖拽事件的資料
            
        Returns:
            List[str]: 檔案路徑列表
        """
        # 處理Windows路徑格式
        files = []
        if data.startswith('{') and data.endswith('}'):
            # 多個檔案的格式: {file1} {file2} ...
            data = data[1:-1]  # 移除大括號
            current_file = ""
            in_quotes = False
            
            i = 0
            while i < len(data):
                char = data[i]
                if char == '"':
                    in_quotes = not in_quotes
                elif char == ' ' and not in_quotes:
                    if current_file.strip():
                        files.append(current_file.strip().strip('"'))
                        current_file = ""
                else:
                    current_file += char
                i += 1
            
            if current_file.strip():
                files.append(current_file.strip().strip('"'))
        else:
            # 單個檔案
            files = [data.strip().strip('{}').strip('"')]
        
        return files
    
    def _add_file(self, file_path: str):
        """
        新增檔案到列表
        
        Args:
            file_path (str): 檔案路徑
        """
        success, message = self.file_handler.add_file(file_path)
        
        if success:
            # 新增到GUI列表
            filename = os.path.basename(file_path)
            self.file_list_widget.add_file(filename)
            
            # 更新文字顯示
            self._update_text_display()
            
            # 更新狀態
            self.status_label.config(text=i18n.get_text("file_added", filename))
        else:
            # 顯示錯誤訊息
            self.status_label.config(text=message)
            messagebox.showwarning(i18n.get_text("warning"), message)
    
    def _on_delete_file(self):
        """刪除選中的檔案"""
        selected_index = self.file_list_widget.get_selected_index()
        if selected_index is not None:
            # 從檔案處理器中移除
            if self.file_handler.remove_file(selected_index):
                # 從GUI列表中移除
                self.file_list_widget.remove_selected()
                
                # 更新文字顯示
                self._update_text_display()
                
                # 更新狀態
                self.status_label.config(text=i18n.get_text("file_deleted"))
        else:
            messagebox.showwarning(i18n.get_text("warning"), i18n.get_text("no_file_selected"))
    
    def _on_restore_file(self):
        """復原最後刪除的檔案"""
        if self.file_handler.restore_last_deleted():
            # 重新載入GUI列表
            self._reload_file_list()
            
            # 更新文字顯示
            self._update_text_display()
            
            # 更新狀態
            self.status_label.config(text=i18n.get_text("file_restored"))
        else:
            messagebox.showinfo(i18n.get_text("info"), i18n.get_text("no_file_to_restore"))
    
    def _on_clear_all_files(self):
        """清空所有檔案"""
        self.file_handler.clear_all()
        self.file_list_widget.clear_all()
        self.text_display_widget.clear_content()
        self.status_label.config(text=i18n.get_text("all_files_cleared"))
    
    def _on_clear_text_content(self):
        """清空文字內容（但保留檔案列表）"""
        self.text_display_widget.clear_content()
        self.status_label.config(text=i18n.get_text("text_content_cleared"))
    
    def _update_text_display(self):
        """更新文字顯示區域"""
        content = self.file_handler.get_combined_content()
        self.text_display_widget.set_content(content)
    
    def _reload_file_list(self):
        """重新載入檔案列表"""
        self.file_list_widget.clear_all()
        file_names = self.file_handler.get_file_list()
        for filename in file_names:
            self.file_list_widget.add_file(filename)
    
    def _on_closing(self):
        """視窗關閉事件"""
        self.root.quit()
        self.root.destroy()
    
    def run(self):
        """執行主程式"""
        self.root.mainloop() 