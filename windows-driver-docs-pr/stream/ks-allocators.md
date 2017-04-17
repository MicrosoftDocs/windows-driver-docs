---
title: KS Allocators
author: windows-driver-content
description: KS Allocators
ms.assetid: 07812703-a66f-450a-b28e-4cf765267c4a
keywords: ["kernel streaming WDK , allocators", "KS WDK , allocators", "allocators WDK kernel streaming"]
---

# KS Allocators


## <a href="" id="ddk-ks-allocators-ksg"></a>


An *Allocator* is a KS object that instantiates data buffers called *frames* for I/O requests. A frame is a chunk of continuous memory, the size of which is vendor-specified through the **AllocatorFraming** member of [**KSPIN\_DESCRIPTOR\_EX**](https://msdn.microsoft.com/library/windows/hardware/ff563534).

Minidrivers can support allocators for multiple buffer types, for instance on-board RAM in a video card. However, most minidrivers use the *default allocator* to allocate system memory. Minidrivers can specify frame size, maximum number of frames, and alignment requirements. The default allocator takes care of meeting the requirements, and may optimize performance by reusing discarded frames.

A minidriver creates an allocator by calling the [**KsCreateAllocator**](https://msdn.microsoft.com/library/windows/hardware/ff561633) routine or related functions. In this call, the minidriver passes a pointer to a [**KSALLOCATOR\_FRAMING**](https://msdn.microsoft.com/library/windows/hardware/ff560979) structure. This structure contains parameters describing the requested allocator.

In the stream class model, minidrivers that create allocators support the [**KSPROPERTY\_CONNECTION\_ALLOCATORFRAMING**](https://msdn.microsoft.com/library/windows/hardware/ff565099) property. This is a read-only request that returns a pointer to the relevant [**KSALLOCATOR\_FRAMING**](https://msdn.microsoft.com/library/windows/hardware/ff560979) structure for the specified sink handle.

Minidrivers that provide allocators should also support the [**KSPROPERTY\_STREAM\_ALLOCATOR**](https://msdn.microsoft.com/library/windows/hardware/ff565684) property. This property provides read/write access to the handle of the allocator currently assigned to the stream connection point.

Minidrivers running under AVStream may include pins that implement their own allocators. Do this by setting the [**KSALLOCATOR\_DISPATCH**](https://msdn.microsoft.com/library/windows/hardware/ff560976) member of the [**KSPIN\_DISPATCH**](https://msdn.microsoft.com/library/windows/hardware/ff563535) structure. Specify **NULL** for this member if you do not want to specify an allocator for this pin.

In addition, AVStream minidrivers use the [**KSALLOCATOR\_FRAMING\_EX**](https://msdn.microsoft.com/library/windows/hardware/ff560982) structure to specify allocator requirements. Clients then use the [**KSPROPERTY\_CONNECTION\_ALLOCATORFRAMING\_EX**](https://msdn.microsoft.com/library/windows/hardware/ff565101) property to retrieve framing requirements for a pin. See [AVStream Allocators](avstream-allocators.md) for more information.

This section contains the following additional information:

[Default Allocators](default-allocators.md)

[Filter Specific Allocators](filter-specific-allocators.md)

[Allocation Schemes](allocation-schemes.md)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstream\stream%5D:%20KS%20Allocators%20%20RELEASE:%20%288/23/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


