---
title: WppAutoLogTrace function
description: The WppAutoLogTrace function is for internal use only.
ms.date: 11/07/2025
keywords: ["WppAutoLogTrace function"]
topic_type:
- apiref
ms.topic: reference
api_name:
- WppAutoLogTrace
api_type:
 - DllExport
api_location:
 - WppRecorder.sys
 - WppRecorderUM.dll
---

# WppAutoLogTrace function

The WppAutoLogTrace function is for internal use only.

## Syntax

```cpp
NTSTATUS
WppAutoLogTrace(
    _In_ PVOID  AutoLogContext,
    _In_ UCHAR  MessageLevel,
    _In_ ULONG  MessageFlags,
    _In_ LPGUID MessageGuid,
    _In_ USHORT MessageNumber,
    ...
    );
```

## Parameters

`AutoLogContext`

`MessageLevel`

`MessageFlags`

`MessageGuid`

`MessageNumber`

## Return value

The method returns **STATUS_SUCCESS** if the operation succeeds. Otherwise, this method might return an appropriate **[NTSTATUS](/windows-hardware/drivers/kernel/ntstatus-values)** error code.

## Remarks

This function is for internal use only.

## Requirements

| Requirement | Value |
| ------ | ------ |
| **Kernel mode library** | WppRecorder.sys |
| **User mode library** | WppRecorderUM.dll |
