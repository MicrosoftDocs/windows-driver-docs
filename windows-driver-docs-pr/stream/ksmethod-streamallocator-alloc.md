---
title: KSMETHOD\_STREAMALLOCATOR\_ALLOC
description: The KSMETHOD\_STREAMALLOCATOR\_ALLOC method is used by a client to allocate a frame from the given allocator.
ms.assetid: 4104d7df-1cc6-4109-9732-220b1065ee01
keywords: ["KSMETHOD_STREAMALLOCATOR_ALLOC Streaming Media Devices"]
topic_type:
- apiref
api_name:
- KSMETHOD_STREAMALLOCATOR_ALLOC
api_type:
- NA
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# KSMETHOD\_STREAMALLOCATOR\_ALLOC


The **KSMETHOD\_STREAMALLOCATOR\_ALLOC** method is used by a client to allocate a frame from the given allocator. The method returns STATUS\_PENDING if no frames are currently available. Otherwise, the method returns a pointer to a frame.

For example, a kernel-mode client could use the following sample code to allocate a frame:

Remarks
-------

```cpp
Method.Identifier.Set = KSMETHODSETID_StreamAllocator;
Method.Identifier.Id = KSMETHOD_STREAMALLOCATOR_ALLOC;
Method.Flags = KSMETHOD_TYPE_WRITE;
DeviceIoControl(
    AllocatorHandle,
    IOCTL_KS_METHOD,
    &amp;Method,
    sizeof(KSMETHOD),
    &amp;Frame,
    sizeof(PVOID),
    &amp;BytesReturned,
    &amp;Overlapped);
```

 

 





