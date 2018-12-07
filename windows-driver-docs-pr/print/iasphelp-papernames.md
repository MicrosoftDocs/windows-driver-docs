---
title: Iasphelp get\_PaperNames method
description: The PaperNames property enables an ASP Web page to obtain a set of strings that name all the paper forms for the printer.
MS-HAID:
- 'webfnc\_be2b332f-6300-4b3e-9fa7-fd2fd0bdffe5.xml'
- 'print.iasphelp\_papernames'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 558cf0a6-d98b-4d59-ae37-d19ced289bf0
keywords: ["get_PaperNames method Print Devices", "get_PaperNames method Print Devices , Iasphelp interface", "Iasphelp interface Print Devices , get_PaperNames method"]
topic_type:
- apiref
api_name:
- Iasphelp.get_PaperNames
api_type:
- COM
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Iasphelp::get\_PaperNames method

The **PaperNames** property enables an ASP Web page to obtain a set of strings that name all the paper forms for the printer.

Syntax
------

```cpp
HRESULT get_PaperNames(
  [out] VARIANT *pVal
);
```

Parameters
----------

*pVal* \[out\]  
Caller-supplied location to receive a pointer to a set of strings representing all the paper forms for the printer.

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

The handler for this property obtains the list of paper forms by calling the printer driver's [**DrvDeviceCapabilities**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/winddiui/nf-winddiui-drvdevicecapabilities) function with the DC\_PAPERNAMES flag set.

The [**Iasphelp::Open**](iasphelp-open.md) method must be called before the **Iasphelp::PaperNames** property can be queried.

```vb
Dim objPrinter, PaperNameArray
strPrinter = Session("MS_printer")
Set objPrinter = Server.CreateObject ("OlePrn.AspHelp")
objPrinter.Open strPrinter
PaperNameArray = objPrinter.PaperNames
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
