---
title: Enabling Support for the Direct3D Version 10 DDI
description: Enabling Support for the Direct3D Version 10 DDI
ms.assetid: ccbfecd2-8609-4e59-ac43-911f57af7980
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Enabling Support for the Direct3D Version 10 DDI


To enable support for a user-mode display driver DLL's version 10 DDI, the INF file that installs the display drivers for a graphics device must list the name of the DLL regardless of whether the Direct3D version 10 DDI exists in the same DLL as the [Direct3D version 9 DDI](https://msdn.microsoft.com/library/windows/hardware/ff552927) or in a separate DLL.

The [Installation Requirements for Display Miniport and User-Mode Display Drivers](installing-display-miniport-and-user-mode-display-drivers.md) section describes how a user-mode display driver is installed and used according to the Windows Vista display driver model. To also enable support for the Direct3D version 10 DDI, you must specify the name of the DLL that contains the version 10 DDI as the second entry in the list of user-mode display driver names even if the version 10 DDI exists in the same DLL as the version 9 DDI. The following example shows how support for the version 10 DDI is enabled if the version 10 DDI is contained in *Umd10*.dll (that is, a separate DLL from the version 9 DDI):

```
[Xxx_SoftwareDeviceSettings]
...
 HKR,, UserModeDriverName,    %REG_MULTI_SZ%, umd9.dll, umd10.dll
 HKR,, InstalledDisplayDrivers,    %REG_MULTI_SZ%, umd9, umd10 
```

The following example shows how support for the version 10 DDI is enabled if the version 10 DDI is contained in *Umd*.dll (that is, the same DLL as the version 9 DDI):

```
[Xxx_SoftwareDeviceSettings]
...
 HKR,, UserModeDriverName,    %REG_MULTI_SZ%, umd.dll, umd.dll
 HKR,, InstalledDisplayDrivers,    %REG_MULTI_SZ%, umd, umd 
```

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Enabling%20Support%20for%20the%20Direct3D%20Version%2010%20DDI%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




