---
title: Iasphelp Open method
description: The Open method enables an ASP Web page to open access to a printer.
MS-HAID:
- 'webfnc_7fa3a36d-4bf6-46d2-9336-e024d3aa1eec.xml'
- 'print.iasphelp_open'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
keywords: ["Open method Print Devices", "Open method Print Devices , Iasphelp interface", "Iasphelp interface Print Devices , Open method"]
topic_type:
- apiref
ms.topic: reference
api_name:
- Iasphelp.Open
api_type:
- COM
ms.date: 06/26/2023
---

# Iasphelp::Open method

The **Open** method enables an ASP Web page to open access to a printer.

## Syntax

```cpp
HRESULT Open(
  [in] BSTR bstrPrinterName
);
```

## Parameters

*bstrPrinterName* \[in\]  
Caller-supplied pointer to a string containing a printer name.

## Return value

Win32 error codes can also be returned.

| Return code | Description |
|--|--|
| **S_OK** | The operation succeeded. |
| **ERROR_INVALID_PRINTER_NAME** | Invalid printer name. |
| **ERROR_NOT_ENOUGH_MEMORY** | Out of memory. |

## VBScript Example

This method obtains access to the specified printer by calling the print spooler's **OpenPrinter** function. For more information about this function, see the Windows SDK Documentation.

After the **Iasphelp::Open** call, the printer remains open until the [**Iasphelp::Close**](iasphelp-close.md) method is called, or until **Iasphelp::Open** is called again with a different printer name.

```vb
Dim objPrinter
strPrinter = Session("MS_printer")
Set objPrinter = Server.CreateObject ("OlePrn.AspHelp")
objPrinter.Open strPrinter
```

## Requirements

**Target platform:** Desktop

## See also

[**Iasphelp::Close**](iasphelp-close.md)
