---
title: Bug Check 0x1D7 EFS_FATAL_ERROR
description: The EFS_FATAL_ERROR bug check has a value of 0x000001D7. It indicates that an EFS error condition has occurred such that cannot be handled without data loss or data corruption.
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

The EFS\_FATAL\_ERROR bug check has a value of 0x000001D7. It indicates that an EFS error condition has occurred such that cannot be handled without data loss or data corruption.


> [!IMPORTANT]
> This topic is for programmers. If you are a customer who has received a blue screen error code while using your computer, see [Troubleshoot blue screen errors](https://www.windows.com/stopcode).

 

## EFS\_FATAL\_ERROR Parameters

|Parameter|Description|
|-------- |---------- |
|1| Bug Check Subclass:  **01** - Pre-offloading failure.|
|2| NTSTATUS return code of the operation.|
|3| The current IRP at the time of failure.|
|4| File encryption context at the time of failure.|

## ## Cause

An EFS error condition has occurred such that cannot be handled without data loss or data corruption.

## Resolution
-----

The [!analyze](-analyze.md) debug extension displays information about the bug check and can be helpful in determining the root cause.

Examine parameter 2 the NTSTATUS field to try and determine why NT_SUCCESS was not returned. This is the expected and only allowed value for file systems that call crypto pre-offloading.

Use the debugger [!IRP](-irp.md) command to investigate parameter 3 for a possible conflicting IRP code or other issues.



## ## See Also-

[Bug Check Code Reference](bug-check-code-reference2.md)

