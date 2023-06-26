---
title: Iasphelp get_PageRate method
description: The PageRate property enables an ASP Web page to determine a printer's page rate.
MS-HAID:
- 'webfnc_f356953e-ac15-4948-9a6e-b83d3aec8e7b.xml'
- 'print.iasphelp_pagerate'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
keywords: ["get_PageRate method Print Devices", "get_PageRate method Print Devices , Iasphelp interface", "Iasphelp interface Print Devices , get_PageRate method"]
topic_type:
- apiref
ms.topic: reference
api_name:
- Iasphelp.get_PageRate
api_type:
- COM
ms.date: 06/26/2023
---

# Iasphelp::get_PageRate method

The **PageRate** property enables an ASP Web page to determine a printer's page rate.

## Syntax

```cpp
HRESULT get_PageRate(
  [out] long *pVal
);
```

## Parameters

*pVal* \[out\]  
A caller-supplied location to receive a numeric value that represents the page rate for the printer. The units in which the page rate is expressed might depend on the printer. For more information about page rates, see the following Remarks section.

## Return value

This property returns one of the values in the following table.

| Return code | Description |
|--|--|
| **S_OK** | The operation succeeded. |
| **E_HANDLE** | The [**Iasphelp::Open**](iasphelp-open.md) method has not been called. |
| **E_OUTOFMEMORY** | Out of memory. |

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

## Requirements

**Target platform:** Desktop

## See also

[**Iasphelp::PageRateUnit**](iasphelp-pagerateunit.md)

[**Iasphelp::Open**](iasphelp-open.md)
