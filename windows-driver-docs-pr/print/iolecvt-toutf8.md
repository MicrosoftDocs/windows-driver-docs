---
title: IOleCvt ToUtf8 method
description: The ToUtf8 property enables an ASP Web page to translate a string of Unicode characters to the UTF-8 format.
MS-HAID:
- 'webfnc_b88265bd-9013-4c9b-abe2-00010d5b43c3.xml'
- 'print.iolecvt_toutf8'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
keywords: ["ToUtf8 method Print Devices", "ToUtf8 method Print Devices , IOleCvt interface", "IOleCvt interface Print Devices , ToUtf8 method"]
topic_type:
- apiref
ms.topic: reference
api_name:
- IOleCvt.ToUtf8
api_type:
- COM
ms.date: 06/26/2023
---

# IOleCvt::ToUtf8 method

The **ToUtf8** property enables an ASP Web page to translate a string of Unicode characters to the UTF-8 format.

## Syntax

```cpp
[propget, id(1), helpstring("property ToUtf8")] HRESULT ToUtf8(
  [in]          BSTR bstrUnicode,
  [out, retval] BSTR *pVal
);
```

## Parameters

*bstrUnicode* \[in\]  
Caller-supplied string to be converted to UTF-8 format.

*pVal* \[out, retval\]  
Caller supplied pointer to a location that will receive the converted string.

## Return value

| Return code | Description |
|--|--|
| **S_OK** | The operation succeeded. |
| **E_POINTER** | At least one of the parameters does not point to a valid memory location. |

## VBScript Example

UTF-8 is an alternative coded-representation form for all of the characters of the UCS (Universal Multibyte Octet-Coded Character Set). It can be used to transmit text data through communication systems which assume that individual octets in the range 0x00 to 0x7F have a definition according to ISO/IEC 4873, including a C0 set of control functions according to the 8-bit structure of ISO/IEC 2022.

In the following example, function **Write** returns a string converted to UTF-8 format, provided that the global variable `bUTF8` is **TRUE**. Otherwise **Write** returns the unmodified string.

```vb
Function Write (strUnicode)
    If bUTF8 Then
        Write = OleCvt.ToUtf8 (strUnicode)
    Else
        Write = strUnicode
    End If
End Function
```

## Requirements

**Target platform:** Desktop
