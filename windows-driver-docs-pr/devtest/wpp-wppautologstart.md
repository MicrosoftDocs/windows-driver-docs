---
title: WppAutoLogStart function
description: For internal use only.
ms.date: 11/07/2025
keywords: ["WppAutoLogStart function"]
topic_type:
- apiref
ms.topic: reference
api_name:
- WppAutoLogStart
api_type:
 - DllExport
api_location:
 - WppRecorder.sys
 - WppRecorderUM.dll
---

# WppAutoLogStart function

This function is for internal use only.

## Syntax

```cpp
VOID
WppAutoLogStart(
    _In_ WPP_CB_TYPE * WppCb,
    _In_ PDRIVER_OBJECT DrvObj,
    _In_ PCUNICODE_STRING RegPath
    );
```

## Parameters

`WppCb`

`DrvObj`

`RegPath`


## Return value

None

## Remarks

This function is for internal use only.

## Requirements

| Requirement | Value |
| ------ | ------ |
| **Kernel mode library** | WppRecorder.sys |
| **User mode library** | WppRecorderUM.dll |
