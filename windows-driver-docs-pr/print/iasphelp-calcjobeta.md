---
title: Iasphelp CalcJobETA method
description: The CalcJobETA method enables an ASP Web page to calculate the time at which a print job is to be completed.
MS-HAID:
- 'webfnc\_65577773-9d44-429e-a2fe-eb1a1475b7f6.xml'
- 'print.iasphelp\_calcjobeta'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: cdf4d590-c236-4ed7-a071-fd0ddbb78590
keywords: ["CalcJobETA method Print Devices", "CalcJobETA method Print Devices , Iasphelp interface", "Iasphelp interface Print Devices , CalcJobETA method"]
topic_type:
- apiref
api_name:
- Iasphelp.CalcJobETA
api_type:
- COM
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Iasphelp::CalcJobETA method

The **CalcJobETA** method enables an ASP Web page to calculate the time at which a print job is to be completed.

Syntax
------

```cpp
HRESULT CalcJobETA();
```

Parameters
----------

This method has no parameters.

Return value
------------

The following table shows possible return values for this method.

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
<td><p>The method succeeded.</p></td>
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

The **CalcJobETA** method calculates print job information that can be subsequently retrieved by using Iasphelp properties. Call **CalcJobETA** before getting any of the following properties:

[**Iasphelp::JobCompletionMinute**](iasphelp-jobcompletionminute.md)

[**Iasphelp::PendingJobCount**](iasphelp-pendingjobcount.md)

[**Iasphelp::AvgJobSize**](iasphelp-avgjobsize.md)

[**Iasphelp::AvgJobSizeUnit**](iasphelp-avgjobsizeunit.md)

Before **CalcJobETA** is called, the value of any of these properties is zero. If **CalcJobETA** determines that the printer rate is not available for the current printer, a subsequent call to JobCompletionMinute retrieves the value -1.

The [**Iasphelp::Open**](iasphelp-open.md) method must be called before the **CalcJobETA** method can be called.

```vb
Dim objPrinter
strPrinter = Session("MS_printer")
Set objPrinter = Server.CreateObject ("OlePrn.AspHelp")
objPrinter.Open strPrinter
objPrinter.CalcJobETA
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

[**Iasphelp::JobCompletionMinute**](iasphelp-jobcompletionminute.md)

[**Iasphelp::PendingJobCount**](iasphelp-pendingjobcount.md)

[**Iasphelp::AvgJobSize**](iasphelp-avgjobsize.md)

[**Iasphelp::AvgJobSizeUnit**](iasphelp-avgjobsizeunit.md)

[**Iasphelp::Open**](iasphelp-open.md)
