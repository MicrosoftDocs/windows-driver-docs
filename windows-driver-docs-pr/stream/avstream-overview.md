---
title: AVStream Overview
author: windows-driver-content
description: AVStream Overview
ms.assetid: 305039fe-0a00-4f3e-ae1a-61c50a2f2fb3
keywords:
- AVStream WDK , about AVStream minidrivers
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# AVStream Overview


## <a href="" id="ddk-avstream-overview-ksg"></a>


AVStream is a Microsoft-provided multimedia class driver that supports video-only streaming and integrated audio/video streaming. Microsoft provides AVStream as part of the operating system, in the export driver *Ks.sys*. Hardware vendors write minidrivers that run under *Ks.sys*.

The preferred class driver for audio drivers is the Microsoft-provided audio [port class](https://msdn.microsoft.com/library/windows/hardware/ff536829) driver. Audio vendors should write minidrivers that run under *Portcls.sys*.

Microsoft supports the [stream class](https://msdn.microsoft.com/library/windows/hardware/ff568275) driver only for existing minidrivers.

AVStream drivers build on Microsoft Windows XP, Microsoft Windows Server 2003, or any platform Windows 98 Gold or later version that has DirectX 8.0 or later version installed.

If you build on an operating system earlier than Windows XP, make sure that you use the latest available DirectX Driver Development Kit (DDK). DirectX 9.0 contains updates for AVStream, kernel streaming components, and stream class.

AVStream offers significant advantages to the vendor by:

-   Requiring minidriver writers to produce less code.

-   Providing a unified kernel streaming class model for both audio and video minidrivers.

-   Providing support for vendors to write user-mode plug-ins. These are COM interfaces that provide methods to access property values. You can provide plug-ins without altering existing minidriver binaries. For more information, see [Kernel Streaming Proxy Plug-ins](kernel-streaming-proxy-plug-ins-design-guide.md).

In the AVStream driver model, vendors provide a minidriver that interacts with a Microsoft-provided class driver, as shown in the following diagram:

![diagram illustrating the relationship between the avstream and ks services](images/avstream.png)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstream\stream%5D:%20AVStream%20Overview%20%20RELEASE:%20%288/23/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


