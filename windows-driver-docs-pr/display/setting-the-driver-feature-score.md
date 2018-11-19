---
title: Setting the Driver Feature Score
description: Setting the Driver Feature Score
ms.assetid: 833e8f29-b90a-4754-9c0a-d8356a731ae4
keywords:
- INF files WDK display , FeatureScore directive
- FeatureScore directive WDK display
ms.date: 04/20/2017
ms.localizationpriority: medium
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

```inf
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

 
