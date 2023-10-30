---
title: IPrinterScriptUsbJobContext JobPropertyBag method
description: Returns the property bag associated with the current print job.
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
keywords: ["JobPropertyBag method Print Devices", "JobPropertyBag method Print Devices , IPrinterScriptUsbJobContext interface", "IPrinterScriptUsbJobContext interface Print Devices , JobPropertyBag method"]
topic_type:
- apiref
ms.topic: reference
api_name:
- IPrinterScriptUsbJobContext.JobPropertyBag
api_type:
- COM
ms.date: 07/13/2023
---

# IPrinterScriptUsbJobContext::JobPropertyBag method

Returns the property bag associated with the current print job.

## Syntax

```cpp
HRESULT JobPropertyBag(
  [out, retval] IPrinterScriptablePropertyBag **ppPropertyBag
);
```

## Parameters

*ppPropertyBag* \[out, retval\]  
The property bag associated with the current print job.

## Return value

This method returns an **HRESULT** value.

## Remarks

**JobPropertyBag** is a read-only method. IHV JavaScript functions can use this property bag to store properties or data that is specific to the print job that is currently being processed. This property bag exists for the duration of the current job only.

## Requirements

**Minimum supported client:** Windows 8.1

**Minimum supported server:** Windows Server 2012 R2

**Target platform:** Desktop

## See also

[**IPrinterScriptUsbJobContext**](iprinterscriptusbjobcontext.md)
