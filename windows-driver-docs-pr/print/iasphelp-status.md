---
title: Iasphelp get_Status method
description: The Status property enables an ASP Web page to determine the printer status.
MS-HAID:
- 'webfnc_30feffa7-1aa0-4b66-9d0a-1f66025272c3.xml'
- 'print.iasphelp_status'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
keywords: ["get_Status method Print Devices", "get_Status method Print Devices , Iasphelp interface", "Iasphelp interface Print Devices , get_Status method"]
topic_type:
- apiref
ms.topic: reference
api_name:
- Iasphelp.get_Status
api_type:
- COM
ms.date: 06/26/2023
---

# Iasphelp::get_Status method

The **Status** property enables an ASP Web page to determine the printer status.

## Syntax

```cpp
HRESULT get_Status(
  [out] long *pVal
);
```

## Parameters

*pVal* \[out\]  
Caller-supplied pointer to a location to receive printer status flags. For more information, see the following Remarks section.

## Return value

Win32 error codes can also be returned.

| Return code | Description |
|--|--|
| **S_OK** | The operation succeeded. |
| **E_HANDLE** | The [**Iasphelp::Open**](iasphelp-open.md) method has not been called. |
| **E_OUTOFMEMORY** | Out of memory. |

## VBScript Example

The property value is a printer status code that is either 0 or the bitwise OR of one or more of the PRINTER_STATUS_*XXX* flags that are defined in header file Winspool.h for the **Status** member of the PRINTER_INFO_2 structure. For more information about this structure, see the Windows SDK documentation.

The [**Iasphelp::Open**](iasphelp-open.md) method must be called before the **Iasphelp::Status** property can be queried.

```vb
Dim objPrinter, PtrStatus
strPrinter = Session("MS_printer")
Set objPrinter = Server.CreateObject ("OlePrn.AspHelp")
objPrinter.Open strPrinter
PtrStatus = objPrinter.Status
```

## Requirements

**Target platform:** Desktop

## See also

[**Iasphelp::Open**](iasphelp-open.md)
