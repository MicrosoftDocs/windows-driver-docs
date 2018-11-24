---
title: Enabling Support for the Direct3D Version 11 DDI
description: Enabling Support for the Direct3D Version 11 DDI
ms.assetid: 997d6b06-110b-403d-bcf5-350a26ecffbd
keywords:
- Direct3D version 11 WDK Windows 7 display , enabling DDI support
- Direct3D version 11 WDK Windows Server 2008 R2 display , enabling DDI support
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Enabling Support for the Direct3D Version 11 DDI


This section applies only to Windows 7 and later, and Windows Server 2008 R2 and later versions of Windows operating system.

To enable support for a user-mode display driver DLL's version 11 DDI, the INF file that installs the display drivers for a graphics device must list the name of the DLL regardless of whether the Direct3D version 11 DDI exists in the same DLL as the [Direct3D version 9 DDI](https://msdn.microsoft.com/library/windows/hardware/ff552927) and [Direct3D version 10 DDI](https://msdn.microsoft.com/library/windows/hardware/ff552909) or in a separate DLL.

The [Installation Requirements for Display Miniport and User-Mode Display Drivers](installing-display-miniport-and-user-mode-display-drivers.md) section describes how a user-mode display driver is installed and used according to the Windows Vista display driver model. To also enable support for the Direct3D version 11 DDI, you must specify the name of the DLL that contains the version 11 DDI as the third entry in the list of user-mode display driver names even if the version 11 DDI exists in the same DLL as the version 9 and 10 DDIs.

You can use the same user-mode display driver DLL name in multiple locations to unify your driver implementation. In fact, the design of the Direct3D version 10 and version 11 DDIs strongly supports a shared implementation of Direct3D version 10 and Direct3D version 11 drivers.

The following example shows how support for the version 11 DDI is enabled if the version 11 DDI is contained in *Umd11*.dll (that is, a separate DLL from the version 9 and 10 DDIs):

```inf
 [Xxx_SoftwareDeviceSettings]
...
 HKR,, UserModeDriverName,    %REG_MULTI_SZ%, umd9.dll, umd10.dll,  umd11.dll
 HKR,, InstalledDisplayDrivers,    %REG_MULTI_SZ%, umd9, umd10, umd11 
```

The following example shows how support for the version 11 DDI is enabled if the version 11 DDI is contained in *Umd*.dll (that is, a shared implementation of Direct3D version 9, 10 and 11 drivers):

```inf
[Xxx_SoftwareDeviceSettings]
...
 HKR,, UserModeDriverName,    %REG_MULTI_SZ%, umd.dll, umd.dll, umd.dll
 HKR,, InstalledDisplayDrivers,    %REG_MULTI_SZ%, umd, umd, umd 
```

 

 





