---
title: Kernel Streaming
author: windows-driver-content
description: Kernel Streaming
ms.assetid: dcd28218-b3bf-4e5d-b1a7-6910103afb96
keywords:
- Windows 2000 Kernel Streaming Model WDK , kernel streaming
- Streaming Model WDK Windows 2000 Kernel , kernel streaming
- Kernel Streaming Model WDK , kernel streaming
- kernel streaming WDK
- kernel streaming WDK , about kernel streaming
- KS WDK
- KS WDK , about kernel streaming
- minidrivers WDK kernel streaming
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Kernel Streaming


## <a href="" id="ddk-kernel-streaming-ksg"></a>


Kernel streaming (KS) refers to the Microsoft-provided services that support kernel-mode processing of streamed data.

Microsoft provides three multimedia class driver models: port class, stream class, and AVStream. The vendor writes a minidriver that runs under one of these three class driver models.

These class drivers are implemented as export drivers (kernel-mode DLLs) in the system files *portcls.sys*, *stream.sys*, and *ks.sys*. In Windows XP and later, *ks.sys* is referred to as AVStream.

In Windows XP SP2 and later, Microsoft provides the [USB Video Class](usb-video-class-driver.md) driver.

This section contains legacy documentation on the following topics relevant to the original (pre-XP) *ks.sys* class driver:

[KS Minidriver Architecture](ks-minidriver-architecture.md)

[KS Properties, Events, and Methods](ks-properties--events--and-methods.md)

[KS Clocks](ks-clocks.md)

[KS Allocators](ks-allocators.md)

For more information about *portcls.sys*, see [Audio Drivers](https://msdn.microsoft.com/library/windows/hardware/ff536191).

To learn about the *stream.sys* driver, refer to [Streaming Minidrivers](https://msdn.microsoft.com/library/windows/hardware/ff568275).

To read about AVStream, see the [AVStream Overview](avstream-overview.md).

[DVD Decoder Minidrivers](https://msdn.microsoft.com/library/windows/hardware/ff558742) are clients of *stream.sys*.

[Video capture minidrivers](video-capture-devices.md) can be clients of either *stream.sys* or *ks.sys*.

[Broadcast Driver Architecture Minidrivers](broadcast-driver-architecture-minidrivers.md) run under AVStream.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstream\stream%5D:%20Kernel%20Streaming%20%20RELEASE:%20%288/23/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


