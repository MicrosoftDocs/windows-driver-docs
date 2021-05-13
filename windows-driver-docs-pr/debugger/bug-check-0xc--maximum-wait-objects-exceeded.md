---
title: Bug Check 0xC MAXIMUM_WAIT_OBJECTS_EXCEEDED
description: The MAXIMUM_WAIT_OBJECTS_EXCEEDED bug check has a value of 0x0000000C. This indicates that the current thread exceeded the permitted number of wait objects.
keywords: ["Bug Check 0xC MAXIMUM_WAIT_OBJECTS_EXCEEDED", "MAXIMUM_WAIT_OBJECTS_EXCEEDED"]
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- MAXIMUM_WAIT_OBJECTS_EXCEEDED
api_type:
- NA
ms.localizationpriority: medium
---

# Bug Check 0xC: MAXIMUM\_WAIT\_OBJECTS\_EXCEEDED


The MAXIMUM\_WAIT\_OBJECTS\_EXCEEDED bug check has a value of 0x0000000C. This indicates that the current thread exceeded the permitted number of wait objects.

> [!IMPORTANT]
> This topic is for programmers. If you are a customer who has received a blue screen error code while using your computer, see [Troubleshoot blue screen errors](https://www.windows.com/stopcode).


## MAXIMUM\_WAIT\_OBJECTS\_EXCEEDED Parameters


None

## Cause

This bug check results from the improper use of **KeWaitForMultipleObjects** or **FsRtlCancellableWaitForMultipleObjects**.

The caller may pass a pointer to a buffer in this routine's *WaitBlockArray* parameter. The system will use this buffer to keep track of wait objects.

If a buffer is supplied, the *Count* parameter may not exceed MAXIMUM\_WAIT\_OBJECTS. If no buffer is supplied, the *Count* parameter may not exceed THREAD\_WAIT\_OBJECTS.

If the value of *Count* exceeds the allowable value, this bug check is issued.

 

 




