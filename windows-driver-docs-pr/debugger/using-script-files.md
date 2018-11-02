---
title: Using Script Files
description: Using Script Files
ms.assetid: b78a651e-57c8-4863-a8cf-dedd8e308e66
keywords: ["script file", "script file, overview"]
ms.author: domars
ms.date: 05/23/2017
ms.localizationpriority: medium
---

# Using Script Files


## <span id="ddk_using_script_files_dbg"></span><span id="DDK_USING_SCRIPT_FILES_DBG"></span>


A *script file* is a text file that contains a sequence of debugger commands. There are a variety of ways for the debugger to load a script file and execute it. A script file can contain commands to be executed sequentially or can use a more complex flow of execution.

To execute a script file, you can do one of the following:

-   (KD and CDB only; only when the debugger starts) Create a script file that is named Ntsd.ini and put it in the directory where you are starting the debugger from. The debugger automatically executes this file when the debugger starts. To use a different file for the startup script file, specify the path and file name by using the **-cf** [command-line option](command-line-options.md) or by using the **IniFile** entry in the [Tools.ini](configuring-tools-ini.md) file.

-   (KD and CDB only; when each session starts) Create a script file and specify its path and file name by using the **-cfr** [command-line option](command-line-options.md). The debugger automatically executes this script file when the debugger starts and every time that the target is restarted.

-   Use the **$&lt;**, **$&gt;&lt;**, **$$&lt;**, and **$$&gt;&lt;** commands to execute a script file after the debugger is running. For more information about the syntax, see [**$&lt;, $&gt;&lt;, $&gt;&lt;, $$&gt;&lt; (Run Script File)**](-----------------------a---run-script-file-.md).

The **$&gt;&lt;** and **$$&gt;&lt;** commands differ from the other methods of running scripts in one important way. When you use these commands, the debugger opens the specified script file, replaces all carriage returns with semicolons, and executes the resulting text as a single command block. These commands are useful for running scripts that contain debugger command programs. For more information about these programs, see [Using Debugger Command Programs](using-debugger-command-programs.md).X

You cannot use commands that are available only in WinDbg (such as [**.lsrcfix (Use Local Source Server)**](-srcfix---lsrcfix--use-source-server-.md), [**.lsrcpath (Set Local Source Path)**](-srcpath---lsrcpath--set-source-path-.md), [**.open (Open Source File)**](-open--open-source-file-.md), and [**.write\_cmd\_hist (Write Command History)**](-write-cmd-hist--write-command-history-.md)) in script files, even if the script file is executed in WinDbg. In addition, you cannot use the [**.beep (Speaker Beep)**](-beep--speaker-beep-.md), [**.cls (Clear Screen)**](-cls--clear-screen-.md), [**.hh (Open HTML Help File)**](-hh--open-html-help-file-.md), [**.idle\_cmd (Set Idle Command)**](-idle-cmd--set-idle-command-.md), [**.remote (Create Remote.exe Server)**](-remote--create-remote-exe-server-.md), kernel-mode [**.restart (Restart Kernel Connection)**](-restart--restart-kernel-connection-.md), user-mode [**.restart (Restart Target Application)**](-restart--restart-target-application-.md), or [**.wtitle (Set Window Title)**](-wtitle--set-window-title-.md) commands in a script file.

WinDbg supports the same scripts as KD and CDB, with one minor exception. You can use the [**.remote\_exit (Exit Debugging Client)**](-remote-exit--exit-debugging-client-.md) command only in a script file that KD or CDB uses. You cannot exit from a debugging client though a script that is executed in WinDbg.

 

 





