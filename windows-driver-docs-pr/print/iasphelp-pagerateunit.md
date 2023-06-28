---
title: Iasphelp get_PageRateUnit method
description: The PageRateUnit enables an ASP Web page to determine the units in which the page rate is expressed.
MS-HAID:
- 'webfnc_c3c557fb-2ce9-4260-838a-4bd0e56fb63d.xml'
- 'print.iasphelp_pagerateunit'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
keywords: ["get_PageRateUnit method Print Devices", "get_PageRateUnit method Print Devices , Iasphelp interface", "Iasphelp interface Print Devices , get_PageRateUnit method"]
topic_type:
- apiref
ms.topic: reference
api_name:
- Iasphelp.get_PageRateUnit
api_type:
- COM
ms.date: 06/26/2023
---

# Iasphelp::get_PageRateUnit method

The **PageRateUnit** enables an ASP Web page to determine the units in which the page rate is expressed.

## Syntax

```cpp
HRESULT get_PageRateUnit(
  [out] long *pVal
);
```

## Parameters

*pVal* \[out\]  
A caller-supplied pointer to a memory location that receives a value that indicates the units used in the page rate. The four possible values are shown in the following table.

| Value | Meaning |
|--|--|
| 1 | Print rate units are pages per minute. |
| 2 | Print rate units are characters per second. |
| 3 | Print rate units are lines per minute. |
| 4 | Print rate units are inches per minute. |

These values correspond to the constants PRINTRATEUNIT_PPM, PRINTRATEUNIT_CPS, PRINTRATEUNIT_LPM, and PRINTRATEUNIT_IPM, which are defined in the Wingdi.h header file. For more information about these constants, see the description of the **DeviceCapabilities** function in the Windows SDK documentation.

## Return value

This property returns one of the values in the following table.

| Return code | Description |
|--|--|
| **S_OK** | The operation succeeded. |
| **E_HANDLE** | The [**Iasphelp::Open**](iasphelp-open.md) method has not been called. |
| **E_OUTOFMEMORY** | Out of memory. |

## VBScript Example

Query this property to determine the units in which the [**Iasphelp::PageRate**](iasphelp-pagerate.md) property value is expressed.

The [**Iasphelp::Open**](iasphelp-open.md) method must be called before the **Iasphelp::PageRateUnit** property can be queried.

```vb
Dim objPrinter, PtrPageRateUnit
strPrinter = Session("MS_printer")
Set objPrinter = Server.CreateObject ("OlePrn.AspHelp")
objPrinter.Open strPrinter
PtrPageRate = objPrinter.PageRateUnit
```

## Requirements

**Target platform:** Desktop

## See also

[**Iasphelp::PageRate**](iasphelp-pagerate.md)

[**Iasphelp::Open**](iasphelp-open.md)
