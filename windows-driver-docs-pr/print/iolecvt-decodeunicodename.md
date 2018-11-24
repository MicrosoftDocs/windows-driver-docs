---
title: IOleCvt DecodeUnicodeName method
description: The DecodeUnicodeName property enables an ASP Web page to translate a Unicode string to its ANSI equivalent.
MS-HAID:
- 'webfnc\_50fe9203-d31e-4af4-a34f-b32dfd3dd7b1.xml'
- 'print.iolecvt\_decodeunicodename'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: d00fdabd-611a-4f26-8ca5-21ba8c28d993
keywords: ["DecodeUnicodeName method Print Devices", "DecodeUnicodeName method Print Devices , IOleCvt interface", "IOleCvt interface Print Devices , DecodeUnicodeName method"]
topic_type:
- apiref
api_name:
- IOleCvt.DecodeUnicodeName
api_type:
- COM
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# IOleCvt::DecodeUnicodeName method

The **DecodeUnicodeName** property enables an ASP Web page to translate a Unicode string to its ANSI equivalent.

Syntax
------

```cpp
[propget, id(3), helpstring("property DecodeUnicodeName")] HRESULT DecodeUnicodeName(
  [in]          BSTR bstrSrcName,
  [out, retval] BSTR *pVal
);
```

Parameters
----------

*bstrSrcName* \[in\]  
Caller-supplied Unicode string to be translated.

*pVal* \[out, retval\]  
Caller-supplied pointer to a location to receive the translated string.

Return value
------------

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
<td><strong>E_POINTER</strong></td>
<td><p>At least one of the parameters does not point to a valid memory location.</p></td>
</tr>
</tbody>
</table>

## VBScript Example

```vb
Dim OleCvt, strPrinter, strEncodedPrinter
Set OleCvt = Server.CreateObject("OlePrn.OleCvt")
strEncodedPrinter = Request ( "eprinter" )
strPrinter = OleCvt.DecodeUnicodeName (strEncodedPrinter)
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
