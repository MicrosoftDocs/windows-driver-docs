---
title: IPrinterScriptUsbJobContext JobPropertyBag method
description: Returns the property bag associated with the current print job.
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 6309CCD2-D53A-4B21-970E-AF19D1DACEE3
keywords: ["JobPropertyBag method Print Devices", "JobPropertyBag method Print Devices , IPrinterScriptUsbJobContext interface", "IPrinterScriptUsbJobContext interface Print Devices , JobPropertyBag method"]
topic_type:
- apiref
api_name:
- IPrinterScriptUsbJobContext.JobPropertyBag
api_type:
- COM
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# IPrinterScriptUsbJobContext::JobPropertyBag method

Returns the property bag associated with the current print job.

Syntax
------

```cpp
HRESULT JobPropertyBag(
  [out, retval] IPrinterScriptablePropertyBag **ppPropertyBag
);
```

Parameters
----------

*ppPropertyBag* \[out, retval\]  
The property bag associated with the current print job.

Return value
------------

This method returns an **HRESULT** value.

Remarks
-------

**JobPropertyBag** is a read-only method. IHV JavaScript functions can use this property bag to store properties or data that is specific to the print job that is currently being processed. This property bag exists for the duration of the current job only.

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
