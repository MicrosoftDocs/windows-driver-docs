---
title: Iasphelp get\_MediaReady method
description: The MediaReady property enables an ASP Web page to obtain a set of strings that name all of the paper forms for the printer that are currently available for use.
MS-HAID:
- 'webfnc\_b10e8434-7e12-4bb5-8c43-77cb890f72a8.xml'
- 'print.iasphelp\_mediaready'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 1e90649a-6075-4b78-93fd-781c3e363b5f
keywords: ["get_MediaReady method Print Devices", "get_MediaReady method Print Devices , Iasphelp interface", "Iasphelp interface Print Devices , get_MediaReady method"]
topic_type:
- apiref
api_name:
- Iasphelp.get_MediaReady
api_type:
- COM
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Iasphelp::get\_MediaReady method

The **MediaReady** property enables an ASP Web page to obtain a set of strings that name all of the paper forms for the printer that are currently available for use.

Syntax
------

```cpp
HRESULT get_MediaReady(
  [out] VARIANT *pVal
);
```

Parameters
----------

*pVal* \[out\]  
A caller-supplied location to receive a pointer to a set of strings that name all of the paper forms for a printer that are currently available for use.

Return value
------------

This property returns one of the values in the following table.

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
<td><strong>E_OUTOFMEMORY</strong></td>
<td><p>Out of memory.</p></td>
</tr>
</tbody>
</table>

## VBScript Example

This method obtains a list of the names of the paper forms that are currently available for use by calling the printer driver's [**DrvDeviceCapabilities**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/winddiui/nf-winddiui-drvdevicecapabilities) function with the DC\_MEDIAREADY flag set.

The [**Iasphelp::Open**](iasphelp-open.md) method must be called before the **Iasphelp::MediaReady** property can be queried.

```vb
Dim objPrinter, MediaReadyArray
strPrinter = Session("MS_printer")
Set objPrinter = Server.CreateObject ("OlePrn.AspHelp")
objPrinter.Open strPrinter
MediaReadyArray = objPrinter.MediaReady
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

[**DrvDeviceCapabilities**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/winddiui/nf-winddiui-drvdevicecapabilities)

[**Iasphelp::Open**](iasphelp-open.md)
