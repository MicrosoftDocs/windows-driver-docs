---
title: Iasphelp get_AvgJobSizeUnit method
description: The AvgJobSizeUnit property enables an ASP Web page to determine the units of the average job size.
MS-HAID:
- 'webfnc_b7542526-ad13-46d7-a1c1-e02d7832dfb6.xml'
- 'print.iasphelp_avgjobsizeunit'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
keywords: ["get_AvgJobSizeUnit method Print Devices", "get_AvgJobSizeUnit method Print Devices , Iasphelp interface", "Iasphelp interface Print Devices , get_AvgJobSizeUnit method"]
topic_type:
- apiref
ms.topic: reference
api_name:
- Iasphelp.get_AvgJobSizeUnit
api_type:
- COM
ms.date: 06/23/2023
---

# Iasphelp::get_AvgJobSizeUnit method

The **AvgJobSizeUnit** property enables an ASP Web page to determine the units of the average job size.

## Syntax

```cpp
HRESULT get_AvgJobSizeUnit(
  [out] long *pVal
);
```

## Parameters

*pVal* \[out\]  
A caller-supplied pointer to a memory location that receives one of the values in the following table. The value indicates the units that are associated with the average job size.

| Value | Meaning |
|--|--|
| 1 | Units of average job size are in pages per job. |
| 2 | Units of average job size are in bytes per job. |

## Return value

This method returns S_OK on success.

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

## Requirements

**Target platform:** Desktop

## See also

[**Iasphelp::AvgJobSize**](iasphelp-avgjobsize.md)

[**Iasphelp::CalcJobETA**](iasphelp-calcjobeta.md)
