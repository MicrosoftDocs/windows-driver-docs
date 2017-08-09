---
title: WinDbg Preview - View Menu 
description: This section describes how work with the view menu.
ms.author: windowsdriverdev
ms.date: 07/28/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---


<h3 style="background-color:rgb(255,0,0)">
This documentation is preliminary and is subject to change.
</h3>

# WinDbg Preview View Menu 

This section describes how work with the view menu in WinDbg Preview.

![View menu in debugger](images/windbgx-view-menu.png)

The view menu will open a new Window for each item, or bring focus to the existing Window, if one is already open.

## Command 
The command Window allows you to enter debugger commands. For more information about debugger commands, see [Debugger Commands](debugger-commands.md).

## Watch 

The watch Window allows you to watch local variables and registers. 

The locals and watch windows are both based off of the data model that is used by the dx command. This means the locals and watch windows will benefit from any NatVis or JavaScript extensions you have loaded, and support full LINQ queries, just like the dx command. 

## Locals
The Locals window displays information about all of the local variables in the current scope.

## Registers

Registers displays the contents of the processors registers when they are available. For more information about registers, see [Registers](registers.md) and [Viewing and Editing Registers in WinDbg](registers-window.md).

## Memory

The memory window .

![Memory menu in debugger](images/windbgx-memory-preview.png)

## Stack 

The stack Window also provides highlighting. 

TBD - - For more information, see [Viewing the Call Stack in WinDbg](calls-window.md).

## Disassembly
The disassembly window highlights the current instruction remains where it is when you scroll. 


## Threads


## Breakpoints

## Logs

 This is a under the covers log of the WinDbg Preview internals. It can be viewed for troubleshooting or to monitor long running processes. 
 
 You can continue to create a command log, using the .logopen command. For more information on that, see [Keeping a Log File in WinDbg](keeping-a-log-file-in-windbg.md).

## Reset Windows

Use this function to reset the 

*Additional content pending*

## See Also

[Debugging Using WinDbg Preview](debugging-using-windbg-preview.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20Debugging%20Using%20WinDbg%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




