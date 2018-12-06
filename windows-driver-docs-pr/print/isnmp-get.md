---
title: ISNMP Get method
description: The Get method enables an ASP Web page to obtain the value identified by an SNMP OID.
MS-HAID:
- 'webfnc\_e3167766-cd60-4ae7-9c06-9a1ccb5ac3b9.xml'
- 'print.isnmp\_get'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 0cecdc34-63d9-46da-ba4e-a44780f5bb25
keywords: ["Get method Print Devices", "Get method Print Devices , ISNMP interface", "ISNMP interface Print Devices , Get method"]
topic_type:
- apiref
api_name:
- ISNMP.Get
api_location:
- olesnmp.h
api_type:
- COM
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# ISNMP::Get method

The `Get` method enables an ASP Web page to obtain the value identified by an SNMP OID.

Syntax
------

```cpp
HRESULT Get(
  [in]  BSTR    bstrOID,
  [out] VARIANT *varValue
);
```

Parameters
----------

*bstrOID* \[in\]  
Caller-supplied pointer to an OID string.

*varValue* \[out\]  
Caller-supplied location to receive the OID's value.

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
<td><strong>E_FAIL</strong></td>
<td><p>The <strong>ISNMP::Open</strong> method has not been called.</p></td>
</tr>
<tr class="odd">
<td><strong>E_INVALIDARG</strong></td>
<td><p>The specified OID is not valid.</p></td>
</tr>
<tr class="even">
<td><strong>E_OUTOFMEMORY</strong></td>
<td><p>Out of memory.</p></td>
</tr>
</tbody>
</table>

## VBScript Example

This method calls the **SnmpMgrRequest** function to obtain the OID value. For more information about this function, see the Windows SDK documentation.

The [**ISNMP::Open**](isnmp-open.md) method must be called before the `ISNMP::Get` method can be called.

```vb
Dim StrIP, strCommunity, objSNMP, OIDValue
strIP = Session("MS_IPaddress")
strCommunity = Session ("MS_Community")
Set objSNMP = Server.CreateObject("OlePrn.OleSNMP")
objSNMP.Open strIP, strCommunity, 2, 1000
OIDValue = objSNMP.Get ("43.18.1.1.2")
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
