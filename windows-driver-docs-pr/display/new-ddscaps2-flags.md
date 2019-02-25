---
title: New DDSCAPS2 Flags
description: New DDSCAPS2 Flags
ms.assetid: a5171865-7339-422f-8470-154a0aadc496
keywords:
- DirectX 8.0 release notes WDK Windows 2000 display , presentation
- presentation WDK DirectX 8.0
- rendering results visible WDK DirectX 8.0
- visible results WDK DirectX 8.0
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# New DDSCAPS2 Flags


## <span id="ddk_new_ddscaps2_flags_gg"></span><span id="DDK_NEW_DDSCAPS2_FLAGS_GG"></span>


A new flag, DDSCAPS2\_DISCARDBACKBUFFER, has been introduced to indicate that preservation of the back buffer is not required. It is set on the primary surface and the back buffers if the application has set D3DSWAPEFFECT\_DISCARD on the **Present** API.

DX8 runtimes now set another new flag, DDSCAPS2\_NOTUSERLOCKABLE, on the primary and the back buffers if the flipping chain is not lockable, or on any render target that is not lockable. This allows drivers to do behind the scenes optimization. Note that it is still possible to lock the surfaces so the driver must handle these cases, but such locks are infrequent and are not expected to be fast.

The driver can also determine whether the depth/stencil buffer is lockable by the presence of the DDSCAPS2\_NOTUSERLOCKABLE flag.

 

 





