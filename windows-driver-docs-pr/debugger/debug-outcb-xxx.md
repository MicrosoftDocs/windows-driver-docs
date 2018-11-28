---
title: DEBUG\_OUTPUT\_XXX
description: The DEBUG\_OUTPUT\_XXX constants are output flags. The output flags form a bit field that indicates the type of the output that accompanies them.
ms.date: 11/28/2018
topic_type:
- apiref
api_name:
- DEBUG_OUTPUT_NORMAL
- DEBUG_OUTPUT_ERROR
- DEBUG_OUTPUT_WARNING
- DEBUG_OUTPUT_VERBOSE
- DEBUG_OUTPUT_PROMPT
- DEBUG_OUTPUT_PROMPT_REGISTERS
- DEBUG_OUTPUT_EXTENSION_WARNING
- DEBUG_OUTPUT_DEBUGGEE
- DEBUG_OUTPUT_DEBUGGEE_PROMPT
- DEBUG_OUTPUT_SYMBOLS
- DEBUG_OUTPUT_STATUS
api_location:
- DbgEng.h
api_type:
- HeaderDef
ms.localizationpriority: medium
---

# DEBUG\_OUTPUT\_XXX


The DEBUG\_OUTPUT\_*XXX* constants are output flags. The output flags form a bit field that indicates the type of the output that accompanies them.

Different kinds of output callback notifications that can be sent to Output2.

The possible values include the following.

|Constant|Description|
|-----|-------|
|DEBUG_OUTCB_TEXT||
|||
|||


// Plain text content, flags are below, argument is mask.
#define            0
// Debugger markup content, flags are below, argument is mask.
#define DEBUG_OUTCB_DML            1
// Notification of an explicit output flush, flags and argument are zero.
#define DEBUG_OUTCB_EXPLICIT_FLUSH 2


Requirements
------------

|||
|-----|-------|
|Header|DbgEng.h (include DbgEng.h)|

 

 





