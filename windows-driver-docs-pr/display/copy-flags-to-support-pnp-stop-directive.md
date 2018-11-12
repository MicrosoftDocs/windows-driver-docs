---
title: Copy flags to support PnP stop directive
description: The Plug and Play (PnP) stop directive file section flag is required for the Windows Display Driver Model (WDDM) to support driver upgrades that don't require a reboot.
ms.assetid: 0D78350C-52D9-49D5-817D-2672F4A1D41A
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Copy flags to support PnP stop directive


The Plug and Play (PnP) stop directive file section flag is required for the Windows Display Driver Model (WDDM) to support driver upgrades that don't require a reboot.

**Note**  
This is required only for the user-mode driver binaries, not for the kernel-mode driver entry.

 

For example:

``` syntax
;
; File sections
;

[r200.Miniport]
r200.sys

[r200.Display]
r200umd.dll,,,0x00004000             ; COPYFLG_IN_USE_TRY_RENAME
r200umd2.dll,,,0x00004000           ; COPYFLG_IN_USE_TRY_RENAME
```

 

 





