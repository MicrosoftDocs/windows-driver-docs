---
title: Introduction to Stream Pointers
description: Introduction to Stream Pointers
ms.assetid: 2682b145-5148-4301-b382-9811bb5e8fa6
keywords:
- stream pointers WDK AVStream , about stream pointers
- advancing stream pointers WDK AVStream
- stream pointers WDK AVStream , advancing
- frame reference counts WDK AVStream
- reference counts WDK stream pointers
- counting references WDK stream pointers
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Introduction to Stream Pointers





In the older stream class model, the minidriver is responsible for maintaining its own data stream request block (SRB) queues. AVStream provides this functionality through stream pointer abstraction. A stream pointer is a reference to a specific AVStream data frame.

Minidrivers that use [pin-centric processing](pin-centric-processing.md) (most hardware drivers), use stream pointers to manage pin queues. Each pin has an independent queue of data buffers. When a data packet arrives at the pin (either a read or write request), AVStream adds the packet to the queue and might call the pin's process dispatch.

Minidrivers that use filter-centric processing should not use stream pointers directly. See [filter-centric processing](filter-centric-processing.md) for more information.

By default, each queue has a leading edge stream pointer. Optionally, it can have a trailing edge stream pointer if the trailing edge flag is specified. The minidriver can create new stream pointers by calling [**KsStreamPointerClone**](https://msdn.microsoft.com/library/windows/hardware/ff567129).

You can move a stream pointer in one direction only: to a newer frame. This is called advancing the stream pointer.

### Advancing a Stream Pointer

When you advance a stream pointer, you move it to a newer frame, or advance it some number of bytes within its current frame. For instance, the minidriver can advance a stream pointer from the first frame arrival to the second frame arrival.

To advance a stream pointer, a pin-centric filter can either call [**KsStreamPointerAdvance**](https://msdn.microsoft.com/library/windows/hardware/ff567125) or [**KsStreamPointerUnlock**](https://msdn.microsoft.com/library/windows/hardware/ff567137) with the *Eject* parameter set to **TRUE**.

### Frame Reference Counts

Frames with stream pointers pointing to them are reference counted, as are frames that are in the window between the leading and trailing edges.

When a minidriver is finished with a stream pointer, it can optionally call [**KsStreamPointerSetStatusCode**](https://msdn.microsoft.com/library/windows/hardware/ff567136) to specify an error code with which to complete the given I/O request packet (IRP). The minidriver must then call [**KsStreamPointerDelete**](https://msdn.microsoft.com/library/windows/hardware/ff567130). AVStream then decrements the reference count on the frame that the deleted stream pointer previously referenced. The leading-edge and trailing-edge stream pointers cannot be deleted.

 

 




