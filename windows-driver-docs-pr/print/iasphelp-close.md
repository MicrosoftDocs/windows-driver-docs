---
title: Iasphelp Close method
description: The Close method enables an ASP Web page to close access to a printer.
MS-HAID:
- 'webfnc_62b91ac5-2f01-44d6-9289-ee2136acacc4.xml'
- 'print.iasphelp_close'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
keywords: ["Close method Print Devices", "Close method Print Devices , Iasphelp interface", "Iasphelp interface Print Devices , Close method"]
topic_type:
- apiref
ms.topic: reference
api_name:
- Iasphelp.Close
api_type:
- COM
ms.date: 06/23/2023
---

# Iasphelp::Close method

The **Close** method enables an ASP Web page to close access to a printer.

## Syntax

```cpp
HRESULT Close();
```

## Parameters

This method has no parameters.

## Return value

The return value is always S_OK.

## VBScript Example

The name of the printer being closed must have been specified in a previous call to the [**Iasphelp::Open**](iasphelp-open.md) method.

```vb
Dim objPrinter
strPrinter = Session("MS_printer")
Set objPrinter = Server.CreateObject ("OlePrn.AspHelp")
objPrinter.Open strPrinter
...
objPrinter.Close
```

## Requirements

**Target platform:** Desktop

## See also

[**Iasphelp::Open**](iasphelp-open.md)
