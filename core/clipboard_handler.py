# -*- coding: utf-8 -*-
import os
import tempfile
import time
from typing import List, Tuple, Optional
import pyperclip

try:
    import win32clipboard
    import win32con
    WINDOWS_CLIPBOARD_AVAILABLE = True
except ImportError:
    WINDOWS_CLIPBOARD_AVAILABLE = False


class ClipboardHandler:
    """剪貼簿處理器 - 分析剪貼簿內容並處理檔案和文字"""
    
    def __init__(self):
        self.temp_dir = tempfile.gettempdir()
        self.paste_count = 0  # 用於生成唯一的貼上檔案名稱
        
    def analyze_clipboard(self) -> Tuple[str, List[str], Optional[str]]:
        """
        分析剪貼簿內容
        
        Returns:
            Tuple[str, List[str], Optional[str]]: (類型, 檔案路徑列表, 文字內容)
            類型可能是: 'files', 'text', 'empty'
        """
        # 首先嘗試檢查是否有檔案
        file_paths = self._get_clipboard_files()
        if file_paths:
            return 'files', file_paths, None
        
        # 檢查是否有文字內容
        text_content = self._get_clipboard_text()
        if text_content and text_content.strip():
            return 'text', [], text_content
        
        return 'empty', [], None
    
    def _get_clipboard_files(self) -> List[str]:
        """
        從剪貼簿取得檔案路徑列表
        
        Returns:
            List[str]: 檔案路徑列表
        """
        if not WINDOWS_CLIPBOARD_AVAILABLE:
            return []
        
        try:
            win32clipboard.OpenClipboard()
            
            # 檢查是否有檔案格式
            if win32clipboard.IsClipboardFormatAvailable(win32con.CF_HDROP):
                # 取得檔案路徑
                files_data = win32clipboard.GetClipboardData(win32con.CF_HDROP)
                file_paths = []
                
                if files_data:
                    for file_path in files_data:
                        if os.path.isfile(file_path):
                            file_paths.append(file_path)
                
                return file_paths
            
        except Exception as e:
            print(f"讀取剪貼簿檔案失敗: {e}")
        finally:
            try:
                win32clipboard.CloseClipboard()
            except:
                pass
        
        return []
    
    def _get_clipboard_text(self) -> Optional[str]:
        """
        從剪貼簿取得文字內容
        
        Returns:
            Optional[str]: 文字內容，如果沒有則返回None
        """
        try:
            return pyperclip.paste()
        except Exception as e:
            print(f"讀取剪貼簿文字失敗: {e}")
            return None
    
    def create_text_file(self, text_content: str) -> str:
        """
        創建臨時文字檔案
        
        Args:
            text_content (str): 文字內容
            
        Returns:
            str: 創建的檔案路徑
        """
        # 生成唯一的檔案名稱
        self.paste_count += 1
        filename = f"paste-text_{self.paste_count}.txt"
        
        # 確保檔案名稱不重複
        file_path = os.path.join(self.temp_dir, filename)
        while os.path.exists(file_path):
            self.paste_count += 1
            filename = f"paste-text_{self.paste_count}.txt"
            file_path = os.path.join(self.temp_dir, filename)
        
        try:
            # 創建檔案並寫入內容
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(text_content)
            
            return file_path
            
        except Exception as e:
            raise Exception(f"創建文字檔案失敗: {e}")
    
    def get_next_paste_filename(self) -> str:
        """
        取得下一個貼上檔案的名稱（不創建檔案）
        
        Returns:
            str: 檔案名稱
        """
        next_count = self.paste_count + 1
        filename = f"paste-text_{next_count}.txt"
        file_path = os.path.join(self.temp_dir, filename)
        
        while os.path.exists(file_path):
            next_count += 1
            filename = f"paste-text_{next_count}.txt"
            file_path = os.path.join(self.temp_dir, filename)
        
        return filename
    
    def cleanup_old_paste_files(self, max_age_hours: int = 24):
        """
        清理舊的貼上檔案
        
        Args:
            max_age_hours (int): 最大保留時間（小時）
        """
        try:
            current_time = time.time()
            max_age_seconds = max_age_hours * 3600
            
            for filename in os.listdir(self.temp_dir):
                if filename.startswith("paste-text_") and filename.endswith(".txt"):
                    file_path = os.path.join(self.temp_dir, filename)
                    try:
                        file_age = current_time - os.path.getctime(file_path)
                        if file_age > max_age_seconds:
                            os.remove(file_path)
                    except Exception as e:
                        print(f"清理檔案失敗 {filename}: {e}")
                        
        except Exception as e:
            print(f"清理舊檔案失敗: {e}") 