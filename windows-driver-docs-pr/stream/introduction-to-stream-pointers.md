---
title: Introduction to Stream Pointers
author: windows-driver-content
description: Introduction to Stream Pointers
ms.assetid: 2682b145-5148-4301-b382-9811bb5e8fa6
keywords:
- stream pointers WDK AVStream , about stream pointers
- advancing stream pointers WDK AVStream
- stream pointers WDK AVStream , advancing
- frame reference counts WDK AVStream
- reference counts WDK stream pointers
- counting references WDK stream pointers
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Introduction to Stream Pointers


## <a href="" id="ddk-introduction-to-stream-pointers-ksg"></a>


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

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstream\stream%5D:%20Introduction%20to%20Stream%20Pointers%20%20RELEASE:%20%288/23/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


