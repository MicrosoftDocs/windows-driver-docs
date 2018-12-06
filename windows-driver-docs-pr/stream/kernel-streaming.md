---
title: Kernel Streaming
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
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Kernel Streaming





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

 

 




