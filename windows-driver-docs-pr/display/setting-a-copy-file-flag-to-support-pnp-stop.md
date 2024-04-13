---
title: Setting a Copy-File Flag to Support PnP Stop
description: Setting a Copy-File Flag to Support PnP Stop
keywords:
- INF files WDK display , copy-file flags
- copy-file flags WDK display
- PnP stop WDK display
- Plug and Play stop WDK display
ms.date: 04/20/2017
---

# Setting a Copy-File Flag to Support PnP Stop


A new copy-file flag is required for display drivers that are written to the Windows Display Driver Model (WDDM) in order to properly support Plug and Play (PnP) stop (that is, driver upgrades that don't require a system restart).

**Note**   This flag is required only for user-mode display driver binaries and not for display miniport drivers.

 

The following example shows the new copy-file flag that is added to just the copy-file section for user-mode display drivers and not display miniport drivers:

```cpp
;
; File sections
;

[r200.Miniport]
r200.sys

[r200.Display]
r200umd.dll,,,0x00004000  ; COPYFLG_IN_USE_TRY_RENAME
r200umd2.dll,,,0x00004000 ; COPYFLG_IN_USE_TRY_RENAME
```

For more information about the **CopyFiles** directive and file sections that are associated with **CopyFiles**, see [**INF CopyFiles Directive**](../install/inf-copyfiles-directive.md).

 

