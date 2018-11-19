---
title: Iasphelp get\_AvgJobSizeUnit method
description: The AvgJobSizeUnit property enables an ASP Web page to determine the units of the average job size.
MS-HAID:
- 'webfnc\_b7542526-ad13-46d7-a1c1-e02d7832dfb6.xml'
- 'print.iasphelp\_avgjobsizeunit'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: f5a701ff-270f-45f5-8c6e-ecf1b8afab20
keywords: ["get_AvgJobSizeUnit method Print Devices", "get_AvgJobSizeUnit method Print Devices , Iasphelp interface", "Iasphelp interface Print Devices , get_AvgJobSizeUnit method"]
topic_type:
- apiref
api_name:
- Iasphelp.get_AvgJobSizeUnit
api_type:
- COM
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Iasphelp::get\_AvgJobSizeUnit method


The **AvgJobSizeUnit** property enables an ASP Web page to determine the units of the average job size.

Syntax
------

```cpp
HRESULT get_AvgJobSizeUnit(
  [out] long *pVal
);
```

Parameters
----------

*pVal* \[out\]  
A caller-supplied pointer to a memory location that receives one of the values in the following table. The value indicates the units that are associated with the average job size.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Value</th>
<th>Meaning</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>1</p></td>
<td><p>Units of average job size are in pages per job.</p></td>
</tr>
<tr class="even">
<td><p>2</p></td>
<td><p>Units of average job size are in bytes per job.</p></td>
</tr>
</tbody>
</table>

 

Return value
------------

This method returns S\_OK on success.

## VBScript Example

Query the **Iasphelp::AvgJobSizeUnit** property to determine the units in which the [**Iasphelp::AvgJobSize**](iasphelp-avgjobsize.md) property value is expressed.

Before you query this property, call the [**Iasphelp::CalcJobETA**](iasphelp-calcjobeta.md) method to initialize the property value.

```vb
Dim objPrinter, strPrinter, JobUnits
strPrinter = Session("MS_printer")
Set objPrinter = Server.CreateObject ("OlePrn.AspHelp")
objPrinter.Open strPrinter
objPrinter.CalcJobETA
JobUnits = objPrinter.AvgJobSizeUnit
' If JobUnits = 1 then job size is in units of pages
' If JobUnits = 2 then job size is in units of bytes
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

[**Iasphelp::AvgJobSize**](iasphelp-avgjobsize.md)

[**Iasphelp::CalcJobETA**](iasphelp-calcjobeta.md)
