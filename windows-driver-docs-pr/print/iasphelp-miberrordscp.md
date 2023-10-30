---
title: Iasphelp get_MibErrorDscp method
description: The MibErrorDscp property enables an ASP Web page to convert a Simple Network Management Protocol (SNMP) management information base (MIB) error code into a text description of the error.
MS-HAID:
- 'webfnc_3931fbc6-1960-4d40-a6e3-8816ee832c89.xml'
- 'print.iasphelp_miberrordscp'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
keywords: ["get_MibErrorDscp method Print Devices", "get_MibErrorDscp method Print Devices , Iasphelp interface", "Iasphelp interface Print Devices , get_MibErrorDscp method"]
topic_type:
- apiref
ms.topic: reference
api_name:
- Iasphelp.get_MibErrorDscp
api_type:
- COM
ms.date: 06/26/2023
---

# Iasphelp::get_MibErrorDscp method

The **MibErrorDscp** property enables an ASP Web page to convert a Simple Network Management Protocol (SNMP) management information base (MIB) error code into a text description of the error.

## Syntax

```cpp
HRESULT get_MibErrorDscp(
  [in]  DWORD dwError,
  [out] BSTR  *pVal
);
```

## Parameters

*dwError* \[in\]  
Caller-supplied SNMP MIB error code.

*pVal* \[out\]  
Caller-supplied location to receive a pointer to a string containing a text description of the error.

## Return value

Win32 error codes can also be returned.

| Return code | Description |
|--|--|
| **S_OK** | The operation succeeded. |
| **E_POINTER** | Invalid *pVal* pointer. |
| **E_OUTOFMEMORY** | Out of memory. |

## VBScript Example

```vb
Dim objPrinter, MIBErrorCode, MIBErrorString
Set objPrinter = Server.CreateObject ("OlePrn.AspHelp")
...
' Get error code from MIB.
...
MIBErrorString = objPrinter.MibErrorDscp(ErrorCodeMIB)
```

## Requirements

**Target platform:** Desktop
