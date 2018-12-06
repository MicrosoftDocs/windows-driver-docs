---
title: Iasphelp Close method
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
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Iasphelp::Close method


The **Close** method enables an ASP Web page to close access to a printer.

Syntax
------

```cpp
HRESULT Close();
```

Parameters
----------

This method has no parameters.

Return value
------------

The return value is always S\_OK.


## VBScript Example

The name of the printer being closed must have been specified in a previous call to the [**Iasphelp::Open**](iasphelp-open.md) method.

```vb
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
</tbody>
</table>

## See also

[**Iasphelp::Open**](iasphelp-open.md)
