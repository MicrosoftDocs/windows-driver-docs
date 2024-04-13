---
title: Bug Check 0x1D1 TELEMETRY_ASSERTS_LIVEDUMP
description: The TELEMETRY_ASSERTS_LIVEDUMP live dump has a value of 0x000001D1.
keywords: ["Bug Check 0x1D1 TELEMETRY_ASSERTS_LIVEDUMP", "TELEMETRY_ASSERTS_LIVEDUMP"]
ms.date: 04/19/2018
topic_type:
- apiref
ms.topic: reference
api_name:
- TELEMETRY_ASSERTS_LIVEDUMP
api_type:
- NA
---

# Bug Check 0x1D1: TELEMETRY\_ASSERTS\_LIVEDUMP

The TELEMETRY_ASSERTS_LIVEDUMP live dump has a value of 0x000001D1. 

A Telemetry Assert verification failed.

This code can never be used for a real bugcheck; it is used to identify live dumps including device telemetry.

To troubleshoot this issue, inspect the callstack to see why the expression in MICROSOFT_TELEMETRY_ASSERT(expression) is invalid.

## TELEMETRY\_ASSERTS\_LIVEDUMP Parameters

| Parameter | Description |
|-----------|-------------|
| 1         | Rva         |
| 2         | ModuleName  |
| 3         | TimeStamp   |
| 4         | SizeOfImage |
 
## See Also

[Kernel Live Dump Code Reference](bug-check-code-reference-live-dump.md)

[Bug Check Code Reference](bug-check-code-reference2.md)
 




