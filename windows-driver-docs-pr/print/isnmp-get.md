---
title: ISNMP Get method
description: The Get method enables an ASP Web page to obtain the value identified by an SNMP OID.
MS-HAID:
- 'webfnc_e3167766-cd60-4ae7-9c06-9a1ccb5ac3b9.xml'
- 'print.isnmp_get'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
keywords: ["Get method Print Devices", "Get method Print Devices , ISNMP interface", "ISNMP interface Print Devices , Get method"]
topic_type:
- apiref
ms.topic: reference
api_name:
- ISNMP.Get
api_location:
- olesnmp.h
api_type:
- COM
ms.date: 07/14/2023
---

# ISNMP::Get method

The `Get` method enables an ASP Web page to obtain the value identified by an SNMP OID.

## Syntax

```cpp
HRESULT Get(
  [in]  BSTR    bstrOID,
  [out] VARIANT *varValue
);
```

## Parameters

*bstrOID* \[in\]  
Caller-supplied pointer to an OID string.

*varValue* \[out\]  
Caller-supplied location to receive the OID's value.

## Return value

Win32 error codes can also be returned.

| Return code | Description |
|--|--|
| S_OK | The operation succeeded. |
| E_FAIL | The **ISNMP::Open** method has not been called. |
| E_INVALIDARG | The specified SNMP OID is not valid. |
| E_OUTOFMEMORY | Out of memory. |

## VBScript example

This method calls the **SnmpMgrRequest** function to obtain the OID value.

The [**ISNMP::Open**](isnmp-open.md) method must be called before the `ISNMP::Get` method can be called.

```vb
Dim StrIP, strCommunity, objSNMP, OIDValue
strIP = Session("MS_IPaddress")
strCommunity = Session ("MS_Community")
Set objSNMP = Server.CreateObject("OlePrn.OleSNMP")
objSNMP.Open strIP, strCommunity, 2, 1000
OIDValue = objSNMP.Get ("43.18.1.1.2")
```

## Requirements

**Target platform:** Desktop

**Header:** Olesnmp.h

## See also

[**ISNMP::Open**](isnmp-open.md)
