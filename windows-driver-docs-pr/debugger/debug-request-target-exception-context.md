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
ms.author: domars
ms.date: 11/28/2017
ms.localizationpriority: medium
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

 

 






