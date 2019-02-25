---
title: ISNMP GetTree method
description: The GetTree method enables an ASP Web page to obtain the values associated with a set of subnodes beneath a specified root SNMP OID.
MS-HAID:
- 'webfnc\_bb1a8a21-716c-41ab-8b88-5f26d19575fa.xml'
- 'print.isnmp\_gettree'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: a58cc911-dc09-4847-b4b7-cf97326cd444
keywords: ["GetTree method Print Devices", "GetTree method Print Devices , ISNMP interface", "ISNMP interface Print Devices , GetTree method"]
topic_type:
- apiref
api_name:
- ISNMP.GetTree
api_location:
- olesnmp.h
api_type:
- COM
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# ISNMP::GetTree method

The `GetTree` method enables an ASP Web page to obtain the values associated with a set of subnodes beneath a specified root SNMP OID.

Syntax
------

```cpp
HRESULT GetTree(
  [in]  BSTR    varTree,
  [out] VARIANT *varValue
);
```

Parameters
----------

*varTree* \[in\]  
Caller-supplied string identifying a root SNMP OID.

*varValue* \[out\]  
Caller-supplied location to receive the address of a two-dimensional array containing SNMP OID strings and associated values.

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

This method calls the **SnmpMgrRequest** function to obtain the SNMP OID values for the subnodes. For more information about this function, see the Windows SDK documentation.

The [**ISNMP::Open**](isnmp-open.md) method must be called before the `ISNMP::GetTree` method can be called.

```vb
Dim StrIP, strCommunity, objSNMP, OIDValueArray
strIP = Session("MS_IPaddress")
strCommunity = Session ("MS_Community")
Set objSNMP = Server.CreateObject("OlePrn.OleSNMP")
objSNMP.Open strIP, strCommunity, 2, 1000
OIDValueArray = objSNMP.GetTree ("43.18.1.1.2")
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
