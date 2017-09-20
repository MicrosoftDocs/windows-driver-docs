---
title: Edit Open/Close Log File
description: Edit Open/Close Log File
ms.assetid: f63549f7-1516-48a0-8af8-38cca103215c
keywords: ["Edit Open/Close Log File", "log file, Edit Open/Close Log File"]
ms.author: windowsdriverdev
ms.date: 05/23/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20Edit%20|%20Open/Close%20Log%20File%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




