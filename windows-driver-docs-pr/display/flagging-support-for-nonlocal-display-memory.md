---
title: Flagging Support for Nonlocal Display Memory
description: Flagging Support for Nonlocal Display Memory
ms.assetid: 5e5187e8-ff93-48e0-997d-71d65d35757f
keywords: ["display memory WDK DirectDraw , compatibility", "nonlocal display memory WDK DirectDraw , compatibility", "AGP WDK DirectDraw , compatibility", "drawing AGP support WDK DirectDraw , compatibility", "DirectDraw AGP support WDK Windows 2000 display , compatibility", "memory WDK DirectDraw AGP , compatibility", "compatibility WDK DirectDraw"]
---

# Flagging Support for Nonlocal Display Memory


## <span id="ddk_flagging_support_for_nonlocal_display_memory_gg"></span><span id="DDK_FLAGGING_SUPPORT_FOR_NONLOCAL_DISPLAY_MEMORY_GG"></span>


A driver must inform DirectDraw (and DirectDraw applications) that it is AGP-compatible. This is accomplished by specifying the capability bit DDCAPS2\_NONLOCALVIDMEM in the **dwCaps2** member of the [**DDCORECAPS**](https://msdn.microsoft.com/library/windows/hardware/ff549248) structure, which is part of the [**DD\_HALINFO**](https://msdn.microsoft.com/library/windows/hardware/ff551627) structure passed to DirectDraw.

If running on an operating system that does not support AGP services, DirectDraw turns off the DDCAPS2\_NONLOCALVIDMEM capability bit and all associated nonlocal heaps.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Flagging%20Support%20for%20Nonlocal%20Display%20Memory%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




