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
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20DEBUG_REQUEST_GET_CAPTURED_EVENT_CODE_OFFSET%20%20RELEASE:%20%2811/27/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





