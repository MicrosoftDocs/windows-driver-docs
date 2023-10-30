---
title: Iasphelp get_Community method
description: The Community property enables an ASP Web page to obtain a print server's Simple Network Management Protocol (SNMP) community name.
MS-HAID:
- 'webfnc_1d85e932-6de7-468a-b1dd-8a5678c65615.xml'
- 'print.iasphelp_community'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
keywords: ["get_Community method Print Devices", "get_Community method Print Devices , Iasphelp interface", "Iasphelp interface Print Devices , get_Community method"]
topic_type:
- apiref
ms.topic: reference
api_name:
- Iasphelp.get_Community
api_type:
- COM
ms.date: 06/23/2023
---

# Iasphelp::get_Community method

The **Community** property enables an ASP Web page to obtain a print server's Simple Network Management Protocol (SNMP) community name.

## Syntax

```cpp
HRESULT get_Community(
  [out] BSTR *pVal
);
```

## Parameters

*pVal* \[out\]  
Caller-supplied pointer to a location to receive a pointer to a community name string.

## Return value

Win32 error codes can also be returned.

| Return code | Description |
|--|--|
| **S_OK** | The operation succeeded. |
| **E_HANDLE** | [**Iasphelp::Open**](iasphelp-open.md) method has not been called. |
| **E_OUTOFMEMORY** | Out of memory. |

## VBScript Example

If the printer is not supported by the TCP/IP port monitor, the returned string is empty.

The [**Iasphelp::Open**](iasphelp-open.md) method must be called before the **Iasphelp::Community** property can be queried.

```vb
Dim objPrinter, CommName
strPrinter = Session("MS_printer")
Set objPrinter = Server.CreateObject ("OlePrn.AspHelp")
objPrinter.Open strPrinter
CommName = objPrinter.Community
```

## Requirements

**Target platform:** Desktop

## See also

[**Iasphelp::Open**](iasphelp-open.md)
