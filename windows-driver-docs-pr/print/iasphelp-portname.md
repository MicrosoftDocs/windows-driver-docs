---
title: Iasphelp get_PortName method
description: The PortName property enables an ASP Web page to obtain a printer's port name.
MS-HAID:
- 'webfnc_67f21c2f-9caf-4cd0-8a4b-df4ab9f63b43.xml'
- 'print.iasphelp_portname'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
keywords: ["get_PortName method Print Devices", "get_PortName method Print Devices , Iasphelp interface", "Iasphelp interface Print Devices , get_PortName method"]
topic_type:
- apiref
ms.topic: reference
api_name:
- Iasphelp.get_PortName
api_type:
- COM
ms.date: 06/26/2023
---

# Iasphelp::get_PortName method

The **PortName** property enables an ASP Web page to obtain a printer's port name.

## Syntax

```cpp
HRESULT get_PortName(
  [out] BSTR *pVal
);
```

## Parameters

*pVal* \[out\]  
Caller-supplied location to receive a pointer to a string representing the printer's port name.

## Return value

Win32 error codes can also be returned.

| Return code | Description |
|--|--|
| **S_OK** | The operation succeeded. |
| **E_HANDLE** | The [**Iasphelp::Open**](iasphelp-open.md) method has not been called. |
| **E_OUTOFMEMORY** | Out of memory. |

## VBScript Example

The [**Iasphelp::Open**](iasphelp-open.md) method must be called before the **Iasphelp::PortName** property can be queried.

```vb
Dim objPrinter, PtrPortName
strPrinter = Session("MS_printer")
Set objPrinter = Server.CreateObject ("OlePrn.AspHelp")
objPrinter.Open strPrinter
PtrPortName = objPrinter.PortName
```

## Requirements

**Target platform:** Desktop

## See also

[**Iasphelp::Open**](iasphelp-open.md)
