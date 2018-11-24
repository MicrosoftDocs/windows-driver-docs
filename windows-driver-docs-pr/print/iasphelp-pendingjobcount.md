---
title: Iasphelp get\_PendingJobCount method
description: The PendingJobCount property enables an ASP Web page to determine the number of pending print jobs.
MS-HAID:
- 'webfnc\_fd1cbaac-f195-4a38-8788-990eb9b3fd6c.xml'
- 'print.iasphelp\_pendingjobcount'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: e0d00abd-0b2a-403c-a7b2-f1f2587b977f
keywords: ["get_PendingJobCount method Print Devices", "get_PendingJobCount method Print Devices , Iasphelp interface", "Iasphelp interface Print Devices , get_PendingJobCount method"]
topic_type:
- apiref
api_name:
- Iasphelp.get_PendingJobCount
api_type:
- COM
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Iasphelp::get\_PendingJobCount method

The **PendingJobCount** property enables an ASP Web page to determine the number of pending print jobs.

Syntax
------

```cpp
HRESULT get_PendingJobCount(
  [out] long *pVal
);
```

Parameters
----------

*pVal* \[out\]  
A caller-supplied pointer to a memory location that receives the number of pending print jobs.

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

Before you query this property, call the [**Iasphelp::CalcJobETA**](iasphelp-calcjobeta.md) method to initialize the property value.

```vb
Dim objPrinter
strPrinter = Session("MS_printer")
Set objPrinter = Server.CreateObject ("OlePrn.AspHelp")
objPrinter.Open strPrinter
objPrinter.CalcJobETA
PendingJobs = objPrinter.PendingJobCount
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

[**Iasphelp::CalcJobETA**](iasphelp-calcjobeta.md)
