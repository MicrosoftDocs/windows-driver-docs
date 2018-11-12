---
title: Bug Check 0x1D1 TELEMETRY_ASSERTS_LIVEDUMP
description: The TELEMETRY_ASSERTS_LIVEDUMP bug check has a value of 0x000001D1.
keywords: ["Bug Check 0x1D1 TELEMETRY_ASSERTS_LIVEDUMP", "TELEMETRY_ASSERTS_LIVEDUMP"]
ms.author: domars
ms.date: 04/19/2018
topic_type:
- apiref
api_name:
- TELEMETRY_ASSERTS_LIVEDUMP
api_type:
- NA
ms.localizationpriority: medium
---

# Bug Check Bug Check 0x1D1: TELEMETRY\_ASSERTS\_LIVEDUMP

**Important** This topic is for programmers. If you are a customer who has received a blue screen error code while using your computer, see [Troubleshoot blue screen errors](https://windows.microsoft.com/windows-10/troubleshoot-blue-screen-errors).

The TELEMETRY_ASSERTS_LIVEDUMP bug check has a value of 0x000001D1. 

A Telemetry Assert verification failed.

This code can never be used for a real bugcheck; it is used to identify live dumps including device telemetry.

To troubleshoot this issue, inspect the callstack to see why the expression in MICROSOFT_TELEMETRY_ASSERT(expression) is invalid.

## TELEMETRY\_ASSERTS\_LIVEDUMP Parameters

Parameter | Description 
|---------|--------------|
1 | Rva
2 | ModuleName
3 | TimeStamp
4 | SizeOfImage

 

 




