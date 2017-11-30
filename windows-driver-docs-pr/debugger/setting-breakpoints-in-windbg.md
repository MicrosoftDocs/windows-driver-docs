---
title: Setting Breakpoints in WinDbg
description: There are several ways you can set, view, and manipulate breakpoints using WinDbg.
ms.assetid: 4A7BE6D2-05AF-4EFB-8F24-C19B1A98217C
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20Setting%20Breakpoints%20in%20WinDbg%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




