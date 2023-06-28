---
title: Iasphelp get_Color method
description: The Color property enables an ASP Web page to determine if a printer supports color printing.
MS-HAID:
- 'webfnc_1eb57c03-7aa3-4acb-8a2c-3327a37e019d.xml'
- 'print.iasphelp_color'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
keywords: ["get_Color method Print Devices", "get_Color method Print Devices , Iasphelp interface", "Iasphelp interface Print Devices , get_Color method"]
topic_type:
- apiref
ms.topic: reference
api_name:
- Iasphelp.get_Color
api_type:
- COM
ms.date: 06/23/2023
---

# Iasphelp::get_Color method

The **Color** property enables an ASP Web page to determine if a printer supports color printing.

## Syntax

```cpp
HRESULT get_Color(
  [out] BOOL *pVal
);
```

## Parameters

*pVal* \[out\]  
Caller-supplied pointer to a location to receive **TRUE** if the printer supports color printing, or **FALSE** if it does not.

## Return value

Win32 error codes can also be returned.

| Return code | Description |
|--|--|
| **S_OK** | The operation succeeded. |
| **E_HANDLE** | The **Iasphelp::Open** method has not been called. |
| **E_OUTOFMEMORY** | Out of memory. |

## VBScript Example

The [**Iasphelp::Open**](iasphelp-open.md) method must be called before the **Iasphelp::Color** property can be queried.

```vb
Dim objPrinter, HasColor
strPrinter = Session("MS_printer")
Set objPrinter = Server.CreateObject ("OlePrn.AspHelp")
objPrinter.Open strPrinter
HasColor = objPrinter.Color
```

## Requirements

**Target platform:** Desktop

## See also

[**Iasphelp::Open**](iasphelp-open.md)
