---
title: Iasphelp get_AvgJobSize method
description: The AvgJobSize property enables an ASP Web page to determine the average job size in a sequence of print jobs.
MS-HAID:
- 'webfnc_de863905-eb8f-430a-a70b-7cb404dd3717.xml'
- 'print.iasphelp_avgjobsize'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
keywords: ["get_AvgJobSize method Print Devices", "get_AvgJobSize method Print Devices , Iasphelp interface", "Iasphelp interface Print Devices , get_AvgJobSize method"]
topic_type:
- apiref
ms.topic: reference
api_name:
- Iasphelp.get_AvgJobSize
api_type:
- COM
ms.date: 06/23/2023
---

# Iasphelp::get_AvgJobSize method

The **AvgJobSize** property enables an ASP Web page to determine the average job size in a sequence of print jobs.

## Syntax

```cpp
HRESULT get_AvgJobSize(
  [out] long *pVal
);
```

## Parameters

*pVal* \[out\]  
A caller-supplied pointer to a memory location that receives the average job size. For more information about this parameter, see the following Remarks section.

## Return value

This method returns S_OK on success.

## VBScript Example

The average job size can be expressed as either the number of pages per job or the number of bytes per job. Use the [**Iasphelp::AvgJobSizeUnit**](iasphelp-avgjobsizeunit.md) property to determine which unit applies to the **Iasphelp::AvgJobSize** property.

Before you query this property, call the [**Iasphelp::CalcJobETA**](iasphelp-calcjobeta.md) method to initialize the property value.

```vb
Dim objPrinter, strPrinter, JobSizeAvg
strPrinter = Session("MS_printer")
Set objPrinter = Server.CreateObject ("OlePrn.AspHelp")
objPrinter.Open strPrinter
objPrinter.CalcJobETA
JobSizeAvg = objPrinter.AvgJobSize
```

## Requirements

**Target platform:** Desktop

## See also

[**Iasphelp::AvgJobSizeUnit**](iasphelp-avgjobsizeunit.md)

[**Iasphelp::CalcJobETA**](iasphelp-calcjobeta.md)
