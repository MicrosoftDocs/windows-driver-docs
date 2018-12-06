---
title: Iasphelp get\_Duplex method
description: The Duplex property enables an ASP Web page to determine if a printer supports duplex printing.
MS-HAID:
- 'webfnc\_346f6357-9ca9-4b97-93a3-50ec9f28c118.xml'
- 'print.iasphelp\_duplex'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: e837f8f2-68a5-4f9a-a253-dfcf33ea7047
keywords: ["get_Duplex method Print Devices", "get_Duplex method Print Devices , Iasphelp interface", "Iasphelp interface Print Devices , get_Duplex method"]
topic_type:
- apiref
api_name:
- Iasphelp.get_Duplex
api_type:
- COM
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Iasphelp::get\_Duplex method

The **Duplex** property enables an ASP Web page to determine if a printer supports duplex printing.

Syntax
------

```cpp
HRESULT get_Duplex(
  [out] BOOL *pVal
);
```

Parameters
----------

*pVal* \[out\]  
Caller-supplied pointer to a location to receive **TRUE** if the printer supports duplex printing, or **FALSE** if it does not.

Return value
------------

Win32 error codes can also be returned.

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
<td><strong>E_HANDLE</strong></td>
<td><p>The <strong>Iasphelp::Open</strong> method has not been called.</p></td>
</tr>
<tr class="odd">
<td><strong>E_OUTOFMEMORY</strong></td>
<td><p>Out of memory.</p></td>
</tr>
</tbody>
</table>

## VBScript Example

The [**Iasphelp::Open**](iasphelp-open.md) method must be called before the **Iasphelp::Duplex** property can be queried.

```vb
Dim objPrinter, DoesDuplex
strPrinter = Session("MS_printer")
Set objPrinter = Server.CreateObject ("OlePrn.AspHelp")
objPrinter.Open strPrinter
DoesDuplex = objPrinter.Duplex
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
