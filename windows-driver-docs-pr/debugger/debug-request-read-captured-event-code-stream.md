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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20DEBUG_REQUEST_READ_CAPTURED_EVENT_CODE_STREAM%20%20RELEASE:%20%2811/27/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





