---
title: File Open Executable
description: File Open Executable
ms.assetid: dee75298-903d-438f-a66e-fddcfcd74ec7
keywords: ["File Open Executable", "starting the debugger, File Open Executable"]
ms.author: domars
ms.date: 05/23/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20File%20|%20Open%20Executable%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




