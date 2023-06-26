---
title: Iasphelp getMaximumResolution method
description: The MaximumResolution property enables an ASP Web page to determine a printer's maximum resolution.
MS-HAID:
- 'webfnc156e8337-489a-44e6-9c81-0a8f6dd3aa08.xml'
- 'print.iasphelpmaximumresolution'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
keywords: ["get_MaximumResolution method Print Devices", "get_MaximumResolution method Print Devices , Iasphelp interface", "Iasphelp interface Print Devices , get_MaximumResolution method"]
topic_type:
- apiref
ms.topic: reference
api_name:
- Iasphelp.get_MaximumResolution
api_type:
- COM
ms.date: 06/23/2023
---

# Iasphelp::getMaximumResolution method

The **MaximumResolution** property enables an ASP Web page to determine a printer's maximum resolution.

## Syntax

```cpp
HRESULT get_MaximumResolution(
  [out] long *pVal
);
```

## Parameters

*pVal* \[out\]  
Caller-supplied location to receive a numeric value representing the printer's maximum resolution, in dots per inch.

## Return value

This property returns one of the values in the following table.

| Return code | Description |
|--|--|
| **S_OK** | The operation succeeded. |
| **E_HANDLE** | The [**Iasphelp::Open**](iasphelp-open.md) method has not been called. |
| **E_OUTOFMEMORY** | Out of memory. |

## VBScript Example

The [**Iasphelp::Open**](iasphelp-open.md) method must be called before the **Iasphelp::MaximumResolution** property can be queried.

```vb
Dim objPrinter, MaxRes
strPrinter = Session("MS_printer")
Set objPrinter = Server.CreateObject ("OlePrn.AspHelp")
objPrinter.Open strPrinter
MaxRes = objPrinter.MaximumResolution
```

## Requirements

**Target platform:** Desktop

## See also

[**Iasphelp::Open**](iasphelp-open.md)
