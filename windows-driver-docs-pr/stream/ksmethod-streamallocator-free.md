---
title: KSMETHOD\_STREAMALLOCATOR\_FREE
description: The KSMETHOD\_STREAMALLOCATOR\_FREE method is used by a client to free a frame back to the given allocator.
ms.assetid: 90d42ae6-4aa2-46fd-b10c-7f07b77c86f1
keywords: ["KSMETHOD_STREAMALLOCATOR_FREE Streaming Media Devices"]
topic_type:
- apiref
api_name:
- KSMETHOD_STREAMALLOCATOR_FREE
api_type:
- NA
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# KSMETHOD\_STREAMALLOCATOR\_FREE


The **KSMETHOD\_STREAMALLOCATOR\_FREE** method is used by a client to free a frame back to the given allocator. A pending [**KSMETHOD\_STREAMALLOCATOR\_ALLOC**](ksmethod-streamallocator-alloc.md), if any, can be completed by using this method.

For example, a kernel-mode client could use the following sample code to free a frame:

Remarks
-------

```cpp
Method.Identifier.Set = KSMETHODSETID_StreamAllocator;
Method.Identifier.Id = KSMETHOD_STREAMALLOCATOR_FREE;
Method.Flags = KSMETHOD_TYPE_READ;
DeviceIoControl(
    AllocatorHandle,
    IOCTL_KS_METHOD,
    &amp;Method,
    sizeof(KSMETHOD),
    &amp;Frame,
    sizeof( PVOID ),
    &amp;BytesReturned,
    &amp;Overlapped);
```

 

 





