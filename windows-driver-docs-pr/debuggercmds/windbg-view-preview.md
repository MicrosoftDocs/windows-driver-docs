---
title: WinDbg - View Menu 
description: This section describes how work with the view menu.
ms.date: 07/02/2020
---

# WinDbg - View Menu

:::image type="content" source="images/windbgx-preview-logo.png" alt-text="WinDbg logo with a magnifying glass inspecting bits.":::

This section describes how work with the view menu in WinDbg.

:::image type="content" source="images/windbgx-view-menu.png" alt-text="Screenshot of the View menu in WinDbg.":::

The view menu will open a new Window for each item, or bring focus to the existing Window, if one is already open.

## Command

The command Window allows you to enter debugger commands. For more information about debugger commands, see [Debugger Commands](debugger-commands.md).

## Watch

The watch Window allows you to watch local variables and registers. 

The locals and watch windows are both based off of the data model that is used by the dx command. This means the locals and watch windows will benefit from any NatVis or JavaScript extensions you have loaded, and support full LINQ queries, just like the dx command. For more information about the data model, see [WinDbg - Data Model](windbg-data-model-preview.md).

## Locals

The locals window displays information about all of the local variables in the current scope. The locals window will highlight values that have changed during the previous code execution.

:::image type="content" source="images/windbgx-locals-window.png" alt-text="Screenshot of the Locals window in WinDbg.":::

## Registers

Registers displays the contents of the processors registers when they are available. For more information about registers, see [Registers](../debugger/registers.md) and [Viewing and Editing Registers in WinDbg (Classic)](../debugger/registers-window.md).

## Memory

Use the memory window to display memory locations. In addition to providing a memory address, you can use the  Pseudo-Register values such as $scopeip and $eventip to examine memory. Pre-append the @ symbol to use the pseudo-register values in the memory window, for example, `@$scopeip`. For more information, see [Pseudo-Register Syntax](pseudo-register-syntax.md)

## Stack

Use the stack Window to view the current call stack. The stack window provides basic highlighting of the current frame. 

## Disassembly

The disassembly window highlights the current instruction and retains that position when you scroll. 

:::image type="content" source="images/windbgx-disassembly.png" alt-text="Screenshot of the Disassembly window in WinDbg.":::

## Threads

The threads window highlights the current thread.

## Breakpoints

Use the breakpoints window to view, enable and clear breakpoints.

:::image type="content" source="images/windbgx-breakpoints-window.png" alt-text="Screenshot of the Breakpoints window in WinDbg.":::

## Logs

 This log is of the WinDbg internals. It can be viewed to monitor long running processes and for troubleshooting the debugger itself.

 You can continue to create a traditional debugger command log, using the .logopen command. For more information on that, see [Keeping a Log File in WinDbg](../debugger/keeping-a-log-file-in-windbg.md).

## Notes

Use the Notes option to open a note taking window.

## Timelines

Use Timelines to open or bring focus to the timelines window. For more information on timelines, see [WinDbg - Timelines](windbg-timeline-preview.md).

## Modules

Use modules to display loaded modules and their related information. Modules displays the following:

- The name of the module including the path location
- The size in bytes of the loaded module
- The base address that the module is loaded at
- The file version

:::image type="content" source="images/windbgx-view-modules.png" alt-text="Screenshot of the Modules view window with five modules listed in WinDbg.":::

## Layouts

Use the Layouts pull down menu to select from three window layouts.

## Reset Windows

Use this function to reset the debugger windows to their default positions.

## Accent Color

Use the pull down menu to set the accent color for the debugger.

## See Also

[WinDbg Features](../debugger/debugging-using-windbg-preview.md)
