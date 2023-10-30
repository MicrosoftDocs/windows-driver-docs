---
title: IOleCvt EncodeUnicodeName method
description: The EncodeUnicodeName property enables an ASP Web page to translate an ANSI string to its Unicode equivalent.
MS-HAID:
- 'webfnc_e31e8dae-76bb-4250-9d16-090a987c0dbf.xml'
- 'print.iolecvt_encodeunicodename'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
keywords: ["EncodeUnicodeName method Print Devices", "EncodeUnicodeName method Print Devices , IOleCvt interface", "IOleCvt interface Print Devices , EncodeUnicodeName method"]
topic_type:
- apiref
ms.topic: reference
api_name:
- IOleCvt.EncodeUnicodeName
api_type:
- COM
ms.date: 04/20/2017
---

# IOleCvt::EncodeUnicodeName method

The **EncodeUnicodeName** property enables an ASP Web page to translate an ANSI string to its Unicode equivalent.

## Syntax

```cpp
[propget, id(2), helpstring("property EncodeUnicodeName")] HRESULT EncodeUnicodeName(
  [in]          BSTR bstrSrcName,
  [out, retval] BSTR *pVal
);
```

## Parameters

*bstrSrcName* \[in\]  
Caller-supplied ANSI string to be translated.

*pVal* \[out, retval\]  
Caller supplied pointer to a location that will receive the translated string.

## Return value

| Return code | Description |
|--|--|
| **S_OK** | The operation succeeded. |
| **E_POINTER** | At least one of the parameters does not point to a valid memory location. |

## VBScript Example

```vb
Dim OleCvt, strPrinter, strEncodedPrinter
Set OleCvt = Server.CreateObject("OlePrn.OleCvt")
strMyUrl = "MyPage.asp?MyVariable=" & 
            OleCvt.EncodeUnicodeName("My&Unicode&Parameter")
```

## Requirements

**Target platform:** Desktop
