---
title: IPrinterScriptUsbJobContext ReturnCodes method
description: Returns an object that can supply return code values that an IHV has defined for their JavaScript functions.
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
keywords: ["ReturnCodes method Print Devices", "ReturnCodes method Print Devices , IPrinterScriptUsbJobContext interface", "IPrinterScriptUsbJobContext interface Print Devices , ReturnCodes method"]
topic_type:
- apiref
ms.topic: reference
api_name:
- IPrinterScriptUsbJobContext.ReturnCodes
api_type:
- COM
ms.date: 07/13/2023
---

# IPrinterScriptUsbJobContext::ReturnCodes method

Returns an object that can supply return code values that an IHV has defined for their JavaScript functions.

## Syntax

```cpp
HRESULT ReturnCodes(
  [out, retval] IPrinterScriptUsbJobContextReturnCodes **ppReturnCodes
);
```

## Parameters

*ppReturnCodes* \[out, retval\]  
The return code values for the IHV JavaScript functions. The return code values are represented by the [**IPrinterScriptUsbJobContextReturnCodes**](iprinterscriptusbjobcontextreturncodes.md) interface.

## Return value

This method returns an **HRESULT** value.

## Remarks

The IHV must develop an interface that implements a property bag associated with the current print job. The IHV JavaScript functions can then use this property bag to store properties or data that is specific to the print job that is currently being processed. This property bag exists for the duration of the current job only.

## Requirements

**Minimum supported client:** Windows 8.1

**Minimum supported server:** Windows Server 2012 R2

**Target platform:** Desktop

## See also

[**IPrinterScriptUsbJobContext**](iprinterscriptusbjobcontext.md)

[**IPrinterScriptUsbJobContextReturnCodes**](iprinterscriptusbjobcontextreturncodes.md)
