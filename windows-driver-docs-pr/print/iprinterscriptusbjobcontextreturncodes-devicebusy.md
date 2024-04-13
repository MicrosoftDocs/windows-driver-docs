---
title: IPrinterScriptUsbJobContextReturnCodes DeviceBusy Method
description: Returns a value of '3' to inform USBMon that the device communication channel isn't accepting data at this time.
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
keywords: ["DeviceBusy method Print Devices", "DeviceBusy method Print Devices , IPrinterScriptUsbJobContextReturnCodes interface", "IPrinterScriptUsbJobContextReturnCodes interface Print Devices , DeviceBusy method"]
topic_type:
- apiref
ms.topic: reference
api_name:
- IPrinterScriptUsbJobContextReturnCodes.DeviceBusy
api_type:
- COM
ms.date: 07/13/2023
---

# IPrinterScriptUsbJobContextReturnCodes::DeviceBusy method

Returns a value of '3' to inform USBMon that the device communication channel isn't accepting data at this time.

## Syntax

```cpp
HRESULT DeviceBusy(
  [out, retval] UINT32 *value
);
```

## Parameters

*value* \[out, retval\]  
Value that indicates that the communication channel isn't accepting data at this time.

## Return value

This method returns an **HRESULT** value.

## Remarks

**DeviceBusy** is a read-only method. A returned value of '3' doesn't indicate a failure, and USBMon should inform the print spooler that the device is busy. USBMon can then call the function again at a later time. The number of bytes processed from the print data stream (printData) is returned in the writePrintDataProgress object.

## Requirements

**Minimum supported client:** Windows 8.1

**Minimum supported server:** Windows Server 2012 R2

**Target platform:** Desktop

## See also

[**IPrinterScriptUsbJobContextReturnCodes**](iprinterscriptusbjobcontextreturncodes.md)
