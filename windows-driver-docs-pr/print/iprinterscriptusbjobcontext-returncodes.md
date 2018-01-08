---
title: IPrinterScriptUsbJobContext ReturnCodes method
author: windows-driver-content
description: Returns an object that can supply return code values that an IHV has defined for their JavaScript functions.
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 0FD3A103-970E-4EB8-9867-7EC21273269C
keywords: ["ReturnCodes method Print Devices", "ReturnCodes method Print Devices , IPrinterScriptUsbJobContext interface", "IPrinterScriptUsbJobContext interface Print Devices , ReturnCodes method"]
topic_type:
- apiref
api_name:
- IPrinterScriptUsbJobContext.ReturnCodes
api_type:
- COM
---

# IPrinterScriptUsbJobContext::ReturnCodes method


Returns an object that can supply return code values that an IHV has defined for their JavaScript functions.

Syntax
------

```ManagedCPlusPlus
HRESULT ReturnCodes(
  [out, retval] IPrinterScriptUsbJobContextReturnCodes **ppReturnCodes
);
```

Parameters
----------

*ppReturnCodes* \[out, retval\]  
The return code values for the IHV JavaScript functions. The return code values are represented by the [**IPrinterScriptUsbJobContextReturnCodes**](iprinterscriptusbjobcontextreturncodes.md) interface.

Return value
------------

This method returns an **HRESULT** value.

Remarks
-------

The IHV must develop an interface that implements a property bag associated with the current print job. The IHV JavaScript functions can then use this property bag to store properties or data that is specific to the print job that is currently being processed. This property bag exists for the duration of the current job only.

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

[**IPrinterScriptUsbJobContextReturnCodes**](iprinterscriptusbjobcontextreturncodes.md)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20IPrinterScriptUsbJobContext::ReturnCodes%20method%20%20RELEASE:%20%281/8/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


