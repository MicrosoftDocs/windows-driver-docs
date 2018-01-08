---
title: Iasphelp get\_AspPage method
description: The AspPage property enables an ASP Web page to obtain the directory path to the initial ASP file used for describing printer-specific details.
MS-HAID:
- 'webfnc\_6b636ee3-bc4f-4fbd-8ad9-87d6abcf3b35.xml'
- 'print.iasphelp\_asppage'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 325c0666-b4c4-48b5-b14f-bdb81e1ee5d2
keywords: ["get_AspPage method Print Devices", "get_AspPage method Print Devices , Iasphelp interface", "Iasphelp interface Print Devices , get_AspPage method"]
topic_type:
- apiref
api_name:
- Iasphelp.get_AspPage
api_type:
- COM
---

# Iasphelp::get\_AspPage method


The **AspPage** property enables an ASP Web page to obtain the directory path to the initial ASP file used for describing printer-specific details.

Syntax
------

```ManagedCPlusPlus
HRESULT get_AspPage(
  [in]  DWORD dwPage,
  [out] BSTR  *pVal
);
```

Parameters
----------

*dwPage* \[in\]  
Must be 1.

*pVal* \[out\]  
Caller-supplied pointer to a location to receive a size-prefixed Unicode string specifying the directory path to the initial Web page describing printer-specific details.

Return value
------------

This method can return one of these values.

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
<td><p>The [<strong>Iasphelp::Open</strong>](iasphelp-open.md) method has not been called.</p></td>
</tr>
<tr class="odd">
<td><strong>E_NOTIMPL</strong></td>
<td><p>An ASP file is not available.</p></td>
</tr>
<tr class="even">
<td><strong>E_POINTER</strong></td>
<td><p>Invalid <em>pVal</em> pointer.</p></td>
</tr>
</tbody>
</table>

 

## <span id="ddk_iasphelp_asppage_gg"></span><span id="DDK_IASPHELP_ASPPAGE_GG"></span>


### <span id="vbscript_example"></span><span id="VBSCRIPT_EXAMPLE"></span>VBScript Example

Remarks
-------

To determine where to find the page's ASP file, the method uses the algorithm described in [Which Printer Details Page is Displayed?](https://msdn.microsoft.com/library/windows/hardware/ff563765).

The [**Iasphelp::Open**](iasphelp-open.md) method must be called before the **Iasphelp::AspPage** property can be queried.

```
    Dim objPrinter, strPrinter, str
    strPrinter = Session("MS_printer")
    Set objPrinter = Server.CreateObject ("OlePrn.AspHelp")
    objPrinter.Open strPrinter
    str = objPrinter.ASPPage(1)
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

## <span id="see_also"></span>See also


[**Iasphelp::Open**](iasphelp-open.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Iasphelp::get_AspPage%20method%20%20RELEASE:%20%281/8/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





