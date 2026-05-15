---
title: WppAutoLogStop function
description: The WppAutoLogStop function is for internal use only.
ms.date: 11/07/2025
keywords: ["WppAutoLogStop function"]
topic_type:
- apiref
ms.topic: reference
api_name:
- WppAutoLogStop
api_type:
 - DllExport
api_location:
 - WppRecorder.sys
 - WppRecorderUM.dll
---

# WppAutoLogStop function

The WppAutoLogStop function is for internal use only.

## Syntax

```cpp
VOID
WppAutoLogStop(
    _In_ WPP_CB_TYPE * WppCb,
    _In_ PDRIVER_OBJECT DrvObj
    );
```

## Parameters

`WppCb`

`DrvObj`

## Return value

None

## Remarks

This function is for internal use only.

## Requirements

| Requirement | Value |
| ------ | ------ |
| **Kernel mode library** | WppRecorder.sys |
| **User mode library** | WppRecorderUM.dll |
