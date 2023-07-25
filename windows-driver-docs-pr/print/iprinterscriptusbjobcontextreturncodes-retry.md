---
title: IPrinterScriptUsbJobContextReturnCodes Retry method
description: Returns a value of '2' to inform USBMon that the method call was successful, with more work to be completed.
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
keywords: ["Retry method Print Devices", "Retry method Print Devices , IPrinterScriptUsbJobContextReturnCodes interface", "IPrinterScriptUsbJobContextReturnCodes interface Print Devices , Retry method"]
topic_type:
- apiref
ms.topic: reference
api_name:
- IPrinterScriptUsbJobContextReturnCodes.Retry
api_type:
- COM
ms.date: 07/13/2023
---

# IPrinterScriptUsbJobContextReturnCodes::Retry method

Returns a value of '2' to inform USBMon that the method call was successful, with more work to be completed.

## Syntax

```cpp
HRESULT Retry(
  [out, retval] UINT32 *value
);
```

## Parameters

*value* \[out, retval\]  
Value indicating a successful method call, with more work to be done.

## Return value

This method returns an **HRESULT** value.

## Remarks

**Retry** is a read-only method. USBMon should process any Bidi Schema updates (including Bidi Events) in a printerBidiSchemaResponses object, and then call the **Retry** method again to allow the IHV code to continue processing the data. The number of bytes processed from the print data stream (printData) is returned in the writePrintDataProgress object associated with the print job.

## Requirements

**Minimum supported client:** Windows 8.1

**Minimum supported server:** Windows Server 2012 R2

**Target platform:** Desktop

## See also

[**IPrinterScriptUsbJobContextReturnCodes**](iprinterscriptusbjobcontextreturncodes.md)
