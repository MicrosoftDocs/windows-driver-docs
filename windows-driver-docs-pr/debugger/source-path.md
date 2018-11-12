---
title: Source Path
description: This topic covers how to set the source path or load the individual source files.
ms.assetid: b5dcb557-b413-401a-be4b-2d45b2597e6c
keywords: source files and paths, source path
ms.author: domars
ms.date: 05/23/2017
ms.localizationpriority: medium
---

# Source Path


## <span id="ddk_source_path_dbg"></span><span id="DDK_SOURCE_PATH_DBG"></span>


The *source path* specifies the directories where the C and C++ source files are located.

If you are debugging a user-mode process on the computer where the executable file was built, and if the source files are still in their original location, the debugger can automatically locate the source files.

In most other situations, you have to set the source path or load the individual source files.

When you are performing [remote debugging through the debugger](remote-debugging-through-the-debugger.md), the debugging server uses the source path. If you are using WinDbg as your debugger, each debugging client also has its own *local source path*. All source-related commands access the source files on the local computer. You have to set the proper paths on any client or server that you want to use source commands.

This multiple-path system also enables a debugging client to use source-related commands without actually sharing the source files with other clients or with the server. This system is useful if there are private or confidential source files that one of the users has access to.

You can also load source files at any time, regardless of the source path.

### <span id="source_path_syntax"></span><span id="SOURCE_PATH_SYNTAX"></span>Source Path Syntax

The debugger's source path is a string that consists of multiple directory paths, separated by semicolons.

Relative paths are supported. However, unless you always start the debugger from the same directory, you should add a drive letter or a network share before each path. Network shares are also supported.

**Note**   If you are connected to a corporate network, the most efficient way to access source files is to use a source server. You can use a source server by using the **srv\\*** string within your source path. For more information about source servers, see [Using a Source Server](using-a-source-server.md).

 

### <span id="controlling_the_source_path"></span><span id="CONTROLLING_THE_SOURCE_PATH"></span>Controlling the Source Path

To control the source path and local source path, you can do one of the following:

-   Before you start the debugger, use the \_NT\_SOURCE\_PATH [environment variable](environment-variables.md) to set the source path. If you try to add an invalid directory through this environment variable, the debugger ignores this directory.

-   When you start the debugger, use the **-srcpath**[command-line option](command-line-options.md) to set the source path.

-   Use the [**.srcpath (Set Source Path)**](-srcpath---lsrcpath--set-source-path-.md) command to display, set, change, or append to the source path. If you are using a source server, [**.srcfix (Use Source Server)**](-srcfix---lsrcfix--use-source-server-.md) is slightly easier.

-   (WinDbg only) Use the [**.lsrcpath (Set Local Source Path)**](-srcpath---lsrcpath--set-source-path-.md) command to display, set, change, or append to the local source path. If you are using a source server, [**.lsrcfix (Use Local Source Server)**](-srcfix---lsrcfix--use-source-server-.md) is slightly easier. You can also use the WinDbg Command-Line with the parameter -lscrpath. For more information, see [**WinDbg Command-Line Options**](windbg-command-line-options.md).

-   (WinDbg only) Use the [File | Source File Path](file---source-file-path.md) command or press CTRL+P to display, set, change, or append to the source path or the local source path.

You can also directly open or close a source file by doing one of the following:

-   Use the [**lsf (Load or Unload Source File)**](lsf--lsf---load-or-unload-source-file-.md) command to open or close a source file.

-   (WinDbg only) Use the [**.open (Open Source File)**](-open--open-source-file-.md) command to open a source file.

-   (WinDbg only) Use the [file | open source file](file---open-source-file.md) command or press ctrl+o to open a source file. you can also use the **open source file (ctrl+o)** button (![screen shot of the open source file button](images/tbopen.png)) on the toolbar.

    **Note**   When you use **File | Open Source File** (or its shortcut menu or button equivalents) to open a source file, the path of that file is automatically appended to the source path.

     

-   (WinDbg only) Use the [File | Recent Files](file---recent-files.md) command to open one of the four source files that you most recently opened in WinDbg.

-   (WinDbg only) Use the [File | Close Current Window](file---close-current-window.md) command or click the **Close** button in the corner of the [Source window](source-window.md) to close a source file.

For more information about how to use source files, see [Debugging in Source Mode](debugging-in-source-mode.md).

 

 





