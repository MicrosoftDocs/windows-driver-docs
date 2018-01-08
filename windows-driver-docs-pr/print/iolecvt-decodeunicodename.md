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
---

# IOleCvt::DecodeUnicodeName method


The **DecodeUnicodeName** property enables an ASP Web page to translate a Unicode string to its ANSI equivalent.

Syntax
------

```ManagedCPlusPlus
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

 

## <span id="ddk_iolecvt_decodeunicodename_gg"></span><span id="DDK_IOLECVT_DECODEUNICODENAME_GG"></span>


### <span id="vbscript_example"></span><span id="VBSCRIPT_EXAMPLE"></span>VBScript Example

Remarks
-------

```
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
<tr class="even">
<td><p>Version</p></td>
<td><p>Available in Windows 2000 and later versions of the Windows operating systems.</p></td>
</tr>
</tbody>
</table>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20IOleCvt::DecodeUnicodeName%20method%20%20RELEASE:%20%281/8/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




