---
title: KS Minidriver Architecture
author: windows-driver-content
description: KS Minidriver Architecture
ms.assetid: a9c17040-72a8-4290-831b-7fb46b00f532
keywords:
- kernel streaming WDK , architecture
- KS WDK , architecture
- filter graphs WDK kernel streaming
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# KS Minidriver Architecture


## <a href="" id="ddk-ks-minidriver-architecture-ksg"></a>


Kernel streaming services support kernel-mode processing of streamed data. In this model, streaming data flows through a series of nodes that are grouped into blocks called filters. Each filter encapsulates some processing task to be performed upon the data. A [KS filter](ks-filters.md) is implemented as a kernel-mode [**DRIVER\_OBJECT**](https://msdn.microsoft.com/library/windows/hardware/ff544174).

A KS filter appears through the proxy as a DirectShow filter in user mode. As such, the graph builder and user-mode applications can interact with KS filters. In an active graph, the kernel-mode components still communicate directly, eliminating resource-consuming transitions between user mode and kernel mode.

Data flows into and out of filters at connection points called [pins](ks-pins.md). A pin instance renders or captures a data stream, such as digital audio.

A filter graph is a group of connected filters. A filter graph links multiple processing tasks to be performed on a stream. You can test various [filter graph configurations](filter-graph-examples.md) by using the GraphEdit tool in the Microsoft Windows Driver Kit (WDK). (For more information about GraphEdit, see the [Filter Graph Editor tool](http://go.microsoft.com/fwlink/p/?linkid=9230) website.)

Drivers that support [on-board clocks](ks-clocks.md) expose the clock as a file object. A minidriver can [query the clock time](https://msdn.microsoft.com/library/windows/hardware/ff566564), or alternatively [**request to be notified**](https://msdn.microsoft.com/library/windows/hardware/ff561764) when the clock reaches a certain time.

A minidriver that supports a custom memory management interface exposes this interface as a file object known as an [allocator](ks-allocators.md). For example, a Device Manager that handles on-board memory might expose such an interface. A minidriver can then use the relevant file object to allocate and deallocate memory.

This section contains additional information about the following topics:

[KS Filters](ks-filters.md)

[KS Pins](ks-pins.md)

[KS Data Formats and Data Ranges](ks-data-formats-and-data-ranges.md)

[KS Mediums](ks-mediums.md)

[KS Interfaces](ks-interfaces.md)

[Quality Management](quality-management.md)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstream\stream%5D:%20KS%20Minidriver%20Architecture%20%20RELEASE:%20%288/23/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


