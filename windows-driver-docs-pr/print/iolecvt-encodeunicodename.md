---
title: IOleCvt EncodeUnicodeName method
description: The EncodeUnicodeName property enables an ASP Web page to translate an ANSI string to its Unicode equivalent.
MS-HAID:
- 'webfnc\_e31e8dae-76bb-4250-9d16-090a987c0dbf.xml'
- 'print.iolecvt\_encodeunicodename'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 326a9374-7ed5-4521-999a-2c4c59faa617
keywords: ["EncodeUnicodeName method Print Devices", "EncodeUnicodeName method Print Devices , IOleCvt interface", "IOleCvt interface Print Devices , EncodeUnicodeName method"]
topic_type:
- apiref
api_name:
- IOleCvt.EncodeUnicodeName
api_type:
- COM
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# IOleCvt::EncodeUnicodeName method

The **EncodeUnicodeName** property enables an ASP Web page to translate an ANSI string to its Unicode equivalent.

Syntax
------

```cpp
[propget, id(2), helpstring("property EncodeUnicodeName")] HRESULT EncodeUnicodeName(
  [in]          BSTR bstrSrcName,
  [out, retval] BSTR *pVal
);
```

Parameters
----------

*bstrSrcName* \[in\]  
Caller-supplied ANSI string to be translated.

*pVal* \[out, retval\]  
Caller supplied pointer to a location that will receive the translated string.

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
strMyUrl = "MyPage.asp?MyVariable=" & 
            OleCvt.EncodeUnicodeName("My&Unicode&Parameter")
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
