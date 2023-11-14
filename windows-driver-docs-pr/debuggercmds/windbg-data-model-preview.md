---
title: WinDbg - Data Model Menu
description: This section describes how to work with the data model menu in the WinDbg debugger.
ms.date: 01/10/2020
---

# WinDbg - Data Model Menu

This section describes how to work with the data model menu in the WinDbg debugger.

## New Model Query

Use the New Model Query dialog to create a new model query. You can put anything here you'd put into a normal `dx` command.

For example, specify `Debugger.Sessions` to examine the debugger sessions objects. 

:::image type="content" source="images/windbgx-data-model-new-model-dialog.png" alt-text="Screenshot of the New data model query dialog box in WinDbg.":::

For general information about the debugger objects refer to [dx (Display Debugger Object Model Expression)](dx--display-visualizer-variables-.md).

Use LINQ queries to dig deeper into the session. This query shows the top 5 processes running the most threads. 

```dbgcmd
Debugger.Sessions.First().Processes.Select(p => new { Name = p.Name, ThreadCount = p.Threads.Count() }).OrderByDescending(p => p.ThreadCount),5
```

:::image type="content" source="images/windbgx-data-model-process-threads.png" alt-text="Screenshot of the Data model explore window displaying processes and threads in WinDbg.":::

## Data Model Explorer

Use the data model explorer to quickly browse every data model object in the `Debugger` namespace.

:::image type="content" source="images/windbgx-data-model-explore-window.png" alt-text="Screenshot of the Data model explorer window with debug object sessions in WinDbg.":::

### Display Mode

Use display mode to toggle between grid and hierarchy display mode. You can right-click column headers to hide or show more columns.

Grid mode can be useful to dig down in the objects. For example, here is the previous top threads query in grid view. 

:::image type="content" source="images/windbgx-data-model-process-threads-grid.png" alt-text="Screenshot of the Data model explore window displaying top threads in grid view in WinDbg.":::

When you click on any underlined item a new tab is opened and a query is run to display that information.

This query shows the devices in the plug and play device tree grouped by the name of the physical device object's driver for a kernel session.

```dbgcmd
Debugger.Sessions.First().Devices.DeviceTree.Flatten(n => n.Children).GroupBy(n => n.PhysicalDeviceObject->Driver->DriverName.ToDisplayString()) 
```

:::image type="content" source="images/windbgx-data-model-pnp-device.png" alt-text="Screenshot of the Data model explore window presenting plug and play device tree in grid view in WinDbg.":::

### Change Query

Use change query to change the query that is used in the active data model window.

---

## See Also

[dx (Display Debugger Object Model Expression)](dx--display-visualizer-variables-.md)

[WinDbg Features](../debugger/debugging-using-windbg-preview.md)
