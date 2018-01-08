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
---

# IPrinterScriptUsbJobContext::PrintedPageCount method


Returns the number of pages that have been printed by the print device in the current job.

Syntax
------

```ManagedCPlusPlus
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

For information about USBMon and USB-based bidirectional communication with a print device, see [USB Bidi Extender](https://msdn.microsoft.com/library/windows/hardware/jj659903).

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

## <span id="see_also"></span>See also


[**IPrinterScriptUsbJobContext**](iprinterscriptusbjobcontext.md)

[USB Bidi Extender](https://msdn.microsoft.com/library/windows/hardware/jj659903)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20IPrinterScriptUsbJobContext::PrintedPageCount%20method%20%20RELEASE:%20%281/8/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





