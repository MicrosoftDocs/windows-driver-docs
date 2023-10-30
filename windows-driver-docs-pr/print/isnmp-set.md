---
title: ISNMP Set method
description: The Set method enables an ASP Web page to associate a value with an SNMP OID.
MS-HAID:
- 'webfnc_b0392f7d-7d17-41ce-97fe-8f8baa691c78.xml'
- 'print.isnmp_set'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
keywords: ["Set method Print Devices", "Set method Print Devices , ISNMP interface", "ISNMP interface Print Devices , Set method"]
topic_type:
- apiref
ms.topic: reference
api_name:
- ISNMP.Set
api_location:
- olesnmp.h
api_type:
- COM
ms.date: 07/14/2023
---

# ISNMP::Set method

The `Set` method enables an ASP Web page to associate a value with an SNMP OID.

## Syntax

```cpp
HRESULT Set(
  [in]  BSTR    bstrOID,
  [out] VARIANT varValue
);
```

## Parameters

*bstrOID* \[in\]  
Caller-supplied pointer to an SNMP OID string.

*varValue* \[out\]  
Caller-supplied location containing the OID's value.

## Return value

Win32 error codes can also be returned.

| Return code | Description |
|--|--|
| S_OK | The operation succeeded. |
| E_FAIL | The **ISNMP::Open** method has not been called. |
| E_INVALIDARG | The specified SNMP OID is not valid. |
| E_OUTOFMEMORY | Out of memory. |

## VBScript example

This method calls the **SnmpMgrRequest** function to set SNMP OID values.

The [**ISNMP::Open**](isnmp-open.md) method must be called before the `ISNMP::Set` method can be called.

```vb
Dim StrIP, strCommunity, objSNMP, OIDValue
strIP = Session("MS_IPaddress")
strCommunity = Session ("MS_Community")
Set objSNMP = Server.CreateObject("OlePrn.OleSNMP")
objSNMP.Open strIP, strCommunity, 2, 1000
...
' Determine value to assign to OID; store it in OIDValue.
...
objSNMP.Set ("43.18.1.1.2", OIDValue)
```

## Requirements

**Target platform:** Desktop

**Header:** Olesnmp.h

## See also

[**ISNMP::Open**](isnmp-open.md)
