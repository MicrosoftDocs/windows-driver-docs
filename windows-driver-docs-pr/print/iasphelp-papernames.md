---
title: Iasphelp get_PaperNames method
description: The PaperNames property enables an ASP Web page to obtain a set of strings that name all the paper forms for the printer.
MS-HAID:
- 'webfnc_be2b332f-6300-4b3e-9fa7-fd2fd0bdffe5.xml'
- 'print.iasphelp_papernames'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
keywords: ["get_PaperNames method Print Devices", "get_PaperNames method Print Devices , Iasphelp interface", "Iasphelp interface Print Devices , get_PaperNames method"]
topic_type:
- apiref
ms.topic: reference
api_name:
- Iasphelp.get_PaperNames
api_type:
- COM
ms.date: 06/26/2023
---

# Iasphelp::get_PaperNames method

The **PaperNames** property enables an ASP Web page to obtain a set of strings that name all the paper forms for the printer.

## Syntax

```cpp
HRESULT get_PaperNames(
  [out] VARIANT *pVal
);
```

## Parameters

*pVal* \[out\]  
Caller-supplied location to receive a pointer to a set of strings representing all the paper forms for the printer.

## Return value

This property returns one of the values in the following table.

| Return code | Description |
|--|--|
| **S_OK** | The operation succeeded. |
| **E_HANDLE** | The [**Iasphelp::Open**](iasphelp-open.md) method has not been called. |
| **E_OUTOFMEMORY** | Out of memory. |

## VBScript Example

The handler for this property obtains the list of paper forms by calling the printer driver's [**DrvDeviceCapabilities**](/windows-hardware/drivers/ddi/winddiui/nf-winddiui-drvdevicecapabilities) function with the DC_PAPERNAMES flag set.

The [**Iasphelp::Open**](iasphelp-open.md) method must be called before the **Iasphelp::PaperNames** property can be queried.

```vb
Dim objPrinter, PaperNameArray
strPrinter = Session("MS_printer")
Set objPrinter = Server.CreateObject ("OlePrn.AspHelp")
objPrinter.Open strPrinter
PaperNameArray = objPrinter.PaperNames
```

## Requirements

**Target platform:** Desktop

## See also

[**DrvDeviceCapabilities**](/windows-hardware/drivers/ddi/winddiui/nf-winddiui-drvdevicecapabilities)

[**Iasphelp::Open**](iasphelp-open.md)
