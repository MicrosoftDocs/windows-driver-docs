---
title: KS Allocators
description: KS Allocators
ms.assetid: 07812703-a66f-450a-b28e-4cf765267c4a
keywords:
- kernel streaming WDK , allocators
- KS WDK , allocators
- allocators WDK kernel streaming
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# KS Allocators





An *Allocator* is a KS object that instantiates data buffers called *frames* for I/O requests. A frame is a chunk of continuous memory, the size of which is vendor-specified through the **AllocatorFraming** member of [**KSPIN\_DESCRIPTOR\_EX**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ks/ns-ks-_kspin_descriptor_ex).

Minidrivers can support allocators for multiple buffer types, for instance on-board RAM in a video card. However, most minidrivers use the *default allocator* to allocate system memory. Minidrivers can specify frame size, maximum number of frames, and alignment requirements. The default allocator takes care of meeting the requirements, and may optimize performance by reusing discarded frames.

A minidriver creates an allocator by calling the [**KsCreateAllocator**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ks/nf-ks-kscreateallocator) routine or related functions. In this call, the minidriver passes a pointer to a [**KSALLOCATOR\_FRAMING**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ks/ns-ks-ksallocator_framing) structure. This structure contains parameters describing the requested allocator.

In the stream class model, minidrivers that create allocators support the [**KSPROPERTY\_CONNECTION\_ALLOCATORFRAMING**](https://docs.microsoft.com/windows-hardware/drivers/stream/ksproperty-connection-allocatorframing) property. This is a read-only request that returns a pointer to the relevant [**KSALLOCATOR\_FRAMING**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ks/ns-ks-ksallocator_framing) structure for the specified sink handle.

Minidrivers that provide allocators should also support the [**KSPROPERTY\_STREAM\_ALLOCATOR**](https://docs.microsoft.com/windows-hardware/drivers/stream/ksproperty-stream-allocator) property. This property provides read/write access to the handle of the allocator currently assigned to the stream connection point.

Minidrivers running under AVStream may include pins that implement their own allocators. Do this by setting the [**KSALLOCATOR\_DISPATCH**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ks/ns-ks-_ksallocator_dispatch) member of the [**KSPIN\_DISPATCH**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ks/ns-ks-_kspin_dispatch) structure. Specify **NULL** for this member if you do not want to specify an allocator for this pin.

In addition, AVStream minidrivers use the [**KSALLOCATOR\_FRAMING\_EX**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ks/ns-ks-ksallocator_framing_ex) structure to specify allocator requirements. Clients then use the [**KSPROPERTY\_CONNECTION\_ALLOCATORFRAMING\_EX**](https://docs.microsoft.com/windows-hardware/drivers/stream/ksproperty-connection-allocatorframing-ex) property to retrieve framing requirements for a pin. See [AVStream Allocators](avstream-allocators.md) for more information.

This section contains the following additional information:

[Default Allocators](default-allocators.md)

[Filter Specific Allocators](filter-specific-allocators.md)

[Allocation Schemes](allocation-schemes.md)

 

 




