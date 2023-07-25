---
title: IPrinterScriptUsbJobContextReturnCodes interface
description: The IPrinterScriptUsbJobContextReturnCodes interface represents an array of return codes that an IHV has defined for their JavaScript functions.
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
keywords: ["IPrinterScriptUsbJobContextReturnCodes interface Print Devices", "IPrinterScriptUsbJobContextReturnCodes interface Print Devices , described"]
topic_type:
- apiref
ms.topic: reference
api_name:
- IPrinterScriptUsbJobContextReturnCodes
api_type:
- COM
ms.date: 07/14/2023
---

# IPrinterScriptUsbJobContextReturnCodes interface

The IPrinterScriptUsbJobContextReturnCodes interface represents an array of return codes that an IHV has defined for their JavaScript functions.

This interface is returned by the [**IPrinterScriptUsbJobContext::ReturnCodes**](iprinterscriptusbjobcontext-returncodes.md) method.

## Members

The **IPrinterScriptUsbJobContextReturnCodes** interface inherits from the [**IUnknown**](/windows/win32/api/unknwn/nn-unknwn-iunknown) interface. **IPrinterScriptUsbJobContextReturnCodes** also has these types of members:

- [Methods](#methods)

### Methods

The **IPrinterScriptUsbJobContextReturnCodes** interface has these methods:

| Method | Description |
|--|--|
| [**AbortTheJob**](iprinterscriptusbjobcontextreturncodes-abortthejob.md) | Returns a value of '4' to inform USBMon that the print job must be aborted. |
| [**DeviceBusy**](iprinterscriptusbjobcontextreturncodes-devicebusy.md) | Returns a value of '3' to inform USBMon that the device communication channel is not accepting data at this time. |
| [**Failure**](iprinterscriptusbjobcontextreturncodes-failure.md) | Returns a value of '1' to inform USBMon that the method call failed. |
| [**Retry**](iprinterscriptusbjobcontextreturncodes-retry.md) | Returns a value of '2' to inform USBMon that the method call was successful, with more work to be completed. |
| [**Success**](iprinterscriptusbjobcontextreturncodes-success.md) | Returns a value of zero (0) to inform USBMon that the function call completed successfully. |

## Requirements

**Minimum supported client:** Windows 8.1

**Minimum supported server:** Windows Server 2012 R2
