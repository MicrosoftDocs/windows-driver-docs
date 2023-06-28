---
title: Iasphelp getLongPaperName method
description: The LongPaperName property enables an ASP Web page to convert a short paper name to a long paper name.
MS-HAID:
- 'webfnc17250b54-29f4-41c5-bdf2-b72e0823d8e4.xml'
- 'print.iasphelplongpapername'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
keywords: ["get_LongPaperName method Print Devices", "get_LongPaperName method Print Devices , Iasphelp interface", "Iasphelp interface Print Devices , get_LongPaperName method"]
topic_type:
- apiref
ms.topic: reference
api_name:
- Iasphelp.get_LongPaperName
api_type:
- COM
ms.date: 06/23/2023
---

# Iasphelp::getLongPaperName method

The **LongPaperName** property enables an ASP Web page to convert a short paper name to a long paper name.

## Syntax

```cpp
HRESULT get_LongPaperName(
  [in]  BSTR bstrShortName,
  [out] BSTR *pVal
);
```

## Parameters

*bstrShortName* \[in\]  
A caller-supplied pointer to a string that contains a short paper name.

*pVal* \[out\]  
A caller-supplied location to receive a pointer to a string that contains a long paper name.

## Return value

Win32 error codes can also be returned.

| Return code | Description |
|--|--|
| **S_OK** | The operation succeeded. |
| **E_POINTER** | At least one of the parameters does not point to a valid memory location. |
| **E_OUTOFMEMORY** | Out of memory. |

## VBScript Example

```vb
Dim objPrinter, LongName
Set objPrinter = Server.CreateObject ("OlePrn.AspHelp")
LongName = objPrinter.LongPaperName("iso-a0")
```

## Requirements

**Target platform:** Desktop
