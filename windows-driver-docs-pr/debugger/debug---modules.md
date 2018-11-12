---
title: Debug Modules
description: Debug Modules
ms.assetid: 4107ff36-31c4-45a6-95f6-b647543f01be
keywords: ["Debug Modules", "executable files and paths, Debug Modules"]
ms.author: domars
ms.date: 05/23/2017
ms.localizationpriority: medium
---

# Debug | Modules


## <span id="ddk_debug_modules_dbg"></span><span id="DDK_DEBUG_MODULES_DBG"></span>


Click **Modules** on the **Debug** menu to display the current list of loaded modules.

### <span id="dialog_box"></span><span id="DIALOG_BOX"></span>Dialog Box

When you click **Modules**, the **Module List** dialog box appears. This dialog box lists all modules that are currently loaded into memory.

**Module List** is divided into the following columns:

-   The **Name** column specifies the module name.

-   The **Start** and **End** columns specify the first and last address of the module's memory image.

-   The **Timestamp** column specifies the build date and time for the module.

-   The **Checksum** column specifies the checksum value.

-   The **Symbols** column displays information about the symbols that this module uses. For more information about the values that appear in this column, see [Symbol Status Abbreviations](symbol-status-abbreviations.md).

-   The **Symbol file** column specifies the path and file name of the associated symbol file. If the debugger is unaware of any symbol file, the name of the executable file is given instead.

If you click the title bar of a column, the display is sorted by the data in that column. If you click the title bar again, the sort order reverses.

If you select a line and then click **Reload**, that module's symbol information is reloaded.

If you select a line and press CTRL+C, the whole line is copied to the clipboard.

Click **Close** to close this dialog box.

 

 





