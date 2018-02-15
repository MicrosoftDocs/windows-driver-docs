---
title: IPrinterScriptUsbJobContextReturnCodes Retry method
author: windows-driver-content
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
---

# IPrinterScriptUsbJobContextReturnCodes::Retry method


Returns a value of '2' to inform USBMon that the method call was successful, with more work to be completed.

Syntax
------

```ManagedCPlusPlus
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

## <span id="see_also"></span>See also


[**IPrinterScriptUsbJobContextReturnCodes**](iprinterscriptusbjobcontextreturncodes.md)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20IPrinterScriptUsbJobContextReturnCodes::Retry%20method%20%20RELEASE:%20%281/8/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


