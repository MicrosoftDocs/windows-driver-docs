---
title: ISNMP OIDFromString method
description: The OIDFromString method enables an ASP Web page to convert an SNMP OID string to a numeric array.
MS-HAID:
- 'webfnc_de08026f-5b6b-4c82-a653-2e16606e6b85.xml'
- 'print.isnmp_oidfromstring'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
keywords: ["OIDFromString method Print Devices", "OIDFromString method Print Devices , ISNMP interface", "ISNMP interface Print Devices , OIDFromString method"]
topic_type:
- apiref
ms.topic: reference
api_name:
- ISNMP.OIDFromString
api_location:
- olesnmp.h
api_type:
- COM
ms.date: 07/14/2023
---

# ISNMP::OIDFromString method

The `OIDFromString` method enables an ASP Web page to convert an SNMP OID string to a numeric array.

## Syntax

```cpp
HRESULT OIDFromString(
  [in]  BSTR    bstrOID,
  [out] VARIANT *varOID
);
```

## Parameters

*bstrOID* \[in\]  
Caller-supplied pointer to an SNMP OID string.

*varOID* \[out\]  
Caller-supplied location to receive a pointer to an array of integer values representing the SNMP OID.

## Return value

Win32 error codes can also be returned.

| Return code | Description |
|--|--|
| S_OK | The operation succeeded. |
| E_FAIL | The **ISNMP::Open** method has not been called. |
| E_INVALIDARG | The specified SNMP OID is not valid. |
| E_OUTOFMEMORY | Out of memory. |

## VBScript Example

This method calls the **SnmpMgrStrToOid** function to convert the SNMP OID string to its corresponding internal object-identifier structure.

```vb
Dim StrIP, strCommunity, objSNMP, OIDArray
strIP = Session("MS_IPaddress")
strCommunity = Session ("MS_Community")
Set objSNMP = Server.CreateObject("OlePrn.OleSNMP")
objSNMP.Open strIP, strCommunity, 2, 1000
OIDArray = objSNMP.OIDFromString (". 43.18.1.1.2")
```

## Requirements

**Target platform:** Desktop

**Header:** Olesnmp.h
