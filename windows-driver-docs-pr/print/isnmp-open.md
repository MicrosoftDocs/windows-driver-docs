---
title: ISNMP Open method
description: The Open method enables an ASP Web page to create a communication path to a specified SNMP agent.
MS-HAID:
- 'webfnc\_2be497fa-98d8-4fb3-997c-fa1345ed4648.xml'
- 'print.isnmp\_open'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: a5d1a8a2-5953-4b7f-8f8e-cb84520ae9e8
keywords: ["Open method Print Devices", "Open method Print Devices , ISNMP interface", "ISNMP interface Print Devices , Open method"]
topic_type:
- apiref
api_name:
- ISNMP.Open
api_location:
- olesnmp.h
api_type:
- COM
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# ISNMP::Open method

The `Open` method enables an ASP Web page to create a communication path to a specified SNMP agent.

Syntax
------

```cpp
HRESULT Open(
  [in] BSTR    bstrHost,
  [in] BSTR    bstrCommunity,
  [in] VARIANT varRetry,
  [in] VARIANT varTimeout
);
```

Parameters
----------

*bstrHost* \[in\]  
Caller-supplied pointer to a string identifying the SNMP agent system. This can be either a dotted-decimal IP address or a host name that can be resolved to an IP address, an IPX address (in 8.12 notation), or an ethernet address.

*bstrCommunity* \[in\]  
Caller-supplied pointer to a string representing the SNMP agent system's community name.

*varRetry* \[in\]  
Optional, caller-supplied retry value. If not specified, a default value is used. The recommended value is 2.

*varTimeout* \[in\]  
Optional, caller-supplied time-out value, in milliseconds. If not specified, a default value is used. The recommended value is 1000.

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
<td><p>Either the <em>varRetry</em> or <em>varTimeOut</em> value could not be converted to a short integer.</p></td>
</tr>
<tr class="odd">
<td><strong>E_FAIL</strong></td>
<td><p>The call to <strong>SnmpMgrOpen</strong> failed.</p></td>
</tr>
</tbody>
</table>

## VBScript Example

This method calls the **SnmpMgrOpen** function, which has the same parameters as `ISNMP::Open`. For more information about this function, see the Windows SDK Documentation.

After the `ISNMP::Open` call, the communication path to the SNMP agent remains open until the [**ISNMP::Close**](isnmp-close.md) method is called, or until `ISNMP::Open` is called again.

```vb
Dim StrIP, strCommunity, objSNMP
strIP = Session("MS_IPaddress")
strCommunity = Session ("MS_Community")
Set objSNMP = Server.CreateObject("OlePrn.OleSNMP")
objSNMP.Open strIP, strCommunity, 2, 1000
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

[**ISNMP::Close**](isnmp-close.md)
