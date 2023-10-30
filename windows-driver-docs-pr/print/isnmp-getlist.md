---
title: ISNMP GetList method
description: The GetList method enables an ASP Web page to obtain the values associated with an array of SNMP OIDs.
MS-HAID:
- 'webfnc_44ada708-01e2-42c3-8080-bd7cf0e46b0e.xml'
- 'print.isnmp\_getlist'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
keywords: ["GetList method Print Devices", "GetList method Print Devices , ISNMP interface", "ISNMP interface Print Devices , GetList method"]
topic_type:
- apiref
ms.topic: reference
api_name:
- ISNMP.GetList
api_location:
- olesnmp.h
api_type:
- COM
ms.date: 07/14/2023
---

# ISNMP::GetList method

The `GetList` method enables an ASP Web page to obtain the values associated with an array of SNMP OIDs.

## Syntax

```cpp
HRESULT GetList(
  [in]  VARIANT *varList,
  [out] VARIANT *varValue
);
```

## Parameters

*varList* \[in\]  
Caller-supplied pointer to an array of SNMP OID strings.

*varValue* \[out\]  
Caller-supplied pointer to a location that receives the address of an array of SNMP OID values.

## Return value

Win32 error codes can also be returned.

| Return code | Description |
|--|--|
| S_OK | The operation succeeded. |
| E_FAIL | The **ISNMP::Open** method has not been called. |
| E_INVALIDARG | The specified SNMP OID is not valid. |
| E_OUTOFMEMORY | Out of memory. |

## VBScript example

This method calls the **SnmpMgrRequest** function to obtain SNMP OID values. For more information about this function, see the Windows SDK Documentation.

The [**ISNMP::Open**](isnmp-open.md) method must be called before the `ISNMP::GetList` method can be called.

```vb
Dim StrIP, strCommunity, objSNMP, OIDArray, OIDValueArray
strIP = Session("MS_IPaddress")
strCommunity = Session ("MS_Community")
Set objSNMP = Server.CreateObject("OlePrn.OleSNMP")
objSNMP.Open strIP, strCommunity, 2, 1000
OIDArray = Array("25.3.2.1.5", "25.3.5.1.1")
OIDValueArray = objSNMP.GetList (OIDArray)
```

## Requirements

**Target platform:** Desktop

**Header:** Olesnmp.h

## See also

[**ISNMP::Open**](isnmp-open.md)
