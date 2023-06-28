---
title: Iasphelp get_SNMPSupported method
description: The SNMPSupported property enables an ASP Web page to determine if SNMP is being used with a printer.
MS-HAID:
- 'webfnc_2128dc9d-a113-4061-a6c9-3ebe2a304dd5.xml'
- 'print.iasphelp_snmpsupported'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
keywords: ["get_SNMPSupported method Print Devices", "get_SNMPSupported method Print Devices , Iasphelp interface", "Iasphelp interface Print Devices , get_SNMPSupported method"]
topic_type:
- apiref
ms.topic: reference
api_name:
- Iasphelp.get_SNMPSupported
api_type:
- COM
ms.date: 06/26/2023
---

# Iasphelp::get_SNMPSupported method

The **SNMPSupported** property enables an ASP Web page to determine if SNMP is being used with a printer.

## Syntax

```cpp
HRESULT get_SNMPSupported(
  [out] BOOL *pVal
);
```

## Parameters

*pVal* \[out\]  
Caller-supplied pointer to a location to receive **TRUE** if SNMP is being used with the printer, or **FALSE** if it is not.

## Return value

Win32 error codes can also be returned.

| Return code | Description |
|--|--|
| **S_OK** | The operation succeeded. |
| **E_HANDLE** | The [**Iasphelp::Open**](iasphelp-open.md) method has not been called. |
| **E_OUTOFMEMORY** | Out of memory. |

## VBScript Example

The [**Iasphelp::Open**](iasphelp-open.md) method must be called before the **Iasphelp::SNMPSupported** property can be queried.

```vb
Dim objPrinter, UsingSNMP
strPrinter = Session("MS_printer")
Set objPrinter = Server.CreateObject ("OlePrn.AspHelp")
objPrinter.Open strPrinter
UsingSNMP = objPrinter.SNMPSupported
```

## Requirements

**Target platform:** Desktop

## See also

[**Iasphelp::Open**](iasphelp-open.md)
