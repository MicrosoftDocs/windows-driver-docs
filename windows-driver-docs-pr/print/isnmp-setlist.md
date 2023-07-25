---
title: ISNMP SetList method
description: The SetList method enables an ASP Web page to associate values with an array of SNMP OIDs.
MS-HAID:
- 'webfnc_56e01eeb-9b33-4f32-b209-cde82d78e2d5.xml'
- 'print.isnmp_setlist'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
keywords: ["SetList method Print Devices", "SetList method Print Devices , ISNMP interface", "ISNMP interface Print Devices , SetList method"]
topic_type:
- apiref
ms.topic: reference
api_name:
- ISNMP.SetList
api_location:
- olesnmp.h
api_type:
- COM
ms.date: 07/14/2023
---

# ISNMP::SetList method

The `SetList` method enables an ASP Web page to associate values with an array of SNMP OIDs.

## Syntax

```cpp
HRESULT SetList(
  [in] VARIANT *varName,
  [in] VARIANT *varValue
);
```

## Parameters

*varName* \[in\]  
Caller-supplied pointer to an array of SNMP OID strings.

*varValue* \[in\]  
Caller-supplied pointer to an array of OID values.

## Return value

Win32 error codes can also be returned.

| Return code | Description |
|--|--|
| S_OK | The operation succeeded. |
| E_FAIL | The **ISNMP::Open** method has not been called. |
| E_INVALIDARG | The specified SNMP OID is not valid. |
| E_OUTOFMEMORY | Out of memory. |

## VBScript example

This method calls the **SnmpMgrRequest** function to set the SNMP OID values.

The [**ISNMP::Open**](isnmp-open.md) method must be called before the `ISNMP::SetList` method can be called.

```vb
Dim StrIP, strCommunity, objSNMP, OIDArray, OIDValueArray
strIP = Session("MS_IPaddress")
strCommunity = Session ("MS_Community")
Set objSNMP = Server.CreateObject("OlePrn.OleSNMP")
objSNMP.Open strIP, strCommunity, 2, 1000
OIDArray = Array("25.3.2.1.5", "25.3.5.1.1")
...
' Determine values to assign to OIDs; store them in OIDArray.
...
OIDValueArray = objSNMP.SetList (OIDArray)
```

## Requirements

**Target platform:** Desktop

**Header:** Olesnmp.h

## See also

[**ISNMP::Open**](isnmp-open.md)
