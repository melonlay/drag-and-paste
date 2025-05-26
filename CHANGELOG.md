# 更新日誌 / Changelog

## v2.1.0 - 智慧剪貼簿版本 / Smart Clipboard Version

### 🎯 新增功能 / New Features
- **智慧剪貼簿支援** / **Smart Clipboard Support**
  - Ctrl+V 自動分析剪貼簿內容 / Ctrl+V automatically analyzes clipboard content
  - 支援檔案複製貼上 / Support file copy and paste
  - 支援文字複製貼上 / Support text copy and paste
  - 自動創建 paste-text_*.txt 檔案 / Automatically create paste-text_*.txt files
  - 避免檔案名稱衝突 / Avoid filename conflicts

### 🔧 技術改進 / Technical Improvements
- **Windows 剪貼簿 API** / **Windows Clipboard API**
  - 使用 pywin32 存取 Windows 剪貼簿 / Use pywin32 to access Windows clipboard
  - 支援檔案格式檢測 (CF_HDROP) / Support file format detection (CF_HDROP)
  - 智慧內容類型判斷 / Smart content type detection

- **檔案管理** / **File Management**
  - 臨時檔案自動清理功能 / Automatic temporary file cleanup
  - 唯一檔案名稱生成 / Unique filename generation
  - 系統暫存目錄整合 / System temp directory integration

### 📁 新增檔案 / New Files
- `core/clipboard_handler.py` - 剪貼簿處理器 / Clipboard handler
- `test_clipboard_functionality.py` - 剪貼簿功能測試 / Clipboard functionality test

### 🔄 更新檔案 / Updated Files
- `gui/main_window.py` - 添加 Ctrl+V 鍵盤綁定 / Added Ctrl+V keyboard binding
- `utils/i18n.py` - 新增剪貼簿相關翻譯 / Added clipboard-related translations
- `requirements.txt` - 新增 pywin32 依賴 / Added pywin32 dependency

---

## v2.0.0 - 國際化版本 / Internationalization Version

### 🌍 新增功能 / New Features
- **多語言支援** / **Multi-language Support**
  - 支援繁體中文和英文介面 / Support Traditional Chinese and English interface
  - 右上角語言選擇下拉選單 / Language selector dropdown in top-right corner
  - 即時語言切換，無需重啟程式 / Real-time language switching without restart

### 🏗️ 架構改進 / Architecture Improvements
- **觀察者模式** / **Observer Pattern**
  - 實現語言變更通知機制 / Implement language change notification mechanism
  - 避免硬編碼的if-else語言處理 / Avoid hardcoded if-else language handling
  - 低耦合設計，易於擴展新語言 / Low coupling design, easy to extend new languages

- **模組化設計** / **Modular Design**
  - 新增 `utils/i18n.py` 國際化翻譯模組 / Added `utils/i18n.py` internationalization module
  - 新增 `gui/language_selector.py` 語言選擇元件 / Added `gui/language_selector.py` language selector component
  - 移除硬編碼文字，統一使用翻譯鍵值 / Removed hardcoded text, unified translation keys

### 🔧 技術改進 / Technical Improvements
- **Unicode支援** / **Unicode Support**
  - 完整支援中文字元顯示和處理 / Full support for Chinese character display and processing
  - 修復批次檔案中文編碼問題 / Fixed Chinese encoding issues in batch files
  - 使用UTF-8編碼確保字元正確顯示 / Use UTF-8 encoding to ensure correct character display

- **檔案編碼處理** / **File Encoding Handling**
  - 自動檢測多種編碼格式 / Auto-detect multiple encoding formats
  - 支援UTF-8、GBK、Big5等編碼 / Support UTF-8, GBK, Big5 and other encodings

### 📁 新增檔案 / New Files
- `utils/i18n.py` - 國際化翻譯管理器 / Internationalization translation manager
- `gui/language_selector.py` - 語言選擇元件 / Language selector component
- `test_chinese.txt` - 中文字元測試檔案 / Chinese character test file

### 🔄 更新檔案 / Updated Files
- `core/file_handler.py` - 使用翻譯功能 / Use translation features
- `gui/file_list_widget.py` - 添加觀察者模式支援 / Added observer pattern support
- `gui/text_display_widget.py` - 添加觀察者模式支援 / Added observer pattern support
- `gui/main_window.py` - 整合語言選擇器 / Integrated language selector
- `install.bat` / `run.bat` - 修復中文編碼問題 / Fixed Chinese encoding issues

---

## v1.0.0 - 初始版本 / Initial Version

### ✨ 基本功能 / Basic Features
- 拖拽文字檔案支援 / Drag and drop text file support
- 檔案列表管理 / File list management
- 文字內容顯示 / Text content display
- 複製和清空功能 / Copy and clear functions
- 刪除和復原功能 / Delete and restore functions

### 🏗️ 程式架構 / Program Architecture
- 原子化模組設計 / Atomic module design
- 樹狀目錄結構 / Tree directory structure
- 職責分離原則 / Separation of concerns principle 