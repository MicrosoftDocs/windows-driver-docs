---
title: IPrinterScriptUsbJobContextReturnCodes AbortTheJob method
description: Returns a value of '4' to inform USBMon that the print job must be aborted.
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 6E56330E-BDD9-4EDC-A006-CA1D8A58DE32
keywords: ["AbortTheJob method Print Devices", "AbortTheJob method Print Devices , IPrinterScriptUsbJobContextReturnCodes interface", "IPrinterScriptUsbJobContextReturnCodes interface Print Devices , AbortTheJob method"]
topic_type:
- apiref
api_name:
- IPrinterScriptUsbJobContextReturnCodes.AbortTheJob
api_type:
- COM
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# IPrinterScriptUsbJobContextReturnCodes::AbortTheJob method

Returns a value of '4' to inform USBMon that the print job must be aborted.

Syntax
------

```cpp
HRESULT AbortTheJob(
  [out, retval] UINT32 *value
);
```

Parameters
----------

*value* \[out, retval\]  
Value that indicates that the print job must be aborted.

Return value
------------

This method returns an **HRESULT** value.

Remarks
-------

**AbortTheJob** is a read-only method. This return code from the IHV JavaScript function informs USBMon that either the device couldn't continue processing the job, or the user canceled the job at the front panel of the device. When USBMon receives the message to abort a print job, it passes the information to the print spooler to abort the job, before returning.

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

[**IPrinterScriptUsbJobContextReturnCodes**](iprinterscriptusbjobcontextreturncodes.md)
