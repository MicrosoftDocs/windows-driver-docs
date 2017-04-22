---
title: Setting the Driver Feature Score
description: Setting the Driver Feature Score
ms.assetid: 833e8f29-b90a-4754-9c0a-d8356a731ae4
keywords:
- INF files WDK display , FeatureScore directive
- FeatureScore directive WDK display
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Setting the Driver Feature Score


The **FeatureScore** directive is required for all drivers that install and run on Windows Vista and later operating systems.

**Note**   Applies only to Windows 7 and later versions.
The system-supplied display class installer determines whether to install display drivers based on the presence of the **FeatureScore** directive and the value that the **FeatureScore** directive sets. If you attempt to install display drivers that do not have feature score set, you receive an error message.

 

**Note**   A logo test requirement is that drivers that install and run on Windows XP and earlier operating systems and Windows Server 2003 and earlier operating systems not set the **FeatureScore** directive.

 

You must use the **FeatureScore** directive to set the feature score to the following values, depending on the display driver model that the driver is written to and how the driver is distributed.

-   **F8** for in-box drivers that are written to the Windows Display Driver Model (WDDM)

-   **F6** for vendor-supplied drivers that are written to WDDM

-   **FC** for vendor-supplied drivers that are written to the [Windows 2000 display driver model](windows-2000-display-driver-model-design-guide.md)

The following examples show how to add the **FeatureScore** directive:

```
[R200_RV200]
FeatureScore=F6
CopyFiles=R200.Miniport, R200.Display
AddReg = R200_SoftwareDeviceSettings
AddReg = R200_RV200_SoftwareDeviceSettings
DelReg = R200_RemoveDeviceSettings

[R200_R200]
FeatureScore=F6
CopyFiles=R200.Miniport, R200.Display
AddReg = R200_SoftwareDeviceSettings
AddReg = R200_R200_SoftwareDeviceSettings
DelReg = R200_RemoveDeviceSettings

[R200_RV250]
FeatureScore=F6
CopyFiles=R200.Miniport, R200.Display
AddReg = R200_SoftwareDeviceSettings
AddReg = R200_RV250_SoftwareDeviceSettings
DelReg = R200_RemoveDeviceSettings
```

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Setting%20the%20Driver%20Feature%20Score%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




