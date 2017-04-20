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
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Video Port Extensions to DirectX


## <span id="ddk_video_port_extensions_to_directx_gg"></span><span id="DDK_VIDEO_PORT_EXTENSIONS_TO_DIRECTX_GG"></span>


Driver developers for devices with a hardware video port should implement the video port extensions (VPE) to Microsoft DirectX. The hardware video port on a VGA graphics controller provides a fast mechanism for getting data to the frame buffer. The hardware video port is a dedicated connection between video devices, typically between a hardware Moving Pictures Experts Group (MPEG) device or National Television Standards Committee (NTSC) decoder and the video card. This dedicated connection carries horizontal sync (H-sync) and vertical sync (V-sync) information with the video data. The hardware video port and overlay can use this sync information to flip automatically between multiple buffers, writing to one surface while the overlay displays another. This allows tear-free video without burdening the application.

VPE allows the client -- typically Microsoft DirectShow -- to negotiate the connection between the MPEG or NTSC decoder and the hardware video port. VPE also allows the client to control effects in the video stream, including cropping and scaling. A VPE implementation should do only what is requested of it by the client; for example, it should crop only when the client requests cropping.

Microsoft DirectDraw VPE objects monitor the incoming signal and pass image data to the frame buffer, using parameters set though their interface methods to modify the image, perform flipping, or carry out other services. VPE objects do not control the video decoder or the video source.

The VPEs are not associated with the Microsoft Windows 2000 and later video port system module, *videoprt.sys*.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Video%20Port%20Extensions%20to%20DirectX%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




