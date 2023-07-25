---
title: ISNMP GetAsByte method
description: The GetAsByte method enables an ASP Web page to get the value identified by an SNMP OID and to convert the value to an unsigned integer.
MS-HAID:
- 'webfnc_915155f7-8444-4824-88be-808f10a9ff8e.xml'
- 'print.isnmp_getasbyte'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
keywords: ["GetAsByte method Print Devices", "GetAsByte method Print Devices , ISNMP interface", "ISNMP interface Print Devices , GetAsByte method"]
topic_type:
- apiref
ms.topic: reference
api_name:
- ISNMP.GetAsByte
api_location:
- olesnmp.h
api_type:
- COM
ms.date: 07/14/2023
---

# ISNMP::GetAsByte method

The `GetAsByte` method enables an ASP Web page to get the value identified by an SNMP OID and to convert the value to an unsigned integer.

## Syntax

```cpp
HRESULT GetAsByte(
  [in]  BSTR  bstrOID,
  [out] PUINT puValue
);
```

## Parameters

*bstrOID* \[in\]  
A caller-supplied BSTR value that contains the SNMP OID.

*puValue* \[out\]  
A caller-supplied pointer to a location that receives the unsigned integer value.

## Return value

This method returns one of the values in the following table.

| Return code | Description |
|--|--|
| S_OK | The operation succeeded. |
| E_FAIL | The **ISNMP::Open** method has not been called. |
| E_INVALIDARG | The specified SNMP OID is not valid. |
| E_OUTOFMEMORY | Out of memory. |

## VBScript example

This method calls the **SnmpMgrRequest** function to retrieve the value identified by an SNMP OID. Before the method passes the value to the caller, it converts the caller to an unsigned integer. For more information about **SnmpMgrRequest**, see the Windows SDK documentation.

For the following data types, the `ISNMP::GetAsByte` method converts the scalar value identified by the SNMP OID to an equivalent unsigned integer value, which the caller receives:

- ASN_INTEGER

- ASN_RFC1155_COUNTER

- ASN_RFC1155_GAUGE

- ASN_RFC1155_TIMETICKS

- ASN_UNSIGNED32

For the following data types, if the size of the value identified by the SNMP OID does not exceed two bytes, the method packs the beginning elements of the string, array, or opaque value into the unsigned integer value that the caller receives:

- ASN_BITS

- ASN_OCTETSTRING

- ASN_RFC1155_OPAQUE

- ASN_SEQUENCE

The method does not currently support conversions from data types other than those in the preceding lists. For more information about these data types, see the description of the SNMP Management API in the Windows SDK documentation.

The [**ISNMP::Open**](isnmp-open.md) method must be called before the `ISNMP::GetAsByte` method can be called.

```vb
Dim StrIP, strCommunity, objSNMP, OIDValue
strIP = Session("MS_IPaddress")
strCommunity = Session ("MS_Community")
Set objSNMP = Server.CreateObject("OlePrn.OleSNMP")
objSNMP.Open strIP, strCommunity, 2, 1000
OIDValue = objSNMP.GetAsByte ("25.3.5.1.2")
```

## Requirements

**Target platform:** Desktop

**Header:** Olesnmp.h

## See also

[**ISNMP::Open**](isnmp-open.md)
