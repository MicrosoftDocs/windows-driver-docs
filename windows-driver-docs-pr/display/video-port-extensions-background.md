---
title: Video Port Extensions Background
description: Video Port Extensions Background
ms.assetid: 77bed8d3-4fe5-4159-88e9-d6565aea9117
keywords:
- DirectX VPE support WDK DirectDraw , about video port extensions
- drawing VPEs WDK DirectDraw , about video port extensions
- DirectDraw VPEs WDK Windows 2000 display , about video port extensions
- video port extensions WDK DirectDraw , about video port extensions
- VPEs WDK DirectDraw , about video port extensions
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Video Port Extensions Background


## <span id="ddk_video_port_extensions_background_gg"></span><span id="DDK_VIDEO_PORT_EXTENSIONS_BACKGROUND_GG"></span>


The video port extensions (VPE) technology is a DirectDraw extension that supports direct hardware connections from a video decoder and autoflipping in the graphics frame buffer.

When video data is placed in the frame buffer, a video overlay can be used to display it. The video overlay in the graphics system tells the digital-to-analog converter (DAC) to show data in regions it would not ordinarily show. The use of overlays is efficient because blitting is not required to make the data visible, and because the video data can be viewed in a higher color depth than the visible frame buffer.

The hardware video port is a video stream delivery option that can be used instead of the PCI or AGP bus. For applications that are expected to run concurrently with other applications that require PCI bandwidth, it is advantageous to use the hardware video port to ensure low-latency video transmission between the decoder and the VGA graphics controller. This route is not as flexible as a PCI bus solution, because it ties the decoder to a particular graphics chipset, but it yields an opportunity to bypass the PCI bus if necessary.

The kernel-mode video transport capabilities, described in the [Kernel-Mode Video Transport](kernel-mode-video-transport.md) section, also provide support for VPE to ensure enhanced video playback quality and enhanced video capture support. The driver must support kernel-mode video transport in order to support VPE under Windows 2000 and later.

VPE supports only hardware-based data connections. Kernel-mode video transport supports direct access for data transfer.

VPE is not a WDM technology. Under Windows 2000 and later, WDM is used for other peripherals, but not for the display driver.

Because VPE support is part of the latest version of DirectX, an application can take advantage of these capabilities with the assurance that the solution works on any graphics card that supports VPE under Windows 2000 and later.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Video%20Port%20Extensions%20Background%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




