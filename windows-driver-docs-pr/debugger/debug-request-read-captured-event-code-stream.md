---
title: DEBUG\_REQUEST\_READ\_CAPTURED\_EVENT\_CODE\_STREAM
description: DEBUG\_REQUEST\_READ\_CAPTURED\_EVENT\_CODE\_STREAM
ms.assetid: 867c6b3e-13d5-46ae-b73c-f90936cb35c5
keywords: ["DEBUG_REQUEST_READ_CAPTURED_EVENT_CODE_STREAM Windows Debugging"]
topic_type:
- apiref
api_name:
- DEBUG_REQUEST_READ_CAPTURED_EVENT_CODE_STREAM
api_type:
- NA
ms.author: domars
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# DEBUG\_REQUEST\_READ\_CAPTURED\_EVENT\_CODE\_STREAM


The DEBUG\_REQUEST\_READ\_CAPTURED\_EVENT\_CODE\_STREAM [**Request**](request.md) operation returns up to 64 bytes of memory at the current event's instruction pointer.

**Parameters**

<span id="InBuffer"></span><span id="inbuffer"></span><span id="INBUFFER"></span>*InBuffer*  
Not used.

<span id="OutBuffer"></span><span id="outbuffer"></span><span id="OUTBUFFER"></span>*OutBuffer*  
The memory at the current event's instruction pointer. Up to 64 bytes of memory may be returned.

Remarks
-------

The memory returned is a snapshot of the memory taken when the event occurred. It does not reflect any changes that may have been made to the target's memory since the event.

The current event's instruction pointer is returned by the [**Request**](request.md) operation [**DEBUG\_REQUEST\_GET\_CAPTURED\_EVENT\_CODE\_OFFSET**](debug-request-get-captured-event-code-offset.md).

## <span id="see_also"></span>See also


[**Request**](request.md)

[**DEBUG\_REQUEST\_GET\_CAPTURED\_EVENT\_CODE\_OFFSET**](debug-request-get-captured-event-code-offset.md)

 

 






