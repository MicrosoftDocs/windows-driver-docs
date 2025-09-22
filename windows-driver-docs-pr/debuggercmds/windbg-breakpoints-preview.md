---
title: "WinDbg - Breakpoints Menu"
description: "This section describes how to set and clear breakpoints by using WinDbg, the debugger for Windows."
keywords: ["Breakpoints Menu", "WinDbg", "Menu", "Windows Debugging"]
ms.date: 08/15/2017
ms.topic: how-to
---

# WinDbg: Breakpoints menu

This section describes how to work with breakpoints by using WinDbg, the debugger for Windows.

## Breakpoints menu

Use the **Breakpoints** menu to create new and remove existing breakpoints. You can also toggle the initial breakpoint. (Currently, the initial breakpoint is kernel only.)

:::image type="content" source="images/windbgx-breakpoints-menu.png" alt-text="Screenshot of the Breakpoints menu in WinDbg.":::

## Breakpoints window

Use the **View** menu to open the Breakpoints window so that you can view, set, and clear breakpoints. You can also double-click a breakpoint to open its source file.

:::image type="content" source="images/windbgx-breakpoints-window.png" alt-text="Screenshot of the Breakpoints window in WinDbg.":::

The Breakpoints window keeps a running total of each time that the breakpoint is hit.

The general process of working with breakpoints is similar to previous versions of WinDbg. For more information about setting breakpoints, see [Set breakpoints in WinDbg (classic)](../debugger/setting-breakpoints-in-windbg.md).