---
title: IPrinterScriptUsbJobContextReturnCodes Failure method
description: Returns a value of '1' to inform USBMon that the method call failed.
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: EEFDB8CA-5B6F-46E5-B181-074354E8B0EE
keywords: ["Failure method Print Devices", "Failure method Print Devices , IPrinterScriptUsbJobContextReturnCodes interface", "IPrinterScriptUsbJobContextReturnCodes interface Print Devices , Failure method"]
topic_type:
- apiref
api_name:
- IPrinterScriptUsbJobContextReturnCodes.Failure
api_type:
- COM
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# IPrinterScriptUsbJobContextReturnCodes::Failure method

Returns a value of '1' to inform USBMon that the method call failed.

Syntax
------

```cpp
HRESULT Failure(
  [out, retval] UINT32 *value
);
```

Parameters
----------

*value* \[out, retval\]  
Value that indicates a failed method call.

Return value
------------

This method returns an **HRESULT** value.

Remarks
-------

**Failure** is a read-only method. When USBMon receives this failure value, it cleans up the Job Context object and returns an error code to the print spooler.

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
