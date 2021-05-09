---
title: DEBUG\_OUTCB\_XXX
description: The DEBUG\_OUTPUTCB\_XXX constants are output flags. The output flags form a bit field that indicates the type of the output that accompanies them.
ms.date: 11/28/2018
topic_type:
- apiref
api_name:
- DEBUG_OUTCB_TEXT
- DEBUG_OUTCB_DML
- DEBUG_OUTCB_EXPLICIT_FLUSH
api_location:
- DbgEng.h
api_type:
- HeaderDef
ms.localizationpriority: medium
---

# DEBUG\_OUTCB\_XXX


The DEBUG\_OUTCB\_XXX constants are output flags. The output flags form a bit field that indicates the type of the output that accompanies them.

DEBUG\_OUTCB\_XXX defines different kinds of output callback notifications that can be sent to Output2.

The possible values include the following.

|Constant|Description|
|-----|-------|
|DEBUG_OUTCB_TEXT|Plain text content, flags are below, argument is mask.|
|DEBUG_OUTCB_DML|Debugger markup content, flags are below, argument is mask.|
|DEBUG_OUTCB_EXPLICIT_FLUSH|Notification of an explicit output flush, flags and argument are zero.|


## Requirements

**Header**: DbgEng.h (include DbgEng.h)


 

 





