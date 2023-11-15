---
title: Viewing and Editing Global Variables in WinDbg (Classic)
description: Viewing and Editing Global Variables in WinDbg (Classic)
ms.date: 11/28/2017
---

# Viewing and Editing Global Variables in WinDbg (Classic)

The debugger interprets the name of a global variable as a virtual address. Therefore, you can use all of the commands that are described in [Accessing Memory by Virtual Address](accessing-memory-by-virtual-address.md) to read or write global variables.

In addition, you can use the [**? (Evaluate Expression)**](../debuggercmds/---evaluate-expression-.md) command to display the address that is associated with any symbol.

In WinDbg, you can also use the Watch window to display and change global and local variables. The Watch window can display any list of variables that you want. These variables can include global variables and local variables from any function. At any time, the Watch window displays the values of those variables that match the current function's scope. You can also change the values of these variables through the Watch window.

To open the Watch window, choose **Watch** from the **View** menu. You can also press ALT+2 or click the **Watch** button on the toolbar: :::image type="content" source="images/tbwatch.png" alt-text="Screenshot of the Watch button on the toolbar.":::

The following screen shot shows an example of a Watch window.

:::image type="content" source="images/window-watch.png" alt-text="Screenshot of an example Watch window in WinDbg.":::

The Watch window can contain four columns. The **Name** and **Value** columns are always displayed, and the **Type** and **Location** columns are optional. To display the **Type** and **Location** columns, click the **Typecast** and **Locations** buttons, respectively, on the toolbar.
