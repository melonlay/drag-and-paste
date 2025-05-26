import os
from utils.constants import SUPPORTED_TEXT_EXTENSIONS


class FileValidator:
    """檔案驗證器，用於檢查檔案是否為支援的文字檔案"""
    
    @staticmethod
    def is_text_file(file_path):
        """
        檢查檔案是否為支援的文字檔案
        
        Args:
            file_path (str): 檔案路徑
            
        Returns:
            bool: 如果是支援的文字檔案返回True，否則返回False
        """
        if not os.path.isfile(file_path):
            return False
            
        # 取得檔案副檔名
        _, ext = os.path.splitext(file_path.lower())
        
        return ext in SUPPORTED_TEXT_EXTENSIONS
    
    @staticmethod
    def get_file_extension(file_path):
        """
        取得檔案副檔名
        
        Args:
            file_path (str): 檔案路徑
            
        Returns:
            str: 檔案副檔名
        """
        _, ext = os.path.splitext(file_path.lower())
        return ext 