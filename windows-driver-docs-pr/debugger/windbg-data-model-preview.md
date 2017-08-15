---
title: WinDbg Preview - Data Model 
description: This section describes how to work with the data model menu in the WinDbg preview debugger.
ms.author: windowsdriverdev
ms.date: 08/10/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

> [!NOTE]
> The information in this topic is preliminary. Updated information will be provided in a later release of the documentation. 
>

## WinDbg Preview - Data Model 

This section describes how to work with the data model menu in the WinDbg Preview debugger.

![Screen shot of data model menu in debugger](images/windbgx-data-model-menu.png)


### New Model Query

Use the New Model Query dialog to create a new model query. You can put anything here you'd put into a normal `dx` command

For example, specify `Debugger.Sessions` to examine the debugger sessions objects. 

![New data model query dialog box](images/windbgx-data-model-new-model-dialog.png)

For general information about the debugger objects refer to [dx (Display Debugger Object Model Expression)](dx--display-visualizer-variables-.md).

Use LINQ queries to dig deeper into the session. This query shows the top 5 processes running the most threads. 

```
Debugger.Sessions.First().Processes.Select(p => new { Name = p.Name, ThreadCount = p.Threads.Count() }).OrderByDescending(p => p.ThreadCount),5
```
![Data model explore window showing process and threads](images/windbgx-data-model-process-threads.png)


### Data Model Explorer

Use the data model explorer to quickly browse every data model object in the `Debugger` namespace.

![Data model explorer window showing debug object sessions](images/windbgx-data-model-explore-window.png)


### Change Query

Use change query to change the query that is used in the active data model window.


### Display Mode

Use display mode to toggle between grid and hierarchy display mode. You can right-click column headers to hide or show more columns.

Grid mode can be useful to dig down in the objects. For example this query shows the devices in the plug and play device tree grouped by the name of the physical device object's driver.

>>> TBD  - Happy to replace this with a handles or module example, if you provide the query string.


```
Debugger.Sessions.First().Devices.DeviceTree.Flatten(n => n.Children).GroupBy(n => n.PhysicalDeviceObject->Driver->DriverName.ToDisplayString()) 
```

![Data model explore window showing plug and play device tree in a grid view](images/windbgx-data-model-pnp-device.png)

When you click on any underlined item a new tab is opened and a query is run to display that information.


---
 
## See Also

[Debugging Using WinDbg Preview](debugging-using-windbg-preview.md)
 
 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20Debugging%20Using%20WinDbg%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




