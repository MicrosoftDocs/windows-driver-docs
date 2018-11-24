---
title: IPrinterScriptUsbJobContextReturnCodes Retry method
description: Returns a value of '2' to inform USBMon that the method call was successful, with more work to be completed.
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 1EDF5EFA-1158-4BC7-99AB-3811E4443E62
keywords: ["Retry method Print Devices", "Retry method Print Devices , IPrinterScriptUsbJobContextReturnCodes interface", "IPrinterScriptUsbJobContextReturnCodes interface Print Devices , Retry method"]
topic_type:
- apiref
api_name:
- IPrinterScriptUsbJobContextReturnCodes.Retry
api_type:
- COM
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# IPrinterScriptUsbJobContextReturnCodes::Retry method

Returns a value of '2' to inform USBMon that the method call was successful, with more work to be completed.

Syntax
------

```cpp
HRESULT Retry(
  [out, retval] UINT32 *value
);
```

Parameters
----------

*value* \[out, retval\]  
Value indicating a successful method call, with more work to be done.

Return value
------------

This method returns an **HRESULT** value.

Remarks
-------

**Retry** is a read-only method. USBMon should process any Bidi Schema updates (including Bidi Events) in a printerBidiSchemaResponses object, and then call the **Retry** method again to allow the IHV code to continue processing the data. The number of bytes processed from the print data stream (printData) is returned in the writePrintDataProgress object associated with the print job.

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
