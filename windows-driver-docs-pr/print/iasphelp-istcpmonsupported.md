---
title: Iasphelp getIsTCPMonSupported method
description: The IsTCPMonSupported property enables an ASP Web page to determine if Microsoft's standard TCP/IP port monitor is being used with a printer.
MS-HAID:
- 'webfnc54f72229-524a-4bf2-917d-6a3ffcc27959.xml'
- 'print.iasphelpistcpmonsupported'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
keywords: ["get_IsTCPMonSupported method Print Devices", "get_IsTCPMonSupported method Print Devices , Iasphelp interface", "Iasphelp interface Print Devices , get_IsTCPMonSupported method"]
topic_type:
- apiref
ms.topic: reference
api_name:
- Iasphelp.get_IsTCPMonSupported
api_type:
- COM
ms.date: 06/23/2023
---

# Iasphelp::getIsTCPMonSupported method

The **IsTCPMonSupported** property enables an ASP Web page to determine if Microsoft's standard TCP/IP [port monitor](./port-monitors.md) is being used with a printer.

## Syntax

```cpp
HRESULT get_IsTCPMonSupported(
  [out] BOOL *pVal
);
```

## Parameters

*pVal* \[out\]  
Caller-supplied pointer to a location to receive **TRUE** if the TCP/IP port monitor is being used with the printer, or **FALSE** if it is not.

## Return value

Win32 error codes can also be returned.

| Return code | Description |
|--|--|
| **S_OK** | The operation succeeded. |
| **E_HANDLE** | The [**Iasphelp::Open**](iasphelp-open.md) method has not been called. |
| **E_OUTOFMEMORY** | Out of memory. |

## VBScript Example

The [**Iasphelp::Open**](iasphelp-open.md) method must be called before the **Iasphelp::IsTCPMonSupported** property can be queried.

```vb
Dim objPrinter, UseStdMon
strPrinter = Session("MS_printer")
Set objPrinter = Server.CreateObject ("OlePrn.AspHelp")
objPrinter.Open strPrinter
UseStdMon = objPrinter.IsTCPMonSupported
```

## Requirements

**Target platform:** Desktop

## See also

[**Iasphelp::Open**](iasphelp-open.md)
