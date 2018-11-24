---
title: Windows 2000 Video Miniport Driver Responsibilities
description: Windows 2000 Video Miniport Driver Responsibilities
ms.assetid: 55301260-af1b-4ef7-8f33-e0acbeb22039
keywords:
- display driver model WDK Windows 2000 , responsibilities
- Windows 2000 display driver model WDK , responsibilities
- video miniport drivers WDK Windows 2000 , responsibilities
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Windows 2000 Video Miniport Driver Responsibilities


## <span id="ddk_video_miniport_driver_responsibilities_gg"></span><span id="DDK_VIDEO_MINIPORT_DRIVER_RESPONSIBILITIES_GG"></span>


The kernel-mode *video miniport driver* (.sys file) generally handles operations that must interact with other NT kernel components. For example, operations such as hardware initialization and memory mapping require action by the NT I/O subsystem. Video miniport driver responsibilities include resource management, such as hardware configuration, and physical device memory mapping. The video miniport driver must be specific to the video hardware.

The display driver uses the video miniport driver for operations that are not frequently requested; for example, to manage resources, perform physical device memory mapping, ensure that register outputs occur in close proximity, or respond to interrupts.

**Note**   The video miniport driver must manage all resources (for example, memory resources) shared between the video miniport driver and the display driver. The system does not guarantee that resources acquired in the display driver will always be accessible to the video miniport driver.

 

The video miniport driver also handles:

-   Mode set interaction with the graphics card.

-   Multiple hardware types, minimizing hardware-type dependency in the display driver.

-   Mapping the video register into the display driver's address space. I/O ports are directly addressable.

The video miniport driver is discussed in detail in [Video Miniport Drivers in the Windows 2000 Display Driver Model](video-miniport-drivers-in-the-windows-2000-display-driver-model.md).

 

 





