---
title: Enabling Support for the Direct3D Version 10 DDI
description: Enabling Support for the Direct3D Version 10 DDI
ms.assetid: ccbfecd2-8609-4e59-ac43-911f57af7980
ms.date: 10/20/2018
ms.localizationpriority: medium
---

# Enabling Support for the Direct3D Version 10 DDI


To enable support for a user-mode display driver DLL's version 10 DDI, the INF file that installs the display drivers for a graphics device must list the name of the DLL regardless of whether the Direct3D version 10 DDI exists in the same DLL as the [Direct3D version 9 DDI](https://docs.microsoft.com/windows-hardware/drivers/display/direct3d-functions-implemented-by-user-mode#direct3d-version-9-functions) or in a separate DLL.

The [Installation Requirements for Display Miniport and User-Mode Display Drivers](installing-display-miniport-and-user-mode-display-drivers.md) section describes how a user-mode display driver is installed and used according to the Windows Vista display driver model. To also enable support for the Direct3D version 10 DDI, you must specify the name of the DLL that contains the version 10 DDI as the second entry in the list of user-mode display driver names even if the version 10 DDI exists in the same DLL as the version 9 DDI. The following example shows how support for the version 10 DDI is enabled if the version 10 DDI is contained in *Umd10*.dll (that is, a separate DLL from the version 9 DDI):

```inf
[Xxx_SoftwareDeviceSettings]
...
 HKR,, UserModeDriverName,    %REG_MULTI_SZ%, umd9.dll, umd10.dll
 HKR,, InstalledDisplayDrivers,    %REG_MULTI_SZ%, umd9, umd10 
```

The following example shows how support for the version 10 DDI is enabled if the version 10 DDI is contained in *Umd*.dll (that is, the same DLL as the version 9 DDI):

```inf
[Xxx_SoftwareDeviceSettings]
...
 HKR,, UserModeDriverName,    %REG_MULTI_SZ%, umd.dll, umd.dll
 HKR,, InstalledDisplayDrivers,    %REG_MULTI_SZ%, umd, umd 
```

 

 





