---
title: DEBUG\_REQUEST\_GET\_CAPTURED\_EVENT\_CODE\_OFFSET
description: DEBUG\_REQUEST\_GET\_CAPTURED\_EVENT\_CODE\_OFFSET
ms.assetid: cdf05d4f-8a8c-4b52-b36f-9d00575fdb7b
keywords: ["DEBUG_REQUEST_GET_CAPTURED_EVENT_CODE_OFFSET Windows Debugging"]
topic_type:
- apiref
api_name:
- DEBUG_REQUEST_GET_CAPTURED_EVENT_CODE_OFFSET
api_type:
- NA
ms.author: domars
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# DEBUG\_REQUEST\_GET\_CAPTURED\_EVENT\_CODE\_OFFSET


The DEBUG\_REQUEST\_GET\_CAPTURED\_EVENT\_CODE\_OFFSET [**Request**](request.md) operation returns the current event's instruction pointer.

**Parameters**

<span id="InBuffer"></span><span id="inbuffer"></span><span id="INBUFFER"></span>*InBuffer*  
Not used.

<span id="OutBuffer"></span><span id="outbuffer"></span><span id="OUTBUFFER"></span>*OutBuffer*  
The instruction pointer of the current event. The type of the instruction pointer is ULONG64.

### <span id="Return_Value"></span><span id="return_value"></span><span id="RETURN_VALUE"></span>Return Value

<span id="S_OK"></span><span id="s_ok"></span>S\_OK  
The method was successful.

<span id="E_NOINTERFACE"></span><span id="e_nointerface"></span>E\_NOINTERFACE  
The memory at the instruction pointer for the current event is not valid.

This method may also return error values. See [**Return Values**](https://msdn.microsoft.com/library/windows/hardware/ff549771) for more details.

Remarks
-------

The memory at the instruction pointer for the current event can be read using the [**Request**](request.md) operation's [**DEBUG\_REQUEST\_READ\_CAPTURED\_EVENT\_CODE\_STREAM**](debug-request-read-captured-event-code-stream.md).

## <span id="see_also"></span>See also


[**Request**](request.md)

[**DEBUG\_REQUEST\_READ\_CAPTURED\_EVENT\_CODE\_STREAM**](debug-request-read-captured-event-code-stream.md)

 

 






