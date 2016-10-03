---
title: AVStream Allocators
author: windows-driver-content
description: AVStream Allocators
MS-HAID:
- 'avsover\_95bbe5c5-5e41-4e53-a6c6-bba905ee7318.xml'
- 'stream.avstream\_allocators'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: cda90faa-d4e3-4f17-aa5a-87dcde314bfd
keywords: ["AVStream allocators WDK", "allocators WDK AVStream", "frames WDK AVStream", "data buffers WDK AVStream", "buffers WDK AVStream", "allocating frames WDK AVStream", "freeing frames WDK AVStream"]
---

# AVStream Allocators


## <a href="" id="ddk-avstream-allocators-ksg"></a>


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

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstream\stream%5D:%20AVStream%20Allocators%20%20RELEASE:%20%288/23/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


