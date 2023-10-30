---
title: Iasphelp get_ErrorDscp method
description: The ErrorDscp property enables an ASP Web page to convert an error code to a descriptive string.
MS-HAID:
- 'webfnc_55f547fe-4cbe-4905-b268-afd7af400de4.xml'
- 'print.iasphelp_errordscp'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
keywords: ["get_ErrorDscp method Print Devices", "get_ErrorDscp method Print Devices , Iasphelp interface", "Iasphelp interface Print Devices , get_ErrorDscp method"]
topic_type:
- apiref
ms.topic: reference
api_name:
- Iasphelp.get_ErrorDscp
api_type:
- COM
ms.date: 06/23/2023
---

# Iasphelp::get_ErrorDscp method

The **ErrorDscp** property enables an ASP Web page to convert an error code to a descriptive string.

## Syntax

```cpp
HRESULT get_ErrorDscp(
  [in]  long lErrCode,
  [out] BSTR *pVal
);
```

## Parameters

*lErrCode* \[in\]  
Specifies the error code to be converted to a descriptive string.

*pVal* \[out\]  
A caller-supplied pointer to a location that receives the descriptive string that corresponds to the error code in the *lErrCode* parameter.

## Return value

Win32 error codes can also be returned.

| Return code | Description |
|--|--|
| **S_OK** | The operation succeeded. |
| **E_HANDLE** | The **Iasphelp::Open** method has not been called. |
| **E_POINTER** | Invalid *pVal* pointer. |
| **E_OUTOFMEMORY** | Out of memory. |

## VBScript Example

The [**Iasphelp::Open**](iasphelp-open.md) method must be called before the **Iasphelp::ErrorDscp** property can be queried.

```vb
Dim objPrinter, ErrorCode, ErrorString
strPrinter = Session("MS_printer")
Set objPrinter = Server.CreateObject ("OlePrn.AspHelp")
objPrinter.Open strPrinter
...
' Get error code.
...
ErrorString = objPrinter.ErrorDscp(ErrorCode)
```

## Requirements

**Target platform:** Desktop

## See also

[**Iasphelp::Open**](iasphelp-open.md)
