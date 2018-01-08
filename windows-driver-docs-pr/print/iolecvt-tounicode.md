---
title: IOleCvt ToUnicode method
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20IOleCvt::ToUnicode%20method%20%20RELEASE:%20%281/8/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




