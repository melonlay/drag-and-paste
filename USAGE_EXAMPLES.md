# 使用示例 / Usage Examples

## 智慧剪貼簿功能 / Smart Clipboard Features

### 1. 文字貼上 / Text Paste

**步驟 / Steps:**
1. 複製任何文字內容到剪貼簿 / Copy any text content to clipboard
2. 在程式中按 `Ctrl+V` / Press `Ctrl+V` in the program
3. 程式會自動創建 `paste-text_1.txt` 檔案 / Program automatically creates `paste-text_1.txt` file
4. 檔案內容會顯示在右側文字區域 / File content displays in right text area

**示例 / Example:**
```
複製文字: "Hello World!\nThis is a test."
結果檔案: paste-text_1.txt
檔案內容: Hello World!
         This is a test.
```

### 2. 檔案貼上 / File Paste

**步驟 / Steps:**
1. 在檔案總管中選擇文字檔案 / Select text files in File Explorer
2. 按 `Ctrl+C` 複製檔案 / Press `Ctrl+C` to copy files
3. 在程式中按 `Ctrl+V` / Press `Ctrl+V` in the program
4. 程式會自動讀取檔案內容並添加到列表 / Program automatically reads file content and adds to list

**支援的檔案格式 / Supported File Formats:**
- 程式語言: `.py`, `.cpp`, `.java`, `.js` 等 / Programming languages
- 標記語言: `.html`, `.xml`, `.md` 等 / Markup languages
- 設定檔案: `.ini`, `.json`, `.yaml` 等 / Configuration files
- 文字檔案: `.txt`, `.log` 等 / Text files

### 3. 混合使用 / Mixed Usage

**場景 / Scenario:**
1. 拖拽一些檔案到程式 / Drag some files to program
2. 複製文字並按 `Ctrl+V` 貼上 / Copy text and paste with `Ctrl+V`
3. 從檔案總管複製更多檔案並貼上 / Copy more files from File Explorer and paste
4. 所有內容會合併顯示在右側 / All content merges and displays on the right

## 檔案命名規則 / File Naming Rules

### 自動命名 / Automatic Naming
- 第一次貼上文字: `paste-text_1.txt`
- 第二次貼上文字: `paste-text_2.txt`
- 依此類推... / And so on...

### 避免衝突 / Conflict Avoidance
- 程式會檢查檔案是否已存在 / Program checks if file already exists
- 自動跳過已存在的編號 / Automatically skips existing numbers
- 確保每個檔案都有唯一名稱 / Ensures each file has unique name

## 實用技巧 / Practical Tips

### 1. 快速文字收集 / Quick Text Collection
```
1. 從網頁複製文字 → Ctrl+V
2. 從郵件複製文字 → Ctrl+V  
3. 從聊天軟體複製文字 → Ctrl+V
4. 一鍵複製所有內容到剪貼簿
```

### 2. 程式碼片段管理 / Code Snippet Management
```
1. 從IDE複製程式碼 → Ctrl+V
2. 從文檔複製範例 → Ctrl+V
3. 拖拽現有檔案
4. 統一查看和比較
```

### 3. 文檔整理 / Document Organization
```
1. 複製檔案從不同資料夾 → Ctrl+V
2. 貼上相關文字說明 → Ctrl+V
3. 一次性查看所有內容
4. 複製合併後的內容
```

## 鍵盤快捷鍵 / Keyboard Shortcuts

| 快捷鍵 / Shortcut | 功能 / Function |
|------------------|----------------|
| `Ctrl+V` | 智慧剪貼簿貼上 / Smart clipboard paste |
| `雙擊檔案` / `Double-click file` | 刪除檔案 / Delete file |
| `Delete鍵` / `Delete key` | 刪除選中檔案 / Delete selected file |

## 故障排除 / Troubleshooting

### 常見問題 / Common Issues

**Q: Ctrl+V 沒有反應？**
A: 確認程式視窗有焦點，剪貼簿中有內容

**Q: 檔案貼上失敗？**
A: 確認檔案是支援的文字格式，檔案沒有被鎖定

**Q: 文字檔案創建失敗？**
A: 檢查系統暫存目錄權限，確保有寫入權限

**Q: Ctrl+V not responding?**
A: Ensure program window has focus and clipboard has content

**Q: File paste failed?**
A: Confirm files are supported text formats and not locked

**Q: Text file creation failed?**
A: Check system temp directory permissions 