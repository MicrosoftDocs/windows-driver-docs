---
title: Using the Guaranteed Contract DMA Buffer Model
description: Using the Guaranteed Contract DMA Buffer Model
ms.assetid: fee6f7eb-157b-466d-b482-110a48045283
keywords:
- DMA buffers WDK display , guaranteed contract mode
- guaranteed contract DMA buffers WDK display
- patch-location lists WDK display
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Using the Guaranteed Contract DMA Buffer Model


The display driver model for Windows Vista guarantees the size of DMA buffers and patch-location lists for a rendering device.

In guaranteed contract mode, the user-mode display driver is aware of the exact size of the DMA buffer and patch-location list that is available for translation when the user-mode display driver fills command buffers and calls [**pfnRenderCb**](https://msdn.microsoft.com/library/windows/hardware/ff568923) to submit them to the display miniport driver. After each call to **pfnRenderCb**, the user-mode display driver receives the size of the DMA buffer and patch-location list that is available for the following translation (that is, the following call to **pfnRenderCb**).

The video memory manager guarantees not to trim the DMA buffers and patch-location lists for that device until the next translation is complete. The display miniport driver must be able to translate one command buffer into exactly one DMA buffer and one patch-location list. If this translation is not possible, the user-mode command buffer is, by definition, invalid. The display miniport driver cannot return status that indicates it is out of DMA buffer space and patch-location lists during the translation; doing so results in the video memory manager bug checking the system because the memory manager failed to meet the requirements of the guaranteed DMA contract.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Using%20the%20Guaranteed%20Contract%20DMA%20Buffer%20Model%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




