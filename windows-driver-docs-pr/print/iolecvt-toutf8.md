---
title: IOleCvt ToUtf8 method
author: windows-driver-content
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
---

# IOleCvt::ToUtf8 method


The **ToUtf8** property enables an ASP Web page to translate a string of Unicode characters to the UTF-8 format.

Syntax
------

```ManagedCPlusPlus
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

 

## <span id="ddk_iolecvt_toutf8_gg"></span><span id="DDK_IOLECVT_TOUTF8_GG"></span>


### <span id="vbscript_example"></span><span id="VBSCRIPT_EXAMPLE"></span>VBScript Example

Remarks
-------

UTF-8 is an alternative coded-representation form for all of the characters of the UCS (Universal Multibyte Octet-Coded Character Set). It can be used to transmit text data through communication systems which assume that individual octets in the range 0x00 to 0x7F have a definition according to ISO/IEC 4873, including a C0 set of control functions according to the 8-bit structure of ISO/IEC 2022.

In the following example, function **Write** returns a string converted to UTF-8 format, provided that the global variable `bUTF8` is **TRUE**. Otherwise **Write** returns the unmodified string.

```
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
<tr class="even">
<td><p>Version</p></td>
<td><p>Available in Windows 2000 and later versions of the Windows operating systems.</p></td>
</tr>
</tbody>
</table>

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20IOleCvt::ToUtf8%20method%20%20RELEASE:%20%281/8/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


