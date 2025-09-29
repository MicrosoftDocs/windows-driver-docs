---
title: 'WinDbg: Data Model Menu'
description: "This article describes how to work with the Data Model menu in the WinDbg debugger."
keywords: ["Data Model Menu", "WinDbg", "Menu", "Windows Debugging"]
ms.date: 01/10/2020
ms.topic: how-to
---

# WinDbg: Data model menu

This article describes how to work with the data model menu in WinDbg, the debugger for Windows.

## New model query

Use the **Specify Model Query** dialog to create a new model query. You can put anything here that you put into a normal `dx` command.

For example, specify `Debugger.Sessions` to examine the debugger sessions objects.

:::image type="content" source="images/windbgx-data-model-new-model-dialog.png" alt-text="Screenshot of the Specify Model Query dialog in WinDbg.":::

For general information about the debugger objects, refer to [dx (Display debugger object model expression)](dx--display-visualizer-variables-.md).

Use LINQ queries to dig deeper into the session. This query shows the top five processes that run the most threads.

```dbgcmd
Debugger.Sessions.First().Processes.Select(p => new { Name = p.Name, ThreadCount = p.Threads.Count() }).OrderByDescending(p => p.ThreadCount),5
```

:::image type="content" source="images/windbgx-data-model-process-threads.png" alt-text="Screenshot of the Data Model window displaying processes and threads in WinDbg.":::

## Data model explorer

Use the data model explorer to quickly browse every data model object in the `Debugger` namespace.

:::image type="content" source="images/windbgx-data-model-explore-window.png" alt-text="Screenshot of the Data Model window with debug object sessions in WinDbg.":::

### Display mode

Use display mode to toggle between grid, hierarchy, and graph display modes. You can right-click column headers to hide or show more columns.

Grid mode is useful when you want to dig down in the objects. For example, here's the previous top threads query in grid view.

:::image type="content" source="images/windbgx-data-model-process-threads-grid.png" alt-text="Screenshot of the Data Model window displaying top threads in grid view in WinDbg.":::

Selecting any underlined item opens a new tab and runs a query to display that information.

This query shows the devices in the plug-and-play device tree grouped by the name of the physical device object's driver for a kernel session.

```dbgcmd
Debugger.Sessions.First().Devices.DeviceTree.Flatten(n => n.Children).GroupBy(n => n.PhysicalDeviceObject->Driver->DriverName.ToDisplayString()) 
```

:::image type="content" source="images/windbgx-data-model-pnp-device.png" alt-text="Screenshot of the Data Model window presenting a plug-and-play device tree in the grid view in WinDbg.":::

### Change query

Edit the query text box to change the query that's used in the active Data Model window.

### Change window or tab title

New generic data model windows are given the Data Model title. You can customize titles by invoking the **Change Title** context menu item from either the tab or window title pane.

:::image type="content" source="images/windbgx-data-model-custom-titles.png" alt-text="Screenshot of the Data Model window presenting two tabs with custom titles in WinDbg.":::

> [!NOTE]
> The title can't be empty or contain semicolons.

---

## Related content

- [dx (Display debugger object model expression)](dx--display-visualizer-variables-.md)
- [WinDbg features](../debugger/debugging-using-windbg-preview.md)
