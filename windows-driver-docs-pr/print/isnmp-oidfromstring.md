---
title: ISNMP OIDFromString method
description: The OIDFromString method enables an ASP Web page to convert an SNMP OID string to a numeric array.
MS-HAID:
- 'webfnc\_de08026f-5b6b-4c82-a653-2e16606e6b85.xml'
- 'print.isnmp\_oidfromstring'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: a0e12657-c34e-4aff-a068-911a6aa6959d
keywords: ["OIDFromString method Print Devices", "OIDFromString method Print Devices , ISNMP interface", "ISNMP interface Print Devices , OIDFromString method"]
topic_type:
- apiref
api_name:
- ISNMP.OIDFromString
api_location:
- olesnmp.h
api_type:
- COM
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# ISNMP::OIDFromString method

The `OIDFromString` method enables an ASP Web page to convert an SNMP OID string to a numeric array.

Syntax
------

```cpp
HRESULT OIDFromString(
  [in]  BSTR    bstrOID,
  [out] VARIANT *varOID
);
```

Parameters
----------

*bstrOID* \[in\]  
Caller-supplied pointer to an SNMP OID string.

*varOID* \[out\]  
Caller-supplied location to receive a pointer to an array of integer values representing the SNMP OID.

Return value
------------

Win32 error codes can also be returned.

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
<td><strong>E_INVALIDARG</strong></td>
<td><p>The specified SNMP OID is not valid.</p></td>
</tr>
<tr class="odd">
<td><strong>E_OUTOFMEMORY</strong></td>
<td><p>Out of memory.</p></td>
</tr>
</tbody>
</table>

## VBScript Example

This method calls the **SnmpMgrStrToOid** function to convert the SNMP OID string to its corresponding internal object-identifier structure. For more information about this function, see the Windows SDK documentation.

```vb
Dim StrIP, strCommunity, objSNMP, OIDArray
strIP = Session("MS_IPaddress")
strCommunity = Session ("MS_Community")
Set objSNMP = Server.CreateObject("OlePrn.OleSNMP")
objSNMP.Open strIP, strCommunity, 2, 1000
OIDArray = objSNMP.OIDFromString (". 43.18.1.1.2")
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
