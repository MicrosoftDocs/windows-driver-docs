---
title: AVStream Minidrivers Design Guide
author: windows-driver-content
description: AVStream Minidrivers Design Guide
ms.assetid: ad717dca-55fe-428a-8d5c-239324251eda
keywords:
- streaming media WDK , AVStream minidrivers
- media streaming WDK , AVStream minidrivers
- AVStream WDK , writing minidrivers
- minidrivers WDK AVStream
- multimedia class drivers WDK AVStream
- video-only streaming WDK AVStream
- integrated audio/video streaming WDK AVStream
- audio/video streaming WDK AVStream
- audio WDK AVStream
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# AVStream Minidrivers Design Guide


## <a href="" id="ddk-avstream-minidrivers-ksg"></a>


This Design Guide describes how to design AVStream minidrivers that control streaming media devices. These topics help guide you through the process of designing high-performance drivers for a variety of device and encoding scenarios:

[New AVStream Interfaces for Windows 8.1](new-avstream-interfaces-for-windows-8-1.md)

[New AVStream Interfaces for Windows 8](new-windows-8-ddis.md)

[Writing an AVStream Minidriver](writing-an-avstream-minidriver.md)

[Broadcast Driver Architecture Drivers](https://msdn.microsoft.com/library/windows/hardware/ff556573)

[Encoder Devices](encoder-devices.md)

[AV/C Client Drivers](https://msdn.microsoft.com/library/windows/hardware/ff556364)

[USB Video Class Driver](usb-video-class-driver.md)

[AVStream Samples](avstream-samples.md)

[Video Capture Devices](video-capture-devices.md)

[Using Hardware Codec Support in AVStream](hardware-codec-support-in-avstream.md)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstream\stream%5D:%20AVStream%20Minidrivers%20Design%20Guide%20%20RELEASE:%20%288/23/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


