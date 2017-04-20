---
title: Filter Specific Allocators
author: windows-driver-content
description: Filter Specific Allocators
ms.assetid: 581f3000-4e66-4ba0-979d-b187115a30b2
keywords:
- filter specific allocators WDK kernel streaming
- filter allocators WDK kernel streaming
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Filter Specific Allocators


## <a href="" id="ddk-filter-specific-allocator-ksg"></a>


Filters that require allocators for on-board memory or other device dependent storage methods can provide a specific allocator by supporting allocator [properties](https://msdn.microsoft.com/library/windows/hardware/ff566592) and [methods](https://msdn.microsoft.com/library/windows/hardware/ff563406). For more information, see [**KSPROPERTY\_STREAM\_ALLOCATOR**](https://msdn.microsoft.com/library/windows/hardware/ff565684).

A filter receives an IRP\_MJ\_CREATE of type KSCREATE\_REQUEST\_ALLOCATOR specifying the framing options for the allocator. The minidriver's allocator creation routine validates the create request by calling [**KsValidateAllocatorCreateRequest**](https://msdn.microsoft.com/library/windows/hardware/ff567219). If the call is successful, this routine returns a pointer to the relevant [**KSALLOCATOR\_FRAMING**](https://msdn.microsoft.com/library/windows/hardware/ff560979) structure.

If the filter cannot satisfy the framing requirements, it returns a failure code in response to the IRP. Otherwise, the filter attaches a pointer to a structure to the **FsContext** member of the file object and services the resulting allocator requests.

If buffers passed to the streaming interface should be modified in-place by the filter, the user-mode client sets the KSALLOCATOR\_REQUIREMENTF\_INPLACE\_MODIFIER flag on the relevant [**KSALLOCATOR\_FRAMING**](https://msdn.microsoft.com/library/windows/hardware/ff560979) structure.

There are two interfaces available to the allocator. First, all allocators must support the IRP-based [KSMETHODSETID\_StreamAllocator](https://msdn.microsoft.com/library/windows/hardware/ff563406). Allocators using this mechanism are limited to a maximum number of allocated frames. Requests to allocate frames beyond this limit will be marked pending.

Second, the minidriver can support function table access if the allocation pool type can be serviced at DISPATCH\_LEVEL. Providing function table access is optional. Do this by supporting the properties in [KSPROPSETID\_StreamAllocator](https://msdn.microsoft.com/library/windows/hardware/ff566592).

The DISPATCH\_LEVEL interface operates as follows:

When an allocate request is submitted to the allocator, the allocator returns a pointer to a frame if one is available. If not, it immediately returns **NULL**.

When a free request is submitted to the allocator, the allocator signals the stream allocator "free frame" event notifying the client that a free frame is available. Additionally, if there are allocation request IRPs waiting to be completed, the allocator must schedule a worker item (if the current IRQL is not PASSIVE\_LEVEL) and complete the request with the free frame.

It is possible for both the DISPATCH\_LEVEL interface and the IRP-based interface to contend for free frames. KS synchronizes this queue using the cancel spin lock.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstream\stream%5D:%20Filter%20Specific%20Allocators%20%20RELEASE:%20%288/23/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


