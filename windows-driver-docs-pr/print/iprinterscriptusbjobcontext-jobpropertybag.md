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
---

# IPrinterScriptUsbJobContext::JobPropertyBag method


Returns the property bag associated with the current print job.

Syntax
------

```ManagedCPlusPlus
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

## <span id="see_also"></span>See also


[**IPrinterScriptUsbJobContext**](iprinterscriptusbjobcontext.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20IPrinterScriptUsbJobContext::JobPropertyBag%20method%20%20RELEASE:%20%281/8/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





