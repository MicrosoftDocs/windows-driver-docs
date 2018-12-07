---
title: IPrinterScriptUsbJobContextReturnCodes DeviceBusy method
description: Returns a value of '3' to inform USBMon that the device communication channel is not accepting data at this time.
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: D1205445-2587-4C9D-B383-587F06A3E899
keywords: ["DeviceBusy method Print Devices", "DeviceBusy method Print Devices , IPrinterScriptUsbJobContextReturnCodes interface", "IPrinterScriptUsbJobContextReturnCodes interface Print Devices , DeviceBusy method"]
topic_type:
- apiref
api_name:
- IPrinterScriptUsbJobContextReturnCodes.DeviceBusy
api_type:
- COM
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# IPrinterScriptUsbJobContextReturnCodes::DeviceBusy method

Returns a value of '3' to inform USBMon that the device communication channel is not accepting data at this time.

Syntax
------

```cpp
HRESULT DeviceBusy(
  [out, retval] UINT32 *value
);
```

Parameters
----------

*value* \[out, retval\]  
Value that indicates that the communication channel is not accepting data at this time.

Return value
------------

This method returns an **HRESULT** value.

Remarks
-------

**DeviceBusy** is a read-only method. A returned value of '3' does not indicate a failure, and USBMon should inform the print spooler that the device is busy. USBMon can then call the function again at a later time. The number of bytes processed from the print data stream (printData) is returned in the writePrintDataProgress object.

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
