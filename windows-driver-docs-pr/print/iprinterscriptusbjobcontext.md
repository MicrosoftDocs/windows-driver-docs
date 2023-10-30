---
title: IPrinterScriptUsbJobContext interface
description: The IPrinterScriptUsbJobContext interface is passed as a parameter to the startPrintJob JavaScript function.
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
keywords: ["IPrinterScriptUsbJobContext interface Print Devices", "IPrinterScriptUsbJobContext interface Print Devices , described"]
topic_type:
- apiref
ms.topic: reference
api_name:
- IPrinterScriptUsbJobContext
api_type:
- COM
ms.date: 07/13/2023
---

# IPrinterScriptUsbJobContext interface

The IPrinterScriptUsbJobContext interface is passed as a parameter to the **startPrintJob** JavaScript function.

## Members

The **IPrinterScriptUsbJobContext** interface inherits from the [**IUnknown**](/windows/win32/api/unknwn/nn-unknwn-iunknown) interface. **IPrinterScriptUsbJobContext** also has these types of members:

- [Methods](#methods)

### Methods

The **IPrinterScriptUsbJobContext** interface has these methods:

| Method | Description |
|--|--|
| [**JobPropertyBag**](iprinterscriptusbjobcontext-jobpropertybag.md) | Returns the property bag associated with the current print job. |
| [**PrintedPageCount**](iprinterscriptusbjobcontext-printedpagecount.md) | Returns the number of pages that have been printed by the print device in the current job. |
| [**PrintedPageCount**](iprinterscriptusbjobcontext-printedpagecount-in.md) | Sets the number of pages that have been printed by the print device in the current job. |
| [**ReturnCodes**](iprinterscriptusbjobcontext-returncodes.md) | Returns an object that can supply return code values that an IHV has defined for their JavaScript functions. |
| [**TemporaryStreams**](iprinterscriptusbjobcontext-temporarystreams.md) | Returns an array of [IPrinterScriptableSequentialStream](/windows-hardware/drivers/ddi/printerextension/nn-printerextension-iprinterscriptablesequentialstream) interfaces for the persistent data streams that can be used by the IHV JavaScript functions for the current job. |

## Requirements

**Minimum supported client:** Windows 8.1

**Minimum supported server:** Windows Server 2012 R2
