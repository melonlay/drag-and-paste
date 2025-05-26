# -*- coding: utf-8 -*-
import json
import os
import tempfile
from typing import List, Dict, Any
from datetime import datetime


class StateManager:
    """狀態管理器 - 負責保存和載入程式狀態"""
    
    def __init__(self):
        # 設定狀態檔案路徑
        self.temp_dir = tempfile.gettempdir()
        self.state_file = os.path.join(self.temp_dir, "drag_n_paste_state.json")
        
    def save_state(self, file_paths: List[str], deleted_files: List[str] = None) -> bool:
        """
        保存程式狀態
        
        Args:
            file_paths (List[str]): 目前的檔案路徑列表
            deleted_files (List[str]): 已刪除的檔案路徑列表
            
        Returns:
            bool: 保存是否成功
        """
        try:
            state_data = {
                "version": "1.0",
                "timestamp": datetime.now().isoformat(),
                "file_paths": file_paths,
                "deleted_files": deleted_files or [],
                "total_files": len(file_paths)
            }
            
            # 確保目錄存在
            os.makedirs(os.path.dirname(self.state_file), exist_ok=True)
            
            # 保存到檔案
            with open(self.state_file, 'w', encoding='utf-8') as f:
                json.dump(state_data, f, ensure_ascii=False, indent=2)
            
            return True
            
        except Exception as e:
            print(f"保存狀態失敗: {e}")
            return False
    
    def load_state(self) -> Dict[str, Any]:
        """
        載入程式狀態
        
        Returns:
            Dict[str, Any]: 狀態資料，如果載入失敗則返回空字典
        """
        try:
            if not os.path.exists(self.state_file):
                return {}
            
            with open(self.state_file, 'r', encoding='utf-8') as f:
                state_data = json.load(f)
            
            # 驗證檔案是否仍然存在
            valid_files = []
            for file_path in state_data.get("file_paths", []):
                if os.path.exists(file_path):
                    valid_files.append(file_path)
            
            state_data["file_paths"] = valid_files
            return state_data
            
        except Exception as e:
            print(f"載入狀態失敗: {e}")
            return {}
    
    def clear_state(self) -> bool:
        """
        清除保存的狀態
        
        Returns:
            bool: 清除是否成功
        """
        try:
            if os.path.exists(self.state_file):
                os.remove(self.state_file)
            return True
        except Exception as e:
            print(f"清除狀態失敗: {e}")
            return False
    
    def get_state_file_path(self) -> str:
        """
        取得狀態檔案路徑
        
        Returns:
            str: 狀態檔案的完整路徑
        """
        return self.state_file
    
    def has_saved_state(self) -> bool:
        """
        檢查是否有保存的狀態
        
        Returns:
            bool: 是否存在保存的狀態
        """
        return os.path.exists(self.state_file) 