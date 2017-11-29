---
title: DEBUG\_REQUEST\_TARGET\_CAN\_DETACH
description: DEBUG\_REQUEST\_TARGET\_CAN\_DETACH
ms.assetid: 1e36715e-3414-4cd2-95f3-2b97878a3989
keywords: ["DEBUG_REQUEST_TARGET_CAN_DETACH Windows Debugging"]
topic_type:
- apiref
api_name:
- DEBUG_REQUEST_TARGET_CAN_DETACH
api_type:
- NA
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# DEBUG\_REQUEST\_TARGET\_CAN\_DETACH


The DEBUG\_REQUEST\_TARGET\_CAN\_DETACH [**Request**](request.md) operation checks to see if it is possible for the debugger engine to detach from the current process (leaving the process running but no longer being debugged).

**Parameters**

<span id="InBuffer"></span><span id="inbuffer"></span><span id="INBUFFER"></span>*InBuffer*  
Not used.

<span id="OutBuffer"></span><span id="outbuffer"></span><span id="OUTBUFFER"></span>*OutBuffer*  
Not used.

### <span id="Return_Value"></span><span id="return_value"></span><span id="RETURN_VALUE"></span>Return Value

<span id="S_OK"></span><span id="s_ok"></span>S\_OK  
It is possible to detach the debugger from the current process.

<span id="S_FALSE"></span><span id="s_false"></span>S\_FALSE  
It is not possible to detach the debugger from the current process.

Remarks
-------

Only targets running on Microsoft Windows XP or later versions of Windows support detaching the debugger from the process.

## <span id="see_also"></span>See also


[**Request**](request.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20DEBUG_REQUEST_TARGET_CAN_DETACH%20%20RELEASE:%20%2811/27/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





