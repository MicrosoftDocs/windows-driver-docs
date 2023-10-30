---
title: Iasphelp CalcJobETA method
description: The CalcJobETA method enables an ASP Web page to calculate the time at which a print job is to be completed.
MS-HAID:
- 'webfnc_65577773-9d44-429e-a2fe-eb1a1475b7f6.xml'
- 'print.iasphelp_calcjobeta'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
keywords: ["CalcJobETA method Print Devices", "CalcJobETA method Print Devices , Iasphelp interface", "Iasphelp interface Print Devices , CalcJobETA method"]
topic_type:
- apiref
ms.topic: reference
api_name:
- Iasphelp.CalcJobETA
api_type:
- COM
ms.date: 06/23/2023
---

# Iasphelp::CalcJobETA method

The **CalcJobETA** method enables an ASP Web page to calculate the time at which a print job is to be completed.

## Syntax

```cpp
HRESULT CalcJobETA();
```

## Parameters

This method has no parameters.

## Return value

The following table shows possible return values for this method.

| Return code | Description |
|--|--|
| **S_OK** | The method succeeded. |
| **E_HANDLE** | The **Iasphelp::Open** method has not been called. |
| **E_OUTOFMEMORY** | Out of memory. |

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

## Requirements

**Target platform:** Desktop

## See also

[**Iasphelp::JobCompletionMinute**](iasphelp-jobcompletionminute.md)

[**Iasphelp::PendingJobCount**](iasphelp-pendingjobcount.md)

[**Iasphelp::AvgJobSize**](iasphelp-avgjobsize.md)

[**Iasphelp::AvgJobSizeUnit**](iasphelp-avgjobsizeunit.md)

[**Iasphelp::Open**](iasphelp-open.md)
