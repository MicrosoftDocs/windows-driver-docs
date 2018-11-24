---
title: ISNMP GetList method
description: The GetList method enables an ASP Web page to obtain the values associated with an array of SNMP OIDs.
MS-HAID:
- 'webfnc\_44ada708-01e2-42c3-8080-bd7cf0e46b0e.xml'
- 'print.isnmp\_getlist'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 6ee90c77-578e-4c2c-b955-4b549625ca14
keywords: ["GetList method Print Devices", "GetList method Print Devices , ISNMP interface", "ISNMP interface Print Devices , GetList method"]
topic_type:
- apiref
api_name:
- ISNMP.GetList
api_location:
- olesnmp.h
api_type:
- COM
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# ISNMP::GetList method

The `GetList` method enables an ASP Web page to obtain the values associated with an array of SNMP OIDs.

Syntax
------

```cpp
HRESULT GetList(
  [in]  VARIANT *varList,
  [out] VARIANT *varValue
);
```

Parameters
----------

*varList* \[in\]  
Caller-supplied pointer to an array of SNMP OID strings.

*varValue* \[out\]  
Caller-supplied pointer to a location that receives the address of an array of SNMP OID values.

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
<td><p>The specified SNMP OID is not valid.</p></td>
</tr>
<tr class="even">
<td><strong>E_OUTOFMEMORY</strong></td>
<td><p>Out of memory.</p></td>
</tr>
</tbody>
</table>

## VBScript Example

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
