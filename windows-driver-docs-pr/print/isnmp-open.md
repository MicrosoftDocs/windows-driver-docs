---
title: ISNMP Open method
description: The Open method enables an ASP Web page to create a communication path to a specified SNMP agent.
MS-HAID:
- 'webfnc_2be497fa-98d8-4fb3-997c-fa1345ed4648.xml'
- 'print.isnmp_open'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
keywords: ["Open method Print Devices", "Open method Print Devices , ISNMP interface", "ISNMP interface Print Devices , Open method"]
topic_type:
- apiref
ms.topic: reference
api_name:
- ISNMP.Open
api_location:
- olesnmp.h
api_type:
- COM
ms.date: 07/14/2023
---

# ISNMP::Open method

The `Open` method enables an ASP Web page to create a communication path to a specified SNMP agent.

## Syntax

```cpp
HRESULT Open(
  [in] BSTR    bstrHost,
  [in] BSTR    bstrCommunity,
  [in] VARIANT varRetry,
  [in] VARIANT varTimeout
);
```

## Parameters

*bstrHost* \[in\]  
Caller-supplied pointer to a string identifying the SNMP agent system. This can be either a dotted-decimal IP address or a host name that can be resolved to an IP address, an IPX address (in 8.12 notation), or an ethernet address.

*bstrCommunity* \[in\]  
Caller-supplied pointer to a string representing the SNMP agent system's community name.

*varRetry* \[in\]  
Optional, caller-supplied retry value. If not specified, a default value is used. The recommended value is 2.

*varTimeout* \[in\]  
Optional, caller-supplied time-out value, in milliseconds. If not specified, a default value is used. The recommended value is 1000.

## Return value

Win32 error codes can also be returned.

| Return code | Description |
|--|--|
| S_OK | The operation succeeded. |
| E_FAIL | The call to **SnmpMgrOpen** failed. |
| E_INVALIDARG | Either the *varRetry* or *varTimeOut* value could not be converted to a short integer. |

## VBScript example

This method calls the **SnmpMgrOpen** function, which has the same parameters as `ISNMP::Open`.

After the `ISNMP::Open` call, the communication path to the SNMP agent remains open until the [**ISNMP::Close**](isnmp-close.md) method is called, or until `ISNMP::Open` is called again.

```vb
Dim StrIP, strCommunity, objSNMP
strIP = Session("MS_IPaddress")
strCommunity = Session ("MS_Community")
Set objSNMP = Server.CreateObject("OlePrn.OleSNMP")
objSNMP.Open strIP, strCommunity, 2, 1000
```

## Requirements

**Target platform:** Desktop

**Header:** Olesnmp.h

## See also

[**ISNMP::Close**](isnmp-close.md)
