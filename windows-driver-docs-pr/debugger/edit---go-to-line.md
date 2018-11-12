---
title: Edit Go to Line
description: Edit Go to Line
ms.assetid: af7f2afc-95cb-4dcd-9b74-1bd46713239f
keywords: ["Edit Go to Line"]
ms.author: domars
ms.date: 05/23/2017
ms.localizationpriority: medium
---

# Edit | Go to Line


## <span id="ddk_edit_go_to_line_dbg"></span><span id="DDK_EDIT_GO_TO_LINE_DBG"></span>


Click **Go to Line** on the **Edit** menu to search for a specific line in the currently-active [Source window](source-window.md). If the active window is not a Source window, this command has no effect.

This command is equivalent to pressing CTRL+L.

### <span id="dialog_box"></span><span id="DIALOG_BOX"></span>Dialog Box

When you click **Go to Line**, the **Go to Line** dialog box appears. In this dialog box, enter the line number that you want to find and then click **OK**. The debugger will move the caret (^) to that line. If the line number is bigger than the last line in the file, the cursor will move to the end of the file.

The **Go to Line** command only changes the WinDbg display. This command does not affect the execution of the target or any other debugger operations.

### <span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>Additional Information

For more information about other ways of finding text in debugging information windows, see [Moving Through a Window](moving-through-a-window.md).

 

 





