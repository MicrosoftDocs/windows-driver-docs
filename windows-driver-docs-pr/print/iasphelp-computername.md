---
title: Iasphelp get\_ComputerName method
description: The ComputerName property enables an ASP Web page to obtain a print server's name.
MS-HAID:
- 'webfnc\_fd5c59b9-c223-4762-898d-693e9960619c.xml'
- 'print.iasphelp\_computername'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 20fbd286-5b09-4c30-ae6c-4245854bc7b3
keywords: ["get_ComputerName method Print Devices", "get_ComputerName method Print Devices , Iasphelp interface", "Iasphelp interface Print Devices , get_ComputerName method"]
topic_type:
- apiref
api_name:
- Iasphelp.get_ComputerName
api_type:
- COM
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Iasphelp::get\_ComputerName method

The **ComputerName** property enables an ASP Web page to obtain a print server's name.

Syntax
------

```cpp
HRESULT get_ComputerName(
  [out] BSTR *pVal
);
```

Parameters
----------

*pVal* \[out\]  
Caller-supplied pointer to a location to receive a pointer to a computer name string.

Return value
------------

This method can return one of these values.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Return code</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>S_OK</strong></td>
<td><p>The operation succeeded.</p></td>
</tr>
<tr class="even">
<td><strong>E_OUTOFMEMORY</strong></td>
<td><p>Out of memory.</p></td>
</tr>
</tbody>
</table>

## VBScript Example

```vb
Dim objPrinter, CompName
strPrinter = Session("MS_printer")
Set objPrinter = Server.CreateObject ("OlePrn.AspHelp")
CompName = objPrinter.ComputerName
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
