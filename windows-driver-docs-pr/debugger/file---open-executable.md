---
title: File Open Executable
description: File Open Executable
ms.assetid: dee75298-903d-438f-a66e-fddcfcd74ec7
keywords: ["File Open Executable", "starting the debugger, File Open Executable"]
ms.author: domars
ms.date: 05/23/2017
ms.localizationpriority: medium
---

# File | Open Executable


## <span id="ddk_file_open_executable_dbg"></span><span id="DDK_FILE_OPEN_EXECUTABLE_DBG"></span>


Click **Open Executable** on the **File** menu to start a new user-mode process and debug it.

This command is equivalent to pressing CTRL+E. You can use this command only when WinDbg is in dormant mode.

### <span id="dialog_box"></span><span id="DIALOG_BOX"></span>Dialog Box

When you click **Open Executable**, the **Open Executable** dialog box appears, and you can do the following:

-   Enter the full path of the executable file in the **File name** box. Alternatively, you can use the dialog box to locate and select the proper file. You must specify the exact path to the executable file. Unlike the Microsoft Windows **Run** dialog box and a Command Prompt window, the **Open Executable** dialog box does not search the current path for an executable name.

-   If you want to use command-line arguments with the executable file, enter them in the **Arguments** box.

-   If you want to change the starting directory from the default directory enter the directory path in the **Start directory** box.

-   If you want WinDbg to attach to any *child processes* (additional processes that the original target process started), select **Debug child processes also**.

After you make your selections, click **Open**.

**Note**   When you use this command to open a source file, the path to that file is automatically appended to the [source path](source-path.md).

 

If WinDbg is connected to a process server, you cannot use the **Open Executable** command.

### <span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>Additional Information

For more information and other methods of starting new processes for debugging, see [Debugging a User-Mode Process Using WinDbg](debugging-a-user-mode-process-using-windbg.md).

 

 





