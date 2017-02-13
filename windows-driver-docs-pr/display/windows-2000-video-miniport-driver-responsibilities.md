---
title: Windows 2000 Video Miniport Driver Responsibilities
description: Windows 2000 Video Miniport Driver Responsibilities
ms.assetid: 55301260-af1b-4ef7-8f33-e0acbeb22039
keywords: ["display driver model WDK Windows 2000 , responsibilities", "Windows 2000 display driver model WDK , responsibilities", "video miniport drivers WDK Windows 2000 , responsibilities"]
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Windows%202000%20Video%20Miniport%20Driver%20Responsibilities%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




