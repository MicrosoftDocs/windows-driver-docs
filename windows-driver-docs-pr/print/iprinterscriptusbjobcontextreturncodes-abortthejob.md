---
title: IPrinterScriptUsbJobContextReturnCodes AbortTheJob method
description: Returns a value of '4' to inform USBMon that the print job must be aborted.
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
keywords: ["AbortTheJob method Print Devices", "AbortTheJob method Print Devices , IPrinterScriptUsbJobContextReturnCodes interface", "IPrinterScriptUsbJobContextReturnCodes interface Print Devices , AbortTheJob method"]
topic_type:
- apiref
ms.topic: reference
api_name:
- IPrinterScriptUsbJobContextReturnCodes.AbortTheJob
api_type:
- COM
ms.date: 07/13/2023
---

# IPrinterScriptUsbJobContextReturnCodes::AbortTheJob method

Returns a value of '4' to inform USBMon that the print job must be aborted.

## Syntax

```cpp
HRESULT AbortTheJob(
  [out, retval] UINT32 *value
);
```

## Parameters

*value* \[out, retval\]  
Value that indicates that the print job must be aborted.

## Return value

This method returns an **HRESULT** value.

## Remarks

**AbortTheJob** is a read-only method. This return code from the IHV JavaScript function informs USBMon that either the device couldn't continue processing the job, or the user canceled the job at the front panel of the device. When USBMon receives the message to abort a print job, it passes the information to the print spooler to abort the job, before returning.

## Requirements

**Minimum supported client:** Windows 8.1

**Minimum supported server:** Windows Server 2012 R2

**Target platform:** Desktop

## See also

[**IPrinterScriptUsbJobContextReturnCodes**](iprinterscriptusbjobcontextreturncodes.md)
