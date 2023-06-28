---
title: IOleCvt DecodeUnicodeName method
description: The DecodeUnicodeName property enables an ASP Web page to translate a Unicode string to its ANSI equivalent.
MS-HAID:
- 'webfnc_50fe9203-d31e-4af4-a34f-b32dfd3dd7b1.xml'
- 'print.iolecvt_decodeunicodename'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
keywords: ["DecodeUnicodeName method Print Devices", "DecodeUnicodeName method Print Devices , IOleCvt interface", "IOleCvt interface Print Devices , DecodeUnicodeName method"]
topic_type:
- apiref
ms.topic: reference
api_name:
- IOleCvt.DecodeUnicodeName
api_type:
- COM
ms.date: 06/26/2023
---

# IOleCvt::DecodeUnicodeName method

The **DecodeUnicodeName** property enables an ASP Web page to translate a Unicode string to its ANSI equivalent.

## Syntax

```cpp
[propget, id(3), helpstring("property DecodeUnicodeName")] HRESULT DecodeUnicodeName(
  [in]          BSTR bstrSrcName,
  [out, retval] BSTR *pVal
);
```

## Parameters

*bstrSrcName* \[in\]  
Caller-supplied Unicode string to be translated.

*pVal* \[out, retval\]  
Caller-supplied pointer to a location to receive the translated string.

## Return value

| Return code | Description |
|--|--|
| **S_OK** | The operation succeeded. |
| **E_POINTER** | At least one of the parameters does not point to a valid memory location. |

## VBScript Example

```vb
Dim OleCvt, strPrinter, strEncodedPrinter
Set OleCvt = Server.CreateObject("OlePrn.OleCvt")
strEncodedPrinter = Request ( "eprinter" )
strPrinter = OleCvt.DecodeUnicodeName (strEncodedPrinter)
```

## Requirements

**Target platform:** Desktop
