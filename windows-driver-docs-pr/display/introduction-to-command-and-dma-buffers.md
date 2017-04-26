---
title: Introduction to Command and DMA Buffers
description: Introduction to Command and DMA Buffers
ms.assetid: e9fa38a2-3243-4578-83c3-4559ec3480a7
keywords:
- command buffers WDK display , about command buffers
- DMA buffers WDK display , about DMA buffers
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Introduction to Command and DMA Buffers


## <span id="ddk_introduction_to_command_and_dma_buffers_gg"></span><span id="DDK_INTRODUCTION_TO_COMMAND_AND_DMA_BUFFERS_GG"></span>


Command and DMA buffers closely resemble each other. However, a command buffer is used by the user-mode display driver, and a DMA buffer is used by the display miniport driver.

A command buffer has the following characteristics:

-   It is never directly accessed by the GPU.

-   The hardware vendor controls the format.

-   It is allocated for the user-mode display driver from regular pageable memory in the private address space of the rendering application.

A DMA buffer has the following characteristics:

-   It is based on the validated content of a command buffer.

-   It is allocated by the display miniport driver from kernel pageable memory.

-   Before the GPU can read from a DMA buffer, the display miniport driver must page-lock the DMA buffer and map the DMA buffer through an aperture.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Introduction%20to%20Command%20and%20DMA%20Buffers%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




