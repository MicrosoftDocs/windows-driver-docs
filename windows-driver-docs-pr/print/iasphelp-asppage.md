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
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Iasphelp::get\_AspPage method


The **AspPage** property enables an ASP Web page to obtain the directory path to the initial ASP file used for describing printer-specific details.

Syntax
------

```cpp
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
<td><p>The <a href="iasphelp-open.md" data-raw-source="[&lt;strong&gt;Iasphelp::Open&lt;/strong&gt;](iasphelp-open.md)"><strong>Iasphelp::Open</strong></a> method has not been called.</p></td>
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

## VBScript Example

To determine where to find the page's ASP file, the method uses the algorithm described in [Which Printer Details Page is Displayed?](https://docs.microsoft.com/windows-hardware/drivers/print/which-printer-details-page-is-displayed-).

The [**Iasphelp::Open**](iasphelp-open.md) method must be called before the **Iasphelp::AspPage** property can be queried.

```vb
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
</tbody>
</table>

## See also

[**Iasphelp::Open**](iasphelp-open.md)
