---
title: Opening a Dump File Using WinDbg
description: There are several ways you can use WinDbg to open a dump file.
ms.assetid: DE2EABE7-2B7A-4DF9-82FD-EF19D69E31A7
ms.author: domars
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# Opening a Dump File Using WinDbg


There are several ways you can use WinDbg to open a dump file.

### <span id="WinDbg_Menu"></span><span id="windbg_menu"></span><span id="WINDBG_MENU"></span>WinDbg Menu

If WinDbg is already running and is in dormant mode, you can open a dump by choosing **Open Crash Dump** from the **File** menu or by pressing CTRL+D. When the Open Crash Dump dialog box appears, enter the full path and name of the crash dump file in the **File name** box, or use the dialog box to select the proper path and file name. When the proper file has been chosen, click **Open**.

### <span id="Command_Prompt"></span><span id="command_prompt"></span><span id="COMMAND_PROMPT"></span>Command Prompt

In a Command Prompt window, you can open a dump file when you launch WinDbg. Use the following command:

**windbg -y** *SymbolPath* **-i** *ImagePath* **-z** *DumpFileName*

The **-v** option (verbose mode) is also useful. For more information about the command-line syntax, see [**WinDbg Command-Line Options**](windbg-command-line-options.md).

### <span id="Debugger_Command_Window"></span><span id="debugger_command_window"></span><span id="DEBUGGER_COMMAND_WINDOW"></span>Debugger Command Window

If WinDbg is already in a kernel-mode debugging session, you can open a dump file by using the [**.opendump (Open Dump File)**](-opendump--open-dump-file-.md) command, followed by [**g (Go)**](g--go-.md).

 

 





