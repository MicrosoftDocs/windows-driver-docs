---
title: IPrinterScriptUsbJobContext TemporaryStreams method
description: Returns an array of IPrinterScriptableSequentialStream interfaces for the persistent data streams used by the IHV JavaScript functions for the current job.
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
keywords: ["TemporaryStreams method Print Devices", "TemporaryStreams method Print Devices , IPrinterScriptUsbJobContext interface", "IPrinterScriptUsbJobContext interface Print Devices , TemporaryStreams method"]
topic_type:
- apiref
ms.topic: reference
api_name:
- IPrinterScriptUsbJobContext.TemporaryStreams
api_type:
- COM
ms.date: 07/13/2023
---

# IPrinterScriptUsbJobContext::TemporaryStreams method

Returns an array of [IPrinterScriptableSequentialStream](/windows-hardware/drivers/ddi/printerextension/nn-printerextension-iprinterscriptablesequentialstream) interfaces for the persistent data streams used by the IHV JavaScript functions for the current job.

## Syntax

```cpp
HRESULT TemporaryStreams(
  [out, retval] IDispatch **ppArray
);
```

## Parameters

*ppArray* \[out, retval\]  
Pointer to an array of [IPrinterScriptableSequentialStream](/windows-hardware/drivers/ddi/printerextension/nn-printerextension-iprinterscriptablesequentialstream) interfaces.

## Return value

This method returns an **HRESULT** value.

## Remarks

**TemporaryStreams** is a read-only method. There are a maximum of two temporary streams available to the IHV JavaScript functions. These streams are only available for the duration of the current print job. The IHV can use this to store data that isn't yet ready to be sent to the print device. On a later **writePrintData** JavaScript function call, these streams can be used to send the stored data to the print device.

## Requirements

**Minimum supported client:** Windows 8.1

**Minimum supported server:** Windows Server 2012 R2

**Target platform:** Desktop

## See also

[**IPrinterScriptUsbJobContext**](iprinterscriptusbjobcontext.md)

[IPrinterScriptableSequentialStream](/windows-hardware/drivers/ddi/printerextension/nn-printerextension-iprinterscriptablesequentialstream)
