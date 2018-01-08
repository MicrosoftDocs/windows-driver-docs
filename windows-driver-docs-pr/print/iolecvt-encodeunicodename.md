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
---

# IOleCvt::EncodeUnicodeName method


The **EncodeUnicodeName** property enables an ASP Web page to translate an ANSI string to its Unicode equivalent.

Syntax
------

```ManagedCPlusPlus
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

 

## <span id="ddk_iolecvt_encodeunicodename_gg"></span><span id="DDK_IOLECVT_ENCODEUNICODENAME_GG"></span>


### <span id="vbscript_example"></span><span id="VBSCRIPT_EXAMPLE"></span>VBScript Example

Remarks
-------

```
    Dim OleCvt, strPrinter, strEncodedPrinter
    Set OleCvt = Server.CreateObject("OlePrn.OleCvt")
    strMyUrl = "MyPage.asp?MyVariable=" &amp; 
                OleCvt.EncodeUnicodeName("My&amp;Unicode&amp;Parameter")
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20IOleCvt::EncodeUnicodeName%20method%20%20RELEASE:%20%281/8/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




