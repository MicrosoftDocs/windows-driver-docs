---
title: IPrinterScriptUsbJobContextReturnCodes Failure method
description: Returns a value of '1' to inform USBMon that the method call failed.
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
keywords: ["Failure method Print Devices", "Failure method Print Devices , IPrinterScriptUsbJobContextReturnCodes interface", "IPrinterScriptUsbJobContextReturnCodes interface Print Devices , Failure method"]
topic_type:
- apiref
ms.topic: reference
api_name:
- IPrinterScriptUsbJobContextReturnCodes.Failure
api_type:
- COM
ms.date: 07/13/2023
---

# IPrinterScriptUsbJobContextReturnCodes::Failure method

Returns a value of '1' to inform USBMon that the method call failed.

## Syntax

```cpp
HRESULT Failure(
  [out, retval] UINT32 *value
);
```

## Parameters

*value* \[out, retval\]  
Value that indicates a failed method call.

## Return value

This method returns an **HRESULT** value.

## Remarks

**Failure** is a read-only method. When USBMon receives this failure value, it cleans up the Job Context object and returns an error code to the print spooler.

## Requirements

**Minimum supported client:** Windows 8.1

**Minimum supported server:** Windows Server 2012 R2

**Target platform:** Desktop

## See also

[**IPrinterScriptUsbJobContextReturnCodes**](iprinterscriptusbjobcontextreturncodes.md)
