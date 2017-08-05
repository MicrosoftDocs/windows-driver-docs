---
title: WinDbg Preview - File Menu
description: This section describes how to use the file menu in the WinDbg preview debugger.
ms.author: windowsdriverdev
ms.date: 08/04/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# WinDbg Preview - File Menu 

This topic describes how to how to use the file menu.

### Start debugging

Use *Start debugging* to configure new and open existing debugger sessions. Session connection information is stored in workspace configuration files. Workspace files are stored with a .debugTarget file extension.

You can use the right click menu to pin workspace files as well as edit them in notepad.

![Workspace file right click menu showing open rename edit in notepad pin and remove from list as well as clear unpinned targets](/images/windbgx-workspace-right-click.png)

For more information on working settings an workspaces see [WinDbg Preview Setup – settings and workspaces](windbg-setup-preview.md).


### Save workspace

Use *Save workspace* to save the current workspace. Do this when TBD.

The default location for workspace files is: 

```
C:\Users\*UserName*\AppData\Local\DBG\targets
```

### Open source file

Use *Open source file* to open a source file. Do this when you want to work with additional source files that have not been loaded because of code execution. For more information on working with source files, see [Source Code Debugging in WinDbg](source-window.md)


### Open script

Use *Open script* to open an existing Java or NatVis script. 
For more information on working with scripts see [WinDbg Preview - Scripting Menu](windbg-scripting-preview.md).
>> TBD - need to test behavior

### Settings

Use the settings menu to set the source and symbol path as well as choose the light and dark theme for the debugger. For more information on settings see [WinDbg Preview Setup – settings and workspaces](windbg-setup-preview.md).


### About
Use *About* to display build version information for the debugger. You can use also use this screen to view the Microsoft privacy statement.

 
## See Also

[Debugging Using WinDbg Preview](debugging-using-windbg-preview.md)
 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20Debugging%20Using%20WinDbg%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




