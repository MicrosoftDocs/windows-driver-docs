---
title: IOleCvt ToUtf8 method
description: The ToUtf8 property enables an ASP Web page to translate a string of Unicode characters to the UTF-8 format.
MS-HAID:
- 'webfnc\_b88265bd-9013-4c9b-abe2-00010d5b43c3.xml'
- 'print.iolecvt\_toutf8'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 1c20041f-b05d-4158-8838-650d25118c65
keywords: ["ToUtf8 method Print Devices", "ToUtf8 method Print Devices , IOleCvt interface", "IOleCvt interface Print Devices , ToUtf8 method"]
topic_type:
- apiref
api_name:
- IOleCvt.ToUtf8
api_type:
- COM
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# IOleCvt::ToUtf8 method

The **ToUtf8** property enables an ASP Web page to translate a string of Unicode characters to the UTF-8 format.

Syntax
------

```cpp
[propget, id(1), helpstring("property ToUtf8")] HRESULT ToUtf8(
  [in]          BSTR bstrUnicode,
  [out, retval] BSTR *pVal
);
```

Parameters
----------

*bstrUnicode* \[in\]  
Caller-supplied string to be converted to UTF-8 format.

*pVal* \[out, retval\]  
Caller supplied pointer to a location that will receive the converted string.

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
