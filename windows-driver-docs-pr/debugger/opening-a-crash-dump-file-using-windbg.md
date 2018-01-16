---
title: Opening a Dump File Using WinDbg
description: There are several ways you can use WinDbg to open a dump file.
ms.assetid: DE2EABE7-2B7A-4DF9-82FD-EF19D69E31A7
ms.author: domars
ms.date: 11/28/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20Opening%20a%20Dump%20File%20Using%20WinDbg%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




