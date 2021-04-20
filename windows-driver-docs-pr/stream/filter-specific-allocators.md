---
title: Filter Specific Allocators
description: Filter Specific Allocators
keywords:
- filter specific allocators WDK kernel streaming
- filter allocators WDK kernel streaming
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Filter Specific Allocators





Filters that require allocators for on-board memory or other device dependent storage methods can provide a specific allocator by supporting allocator [properties](./kspropsetid-streamallocator.md) and [methods](./ksmethodsetid-streamallocator.md). For more information, see [**KSPROPERTY\_STREAM\_ALLOCATOR**](./ksproperty-stream-allocator.md).

A filter receives an IRP\_MJ\_CREATE of type KSCREATE\_REQUEST\_ALLOCATOR specifying the framing options for the allocator. The minidriver's allocator creation routine validates the create request by calling [**KsValidateAllocatorCreateRequest**](/windows-hardware/drivers/ddi/ks/nf-ks-ksvalidateallocatorcreaterequest). If the call is successful, this routine returns a pointer to the relevant [**KSALLOCATOR\_FRAMING**](/windows-hardware/drivers/ddi/ks/ns-ks-ksallocator_framing) structure.

If the filter cannot satisfy the framing requirements, it returns a failure code in response to the IRP. Otherwise, the filter attaches a pointer to a structure to the **FsContext** member of the file object and services the resulting allocator requests.

If buffers passed to the streaming interface should be modified in-place by the filter, the user-mode client sets the KSALLOCATOR\_REQUIREMENTF\_INPLACE\_MODIFIER flag on the relevant [**KSALLOCATOR\_FRAMING**](/windows-hardware/drivers/ddi/ks/ns-ks-ksallocator_framing) structure.

There are two interfaces available to the allocator. First, all allocators must support the IRP-based [KSMETHODSETID\_StreamAllocator](./ksmethodsetid-streamallocator.md). Allocators using this mechanism are limited to a maximum number of allocated frames. Requests to allocate frames beyond this limit will be marked pending.

Second, the minidriver can support function table access if the allocation pool type can be serviced at DISPATCH\_LEVEL. Providing function table access is optional. Do this by supporting the properties in [KSPROPSETID\_StreamAllocator](./kspropsetid-streamallocator.md).

The DISPATCH\_LEVEL interface operates as follows:

When an allocate request is submitted to the allocator, the allocator returns a pointer to a frame if one is available. If not, it immediately returns **NULL**.

When a free request is submitted to the allocator, the allocator signals the stream allocator "free frame" event notifying the client that a free frame is available. Additionally, if there are allocation request IRPs waiting to be completed, the allocator must schedule a worker item (if the current IRQL is not PASSIVE\_LEVEL) and complete the request with the free frame.

It is possible for both the DISPATCH\_LEVEL interface and the IRP-based interface to contend for free frames. KS synchronizes this queue using the cancel spin lock.

 

