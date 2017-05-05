---
title: Adding Software Registry Settings
description: Adding Software Registry Settings
ms.assetid: 96c7fc9e-885c-43ec-973a-6e6d984fe7d0
keywords:
- INF files WDK display , software registry settings
- software registry settings WDK display
- registry WDK display
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Adding Software Registry Settings


The INF file must add all software registry settings to the Plug and Play (PnP) software key as shown in the following example:

```
[Xxx.Mfg]
"RADEON 8500/RADEON 8500LE (R200 LDDM)" = R200_R200, PCI\VEN_1002&DEV_514c&SUBSYS_003a1002

[R200_R200]
Include=msdv.inf
CopyFiles=R200.Miniport, R200.Display
AddReg = R200_SoftwareDeviceSettings
AddReg = R200_R200_SoftwareDeviceSettings
DelReg = R200_RemoveDeviceSettings 
```

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Adding%20Software%20Registry%20Settings%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




