---
title: ISNMP Close method
description: The Close method enables an ASP Web page to close a communication path to an SNMP agent.
MS-HAID:
- 'webfnc\_e925ae51-c717-4b4f-8ab2-b18e9d770c63.xml'
- 'print.isnmp\_close'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: ea3c462d-881d-48ad-8751-d3ee0468697e
keywords: ["Close method Print Devices", "Close method Print Devices , ISNMP interface", "ISNMP interface Print Devices , Close method"]
topic_type:
- apiref
api_name:
- ISNMP.Close
api_location:
- olesnmp.h
api_type:
- COM
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# ISNMP::Close method

The `Close` method enables an ASP Web page to close a communication path to an SNMP agent.

Syntax
------

```cpp
HRESULT Close();
```

Parameters
----------

This method has no parameters.

Return value
------------

The method always returns S\_OK.

## VBScript Example

This method calls the **SnmpMgrClose** function, which is described in the Windows SDK documentation, to close the communication path that was created by the previous call to the [**ISNMP::Open**](isnmp-open.md) method.

```vb
Dim StrIP, strCommunity, objSNMP
strIP = Session("MS_IPaddress")
strCommunity = Session ("MS_Community")
Set objSNMP = Server.CreateObject("OlePrn.OleSNMP")
objSNMP.Open strIP, strCommunity, 2, 1000
...
objSNMP.Close
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
