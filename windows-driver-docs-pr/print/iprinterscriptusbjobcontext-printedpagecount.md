---
title: IPrinterScriptUsbJobContext PrintedPageCount method
description: Returns the number of pages that have been printed by the print device in the current job.
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 5933D374-D134-4731-994A-B16027225CA3
keywords: ["PrintedPageCount method Print Devices", "PrintedPageCount method Print Devices , IPrinterScriptUsbJobContext interface", "IPrinterScriptUsbJobContext interface Print Devices , PrintedPageCount method"]
topic_type:
- apiref
api_name:
- IPrinterScriptUsbJobContext.PrintedPageCount
api_type:
- COM
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# IPrinterScriptUsbJobContext::PrintedPageCount method

Returns the number of pages that have been printed by the print device in the current job.

Syntax
------

```cpp
HRESULT PrintedPageCount(
  [out, retval] UINT32 *value
);
```

Parameters
----------

*value* \[out, retval\]  
The number of pages that have been printed by the print device in the current job.

Return value
------------

This method returns an **HRESULT** value.

Remarks
-------

**PrintedPageCount** is a read/write method. The IHV JavaScript **writeData** function should keep the printed page count up to date to allow USBMon to set the correct progress on the job.

If the IHV JavaScript code never calls **PrintedPageCount** to set the printed page count, it is assumed that an accurate count of the pages is not possible and USBMon will allow the spooler to continue estimating progress.

For information about USBMon and USB-based bidirectional communication with a print device, see [USB Bidi Extender](https://docs.microsoft.com/windows-hardware/drivers/print/usb-bidi-extender).

Requirements
------------

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Minimum supported client</p></td>
<td><p>Windows 8.1</p></td>
</tr>
<tr class="even">
<td><p>Minimum supported server</p></td>
<td><p>Windows Server 2012 R2</p></td>
</tr>
<tr class="odd">
<td><p>Target platform</p></td>
<td>Desktop</td>
</tr>
</tbody>
</table>

## See also

[**IPrinterScriptUsbJobContext**](iprinterscriptusbjobcontext.md)

[USB Bidi Extender](https://docs.microsoft.com/windows-hardware/drivers/print/usb-bidi-extender)
