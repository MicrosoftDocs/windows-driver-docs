---
title: Iasphelp get\_JobCompletionMinute method
description: The JobCompletionMinute property enables an ASP Web page to determine when the print jobs that are currently pending will be finished.
MS-HAID:
- 'webfnc\_63bca3eb-0ead-4430-8e82-9014d58c133b.xml'
- 'print.iasphelp\_jobcompletionminute'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: e3dba870-84b4-4959-8ed4-102ac82be14b
keywords: ["get_JobCompletionMinute method Print Devices", "get_JobCompletionMinute method Print Devices , Iasphelp interface", "Iasphelp interface Print Devices , get_JobCompletionMinute method"]
topic_type:
- apiref
api_name:
- Iasphelp.get_JobCompletionMinute
api_type:
- COM
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Iasphelp::get\_JobCompletionMinute method

The **JobCompletionMinute** property enables an ASP Web page to determine when the print jobs that are currently pending will be finished.

Syntax
------

```cpp
HRESULT get_JobCompletionMinute(
  [out] long *pVal
);
```

Parameters
----------

*pVal* \[out\]  
A caller-supplied pointer to a memory location that receives the required time, in minutes, for all print jobs that are currently pending completion.

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

Before you query this property, call the [**Iasphelp::CalcJobETA**](iasphelp-calcjobeta.md) method to initialize the property value. To determine the number of pending print jobs, query the [**Iasphelp::PendingJobCount**](iasphelp-pendingjobcount.md) property.

```vb
Dim objPrinter, EndMinute
strPrinter = Session("MS_printer")
Set objPrinter = Server.CreateObject ("OlePrn.AspHelp")
objPrinter.Open strPrinter
objPrinter.CalcJobETA
EndMinute = objPrinter.JobCompletionMinute
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

[**Iasphelp::PendingJobCount**](iasphelp-pendingjobcount.md)
