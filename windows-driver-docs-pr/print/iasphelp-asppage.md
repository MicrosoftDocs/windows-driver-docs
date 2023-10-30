---
title: Iasphelp get_AspPage method
description: The AspPage property enables an ASP Web page to obtain the directory path to the initial ASP file used for describing printer-specific details.
MS-HAID:
- 'webfnc_6b636ee3-bc4f-4fbd-8ad9-87d6abcf3b35.xml'
- 'print.iasphelp_asppage'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
keywords: ["get_AspPage method Print Devices", "get_AspPage method Print Devices , Iasphelp interface", "Iasphelp interface Print Devices , get_AspPage method"]
topic_type:
- apiref
ms.topic: reference
api_name:
- Iasphelp.get_AspPage
api_type:
- COM
ms.date: 06/23/2023
---

# Iasphelp::get_AspPage method

The **AspPage** property enables an ASP Web page to obtain the directory path to the initial ASP file used for describing printer-specific details.

## Syntax

```cpp
HRESULT get_AspPage(
  [in]  DWORD dwPage,
  [out] BSTR  *pVal
);
```

## Parameters

*dwPage* \[in\]  
Must be 1.

*pVal* \[out\]  
Caller-supplied pointer to a location to receive a size-prefixed Unicode string specifying the directory path to the initial Web page describing printer-specific details.

## Return value

This method can return one of these values.

| Return code | Description |
|--|--|
| **S_OK** | The operation succeeded. |
| **E_HANDLE** | [**Iasphelp::Open**](iasphelp-open.md) method has not been called. |
| **E_NOTIMPL** | An ASP file is not available. |
| **E_POINTER** | Invalid *pVal* pointer. |

## VBScript Example

To determine where to find the page's ASP file, the method uses the algorithm described in [Which Printer Details Page is Displayed?](./which-printer-details-page-is-displayed-.md).

The [**Iasphelp::Open**](iasphelp-open.md) method must be called before the **Iasphelp::AspPage** property can be queried.

```vb
    Dim objPrinter, strPrinter, str
    strPrinter = Session("MS_printer")
    Set objPrinter = Server.CreateObject ("OlePrn.AspHelp")
    objPrinter.Open strPrinter
    str = objPrinter.ASPPage(1)
```

## Requirements

**Target platform:** Desktop

## See also

[**Iasphelp::Open**](iasphelp-open.md)
