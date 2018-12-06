---
title: AVStream Allocators
description: AVStream Allocators
ms.assetid: cda90faa-d4e3-4f17-aa5a-87dcde314bfd
keywords:
- AVStream allocators WDK
- allocators WDK AVStream
- frames WDK AVStream
- data buffers WDK AVStream
- buffers WDK AVStream
- allocating frames WDK AVStream
- freeing frames WDK AVStream
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# AVStream Allocators





The AVStream class driver uses an *Allocator* to allocate data buffers in units called *frames*. A frame is a chunk of continuous memory, the size of which is vendor-specified through the **AllocatorFraming** member of [**KSPIN\_DESCRIPTOR\_EX**](https://msdn.microsoft.com/library/windows/hardware/ff563534).

Minidrivers access these buffers through the [Stream Pointers](stream-pointers.md) API; call [**KsPinGetLeadingEdgeStreamPointer**](https://msdn.microsoft.com/library/windows/hardware/ff563513) to acquire a pointer into the stream.

AVStream clients can obtain information about the framing requirements of a pin by using the read-only property [**KSPROPERTY\_CONNECTION\_ALLOCATORFRAMING\_EX**](https://msdn.microsoft.com/library/windows/hardware/ff565101). This property returns a structure of type [**KSALLOCATOR\_FRAMING\_EX**](https://msdn.microsoft.com/library/windows/hardware/ff560982) that describe the framing requirements for the pin.

When data is no longer in use, AVStream uses the allocator to free the buffer.

AVStream provides a default allocator. The default allocator allocates pool memory based on the allocator requirements that the minidriver provides in the **AllocatorFraming** member of the [**KSPIN\_DESCRIPTOR\_EX**](https://msdn.microsoft.com/library/windows/hardware/ff563534) structure.

A vendor with device-specific allocation requirements can write a minidriver that includes its own allocation routines. For example, you might provide an allocator if your driver allocates memory from a [common DMA buffer](https://msdn.microsoft.com/library/windows/hardware/ff565362).

To provide an allocator, supply a [**KSALLOCATOR\_DISPATCH**](https://msdn.microsoft.com/library/windows/hardware/ff560976) structure that contains pointers to the following vendor-supplied callback routines:

-   [*AVStrMiniInitializeAllocator*](https://msdn.microsoft.com/library/windows/hardware/ff556321)

-   [*AVStrMiniDeleteAllocator*](https://msdn.microsoft.com/library/windows/hardware/ff554273)

-   [*AVStrMiniAllocate*](https://msdn.microsoft.com/library/windows/hardware/ff554265)

-   [*AVStrMiniAllocatorFreeFrame*](https://msdn.microsoft.com/library/windows/hardware/ff554266)

Provide a pointer to this allocator dispatch structure in the **Allocator** member of the [**KSPIN\_DISPATCH**](https://msdn.microsoft.com/library/windows/hardware/ff563535) structure describing the pin for which this allocator will instantiate frames.

Supply a pointer to this pin dispatch structure in the **Dispatch** member of the corresponding [**KSPIN\_DESCRIPTOR\_EX**](https://msdn.microsoft.com/library/windows/hardware/ff563534) structure. To learn more about dispatch structures in AVStream, read [AVStream Dispatch Tables](avstream-dispatch-tables.md).

At run time, the graph manager (for example, the [Kernel Streaming Proxy](https://msdn.microsoft.com/library/windows/hardware/ff560877) module) handles allocator selection. A vendor-supplied allocator is *not* guaranteed to be selected by the graph manager.

A kernel-mode allocator is only chosen if the connection is in kernel mode. In addition, your allocator could be rejected if there is a mismatch in allocator requirements and your allocator's capabilities. If your allocator is not selected, your [*AVStrMiniInitializeAllocator*](https://msdn.microsoft.com/library/windows/hardware/ff556321) callback routine is never called.

Also see [AVStream DMA Services](avstream-dma-services.md) and [Stream Pointers](stream-pointers.md).

 

 




