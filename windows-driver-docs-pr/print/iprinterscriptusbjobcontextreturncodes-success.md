---
title: IPrinterScriptUsbJobContextReturnCodes Success method
description: Returns a value of zero (0) to inform USBMon that the function call completed successfully.
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
keywords: ["Success method Print Devices", "Success method Print Devices , IPrinterScriptUsbJobContextReturnCodes interface", "IPrinterScriptUsbJobContextReturnCodes interface Print Devices , Success method"]
topic_type:
- apiref
ms.topic: reference
api_name:
- IPrinterScriptUsbJobContextReturnCodes.Success
api_type:
- COM
ms.date: 07/13/2023
---

# IPrinterScriptUsbJobContextReturnCodes::Success method

Returns a value of zero (0) to inform USBMon that the function call completed successfully.

## Syntax

```cpp
HRESULT Success(
  [out, retval] UINT32 *value
);
```

## Parameters

*value* \[out, retval\]  
Value indicating a successful method call.

## Return value

This method returns an **HRESULT** value.

## Remarks

**Success** is a read-only method.

## Requirements

**Minimum supported client:** Windows 8.1

**Minimum supported server:** Windows Server 2012 R2

**Target platform:** Desktop

## See also

[**IPrinterScriptUsbJobContextReturnCodes**](iprinterscriptusbjobcontextreturncodes.md)
