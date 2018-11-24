---
title: AV/C kernel interface and streaming proxy plug-ins
description: Provides information about AV/C kernel-streaming interface and kernel-streaming proxy plug-ins
ms.assetid: 0831d917-5afc-4c0c-832a-c2b2669b8c22
keywords:
- kernel-streaming interface WDK AV/C
- kernel-streaming proxy plug-ins WDK AV/C
- AV/C WDK , kernel-streaming proxy plug-ins
- AV/C WDK , kernel-streaming interface
- proxy plug-ins WDK AV/C
- Kernel Streaming Proxy WDK AVStream
- KS proxy WDK AVStream
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# AV/C kernel-streaming interface and kernel-streaming proxy plug-ins



Vendors should write peer and/or virtual subunit drivers as WDM drivers that use either the Stream class interface (Kernel Streaming 1.0, which is implemented in the file *Stream.sys*) or the AVStream interface (Kernel Streaming 2.0, which is implemented in the file *Ks.sys*). AVStream is the preferred interface because the stream class interface is obsolete and Microsoft has discontinued any further development on it.

Subunit drivers that use either interface can coexist, even within the same AV/C unit. For example, if a subunit driver uses AVStream, the subunit driver lays out static structures that correspond to the pin and filter descriptors of the subunit. The subunit driver then registers with AVStream by calling the [**KsInitializeDriver**](https://msdn.microsoft.com/library/windows/hardware/ff562683) AVStream function. For more information about the concepts used in both interfaces, see [Kernel Streaming](kernel-streaming.md). For more information about AVStream, see [AVStream Overview](avstream-overview.md). For more information about the Stream class, see [Streaming Minidrivers](https://msdn.microsoft.com/library/windows/hardware/ff568275).

Either kernel-streaming interface provides the same standard mechanism that applications use to interact with and control a subunit driver. The recommended approach to control AV/C subunits at the application level is through Microsoft DirectShow filters and filter graphs. The kernel streaming (KS) proxy mechanism of DirectShow provides a generic filter (*ksproxy.ax*) that enables a standard way to represent the properties of the subunit as well as a standard way to represent events that the subunit might trigger. You implement the code required to support the relevant KS properties and events in your AV/C subunit driver. For more information about representing subunit properties, see [Kernel Streaming Property Sets](https://msdn.microsoft.com/library/windows/hardware/ff554246). For more information about representing subunit events, see [Kernel Streaming Event Sets](https://msdn.microsoft.com/library/windows/hardware/ff560847).

The KS proxy filter can be extended with proxy plug-ins, provided by Microsoft or by a vendor. Extending the KS proxy filter allows COM interfaces to hide the low-level details of the KS property and event sets. You associate the plug-in with your subunit driver in your device's INF file.

A general way to directly access the property and event sets remains available. The **IAMExtTransport** interface (used for tape subunits) is an example of an interface that is implemented in a proxy plug-in. The plug-in can also include property pages that provide a user interface to control the device. These property pages are generally used for testing purposes rather than for end-user device interaction. The GraphEdit or AMCap utilities can be used to test the plug-in's KS properties. These utilities are included in both the WDK and Windows SDK.

 





