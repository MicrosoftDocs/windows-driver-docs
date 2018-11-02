---
title: Adding Software Registry Settings
description: Adding Software Registry Settings
ms.assetid: 96c7fc9e-885c-43ec-973a-6e6d984fe7d0
keywords:
- INF files WDK display , software registry settings
- software registry settings WDK display
- registry WDK display
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Adding Software Registry Settings


The INF file must add all software registry settings to the Plug and Play (PnP) software key as shown in the following example:

```inf
[Xxx.Mfg]
"RADEON 8500/RADEON 8500LE (R200 LDDM)" = R200_R200, PCI\VEN_1002&DEV_514c&SUBSYS_003a1002

[R200_R200]
Include=msdv.inf
CopyFiles=R200.Miniport, R200.Display
AddReg = R200_SoftwareDeviceSettings
AddReg = R200_R200_SoftwareDeviceSettings
DelReg = R200_RemoveDeviceSettings 
```

 

 





