---
title: Iasphelp get\_ErrorDscp method
description: The ErrorDscp property enables an ASP Web page to convert an error code to a descriptive string.
MS-HAID:
- 'webfnc\_55f547fe-4cbe-4905-b268-afd7af400de4.xml'
- 'print.iasphelp\_errordscp'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 46d44c54-4fd5-489f-9624-1df3c8917237
keywords: ["get_ErrorDscp method Print Devices", "get_ErrorDscp method Print Devices , Iasphelp interface", "Iasphelp interface Print Devices , get_ErrorDscp method"]
topic_type:
- apiref
api_name:
- Iasphelp.get_ErrorDscp
api_type:
- COM
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Iasphelp::get\_ErrorDscp method

The **ErrorDscp** property enables an ASP Web page to convert an error code to a descriptive string.

Syntax
------

```cpp
HRESULT get_ErrorDscp(
  [in]  long lErrCode,
  [out] BSTR *pVal
);
```

Parameters
----------

*lErrCode* \[in\]  
Specifies the error code to be converted to a descriptive string.

*pVal* \[out\]  
A caller-supplied pointer to a location that receives the descriptive string that corresponds to the error code in the *lErrCode* parameter.

Return value
------------

Win32 error codes can also be returned.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Return code</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>S_OK</strong></td>
<td><p>The operation succeeded.</p></td>
</tr>
<tr class="even">
<td><strong>E_HANDLE</strong></td>
<td><p>The <strong>Iasphelp::Open</strong> method has not been called.</p></td>
</tr>
<tr class="odd">
<td><strong>E_POINTER</strong></td>
<td><p>Invalid <em>pVal</em> pointer.</p></td>
</tr>
<tr class="even">
<td><strong>E_OUTOFMEMORY</strong></td>
<td><p>Out of memory.</p></td>
</tr>
</tbody>
</table>

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

Requirements
------------

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Target platform</p></td>
<td>Desktop</td>
</tr>
</tbody>
</table>

## See also

[**Iasphelp::Open**](iasphelp-open.md)
