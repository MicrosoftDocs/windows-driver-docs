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
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# KSMETHOD\_STREAMALLOCATOR\_ALLOC


The **KSMETHOD\_STREAMALLOCATOR\_ALLOC** method is used by a client to allocate a frame from the given allocator. The method returns STATUS\_PENDING if no frames are currently available. Otherwise, the method returns a pointer to a frame.

For example, a kernel-mode client could use the following sample code to allocate a frame:

Remarks
-------

```
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstream\stream%5D:%20KSMETHOD_STREAMALLOCATOR_ALLOC%20%20RELEASE:%20%2811/22/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




