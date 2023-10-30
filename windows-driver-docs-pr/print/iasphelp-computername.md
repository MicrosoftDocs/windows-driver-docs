---
title: Iasphelp get_ComputerName method
description: The ComputerName property enables an ASP Web page to obtain a print server's name.
MS-HAID:
- 'webfnc_fd5c59b9-c223-4762-898d-693e9960619c.xml'
- 'print.iasphelp_computername'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
keywords: ["get_ComputerName method Print Devices", "get_ComputerName method Print Devices , Iasphelp interface", "Iasphelp interface Print Devices , get_ComputerName method"]
topic_type:
- apiref
ms.topic: reference
api_name:
- Iasphelp.get_ComputerName
api_type:
- COM
ms.date: 06/23/2023
---

# Iasphelp::get_ComputerName method

The **ComputerName** property enables an ASP Web page to obtain a print server's name.

## Syntax

```cpp
HRESULT get_ComputerName(
  [out] BSTR *pVal
);
```

## Parameters

*pVal* \[out\]  
Caller-supplied pointer to a location to receive a pointer to a computer name string.

## Return value

This method can return one of these values.

| Return code | Description |
|--|--|
| **S_OK** | The operation succeeded. |
| **E_OUTOFMEMORY** | Out of memory. |

## VBScript Example

```vb
Dim objPrinter, CompName
strPrinter = Session("MS_printer")
Set objPrinter = Server.CreateObject ("OlePrn.AspHelp")
CompName = objPrinter.ComputerName
```

## Requirements

**Target platform:** Desktop
