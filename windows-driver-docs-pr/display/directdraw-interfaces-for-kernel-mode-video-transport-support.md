---
title: DirectDraw Interfaces for Kernel-Mode Video Transport Support
description: DirectDraw Interfaces for Kernel-Mode Video Transport Support
ms.assetid: 8012f6b0-3b55-438f-8146-4f62e6bafad3
keywords:
- kernel-mode video transport WDK DirectDraw , interfaces
- DirectX VPE support WDK DirectDraw , kernel-mode video transport
- drawing VPEs WDK DirectDraw , kernel-mode video transport
- DirectDraw VPEs WDK Windows 2000 display , kernel-mode video transport
- video port extensions WDK DirectDraw , kernel-mode video transport
- VPEs WDK DirectDraw , kernel-mode video transport
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# DirectDraw Interfaces for Kernel-Mode Video Transport Support


## <span id="ddk_directdraw_interfaces_for_kernel_mode_video_transport_support_gg"></span><span id="DDK_DIRECTDRAW_INTERFACES_FOR_KERNEL_MODE_VIDEO_TRANSPORT_SUPPORT_GG"></span>


The kernel-mode video transport must keep track of surface information for each surface it uses, and for each VPE object. This information must be updated every time [*DdUpdateOverlay*](https://msdn.microsoft.com/library/windows/hardware/ff550369) or [*DdVideoPortUpdate*](https://msdn.microsoft.com/library/windows/hardware/ff550450) is called for the surface or hardware video port. Before DirectDraw sends this information to the kernel-mode video transport, it calls one of two driver functions: [*DdSyncSurfaceData*](https://msdn.microsoft.com/library/windows/hardware/ff550345) or [*DdSyncVideoPortData*](https://msdn.microsoft.com/library/windows/hardware/ff550350). These functions allow the driver to fill in or modify some of the structure information and to use four **dwDriverReserved***N* members of the [**DD\_SYNCSURFACEDATA**](https://msdn.microsoft.com/library/windows/hardware/ff551739) or three **dwDriverReserved***N* members of the [**DD\_SYNCVIDEOPORTDATA**](https://msdn.microsoft.com/library/windows/hardware/ff551740) structure for its own purposes. These driver functions are required for the kernel-mode video transport support to work correctly.

A good example of how a driver can use these **dwDriverReserved***N* members is to set a flag indicating which physical overlay an overlay surface is using if the hardware supports more than one physical overlay.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20DirectDraw%20Interfaces%20for%20Kernel-Mode%20Video%20Transport%20Support%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




