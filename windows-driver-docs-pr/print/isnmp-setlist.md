---
title: ISNMP SetList method
description: The SetList method enables an ASP Web page to associate values with an array of SNMP OIDs.
MS-HAID:
- 'webfnc\_56e01eeb-9b33-4f32-b209-cde82d78e2d5.xml'
- 'print.isnmp\_setlist'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: c783fc1b-e354-4b79-a57d-975ce0d0a0a4
keywords: ["SetList method Print Devices", "SetList method Print Devices , ISNMP interface", "ISNMP interface Print Devices , SetList method"]
topic_type:
- apiref
api_name:
- ISNMP.SetList
api_location:
- olesnmp.h
api_type:
- COM
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# ISNMP::SetList method

The `SetList` method enables an ASP Web page to associate values with an array of SNMP OIDs.

Syntax
------

```cpp
HRESULT SetList(
  [in] VARIANT *varName,
  [in] VARIANT *varValue
);
```

Parameters
----------

*varName* \[in\]  
Caller-supplied pointer to an array of SNMP OID strings.

*varValue* \[in\]  
Caller-supplied pointer to an array of OID values.

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

This method calls the **SnmpMgrRequest** function to set the SNMP OID values. For more information about this function, see the Windows SDK Documentation.

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
