---
title: Iasphelp get_ShareName method
description: The ShareName property enables an ASP Web page to obtain the printer's shared name.
MS-HAID:
- 'webfnc_68b8e99e-a40b-44ee-94c8-2a8bcc293fa3.xml'
- 'print.iasphelp_sharename'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
keywords: ["get_ShareName method Print Devices", "get_ShareName method Print Devices , Iasphelp interface", "Iasphelp interface Print Devices , get_ShareName method"]
topic_type:
- apiref
ms.topic: reference
api_name:
- Iasphelp.get_ShareName
api_type:
- COM
ms.date: 06/26/2023
---

# Iasphelp::get_ShareName method

The **ShareName** property enables an ASP Web page to obtain the printer's shared name.

## Syntax

```cpp
HRESULT get_ShareName(
  [out] BSTR *pVal
);
```

## Parameters

*pVal* \[out\]  
Caller-supplied pointer to a location to receive a pointer to a share name string.

## Return value

Win32 error codes can also be returned.

| Return code | Description |
|--|--|
| **S_OK** | The operation succeeded. |
| **E_HANDLE** | The [**Iasphelp::Open**](iasphelp-open.md) method has not been called. |
| **E_OUTOFMEMORY** | Out of memory. |

## VBScript Example

The [**Iasphelp::Open**](iasphelp-open.md) method must be called before the **Iasphelp::ShareName** property can be queried.

```vb
Dim objPrinter, DrvrName
strPrinter = Session("MS_printer")
Set objPrinter = Server.CreateObject ("OlePrn.AspHelp")
objPrinter.Open strPrinter
DrvrName = objPrinter.ShareName
```

## Requirements

**Target platform:** Desktop

## See also

[**Iasphelp::Open**](iasphelp-open.md)
