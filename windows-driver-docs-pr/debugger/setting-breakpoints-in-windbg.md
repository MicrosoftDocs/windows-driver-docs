---
title: Setting Breakpoints in WinDbg
description: There are several ways you can set, view, and manipulate breakpoints using WinDbg.
ms.assetid: 4A7BE6D2-05AF-4EFB-8F24-C19B1A98217C
ms.author: domars
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# Setting Breakpoints in WinDbg


There are several ways you can set, view, and manipulate breakpoints using WinDbg.

## <span id="Debugger_Command_Window"></span><span id="debugger_command_window"></span><span id="DEBUGGER_COMMAND_WINDOW"></span>Debugger Command Window


You can set, view, and manipulate breakpoints by entering commands in the Debugger Command Window. For a list of commands, see [Methods of Controlling Breakpoints](methods-of-controlling-breakpoints.md).

## <span id="WinDbg_Menu"></span><span id="windbg_menu"></span><span id="WINDBG_MENU"></span>WinDbg Menu


You can open the **Breakpoints** dialog box by choosing **Breakpoints** from the **Edit** menu or by pressing ALT+F9. This dialog box lists all breakpoints, and you can use it to disable, enable, or clear existing breakpoints or to set new breakpoints.

## <span id="Code_Windows"></span><span id="code_windows"></span><span id="CODE_WINDOWS"></span>Code Windows


The Disassembly window and the Source windows highlight lines that have breakpoints set. Enabled breakpoints are red, and disabled breakpoints are yellow.

If you set the cursor on a specific line in the Disassembly window or in a Source window, you can press F9 to set a breakpoint at that line.

 

 





