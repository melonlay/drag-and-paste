# -*- coding: utf-8 -*-
import os
from typing import List, Tuple
from core.file_validator import FileValidator
from core.state_manager import StateManager
from utils.i18n import i18n


class FileHandler:
    """檔案處理器，負責檔案的讀取和管理"""
    
    def __init__(self):
        self.file_list = []  # 儲存檔案路徑列表
        self.file_contents = []  # 儲存檔案內容列表
        self.deleted_files = []  # 儲存被刪除的檔案（用於復原功能）
        self.state_manager = StateManager()  # 狀態管理器
        
        # 載入上次的狀態
        self._load_previous_state()
    
    def add_file(self, file_path: str) -> Tuple[bool, str]:
        """
        新增檔案到列表
        
        Args:
            file_path (str): 檔案路徑
            
        Returns:
            Tuple[bool, str]: (是否成功, 訊息)
        """
        # 檢查檔案是否為文字檔案
        if not FileValidator.is_text_file(file_path):
            return False, i18n.get_text("invalid_file")
        
        # 檢查檔案是否已存在於列表中
        if file_path in self.file_list:
            return False, i18n.get_text("file_exists")
        
        try:
            # 讀取檔案內容
            content = self._read_file_content(file_path)
            
            # 新增到列表
            self.file_list.append(file_path)
            self.file_contents.append(content)
            
            # 保存狀態
            self._save_current_state()
            
            return True, i18n.get_text("file_added")
        except Exception as e:
            return False, i18n.get_text("read_file_error", str(e))
    
    def remove_file(self, index: int) -> bool:
        """
        從列表中移除檔案
        
        Args:
            index (int): 檔案在列表中的索引
            
        Returns:
            bool: 是否成功移除
        """
        if 0 <= index < len(self.file_list):
            # 儲存被刪除的檔案資訊（用於復原）
            deleted_file = {
                'path': self.file_list[index],
                'content': self.file_contents[index],
                'index': index
            }
            self.deleted_files.append(deleted_file)
            
            # 從列表中移除
            del self.file_list[index]
            del self.file_contents[index]
            
            # 保存狀態
            self._save_current_state()
            
            return True
        return False
    
    def restore_last_deleted(self) -> bool:
        """
        復原最後一個被刪除的檔案
        
        Returns:
            bool: 是否成功復原
        """
        if not self.deleted_files:
            return False
        
        # 取得最後被刪除的檔案
        deleted_file = self.deleted_files.pop()
        
        # 復原到原來的位置
        insert_index = min(deleted_file['index'], len(self.file_list))
        self.file_list.insert(insert_index, deleted_file['path'])
        self.file_contents.insert(insert_index, deleted_file['content'])
        
        # 保存狀態
        self._save_current_state()
        
        return True
    
    def get_combined_content(self) -> str:
        """
        取得所有檔案的合併內容
        
        Returns:
            str: 合併後的內容
        """
        if not self.file_contents:
            return ""
        
        combined = []
        for i, (file_path, content) in enumerate(zip(self.file_list, self.file_contents)):
            file_name = os.path.basename(file_path)
            combined.append(f"=== {file_name} ===\n")
            combined.append(content)
            if i < len(self.file_contents) - 1:
                combined.append("\n\n")
        
        return "".join(combined)
    
    def get_file_list(self) -> List[str]:
        """
        取得檔案列表（僅檔案名稱）
        
        Returns:
            List[str]: 檔案名稱列表
        """
        return [os.path.basename(path) for path in self.file_list]
    
    def clear_all(self):
        """清空所有檔案"""
        self.file_list.clear()
        self.file_contents.clear()
        self.deleted_files.clear()
        
        # 清除保存的狀態
        self.state_manager.clear_state()
    
    def _read_file_content(self, file_path: str) -> str:
        """
        讀取檔案內容
        
        Args:
            file_path (str): 檔案路徑
            
        Returns:
            str: 檔案內容
        """
        encodings = ['utf-8', 'utf-8-sig', 'gbk', 'big5', 'latin-1']
        
        for encoding in encodings:
            try:
                with open(file_path, 'r', encoding=encoding) as file:
                    return file.read()
            except UnicodeDecodeError:
                continue
            except Exception as e:
                raise e
        
        raise UnicodeDecodeError(i18n.get_text("read_file_error", "無法使用任何編碼讀取檔案"))
    
    def _save_current_state(self):
        """保存目前狀態"""
        deleted_file_paths = [f['path'] for f in self.deleted_files]
        self.state_manager.save_state(self.file_list, deleted_file_paths)
    
    def _load_previous_state(self):
        """載入上次的狀態"""
        try:
            state_data = self.state_manager.load_state()
            if not state_data:
                return
            
            # 載入檔案列表
            for file_path in state_data.get("file_paths", []):
                if os.path.exists(file_path):
                    try:
                        content = self._read_file_content(file_path)
                        self.file_list.append(file_path)
                        self.file_contents.append(content)
                    except Exception as e:
                        print(f"載入檔案失敗 {file_path}: {e}")
            
            # 載入已刪除檔案列表（用於復原功能）
            for file_path in state_data.get("deleted_files", []):
                if os.path.exists(file_path):
                    try:
                        content = self._read_file_content(file_path)
                        deleted_file = {
                            'path': file_path,
                            'content': content,
                            'index': len(self.file_list)  # 預設插入到最後
                        }
                        self.deleted_files.append(deleted_file)
                    except Exception as e:
                        print(f"載入已刪除檔案失敗 {file_path}: {e}")
                        
        except Exception as e:
            print(f"載入狀態失敗: {e}")
    
    def get_file_paths(self) -> List[str]:
        """
        取得完整檔案路徑列表
        
        Returns:
            List[str]: 檔案路徑列表
        """
        return self.file_list.copy() 