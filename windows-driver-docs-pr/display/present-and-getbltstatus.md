---
title: Present and GetBltStatus
description: Present and GetBltStatus
keywords:
- DirectX 8.0 release notes WDK Windows 2000 display , presentation
- presentation WDK DirectX 8.0
- rendering results visible WDK DirectX 8.0
- visible results WDK DirectX 8.0
- DdGetBltStatus
ms.date: 04/20/2017
---

# Present and GetBltStatus


## <span id="ddk_present_and_getbltstatus_gg"></span><span id="DDK_PRESENT_AND_GETBLTSTATUS_GG"></span>


For DX8 the runtime no longer calls [*DdGetBltStatus*](/windows/win32/api/ddrawint/nc-ddrawint-pdd_surfcb_getbltstatus) on blts involving system memory surfaces. This was always the behavior on Windows 2000. The result is that asynchronous DMA to or from system memory surfaces is no longer possible. DX8 drivers should not page lock system memory surfaces by themselves, and system memory to video memory transfers should be synchronous.

 

