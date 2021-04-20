---
title: Loading a User-Mode Display Driver
description: Loading a User-Mode Display Driver
keywords:
- INF files WDK display , user-mode driver loading
- user-mode display drivers WDK Windows Vista , loading
- loading drivers WDK display
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Loading a User-Mode Display Driver


You must set the following entry in an add-registry section of the INF file so that the user-mode display driver's DLL name is added to the registry during driver installation and so that the Microsoft Direct3D runtime can subsequently load the DLL:

```inf
[Xxx_SoftwareDeviceSettings]
...
HKR,, UserModeDriverName,    %REG_MULTI_SZ%, Xxx.dll
```

The INF file must contain information to direct the operating system to copy the user-mode display driver into the system's %systemroot%\\system32 directory. For more information, see [**INF CopyFiles Directive**](../install/inf-copyfiles-directive.md) and [**INF DestinationDirs Section**](../install/inf-destinationdirs-section.md).

The Direct3D runtime obtains the user-mode display driver's DLL name from the registry in order to load the user-mode display driver in the runtime's process space.

 

