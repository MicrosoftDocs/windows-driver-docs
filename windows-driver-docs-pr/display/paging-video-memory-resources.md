---
title: Paging Video Memory Resources
description: Paging Video Memory Resources
ms.assetid: e9734db6-3ad0-4c64-a9c6-15ba956b2dce
keywords:
- DMA buffers WDK display , paging video memory resources
- paging video memory resources WDK display
- video memory resource paging WDK display
- paging buffers WDK display
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Paging Video Memory Resources


## <span id="ddk_paging_video_memory_resources_gg"></span><span id="DDK_PAGING_VIDEO_MEMORY_RESOURCES_GG"></span>


Unlike the Microsoft [Windows 2000 Display Driver Model](windows-2000-display-driver-model-design-guide.md), the Windows Vista display driver model allows more video memory resources to be created than the total amount of physical video memory available, which are then paged in and out of video memory as necessary. In other words, not all video memory resources are in video memory simultaneously.

The GPU can have multiple DMA buffers in its pipeline. The video memory resources that are referenced by these active DMA buffers must be in video memory. Other idle video memory resources can be paged out to system memory.

Before the GPU scheduler can call the display miniport driver's [**DxgkDdiSubmitCommand**](https://msdn.microsoft.com/library/windows/hardware/ff560790) function to submit a DMA buffer to the GPU, the scheduler must ensure that all video memory resources used by the DMA buffer are actually in the video memory. If some resources are not in video memory, they must be paged in from system memory. The GPU scheduler must call upon the video memory manager to find space in video memory to transfer necessary video memory resource data from system memory to video memory. When video memory demand is high, the GPU scheduler must call upon the video memory manager to transfer idle video memory resource data to system memory to make room for the required video memory resource data. The special purpose DMA buffers that contain the commands for transferring data between video and system memory are known as paging buffers. The video memory manager calls the display miniport driver's [**DxgkDdiBuildPagingBuffer**](https://msdn.microsoft.com/library/windows/hardware/ff559587) function to create paging buffers to which the driver writes hardware-specific data transfer commands.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Paging%20Video%20Memory%20Resources%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




