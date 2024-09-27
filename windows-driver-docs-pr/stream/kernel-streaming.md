---
title: Kernel Streaming
description: Kernel streaming
keywords:
- Kernel Streaming Model WDK , kernel streaming
- kernel streaming WDK
- kernel streaming WDK , about kernel streaming
- KS WDK
- KS WDK , about kernel streaming
- minidrivers WDK kernel streaming
ms.date: 09/24/2024
---

# Kernel streaming

Kernel streaming (KS) refers to the Microsoft-provided services that support kernel-mode processing of streamed data.

Microsoft provides three multimedia class driver models: port class, stream class, and AVStream. The vendor writes a minidriver that runs under one of these three class driver models.

These class drivers are implemented as export drivers (kernel-mode DLLs) in the system files *portcls.sys*, *stream.sys*, and *ks.sys* (also referred to as AVStream).

Microsoft also provides the [USB Video Class](usb-video-class-driver.md) driver.

This section contains legacy documentation on the following topics relevant to the original *ks.sys* class driver:

[KS minidriver architecture](ks-minidriver-architecture.md)

[KS properties, events, and methods](ks-properties--events--and-methods.md)

[KS clocks](ks-clocks.md)

[KS allocators](ks-allocators.md)

For more information about *portcls.sys*, see [Audio drivers](../audio/index.md).

To learn about the *stream.sys* driver, refer to [Streaming minidrivers](/windows-hardware/drivers/ddi/_stream/index).

To read about AVStream, see the [AVStream overview](avstream-overview.md).

[DVD decoder minidrivers](/windows-hardware/drivers/ddi/_stream/index) are clients of *stream.sys*.

[Video capture minidrivers](video-capture-devices.md) can be clients of either *stream.sys* or *ks.sys*.

[Broadcast Driver Architecture minidrivers](broadcast-driver-architecture-minidrivers.md) run under AVStream.
