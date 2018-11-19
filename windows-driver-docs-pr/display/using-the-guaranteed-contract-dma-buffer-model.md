---
title: Using the Guaranteed Contract DMA Buffer Model
description: Using the Guaranteed Contract DMA Buffer Model
ms.assetid: fee6f7eb-157b-466d-b482-110a48045283
keywords:
- DMA buffers WDK display , guaranteed contract mode
- guaranteed contract DMA buffers WDK display
- patch-location lists WDK display
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Using the Guaranteed Contract DMA Buffer Model


The display driver model for Windows Vista guarantees the size of DMA buffers and patch-location lists for a rendering device.

In guaranteed contract mode, the user-mode display driver is aware of the exact size of the DMA buffer and patch-location list that is available for translation when the user-mode display driver fills command buffers and calls [**pfnRenderCb**](https://msdn.microsoft.com/library/windows/hardware/ff568923) to submit them to the display miniport driver. After each call to **pfnRenderCb**, the user-mode display driver receives the size of the DMA buffer and patch-location list that is available for the following translation (that is, the following call to **pfnRenderCb**).

The video memory manager guarantees not to trim the DMA buffers and patch-location lists for that device until the next translation is complete. The display miniport driver must be able to translate one command buffer into exactly one DMA buffer and one patch-location list. If this translation is not possible, the user-mode command buffer is, by definition, invalid. The display miniport driver cannot return status that indicates it is out of DMA buffer space and patch-location lists during the translation; doing so results in the video memory manager bug checking the system because the memory manager failed to meet the requirements of the guaranteed DMA contract.

 

 





