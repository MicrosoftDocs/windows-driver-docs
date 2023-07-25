---
title: ISNMP GetTree method
description: The GetTree method enables an ASP Web page to obtain the values associated with a set of subnodes beneath a specified root SNMP OID.
MS-HAID:
- 'webfnc_bb1a8a21-716c-41ab-8b88-5f26d19575fa.xml'
- 'print.isnmp_gettree'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
keywords: ["GetTree method Print Devices", "GetTree method Print Devices , ISNMP interface", "ISNMP interface Print Devices , GetTree method"]
topic_type:
- apiref
ms.topic: reference
api_name:
- ISNMP.GetTree
api_location:
- olesnmp.h
api_type:
- COM
ms.date: 07/14/2023
---

# ISNMP::GetTree method

The `GetTree` method enables an ASP Web page to obtain the values associated with a set of subnodes beneath a specified root SNMP OID.

## Syntax

```cpp
HRESULT GetTree(
  [in]  BSTR    varTree,
  [out] VARIANT *varValue
);
```

## Parameters

*varTree* \[in\]  
Caller-supplied string identifying a root SNMP OID.

*varValue* \[out\]  
Caller-supplied location to receive the address of a two-dimensional array containing SNMP OID strings and associated values.

## Return value

Win32 error codes can also be returned.

| Return code | Description |
|--|--|
| S_OK | The operation succeeded. |
| E_FAIL | The **ISNMP::Open** method has not been called. |
| E_INVALIDARG | The specified SNMP OID is not valid. |
| E_OUTOFMEMORY | Out of memory. |

## VBScript example

This method calls the **SnmpMgrRequest** function to obtain the SNMP OID values for the subnodes.

The [**ISNMP::Open**](isnmp-open.md) method must be called before the `ISNMP::GetTree` method can be called.

```vb
Dim StrIP, strCommunity, objSNMP, OIDValueArray
strIP = Session("MS_IPaddress")
strCommunity = Session ("MS_Community")
Set objSNMP = Server.CreateObject("OlePrn.OleSNMP")
objSNMP.Open strIP, strCommunity, 2, 1000
OIDValueArray = objSNMP.GetTree ("43.18.1.1.2")
```

## Requirements

**Target platform:** Desktop

**Header:** Olesnmp.h

## See also

[**ISNMP::Open**](isnmp-open.md)
