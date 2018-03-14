---
title: IOleCvt ToUnicode method
author: windows-driver-content
description: The ToUnicode property enables an ASP Web page to convert one Unicode string to another using a specified code page.
MS-HAID:
- 'webfnc\_37f4684f-4af9-4e25-8c5e-6ad63748cf5d.xml'
- 'print.iolecvt\_tounicode'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: e03997f6-e9b5-403e-99da-52504960cb99
keywords: ["ToUnicode method Print Devices", "ToUnicode method Print Devices , IOleCvt interface", "IOleCvt interface Print Devices , ToUnicode method"]
topic_type:
- apiref
api_name:
- IOleCvt.ToUnicode
api_type:
- COM
---

# IOleCvt::ToUnicode method


The **ToUnicode** property enables an ASP Web page to convert one Unicode string to another using a specified code page.

Syntax
------

```ManagedCPlusPlus
[propget, id(4), helpstring("property ToUnicode")] HRESULT ToUnicode(
  [in]          BSTR bstrString,
  [in]          Long lCodePage,
  [out, retval] BSTR *pVal
);
```

Parameters
----------

*bstrString* \[in\]  
Caller-supplied string to be converted.

*lCodePage* \[in\]  
Caller-supplied code page to use for the conversion. For more information, see the following Remarks section.

*pVal* \[out, retval\]  
Caller-supplied pointer to a location to receive the converted Unicode string.

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

 

## <span id="ddk_iolecvt_tounicode_gg"></span><span id="DDK_IOLECVT_TOUNICODE_GG"></span>


### <span id="vbscript_example"></span><span id="VBSCRIPT_EXAMPLE"></span>VBScript Example

Remarks
-------

Set the *lCodePage* parameter to one of the code page identifiers that are defined for the *CodePage* parameter of the **MultiByteToWideChar** function. For more information about this function, see the Windows SDK documentation.

Although most applications now use Unicode (UTF-16) encoding for character data, some Windows desktop applications use character sets based on Windows code pages. A code page assigns international characters to ANSI character codes greater than 127. For more information about code pages, see the Windows SDK documentation.

Convert to Unicode using the Japanese code page, if applicable.

```
If strLang = "JP" Then
    tmpStr = OleCvt.ToUnicode (str, 932)
Else
    tmpStr = str
End If
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
<tr class="even">
<td><p>Version</p></td>
<td><p>Available in Windows 2000 and later versions of the Windows operating systems.</p></td>
</tr>
</tbody>
</table>

 

 




