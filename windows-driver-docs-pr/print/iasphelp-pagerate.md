---
title: Iasphelp get\_PageRate method
description: The PageRate property enables an ASP Web page to determine a printer's page rate.
MS-HAID:
- 'webfnc\_f356953e-ac15-4948-9a6e-b83d3aec8e7b.xml'
- 'print.iasphelp\_pagerate'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 010f4871-f64f-465f-a78b-a86f91a9f194
keywords: ["get_PageRate method Print Devices", "get_PageRate method Print Devices , Iasphelp interface", "Iasphelp interface Print Devices , get_PageRate method"]
topic_type:
- apiref
api_name:
- Iasphelp.get_PageRate
api_type:
- COM
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Iasphelp::get\_PageRate method

The **PageRate** property enables an ASP Web page to determine a printer's page rate.

Syntax
------

```cpp
HRESULT get_PageRate(
  [out] long *pVal
);
```

Parameters
----------

*pVal* \[out\]  
A caller-supplied location to receive a numeric value that represents the page rate for the printer. The units in which the page rate is expressed might depend on the printer. For more information about page rates, see the following Remarks section.

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


To determine the units in which the page rate is measured, query the [**Iasphelp::PageRateUnit**](iasphelp-pagerateunit.md) property.

The [**Iasphelp::Open**](iasphelp-open.md) method must be called before the **Iasphelp::PageRate** property can be queried.

```vb
Dim objPrinter, PtrPageRate
strPrinter = Session("MS_printer")
Set objPrinter = Server.CreateObject ("OlePrn.AspHelp")
objPrinter.Open strPrinter
PtrPageRate = objPrinter.PageRate
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

[**Iasphelp::PageRateUnit**](iasphelp-pagerateunit.md)

[**Iasphelp::Open**](iasphelp-open.md)
