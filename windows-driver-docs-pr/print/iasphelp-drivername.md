---
title: Iasphelp get_DriverName method
description: The DriverName property enables an ASP Web page to obtain the name of the printer driver.
MS-HAID:
- 'webfnc_99826bd3-a4fb-41b4-9f05-10598c4fcc01.xml'
- 'print.iasphelp_drivername'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
keywords: ["get_DriverName method Print Devices", "get_DriverName method Print Devices , Iasphelp interface", "Iasphelp interface Print Devices , get_DriverName method"]
topic_type:
- apiref
ms.topic: reference
api_name:
- Iasphelp.get_DriverName
api_type:
- COM
ms.date: 06/23/2023
---

# Iasphelp::get_DriverName method

The **DriverName** property enables an ASP Web page to obtain the name of the printer driver.

## Syntax

```cpp
HRESULT get_DriverName(
  [out] BSTR *pVal
);
```

## Parameters

*pVal* \[out\]  
Caller-supplied pointer to a location to receive a pointer to a driver name string.

## Return value

Win32 error codes can also be returned.

| Return code | Description |
|--|--|
| **S_OK** | The operation succeeded. |
| **E_HANDLE** | The **Iasphelp::Open** method has not been called. |
| **E_OUTOFMEMORY** | Out of memory. |

## VBScript Example

The [**Iasphelp::Open**](iasphelp-open.md) method must be called before the **Iasphelp::DriverName** property can be queried.

```vb
Dim objPrinter, DrvrName
strPrinter = Session("MS_printer")
Set objPrinter = Server.CreateObject ("OlePrn.AspHelp")
objPrinter.Open strPrinter
DrvrName = objPrinter.DriverName
```

## Requirements

**Target platform:** Desktop

## See also

[**Iasphelp::Open**](iasphelp-open.md)
