---
title: DEBUG\_REQUEST\_TARGET\_EXCEPTION\_CONTEXT
description: DEBUG\_REQUEST\_TARGET\_EXCEPTION\_CONTEXT
ms.assetid: e599a3f7-110b-46fc-8266-3a00ea1efe03
keywords: ["DEBUG_REQUEST_TARGET_EXCEPTION_CONTEXT Windows Debugging"]
topic_type:
- apiref
api_name:
- DEBUG_REQUEST_TARGET_EXCEPTION_CONTEXT
api_type:
- NA
---

# DEBUG\_REQUEST\_TARGET\_EXCEPTION\_CONTEXT


The DEBUG\_REQUEST\_TARGET\_EXCEPTION\_CONTEXT [**Request**](request.md) operation returns the [thread context](https://msdn.microsoft.com/library/windows/hardware/ff554702#thread-context) for the stored event in a user-mode minidump file.

**Parameters**

<span id="InBuffer"></span><span id="inbuffer"></span><span id="INBUFFER"></span>*InBuffer*  
Not used.

<span id="OutBuffer"></span><span id="outbuffer"></span><span id="OUTBUFFER"></span>*OutBuffer*  
The thread context for the stored event. The type of the thread context is the CONTEXT structure for the target's effective processor at the time of the event. *OutBuffer* must be large enough to hold this structure.

Remarks
-------

This information is also returned to the *Context* parameter by the [**GetStoredEventInformation**](https://msdn.microsoft.com/library/windows/hardware/ff548431) method.

## <span id="see_also"></span>See also


[**Request**](request.md)

[**GetStoredEventInformation**](https://msdn.microsoft.com/library/windows/hardware/ff548431)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20DEBUG_REQUEST_TARGET_EXCEPTION_CONTEXT%20%20RELEASE:%20%2811/27/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





