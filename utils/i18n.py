# -*- coding: utf-8 -*-
"""
國際化翻譯模組
支援中文和英文語言切換
"""

import json
import os
from typing import Dict, Any


class I18nManager:
    """國際化管理器"""
    
    def __init__(self):
        self.current_language = "zh_TW"  # 預設繁體中文
        self.translations = {}
        self.observers = []  # 觀察者列表，用於通知語言變更
        self._load_translations()
    
    def _load_translations(self):
        """載入翻譯資源"""
        # 中文翻譯
        self.translations["zh_TW"] = {
            # 視窗標題
            "window_title": "文字檔案拖拽工具",
            
            # 元件標題
            "file_list_title": "檔案列表",
            "text_content_title": "文字內容",
            
            # 按鈕文字
            "delete_selected": "刪除選中",
            "restore": "復原",
            "clear": "清空",
            "copy_content": "複製內容",
            "clear_content": "清空內容",
            
            # 狀態訊息
            "drag_files_hint": "拖拽文字檔案到此視窗以新增到列表",
            "file_added": "已新增: {}",
            "file_deleted": "檔案已刪除",
            "file_restored": "檔案已復原",
            "all_files_cleared": "所有檔案已清空",
            "text_content_cleared": "文字內容已清空",
            
            # 錯誤訊息
            "invalid_file": "不是合法的文字檔案",
            "file_exists": "檔案已存在於列表中",
            "read_file_error": "讀取檔案失敗: {}",
            "no_file_selected": "請先選擇要刪除的檔案",
            "no_file_to_restore": "沒有可復原的檔案",
            "no_content_to_copy": "沒有內容可複製",
            "copy_failed": "複製失敗: {}",
            
            # 對話框訊息
            "confirm": "確認",
            "warning": "警告",
            "error": "錯誤",
            "success": "成功",
            "info": "資訊",
            "confirm_clear_files": "確定要清空所有檔案嗎？",
            "confirm_clear_content": "確定要清空文字內容嗎？",
            "content_copied": "內容已複製到剪貼簿",
            
            # 狀態資訊
            "lines_chars": "行數: {}, 字元數: {}",
            
            # 語言選項
            "language": "語言",
            "chinese": "中文",
            "english": "English",
            
            # 狀態載入
            "state_loaded": "已載入 {} 個檔案",
            
            # 剪貼簿功能
            "clipboard_empty": "剪貼簿為空",
            "paste_failed": "貼上失敗: {}",
            "files_pasted": "已貼上 {} 個檔案",
            "no_valid_files_in_clipboard": "剪貼簿中沒有有效的文字檔案",
            "text_pasted": "已貼上文字檔案: {}",
            "create_text_file_failed": "創建文字檔案失敗: {}"
        }
        
        # 英文翻譯
        self.translations["en_US"] = {
            # Window title
            "window_title": "Text File Drag & Drop Tool",
            
            # Component titles
            "file_list_title": "File List",
            "text_content_title": "Text Content",
            
            # Button text
            "delete_selected": "Delete Selected",
            "restore": "Restore",
            "clear": "Clear",
            "copy_content": "Copy Content",
            "clear_content": "Clear Content",
            
            # Status messages
            "drag_files_hint": "Drag text files to this window to add to list",
            "file_added": "Added: {}",
            "file_deleted": "File deleted",
            "file_restored": "File restored",
            "all_files_cleared": "All files cleared",
            "text_content_cleared": "Text content cleared",
            
            # Error messages
            "invalid_file": "Not a valid text file",
            "file_exists": "File already exists in list",
            "read_file_error": "Failed to read file: {}",
            "no_file_selected": "Please select a file to delete first",
            "no_file_to_restore": "No file to restore",
            "no_content_to_copy": "No content to copy",
            "copy_failed": "Copy failed: {}",
            
            # Dialog messages
            "confirm": "Confirm",
            "warning": "Warning",
            "error": "Error",
            "success": "Success",
            "info": "Information",
            "confirm_clear_files": "Are you sure you want to clear all files?",
            "confirm_clear_content": "Are you sure you want to clear text content?",
            "content_copied": "Content copied to clipboard",
            
            # Status info
            "lines_chars": "Lines: {}, Characters: {}",
            
            # Language options
            "language": "Language",
            "chinese": "中文",
            "english": "English",
            
            # State loading
            "state_loaded": "Loaded {} files",
            
            # Clipboard functionality
            "clipboard_empty": "Clipboard is empty",
            "paste_failed": "Paste failed: {}",
            "files_pasted": "Pasted {} files",
            "no_valid_files_in_clipboard": "No valid text files in clipboard",
            "text_pasted": "Pasted text file: {}",
            "create_text_file_failed": "Failed to create text file: {}"
        }
    
    def get_text(self, key: str, *args) -> str:
        """
        取得翻譯文字
        
        Args:
            key (str): 翻譯鍵值
            *args: 格式化參數
            
        Returns:
            str: 翻譯後的文字
        """
        translation = self.translations.get(self.current_language, {})
        text = translation.get(key, key)  # 如果找不到翻譯，返回原鍵值
        
        if args:
            try:
                return text.format(*args)
            except:
                return text
        return text
    
    def set_language(self, language: str):
        """
        設定語言
        
        Args:
            language (str): 語言代碼 (zh_TW 或 en_US)
        """
        if language in self.translations:
            self.current_language = language
            self._notify_observers()
    
    def get_current_language(self) -> str:
        """取得當前語言"""
        return self.current_language
    
    def get_available_languages(self) -> Dict[str, str]:
        """取得可用語言列表"""
        return {
            "zh_TW": self.get_text("chinese"),
            "en_US": self.get_text("english")
        }
    
    def add_observer(self, observer):
        """
        添加觀察者
        
        Args:
            observer: 觀察者物件，需要有 on_language_changed 方法
        """
        if observer not in self.observers:
            self.observers.append(observer)
    
    def remove_observer(self, observer):
        """移除觀察者"""
        if observer in self.observers:
            self.observers.remove(observer)
    
    def _notify_observers(self):
        """通知所有觀察者語言已變更"""
        for observer in self.observers:
            if hasattr(observer, 'on_language_changed'):
                try:
                    observer.on_language_changed()
                except Exception as e:
                    print(f"Error notifying observer: {e}")


# 全域翻譯管理器實例
i18n = I18nManager() 