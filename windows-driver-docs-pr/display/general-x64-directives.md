---
title: General x64 directives
description: This topic describes the changes that are needed to properly decorate the INF for use on 64-bit Windows.
ms.assetid: FC372524-0422-4022-AF54-4C6116C89F30
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# General x64 directives


This topic describes the changes that are needed to properly decorate the INF for use on 64-bit Windows.

For example:

``` syntax
[DestinationDirs]
DefaultDestDir  = 11
R200.Miniport   = 12  ; drivers
R200.Display    = 11  ; system32
R200.DispWow  = 10, SysWow64

[Manufacturer]
%ATI% = ATI.Mfg, NTamd64

[ATI.Mfg.NTamd64]

[R200_RV200]
FeatureScore=F8
CopyFiles=R200.Miniport, R200.Display, R200.DispWow
AddReg = R200_SoftwareDeviceSettings
AddReg = R200_RV200_SoftwareDeviceSettings
DelReg = R200_RemoveDeviceSettings

; File sections
;

[r200.Miniport]
r200.sys

[r200.Display]
r200umd.dll,,,0x00004000             ; COPYFLG_IN_USE_TRY_RENAME

[R200.DispWow]
r2umd32.dll,,,0x00004000             ; COPYFLG_IN_USE_TRY_RENAME
```

 

 





