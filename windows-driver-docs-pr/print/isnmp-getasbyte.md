---
title: ISNMP GetAsByte method
description: The GetAsByte method enables an ASP Web page to get the value identified by an SNMP OID and to convert the value to an unsigned integer.
MS-HAID:
- 'webfnc\_915155f7-8444-4824-88be-808f10a9ff8e.xml'
- 'print.isnmp\_getasbyte'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 0a9d170d-486f-49e9-a8f9-c0d8b17f681b
keywords: ["GetAsByte method Print Devices", "GetAsByte method Print Devices , ISNMP interface", "ISNMP interface Print Devices , GetAsByte method"]
topic_type:
- apiref
api_name:
- ISNMP.GetAsByte
api_location:
- olesnmp.h
api_type:
- COM
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# ISNMP::GetAsByte method

The `GetAsByte` method enables an ASP Web page to get the value identified by an SNMP OID and to convert the value to an unsigned integer.

Syntax
------

```cpp
HRESULT GetAsByte(
  [in]  BSTR  bstrOID,
  [out] PUINT puValue
);
```

Parameters
----------

*bstrOID* \[in\]  
A caller-supplied BSTR value that contains the SNMP OID.

*puValue* \[out\]  
A caller-supplied pointer to a location that receives the unsigned integer value.

Return value
------------

This method returns one of the values in the following table.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Return code</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>S_OK</strong></td>
<td><p>The operation succeeded.</p></td>
</tr>
<tr class="even">
<td><strong>E_FAIL</strong></td>
<td><p>The <strong>ISNMP::Open</strong> method has not been called.</p></td>
</tr>
<tr class="odd">
<td><strong>E_INVALIDARG</strong></td>
<td><p>The specified SNMP OID is not valid.</p></td>
</tr>
<tr class="even">
<td><strong>E_OUTOFMEMORY</strong></td>
<td><p>Out of memory.</p></td>
</tr>
</tbody>
</table>

## VBScript Example

This method calls the **SnmpMgrRequest** function to retrieve the value identified by an SNMP OID. Before the method passes the value to the caller, it converts the caller to an unsigned integer. For more information about **SnmpMgrRequest**, see the Windows SDK documentation.

For the following data types, the `ISNMP::GetAsByte` method converts the scalar value identified by the SNMP OID to an equivalent unsigned integer value, which the caller receives:

-   ASN\_INTEGER

-   ASN\_RFC1155\_COUNTER

-   ASN\_RFC1155\_GAUGE

-   ASN\_RFC1155\_TIMETICKS

-   ASN\_UNSIGNED32

For the following data types, if the size of the value identified by the SNMP OID does not exceed two bytes, the method packs the beginning elements of the string, array, or opaque value into the unsigned integer value that the caller receives:

-   ASN\_BITS

-   ASN\_OCTETSTRING

-   ASN\_RFC1155\_OPAQUE

-   ASN\_SEQUENCE

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

Requirements
------------

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Target platform</p></td>
<td>Desktop</td>
</tr>
<tr class="odd">
<td><p>Header</p></td>
<td>Olesnmp.h</td>
</tr>
</tbody>
</table>

## See also

[**ISNMP::Open**](isnmp-open.md)
