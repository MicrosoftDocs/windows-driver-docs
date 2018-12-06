---
title: KSEVENTSETID\_StreamAllocator
description: The KSEVENTSETID\_StreamAllocator event set specifies two events.
ms.assetid: 2ca3914c-b3f3-467d-86ef-fe3331421e27
keywords: ["KSEVENTSETID_StreamAllocator Streaming Media Devices"]
topic_type:
- apiref
api_name:
- KSEVENTSETID_StreamAllocator
api_type:
- NA
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# KSEVENTSETID\_StreamAllocator


The KSEVENTSETID\_StreamAllocator event set specifies two events. One event is used internally in the default allocator implementation to service outstanding allocation requests made through the IRP interface. The other, a public event, is used to notify clients of free frame availability.

The KSEVENTSETID\_StreamAllocator event set includes:

[**KSEVENT\_STREAMALLOCATOR\_INTERNAL\_FREEFRAME**](ksevent-streamallocator-internal-freeframe.md)

[**KSEVENT\_STREAMALLOCATOR\_FREEFRAME**](ksevent-streamallocator-freeframe.md)

 

 





