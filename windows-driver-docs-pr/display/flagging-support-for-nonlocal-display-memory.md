---
title: Flagging Support for Nonlocal Display Memory
description: Flagging Support for Nonlocal Display Memory
keywords:
- display memory WDK DirectDraw , compatibility
- nonlocal display memory WDK DirectDraw , compatibility
- AGP WDK DirectDraw , compatibility
- drawing AGP support WDK DirectDraw , compatibility
- DirectDraw AGP support WDK Windows 2000 display , compatibility
- memory WDK DirectDraw AGP , compatibility
- compatibility WDK DirectDraw
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Flagging Support for Nonlocal Display Memory


## <span id="ddk_flagging_support_for_nonlocal_display_memory_gg"></span><span id="DDK_FLAGGING_SUPPORT_FOR_NONLOCAL_DISPLAY_MEMORY_GG"></span>


A driver must inform DirectDraw (and DirectDraw applications) that it is AGP-compatible. This is accomplished by specifying the capability bit DDCAPS2\_NONLOCALVIDMEM in the **dwCaps2** member of the [**DDCORECAPS**](/windows/win32/api/ddrawi/ns-ddrawi-ddcorecaps) structure, which is part of the [**DD\_HALINFO**](/windows/win32/api/ddrawint/ns-ddrawint-dd_halinfo) structure passed to DirectDraw.

If running on an operating system that does not support AGP services, DirectDraw turns off the DDCAPS2\_NONLOCALVIDMEM capability bit and all associated nonlocal heaps.

 

