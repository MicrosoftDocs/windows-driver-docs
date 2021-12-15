---
title: IPrinterScriptUsbJobContext PrintedPageCount method (in)
description: Sets the number of pages that have been printed by the print device in the current job.
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
keywords: ["PrintedPageCount method Print Devices", "PrintedPageCount method Print Devices , IPrinterScriptUsbJobContext interface", "IPrinterScriptUsbJobContext interface Print Devices , PrintedPageCount method"]
topic_type:
- apiref
api_name:
- IPrinterScriptUsbJobContext.PrintedPageCount
api_type:
- COM
ms.date: 07/07/2020
---

# IPrinterScriptUsbJobContext::PrintedPageCount method (in)

Sets the number of pages that have been printed by the print device in the current job.

## Syntax

```cpp
HRESULT PrintedPageCount(
  [in] UINT32 value
);
```

## Parameters

*value* \[in\]  
The number of pages that have been printed by the print device in the current job.

## Return value

This method returns an **HRESULT** value.

## Remarks

**PrintedPageCount** is a read/write method. The IHV JavaScript **writeData** function should keep the printed page count up to date to allow USBMon to set the correct progress on the job.

If the IHV JavaScript code never calls **PrintedPageCount** to set the printed page count, it is assumed that an accurate count of the pages is not possible and USBMon will allow the spooler to continue estimating progress.

For information about USBMon and USB-based bidirectional communication with a print device, see [USB Bidi Extender](./usb-bidi-extender.md).

## Requirements

**Minimum supported client:** Windows 8.1

**Minimum supported server:** Windows Server 2012 R2

**Target platform:** Desktop

## See also

[**IPrinterScriptUsbJobContext**](iprinterscriptusbjobcontext.md)

[USB Bidi Extender](./usb-bidi-extender.md)
