---
title: Using Script Files
description: Using Script Files
ms.assetid: b78a651e-57c8-4863-a8cf-dedd8e308e66
keywords: ["script file", "script file, overview"]
---

# Using Script Files


## <span id="ddk_using_script_files_dbg"></span><span id="DDK_USING_SCRIPT_FILES_DBG"></span>


A *script file* is a text file that contains a sequence of debugger commands. There are a variety of ways for the debugger to load a script file and execute it. A script file can contain commands to be executed sequentially or can use a more complex flow of execution.

To execute a script file, you can do one of the following:

-   (KD and CDB only; only when the debugger starts) Create a script file that is named Ntsd.ini and put it in the directory where you are starting the debugger from. The debugger automatically executes this file when the debugger starts. To use a different file for the startup script file, specify the path and file name by using the **-cf** [command-line option](https://msdn.microsoft.com/library/windows/hardware/ff539174) or by using the **IniFile** entry in the [Tools.ini](configuring-tools-ini.md) file.

-   (KD and CDB only; when each session starts) Create a script file and specify its path and file name by using the **-cfr** [command-line option](https://msdn.microsoft.com/library/windows/hardware/ff539174). The debugger automatically executes this script file when the debugger starts and every time that the target is restarted.

-   Use the **$&lt;**, **$&gt;&lt;**, **$$&lt;**, and **$$&gt;&lt;** commands to execute a script file after the debugger is running. For more information about the syntax, see [**$&lt;, $&gt;&lt;, $&gt;&lt;, $$&gt;&lt; (Run Script File)**](https://msdn.microsoft.com/library/windows/hardware/ff566261).

The **$&gt;&lt;** and **$$&gt;&lt;** commands differ from the other methods of running scripts in one important way. When you use these commands, the debugger opens the specified script file, replaces all carriage returns with semicolons, and executes the resulting text as a single command block. These commands are useful for running scripts that contain debugger command programs. For more information about these programs, see [Using Debugger Command Programs](using-debugger-command-programs.md).X

You cannot use commands that are available only in WinDbg (such as [**.lsrcfix (Use Local Source Server)**](https://msdn.microsoft.com/library/windows/hardware/ff565371), [**.lsrcpath (Set Local Source Path)**](https://msdn.microsoft.com/library/windows/hardware/ff565378), [**.open (Open Source File)**](https://msdn.microsoft.com/library/windows/hardware/ff564622), and [**.write\_cmd\_hist (Write Command History)**](https://msdn.microsoft.com/library/windows/hardware/ff566180)) in script files, even if the script file is executed in WinDbg. In addition, you cannot use the [**.beep (Speaker Beep)**](https://msdn.microsoft.com/library/windows/hardware/ff562141), [**.cls (Clear Screen)**](https://msdn.microsoft.com/library/windows/hardware/ff562246), [**.hh (Open HTML Help File)**](https://msdn.microsoft.com/library/windows/hardware/ff563197), [**.idle\_cmd (Set Idle Command)**](https://msdn.microsoft.com/library/windows/hardware/ff563217), [**.remote (Create Remote.exe Server)**](https://msdn.microsoft.com/library/windows/hardware/ff564818), kernel-mode [**.restart (Restart Kernel Connection)**](https://msdn.microsoft.com/library/windows/hardware/ff564821), user-mode [**.restart (Restart Target Application)**](https://msdn.microsoft.com/library/windows/hardware/ff564823), or [**.wtitle (Set Window Title)**](https://msdn.microsoft.com/library/windows/hardware/ff566185) commands in a script file.

WinDbg supports the same scripts as KD and CDB, with one minor exception. You can use the [**.remote\_exit (Exit Debugging Client)**](https://msdn.microsoft.com/library/windows/hardware/ff564812) command only in a script file that KD or CDB uses. You cannot exit from a debugging client though a script that is executed in WinDbg.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20Using%20Script%20Files%20%20RELEASE:%20%284/24/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




