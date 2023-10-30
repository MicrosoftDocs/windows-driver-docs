---
title: ISNMP Close method
description: The Close method enables an ASP Web page to close a communication path to an SNMP agent.
MS-HAID:
- 'webfnc_e925ae51-c717-4b4f-8ab2-b18e9d770c63.xml'
- 'print.isnmp_close'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
keywords: ["Close method Print Devices", "Close method Print Devices , ISNMP interface", "ISNMP interface Print Devices , Close method"]
topic_type:
- apiref
ms.topic: reference
api_name:
- ISNMP.Close
api_location:
- olesnmp.h
api_type:
- COM
ms.date: 07/14/2023
---

# ISNMP::Close method

The `Close` method enables an ASP Web page to close a communication path to an SNMP agent.

## Syntax

```cpp
HRESULT Close();
```

## Parameters

This method has no parameters.

## Return value

The method always returns S_OK.

## VBScript example

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

## Requirements

**Target platform:** Desktop

**Header:** Olesnmp.h

## See also

[**ISNMP::Open**](isnmp-open.md)
