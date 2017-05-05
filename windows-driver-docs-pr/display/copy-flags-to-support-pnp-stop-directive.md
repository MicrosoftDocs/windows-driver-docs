---
title: Copy flags to support PnP stop directive
description: The Plug and Play (PnP) stop directive file section flag is required for the Windows Display Driver Model (WDDM) to support driver upgrades that don't require a reboot.
ms.assetid: 0D78350C-52D9-49D5-817D-2672F4A1D41A
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Copy%20flags%20to%20support%20PnP%20stop%20directive%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




