---
title: KSEVENTSETID\_StreamAllocator
description: The KSEVENTSETID\_StreamAllocator event set specifies two events.
MS-HAID:
- 'ks-event\_1b3f694c-e59e-4f5e-9f80-ac8f748aa559.xml'
- 'stream.kseventsetid\_streamallocator'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 2ca3914c-b3f3-467d-86ef-fe3331421e27
keywords: ["KSEVENTSETID_StreamAllocator Streaming Media Devices"]
topic_type:
- apiref
api_name:
- KSEVENTSETID_StreamAllocator
api_type:
- NA
---

# KSEVENTSETID\_StreamAllocator


The KSEVENTSETID\_StreamAllocator event set specifies two events. One event is used internally in the default allocator implementation to service outstanding allocation requests made through the IRP interface. The other, a public event, is used to notify clients of free frame availability.

The KSEVENTSETID\_StreamAllocator event set includes:

[**KSEVENT\_STREAMALLOCATOR\_INTERNAL\_FREEFRAME**](ksevent-streamallocator-internal-freeframe.md)

[**KSEVENT\_STREAMALLOCATOR\_FREEFRAME**](ksevent-streamallocator-freeframe.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstream\stream%5D:%20KSEVENTSETID_StreamAllocator%20%20RELEASE:%20%2811/22/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




