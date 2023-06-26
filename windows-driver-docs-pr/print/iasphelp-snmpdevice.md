---
title: Iasphelp get_SNMPDevice method
description: The SNMPDevice property enables an ASP Web page to obtain a printer's SNMP device index (as defined by RFC 1759).
MS-HAID:
- 'webfnc_e4a9d1b3-1168-45a7-98cb-9c19fdf83009.xml'
- 'print.iasphelp_snmpdevice'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
keywords: ["get_SNMPDevice method Print Devices", "get_SNMPDevice method Print Devices , Iasphelp interface", "Iasphelp interface Print Devices , get_SNMPDevice method"]
topic_type:
- apiref
ms.topic: reference
api_name:
- Iasphelp.get_SNMPDevice
api_type:
- COM
ms.date: 06/26/2023
---

# Iasphelp::get_SNMPDevice method

The **SNMPDevice** property enables an ASP Web page to obtain a printer's SNMP device index (as defined by RFC 1759).

## Syntax

```cpp
HRESULT get_SNMPDevice(
  [out] DWORD *pVal
);
```

## Parameters

*pVal* \[out\]  
Caller-supplied location to receive a numeric value representing the printer's SNMP device index.

## Return value

Win32 error codes can also be returned.

| Return code | Description |
|--|--|
| **S_OK** | The operation succeeded. |
| **E_HANDLE** | The [**Iasphelp::Open**](iasphelp-open.md) method has not been called. |
| **E_OUTOFMEMORY** | Out of memory. |

## VBScript Example

The [**Iasphelp::Open**](iasphelp-open.md) method must be called before the **Iasphelp::SNMPDevice** property can be queried.

```vb
Dim objPrinter, SNMPDeviceIndex
strPrinter = Session("MS_printer")
Set objPrinter = Server.CreateObject ("OlePrn.AspHelp")
objPrinter.Open strPrinter
SNMPDeviceIndex = objPrinter.SNMPDevice
```

## Requirements

**Target platform:** Desktop

## See also

[**Iasphelp::Open**](iasphelp-open.md)
