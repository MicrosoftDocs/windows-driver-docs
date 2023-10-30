---
title: Iasphelp get_IPAddress method
description: The IPAddress property enables an ASP Web page to obtain a printer's IP address.
MS-HAID:
- 'webfnc_f0b5a4c6-50db-48a0-a10d-2a835cac32ac.xml'
- 'print.iasphelp_ipaddress'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
keywords: ["get_IPAddress method Print Devices", "get_IPAddress method Print Devices , Iasphelp interface", "Iasphelp interface Print Devices , get_IPAddress method"]
topic_type:
- apiref
ms.topic: reference
api_name:
- Iasphelp.get_IPAddress
api_type:
- COM
ms.date: 06/23/2023
---

# Iasphelp::get_IPAddress method

The **IPAddress** property enables an ASP Web page to obtain a printer's IP address.

## Syntax

```cpp
HRESULT get_IPAddress(
  [out] BSTR *pVal
);
```

## Parameters

*pVal* \[out\]  
Caller-supplied pointer to a location to receive a pointer to an IP address string.

## Return value

Win32 error codes can also be returned.

| Return code | Description |
|--|--|
| **S_OK** | The operation succeeded. |
| **E_HANDLE** | The **Iasphelp::Open** method has not been called. |
| **E_OUTOFMEMORY** | Out of memory. |

## VBScript Example

The [**Iasphelp::Open**](iasphelp-open.md) method must be called before the **Iasphelp::IPAddress** property can be queried.

If the printer is not supported by the TCP/IP port monitor, the returned string is empty.

```vb
Dim objPrinter, PrinterIP
strPrinter = Session("MS_printer")
Set objPrinter = Server.CreateObject ("OlePrn.AspHelp")
objPrinter.Open strPrinter
PrinterIP = objPrinter.IPAddress
```

## Requirements

**Target platform:** Desktop

## See also

[**Iasphelp::Open**](iasphelp-open.md)
