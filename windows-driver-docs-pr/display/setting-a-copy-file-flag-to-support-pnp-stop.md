---
title: Setting a Copy-File Flag to Support PnP Stop
description: Setting a Copy-File Flag to Support PnP Stop
ms.assetid: 9f716ac0-c181-489f-8bc4-ccca8c141b06
keywords: ["INF files WDK display , copy-file flags", "copy-file flags WDK display", "PnP stop WDK display", "Plug and Play stop WDK display"]
---

# Setting a Copy-File Flag to Support PnP Stop


A new copy-file flag is required for display drivers that are written to the Windows Display Driver Model (WDDM) in order to properly support Plug and Play (PnP) stop (that is, driver upgrades that don't require a system restart).

**Note**   This flag is required only for user-mode display driver binaries and not for display miniport drivers.

 

The following example shows the new copy-file flag that is added to just the copy-file section for user-mode display drivers and not display miniport drivers:

```
;
; File sections
;

[r200.Miniport]
r200.sys

[r200.Display]
r200umd.dll,,,0x00004000  ; COPYFLG_IN_USE_TRY_RENAME
r200umd2.dll,,,0x00004000 ; COPYFLG_IN_USE_TRY_RENAME
```

For more information about the **CopyFiles** directive and file sections that are associated with **CopyFiles**, see [**INF CopyFiles Directive**](https://msdn.microsoft.com/library/windows/hardware/ff546346).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Setting%20a%20Copy-File%20Flag%20to%20Support%20PnP%20Stop%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




