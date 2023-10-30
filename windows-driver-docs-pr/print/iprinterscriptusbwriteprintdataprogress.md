---
title: IPrinterScriptUsbWritePrintDataProgress interface
description: The IPrinterScriptUsbWritePrintDataProgress interface is passed as a parameter in the writePrintData JavaScript function call.
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
keywords: ["IPrinterScriptUsbWritePrintDataProgress interface Print Devices", "IPrinterScriptUsbWritePrintDataProgress interface Print Devices , described"]
topic_type:
- apiref
ms.topic: reference
api_name:
- IPrinterScriptUsbWritePrintDataProgress
api_type:
- COM
ms.date: 07/14/2023
---

# IPrinterScriptUsbWritePrintDataProgress interface

The IPrinterScriptUsbWritePrintDataProgress interface is passed as a parameter in the **writePrintData** JavaScript function call.

## Members

The **IPrinterScriptUsbWritePrintDataProgress** interface inherits from the [**IUnknown**](/windows/win32/api/unknwn/nn-unknwn-iunknown) interface. **IPrinterScriptUsbWritePrintDataProgress** also has these types of members:

- [Methods](#methods)

### Methods

The **IPrinterScriptUsbWritePrintDataProgress** interface has these methods:

| Method | Description |
|--|--|
| [**ProcessedByteCount** [out]](iprinterscriptusbwriteprintdataprogress-processedbytecount.md) | Returns the number of bytes that the IHV JavaScript function has processed by the time this method was called. |
| [**ProcessedByteCount** [in]](iprinterscriptusbwriteprintdataprogress-processedbytecount-in.md) | Sets the number of bytes that the IHV JavaScript function has processed at the time this method was called. |
