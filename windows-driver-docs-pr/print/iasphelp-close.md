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
ms.localizationpriority: medium
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

 

 




