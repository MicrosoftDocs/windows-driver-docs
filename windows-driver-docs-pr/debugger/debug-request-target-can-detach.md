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
ms.author: domars
ms.date: 11/28/2017
ms.localizationpriority: medium
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

 

 






