---
title: General x64 INF Information
description: General x64 INF Information
keywords:
- INF files WDK display , 64-bit
- 64-bit WDK display
ms.date: 04/20/2017
---

# General x64 INF Information


The following x64-specific information is required for an INF file that loads display drivers that run on 64-bit Windows Vista and later:

```inf
[DestinationDirs]
DefaultDestDir  = 11
R200.Miniport   = 12  ; drivers
R200.Display    = 11  ; system32
R200.DispWow  = 10, SysWow64 ; x64-specific

[Manufacturer]
%ATI% = ATI.Mfg, NTamd64 ; Ntamd64 is x64-specific

[ATI.Mfg.NTamd64] ; Ntamd64 is x64-specific

[R200_RV200]
FeatureScore=F8
CopyFiles=R200.Miniport, R200.Display, R200.DispWow ; R200.DispWow is x64-specific
AddReg = R200_SoftwareDeviceSettings
AddReg = R200_RV200_SoftwareDeviceSettings
DelReg = R200_RemoveDeviceSettings

; File sections
;

[r200.Miniport]
r200.sys

[r200.Display]
r200umd.dll,,,0x00004000  ; COPYFLG_IN_USE_TRY_RENAME

; The following [R200.DispWow] section is x64-specific

[R200.DispWow]
r2umd32.dll,,,0x00004000  ; COPYFLG_IN_USE_TRY_RENAME
```
