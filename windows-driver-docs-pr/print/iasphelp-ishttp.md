---
title: Iasphelp get_IsHTTP method
description: The IsHTTP property enables an ASP Web page to determine whether the printer is connected to an HTTP port.
MS-HAID:
- 'webfnc_e3e58eea-498f-4e85-8072-2c49ac50d733.xml'
- 'print.iasphelp_ishttp'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
keywords: ["get_IsHTTP method Print Devices", "get_IsHTTP method Print Devices , Iasphelp interface", "Iasphelp interface Print Devices , get_IsHTTP method"]
topic_type:
- apiref
ms.topic: reference
api_name:
- Iasphelp.get_IsHTTP
api_type:
- COM
ms.date: 06/23/2023
---

# Iasphelp::get_IsHTTP method

The **IsHTTP** property enables an ASP Web page to determine whether the printer is connected to an HTTP port.

## Syntax

```cpp
HRESULT get_IsHTTP(
  [out] BOOL *pVal
);
```

## Parameters

*pVal* \[out\]  
A caller-supplied pointer to a memory location that receives **TRUE** if the printer is connected to an HTTP port, and **FALSE** otherwise.

## Return value

The property return one of the values in the following table.

| Return code | Description |
|--|--|
| **S_OK** | The operation succeeded. |
| **E_HANDLE** | The [**Iasphelp::Open**](iasphelp-open.md) method has not been called. |
| **E_OUTOFMEMORY** | Out of memory. |

## VBScript Example

The [**Iasphelp::Open**](iasphelp-open.md) method must be called before the **Iasphelp::IsHTTP** property can be queried.

```vb
Dim objPrinter, IsHTTPPort
strPrinter = Session("MS_printer")
Set objPrinter = Server.CreateObject ("OlePrn.AspHelp")
objPrinter.Open strPrinter
IsHTTPPort = objPrinter.IsHTTP
```

## Requirements

**Target platform:** Desktop

## See also

[**Iasphelp::Open**](iasphelp-open.md)
