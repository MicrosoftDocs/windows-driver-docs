---
title: DEBUG_REQUEST_TARGET_EXCEPTION_RECORD
description: DEBUG\_REQUEST\_TARGET\_EXCEPTION\_RECORD
keywords: ["DEBUG_REQUEST_TARGET_EXCEPTION_RECORD Windows Debugging"]
topic_type:
- apiref
ms.topic: reference
api_name:
- DEBUG_REQUEST_TARGET_EXCEPTION_RECORD
api_type:
- NA
ms.date: 11/28/2017
---

# DEBUG\_REQUEST\_TARGET\_EXCEPTION\_RECORD


The DEBUG\_REQUEST\_TARGET\_EXCEPTION\_RECORD [**Request**](request.md) operation returns the exception record for the stored event in a user-mode minidump file.

<span id="InBuffer"></span><span id="inbuffer"></span><span id="INBUFFER"></span>*InBuffer*  
Not used.

<span id="OutBuffer"></span><span id="outbuffer"></span><span id="OUTBUFFER"></span>*OutBuffer*  
The exception record for the stored event. The type of the exception record is EXCEPTION\_RECORD64, which is defined in winnt.h.

## <span id="see_also"></span>See also


[**Request**](request.md)

 

 
