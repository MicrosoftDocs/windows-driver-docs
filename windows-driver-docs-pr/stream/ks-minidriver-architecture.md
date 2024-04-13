---
title: KS Minidriver Architecture
description: KS minidriver architecture
keywords:
- kernel streaming WDK , architecture
- KS WDK , architecture
- filter graphs WDK kernel streaming
ms.date: 06/18/2020
---

# KS minidriver architecture

Kernel streaming services support kernel-mode processing of streamed data. In this model, streaming data flows through a series of nodes that are grouped into blocks called filters. Each filter encapsulates some processing task to be performed upon the data. A [KS filter](ks-filters.md) is implemented as a kernel-mode [**DRIVER\_OBJECT**](/windows-hardware/drivers/ddi/wdm/ns-wdm-_driver_object).

A KS filter appears through the proxy as a DirectShow filter in user mode. As such, the graph builder and user-mode applications can interact with KS filters. In an active graph, the kernel-mode components still communicate directly, eliminating resource-consuming transitions between user mode and kernel mode.

Data flows into and out of filters at connection points called [pins](ks-pins.md). A pin instance renders or captures a data stream, such as digital audio.

A filter graph is a group of connected filters. A filter graph links multiple processing tasks to be performed on a stream. You can test various [filter graph configurations](filter-graph-examples.md) by using the GraphEdit tool in the Microsoft Windows Driver Kit (WDK). For more information about, see the [Filter Graph Editor tool](/windows/win32/directshow/simulating-graph-building-with-graphedit) website.

Drivers that support [on-board clocks](ks-clocks.md) expose the clock as a file object. A minidriver can [query the clock time](./kspropsetid-clock.md), or alternatively [**request to be notified**](./kseventsetid-clock.md) when the clock reaches a certain time.

A minidriver that supports a custom memory management interface exposes this interface as a file object known as an [allocator](ks-allocators.md). For example, a Device Manager that handles on-board memory might expose such an interface. A minidriver can then use the relevant file object to allocate and deallocate memory.

This section contains additional information about the following topics:

[KS Filters](ks-filters.md)

[KS Pins](ks-pins.md)

[KS Data Formats and Data Ranges](ks-data-formats-and-data-ranges.md)

[KS Mediums](ks-mediums.md)

[KS Interfaces](ks-interfaces.md)

[Quality Management](quality-management.md)
