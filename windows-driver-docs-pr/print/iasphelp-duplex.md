---
title: Iasphelp get_Duplex method
description: The Duplex property enables an ASP Web page to determine if a printer supports duplex printing.
MS-HAID:
- 'webfnc_346f6357-9ca9-4b97-93a3-50ec9f28c118.xml'
- 'print.iasphelp_duplex'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
keywords: ["get_Duplex method Print Devices", "get_Duplex method Print Devices , Iasphelp interface", "Iasphelp interface Print Devices , get_Duplex method"]
topic_type:
- apiref
ms.topic: reference
api_name:
- Iasphelp.get_Duplex
api_type:
- COM
ms.date: 06/23/2023
---

# Iasphelp::get_Duplex method

The **Duplex** property enables an ASP Web page to determine if a printer supports duplex printing.

## Syntax

```cpp
HRESULT get_Duplex(
  [out] BOOL *pVal
);
```

## Parameters

*pVal* \[out\]  
Caller-supplied pointer to a location to receive **TRUE** if the printer supports duplex printing, or **FALSE** if it does not.

## Return value

Win32 error codes can also be returned.

| Return code | Description |
|--|--|
| **S_OK** | The operation succeeded. |
| **E_HANDLE** | The **Iasphelp::Open** method has not been called. |
| **E_OUTOFMEMORY** | Out of memory. |

## VBScript Example

The [**Iasphelp::Open**](iasphelp-open.md) method must be called before the **Iasphelp::Duplex** property can be queried.

```vb
Dim objPrinter, DoesDuplex
strPrinter = Session("MS_printer")
Set objPrinter = Server.CreateObject ("OlePrn.AspHelp")
objPrinter.Open strPrinter
DoesDuplex = objPrinter.Duplex
```

## Requirements

**Target platform:** Desktop

## See also

[**Iasphelp::Open**](iasphelp-open.md)
