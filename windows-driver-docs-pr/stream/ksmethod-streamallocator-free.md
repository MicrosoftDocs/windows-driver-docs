---
title: KSMETHOD\_STREAMALLOCATOR\_FREE
description: The KSMETHOD\_STREAMALLOCATOR\_FREE method is used by a client to free a frame back to the given allocator.
MS-HAID:
- 'ks-method\_89ca7b07-629c-4128-a2ed-79bfb913707d.xml'
- 'stream.ksmethod\_streamallocator\_free'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 90d42ae6-4aa2-46fd-b10c-7f07b77c86f1
keywords: ["KSMETHOD_STREAMALLOCATOR_FREE Streaming Media Devices"]
topic_type:
- apiref
api_name:
- KSMETHOD_STREAMALLOCATOR_FREE
api_type:
- NA
---

# KSMETHOD\_STREAMALLOCATOR\_FREE


The **KSMETHOD\_STREAMALLOCATOR\_FREE** method is used by a client to free a frame back to the given allocator. A pending [**KSMETHOD\_STREAMALLOCATOR\_ALLOC**](ksmethod-streamallocator-alloc.md), if any, can be completed by using this method.

For example, a kernel-mode client could use the following sample code to free a frame:

Remarks
-------

```
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstream\stream%5D:%20KSMETHOD_STREAMALLOCATOR_FREE%20%20RELEASE:%20%2811/22/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




