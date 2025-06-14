# Text File Drag & Drop Tool

> **Language Selection / 語言選擇:**  
> 🇺🇸 [English](README_EN.md) | 🇹🇼 [繁體中文](README.md)

A GUI application developed with Python and Tkinter that supports dragging and dropping text files to display their content.

![Program Demo](img/demo.png)

## Features

### 🎯 Main Functions
1. **Enhanced Drag & Drop Support** - Support multiple file drag sources (File Explorer, other apps, text paths)
2. **File List Management** - Display added file list
3. **Text Content Display** - Show file content in scrollable text area
4. **File Operations** - Support delete and restore functions
5. **Content Copy** - One-click copy all text content to clipboard
6. **Smart Clipboard** - Ctrl+V intelligently analyzes clipboard content (files or text)
7. **Multi-language Support** - Support Chinese and English interface switching
8. **State Persistence** - Automatically save program state and restore file list on restart

### 📁 Supported File Formats
- Programming language files: `.py`, `.cpp`, `.c`, `.h`, `.java`, `.js`, `.php`, `.go`, `.rs`, etc.
- Markup language files: `.html`, `.xml`, `.md`, `.rst`, `.yaml`, etc.
- Configuration files: `.ini`, `.cfg`, `.conf`, `.json`, etc.
- Text files: `.txt`, `.log`, etc.
- Script files: `.sh`, `.bat`, `.ps1`, etc.

## Installation Requirements

### System Requirements
- Windows 10/11
- Python 3.7+

### Dependencies
```bash
pip install -r requirements.txt
```

Main dependencies:
- `tkinterdnd2` - Drag and drop functionality
- `pyperclip` - Clipboard operations
- `pywin32` - Windows clipboard API

## Usage

### Starting the Program
```bash
python main.py
```

### Basic Operations

#### 1. Adding Files
- **From File Explorer**: Drag text files from File Explorer to any position in the program window
- **From Other Applications**: Support dragging file paths from text editors, IDEs, and other programs
- **Multiple Path Formats**: Support standard paths, quoted paths, multi-line paths, etc.
- **Smart Clipboard Paste**: Press Ctrl+V to intelligently analyze clipboard content
  - File Copy: Copy files from File Explorer and paste to automatically read file content
  - Text Copy: Copy text and paste to automatically create paste-text_*.txt files
- **Auto State Saving**: Automatically save to system temp directory after adding files
- Supported files will be automatically added to the left list
- File content will be displayed in the right text area

#### 2. Managing File List
- **Select File**: Click on file name in the list
- **Delete File**: Select file and click "Delete Selected" button, or double-click file
- **Restore File**: Click "Restore" button to recover last deleted file
- **Clear List**: Click "Clear" button to remove all files

#### 3. Text Content Operations
- **Copy Content**: Click "Copy Content" button to copy all text to clipboard
- **Clear Content**: Click "Clear Content" button to clear text display area

#### 4. Clipboard Operations
- **Smart Paste**: Press Ctrl+V to automatically analyze clipboard content
- **File Paste**: Copy files from File Explorer (Ctrl+C), then paste in program (Ctrl+V)
- **Text Paste**: Copy any text content, paste to automatically create temporary text files
- **Auto Naming**: Text files automatically named as paste-text_1.txt, paste-text_2.txt, etc., avoiding overwrite

#### 5. Language Switching
- **Language Selection**: Click language dropdown menu in top-right corner
- **Supported Languages**: Traditional Chinese and English
- **Real-time Switching**: Interface updates immediately after language selection

### Interface Overview

```
┌─────────────────────────────────────────────────────────────┐
│            Text File Drag & Drop Tool        [Language: EN ▼] │
├─────────────────┬───────────────────────────────────────────┤
│   File List     │              Text Content                 │
│ ┌─────────────┐ │ ┌───────────────────────────────────────┐ │
│ │ file1.py    │ │ │ === file1.py ===                     │ │
│ │ file2.txt   │ │ │ print("Hello World")                 │ │
│ │ file3.md    │ │ │                                       │ │
│ │             │ │ │ === file2.txt ===                    │ │
│ └─────────────┘ │ │ This is a text file...               │ │
│ [Delete][Restore][Clear] │ └───────────────────────────────────────┘ │
│                 │ [Copy Content] [Clear Content]  Lines: 25, Chars: 512 │
├─────────────────┴───────────────────────────────────────────┤
│ Status: Drag text files to this window to add to list        │
└─────────────────────────────────────────────────────────────┘
```

## Program Architecture

### Directory Structure
```
drag_n_paste/
├── main.py                 # Main program entry
├── requirements.txt        # Dependencies
├── README.md              # Documentation (Chinese)
├── README_EN.md           # Documentation (English)
├── USAGE_EXAMPLES.md      # Usage examples
├── CHANGELOG.md           # Changelog
├── LICENSE                # GPL 3.0 License
├── install.bat            # Windows installation script
├── run.bat               # Windows startup script
├── img/                   # Image resources
│   └── demo.png          # Program demo screenshot
├── test_sample/           # Test files
│   ├── test_chinese.txt   # Chinese test file
│   ├── test_sample.py     # Python test file
│   └── test_sample.txt    # Text test file
├── core/                  # Core functionality modules
│   ├── file_handler.py    # File handling
│   ├── file_validator.py  # File validation
│   ├── state_manager.py   # State management
│   └── clipboard_handler.py # Clipboard handling
├── gui/                   # GUI component modules
│   ├── main_window.py     # Main window
│   ├── file_list_widget.py # File list component
│   ├── text_display_widget.py # Text display component
│   └── language_selector.py # Language selector component
└── utils/                 # Utility modules
    ├── constants.py       # Constants definition
    └── i18n.py           # Internationalization module
```

### Design Principles
- **Atomic**: Each file provides only one basic function
- **Tree Structure**: Use folders for modular management
- **Low Coupling**: Proper decoupling to reduce module dependencies
- **Observer Pattern**: Language switching uses observer pattern to avoid hardcoding

## Key Features

### 🔄 Smart File Processing
- Auto-detect file encoding (UTF-8, GBK, Big5, etc.)
- Support multiple text file formats
- Duplicate file detection
- Full Unicode character support
- **Enhanced Drag Parsing**: Support multiple drag sources and path formats
- **Smart Clipboard**: Ctrl+V automatically analyzes file or text content
- **State Persistence**: Automatically save/load program state to system temp directory

### 🎨 User-Friendly Interface
- Modern GUI design
- Adjustable split window
- Real-time status feedback
- Scrollbar support
- Multi-language interface (Chinese/English)
- Observer pattern for real-time language switching

### 📋 Convenient Operations
- Drag and drop file addition
- **Ctrl+V Smart Clipboard Paste**:
  - Automatically detect file or text content
  - Files automatically read and added to list
  - Text automatically creates paste-text_*.txt files
  - Avoid filename conflicts
- One-click copy all content
- Restore delete function
- Batch clear operations

## Troubleshooting

### Common Issues

**Q: Drag and drop files not responding?**
A: Please check:
- File is in supported text format
- File is not locked by other programs
- File path doesn't contain special characters
- Try different drag methods (from File Explorer, text editors, etc.)

**Q: File content displays garbled text?**
A: The program automatically tries multiple encodings. If problems persist, please check if the file encoding is in a common format.

**Q: Copy function not working?**
A: Please ensure `pyperclip` package is installed and system clipboard function is working properly.

**Q: Ctrl+V paste function not working?**
A: Please check:
- `pywin32` package is installed (Windows clipboard API)
- Clipboard has content (text or files)
- Program window has focus
- For file paste, ensure files are supported text formats

## Quick Start

1. **Install Dependencies**:
   ```bash
   .\install.bat
   ```

2. **Run Program**:
   ```bash
   .\run.bat
   # or
   python main.py
   ```

3. **Test Features**:
   - Drag `test_sample/test_chinese.txt` to test Unicode character support
   - Drag `test_sample/test_sample.py` to test code file support
   - Copy some text, then press Ctrl+V to test text paste function
   - Copy text files from File Explorer, then press Ctrl+V to test file paste function
   - Switch language using the dropdown in top-right corner

## Version History

See [CHANGELOG.md](CHANGELOG.md) for detailed version history.

## Related Links

- [Usage Examples](USAGE_EXAMPLES.md)
- [更新日誌 (Changelog)](CHANGELOG.md)

## License

This project is licensed under the GPL 3.0 License.

## Contributing

Welcome to submit Issues and Pull Requests to improve this project! 