---
title: Bug Check 0x1D7 EFS_FATAL_ERROR
description: The EFS_FATAL_ERROR bug check has a value of 0x000001D7. It indicates that an EFS error condition has occured such that cannot be handled without data loss or data corruption.
keywords: ["Bug Check 0x1D7 EFS_FATAL_ERROR", "EFS_FATAL_ERROR"]
ms.date: 01/22/2019
topic_type:
- apiref
api_name:
- EFS_FATAL_ERROR
api_type:
- NA
ms.localizationpriority: medium
---

# Bug Check 0x1D7: EFS\_FATAL\_ERROR

The EFS\_FATAL\_ERROR bug check has a value of 0x000001D7. It indicates that an EFS error condition has occured such that cannot be handled without data loss or data corruption.


**Important** This topic is for programmers. If you are a customer who has received a blue screen error code while using your computer, see [Troubleshoot blue screen errors](https://windows.microsoft.com/windows-10/troubleshoot-blue-screen-errors).
 

## EFS\_FATAL\_ERROR Parameters

|Parameter|Description|
|-------- |---------- |
|1| Bug Check Subclass:  **01** - Pre-offloading failure.|
|2| NTSTATUS return code of the operation.|
|3| The current IRP at the time of failure.|
|4| File encryption context at the time of failure.|

## Cause
-----

An EFS error condition has occured such that cannot be handled without data loss or data corruption.


## See Also
----------

[Bug Check Code Reference](bug-check-code-reference2.md)

