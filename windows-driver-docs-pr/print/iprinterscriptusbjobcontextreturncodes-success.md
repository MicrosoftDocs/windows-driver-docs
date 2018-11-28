---
title: IPrinterScriptUsbJobContextReturnCodes Success method
description: Returns a value of zero (0) to inform USBMon that the function call completed successfully.
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 783F9BCA-468E-4505-A6F3-9592D400E62C
keywords: ["Success method Print Devices", "Success method Print Devices , IPrinterScriptUsbJobContextReturnCodes interface", "IPrinterScriptUsbJobContextReturnCodes interface Print Devices , Success method"]
topic_type:
- apiref
api_name:
- IPrinterScriptUsbJobContextReturnCodes.Success
api_type:
- COM
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# IPrinterScriptUsbJobContextReturnCodes::Success method

Returns a value of zero (0) to inform USBMon that the function call completed successfully.

Syntax
------

```cpp
HRESULT Success(
  [out, retval] UINT32 *value
);
```

Parameters
----------

*value* \[out, retval\]  
Value indicating a successful method call.

Return value
------------

This method returns an **HRESULT** value.

Remarks
-------

**Success** is a read-only method.

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
