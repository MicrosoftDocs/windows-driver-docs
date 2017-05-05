---
title: VPE Functions in DirectDraw API and Driver
description: VPE Functions in DirectDraw API and Driver
ms.assetid: 7e899f20-4082-4438-b7f2-198d1a4ad344
keywords:
- DirectX VPE support WDK DirectDraw , functions
- drawing VPEs WDK DirectDraw , functions
- DirectDraw VPEs WDK Windows 2000 display , functions
- video port extensions WDK DirectDraw , functions
- VPEs WDK DirectDraw , functions
- functions WDK video port extensions
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# VPE Functions in DirectDraw API and Driver


## <span id="ddk_vpe_functions_in_directdraw_api_and_driver_gg"></span><span id="DDK_VPE_FUNCTIONS_IN_DIRECTDRAW_API_AND_DRIVER_GG"></span>


The video port extensions in the latest DirectX release are low-level extensions to the DirectDraw API. VPE allows the client -- usually DirectShow -- to negotiate the connection between the MPEG or NTSC decoder and the hardware video port. VPE also allows the client to control effects in the video stream, including cropping and scaling.

VPE is not a high-level API designed for broad use by applications. Applications should use DirectShow, which provides free support for VPE. The following figure shows a simple view of the VPE and kernel-mode architecture. For more information, see [Kernel-Mode Video Transport](kernel-mode-video-transport.md).

![diagram illustrating video port extensions and kernel-mode architecture](images/ddfig10.png)

The preceding figure shows VPE in relation to other components of DirectDraw architecture. DirectShow uses VPE to negotiate the connection, which provides information about how data and V-sync and H-sync information are transferred. This information can be an APIC connection (ITU 656), external data lines with extra pins, or proprietary data streams such as those implemented by Brooktree and Philips.

In the negotiation for the connection, the VGA hardware indicates what connections can be supported, and the MPEG or NTSC decoder indicates its preferences. DirectShow negotiates the best connection between the two. The connection is described as a globally unique identifier (GUID), with flags to describe other parameters, such as double clocking and video active.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20VPE%20Functions%20in%20DirectDraw%20API%20and%20Driver%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




