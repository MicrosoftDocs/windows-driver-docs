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
ms.date: 04/20/2017
ms.localizationpriority: medium
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

 

 





