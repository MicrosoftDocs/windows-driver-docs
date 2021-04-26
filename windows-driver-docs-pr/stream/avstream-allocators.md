---
title: AVStream Allocators
description: AVStream Allocators
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





The AVStream class driver uses an *Allocator* to allocate data buffers in units called *frames*. A frame is a chunk of continuous memory, the size of which is vendor-specified through the **AllocatorFraming** member of [**KSPIN\_DESCRIPTOR\_EX**](/windows-hardware/drivers/ddi/ks/ns-ks-_kspin_descriptor_ex).

Minidrivers access these buffers through the [Stream Pointers](stream-pointers.md) API; call [**KsPinGetLeadingEdgeStreamPointer**](/windows-hardware/drivers/ddi/ks/nf-ks-kspingetleadingedgestreampointer) to acquire a pointer into the stream.

AVStream clients can obtain information about the framing requirements of a pin by using the read-only property [**KSPROPERTY\_CONNECTION\_ALLOCATORFRAMING\_EX**](./ksproperty-connection-allocatorframing-ex.md). This property returns a structure of type [**KSALLOCATOR\_FRAMING\_EX**](/windows-hardware/drivers/ddi/ks/ns-ks-ksallocator_framing_ex) that describe the framing requirements for the pin.

When data is no longer in use, AVStream uses the allocator to free the buffer.

AVStream provides a default allocator. The default allocator allocates pool memory based on the allocator requirements that the minidriver provides in the **AllocatorFraming** member of the [**KSPIN\_DESCRIPTOR\_EX**](/windows-hardware/drivers/ddi/ks/ns-ks-_kspin_descriptor_ex) structure.

A vendor with device-specific allocation requirements can write a minidriver that includes its own allocation routines. For example, you might provide an allocator if your driver allocates memory from a [common DMA buffer](../kernel/using-common-buffer-system-dma.md).

To provide an allocator, supply a [**KSALLOCATOR\_DISPATCH**](/windows-hardware/drivers/ddi/ks/ns-ks-_ksallocator_dispatch) structure that contains pointers to the following vendor-supplied callback routines:

-   [*AVStrMiniInitializeAllocator*](/windows-hardware/drivers/ddi/ks/nc-ks-pfnkspininitializeallocator)

-   [*AVStrMiniDeleteAllocator*](/windows-hardware/drivers/ddi/ks/nc-ks-pfnksdeleteallocator)

-   [*AVStrMiniAllocate*](/windows-hardware/drivers/ddi/ks/nc-ks-pfnksdefaultallocate)

-   [*AVStrMiniAllocatorFreeFrame*](/windows-hardware/drivers/ddi/ks/nc-ks-pfnksdefaultfree)

Provide a pointer to this allocator dispatch structure in the **Allocator** member of the [**KSPIN\_DISPATCH**](/windows-hardware/drivers/ddi/ks/ns-ks-_kspin_dispatch) structure describing the pin for which this allocator will instantiate frames.

Supply a pointer to this pin dispatch structure in the **Dispatch** member of the corresponding [**KSPIN\_DESCRIPTOR\_EX**](/windows-hardware/drivers/ddi/ks/ns-ks-_kspin_descriptor_ex) structure. To learn more about dispatch structures in AVStream, read [AVStream Dispatch Tables](avstream-dispatch-tables.md).

At run time, the graph manager (for example, the [Kernel Streaming Proxy](/windows-hardware/drivers/ddi/_stream/index) module) handles allocator selection. A vendor-supplied allocator is *not* guaranteed to be selected by the graph manager.

A kernel-mode allocator is only chosen if the connection is in kernel mode. In addition, your allocator could be rejected if there is a mismatch in allocator requirements and your allocator's capabilities. If your allocator is not selected, your [*AVStrMiniInitializeAllocator*](/windows-hardware/drivers/ddi/ks/nc-ks-pfnkspininitializeallocator) callback routine is never called.

Also see [AVStream DMA Services](avstream-dma-services.md) and [Stream Pointers](stream-pointers.md).

 

