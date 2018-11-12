---
title: Edit Open/Close Log File
description: Edit Open/Close Log File
ms.assetid: f63549f7-1516-48a0-8af8-38cca103215c
keywords: ["Edit Open/Close Log File", "log file, Edit Open/Close Log File"]
ms.author: domars
ms.date: 05/23/2017
ms.localizationpriority: medium
---

# Edit | Open/Close Log File


## <span id="ddk_edit_open_close_log_file_dbg"></span><span id="DDK_EDIT_OPEN_CLOSE_LOG_FILE_DBG"></span>


Click **Open/Close Log File** on the **Edit** menu to write to a new log file, append to an existing log file, or close an open log file.

### <span id="dialog_box"></span><span id="DIALOG_BOX"></span>Dialog Box

When you click **Open/Close Log File**, the **Open/Close Log File** dialog box appears. This dialog box displays the current log file, if one is already open.

If the **Log file name** box is blank, you can enter a log file name. If this file already exists, WinDbg overwrites the existing file, unless you select the **Append** check box. If you specify a file name but no path, WinDbg puts the file in the default directory that you started WinDbg from.

If the **Log file name** box already displays a file name, you can click **Close Open Log File** to close the file. If you clear the **Log file name** box and enter a new log file name, the previous log file will be closed.

Click **OK** to save changes, or click **Cancel** to discard changes.

If you click **OK** when no log file name appears in the **Log file name** box, it has no effect. That is, WinDbg does not close a log file or open a log file.

However, if a log file is already active and you click **OK** without clearing its name or selecting **Append**, WinDbg deletes the log file and uses a new file that has the same name.

 

 





