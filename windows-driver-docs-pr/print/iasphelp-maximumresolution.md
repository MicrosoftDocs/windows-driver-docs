---
title: Iasphelp get\_MaximumResolution method
description: The MaximumResolution property enables an ASP Web page to determine a printer's maximum resolution.
MS-HAID:
- 'webfnc\_156e8337-489a-44e6-9c81-0a8f6dd3aa08.xml'
- 'print.iasphelp\_maximumresolution'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 74dffe85-0e6d-4c2c-a933-2afb68624c76
keywords: ["get_MaximumResolution method Print Devices", "get_MaximumResolution method Print Devices , Iasphelp interface", "Iasphelp interface Print Devices , get_MaximumResolution method"]
topic_type:
- apiref
api_name:
- Iasphelp.get_MaximumResolution
api_type:
- COM
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Iasphelp::get\_MaximumResolution method

The **MaximumResolution** property enables an ASP Web page to determine a printer's maximum resolution.

Syntax
------

```cpp
HRESULT get_MaximumResolution(
  [out] long *pVal
);
```

Parameters
----------

*pVal* \[out\]  
Caller-supplied location to receive a numeric value representing the printer's maximum resolution, in dots per inch.

Return value
------------

This property returns one of the values in the following table.

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
<td><p>The <a href="iasphelp-open.md" data-raw-source="[&lt;strong&gt;Iasphelp::Open&lt;/strong&gt;](iasphelp-open.md)"><strong>Iasphelp::Open</strong></a> method has not been called.</p></td>
</tr>
<tr class="odd">
<td><strong>E_OUTOFMEMORY</strong></td>
<td><p>Out of memory.</p></td>
</tr>
</tbody>
</table>

## VBScript Example

The [**Iasphelp::Open**](iasphelp-open.md) method must be called before the **Iasphelp::MaximumResolution** property can be queried.

```vb
Dim objPrinter, MaxRes
strPrinter = Session("MS_printer")
Set objPrinter = Server.CreateObject ("OlePrn.AspHelp")
objPrinter.Open strPrinter
MaxRes = objPrinter.MaximumResolution
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
