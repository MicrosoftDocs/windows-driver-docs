---
title: Video Port Extensions to DirectX
description: Video Port Extensions to DirectX
ms.assetid: 42309279-e98a-4091-8f01-5d0d418e9ef2
keywords:
- DirectX VPE support WDK DirectDraw
- drawing VPEs WDK DirectDraw
- DirectDraw VPEs WDK Windows 2000 display
- video port extensions WDK DirectDraw
- VPEs WDK DirectDraw
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Video Port Extensions to DirectX


## <span id="ddk_video_port_extensions_to_directx_gg"></span><span id="DDK_VIDEO_PORT_EXTENSIONS_TO_DIRECTX_GG"></span>


Driver developers for devices with a hardware video port should implement the video port extensions (VPE) to Microsoft DirectX. The hardware video port on a VGA graphics controller provides a fast mechanism for getting data to the frame buffer. The hardware video port is a dedicated connection between video devices, typically between a hardware Moving Pictures Experts Group (MPEG) device or National Television Standards Committee (NTSC) decoder and the video card. This dedicated connection carries horizontal sync (H-sync) and vertical sync (V-sync) information with the video data. The hardware video port and overlay can use this sync information to flip automatically between multiple buffers, writing to one surface while the overlay displays another. This allows tear-free video without burdening the application.

VPE allows the client -- typically Microsoft DirectShow -- to negotiate the connection between the MPEG or NTSC decoder and the hardware video port. VPE also allows the client to control effects in the video stream, including cropping and scaling. A VPE implementation should do only what is requested of it by the client; for example, it should crop only when the client requests cropping.

Microsoft DirectDraw VPE objects monitor the incoming signal and pass image data to the frame buffer, using parameters set though their interface methods to modify the image, perform flipping, or carry out other services. VPE objects do not control the video decoder or the video source.

The VPEs are not associated with the Microsoft Windows 2000 and later video port system module, *videoprt.sys*.

 

 





