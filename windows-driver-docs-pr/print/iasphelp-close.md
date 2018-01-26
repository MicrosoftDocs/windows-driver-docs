---
title: Iasphelp Close method
author: windows-driver-content
description: The Close method enables an ASP Web page to close access to a printer.
MS-HAID:
- 'webfnc\_62b91ac5-2f01-44d6-9289-ee2136acacc4.xml'
- 'print.iasphelp\_close'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 45457eb9-a791-450f-b3fd-f4e7dabc7a70
keywords: ["Close method Print Devices", "Close method Print Devices , Iasphelp interface", "Iasphelp interface Print Devices , Close method"]
topic_type:
- apiref
api_name:
- Iasphelp.Close
api_type:
- COM
---

# Iasphelp::Close method


The **Close** method enables an ASP Web page to close access to a printer.

Syntax
------

```ManagedCPlusPlus
HRESULT Close();
```

Parameters
----------

This method has no parameters.

Return value
------------

The return value is always S\_OK.

## <span id="ddk_iasphelp_close_gg"></span><span id="DDK_IASPHELP_CLOSE_GG"></span>


### <span id="vbscript_example"></span><span id="VBSCRIPT_EXAMPLE"></span>VBScript Example

Remarks
-------

The name of the printer being closed must have been specified in a previous call to the [**Iasphelp::Open**](iasphelp-open.md) method.

```
    Dim objPrinter
    strPrinter = Session("MS_printer")
    Set objPrinter = Server.CreateObject ("OlePrn.AspHelp")
    objPrinter.Open strPrinter
    ...
    objPrinter.Close
```

Requirements
------------

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Target platform</p></td>
<td>Desktop</td>
</tr>
<tr class="even">
<td><p>Version</p></td>
<td><p>Available in Windows 2000 and later versions of the Windows operating systems.</p></td>
</tr>
</tbody>
</table>

## <span id="see_also"></span>See also


[**Iasphelp::Open**](iasphelp-open.md)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Iasphelp::Close%20method%20%20RELEASE:%20%281/8/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


