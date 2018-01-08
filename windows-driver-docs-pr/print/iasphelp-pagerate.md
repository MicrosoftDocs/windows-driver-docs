---
title: Iasphelp get\_PageRate method
description: The PageRate property enables an ASP Web page to determine a printer's page rate.
MS-HAID:
- 'webfnc\_f356953e-ac15-4948-9a6e-b83d3aec8e7b.xml'
- 'print.iasphelp\_pagerate'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 010f4871-f64f-465f-a78b-a86f91a9f194
keywords: ["get_PageRate method Print Devices", "get_PageRate method Print Devices , Iasphelp interface", "Iasphelp interface Print Devices , get_PageRate method"]
topic_type:
- apiref
api_name:
- Iasphelp.get_PageRate
api_type:
- COM
---

# Iasphelp::get\_PageRate method


The **PageRate** property enables an ASP Web page to determine a printer's page rate.

Syntax
------

```ManagedCPlusPlus
HRESULT get_PageRate(
  [out] long *pVal
);
```

Parameters
----------

*pVal* \[out\]  
A caller-supplied location to receive a numeric value that represents the page rate for the printer. The units in which the page rate is expressed might depend on the printer. For more information about page rates, see the following Remarks section.

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
<td><p>The [<strong>Iasphelp::Open</strong>](iasphelp-open.md) method has not been called.</p></td>
</tr>
<tr class="odd">
<td><strong>E_OUTOFMEMORY</strong></td>
<td><p>Out of memory.</p></td>
</tr>
</tbody>
</table>

 

## <span id="ddk_iasphelp_pagerate_gg"></span><span id="DDK_IASPHELP_PAGERATE_GG"></span>


### <span id="vbscript_example"></span><span id="VBSCRIPT_EXAMPLE"></span>VBScript Example

Remarks
-------

To determine the units in which the page rate is measured, query the [**Iasphelp::PageRateUnit**](iasphelp-pagerateunit.md) property.

The [**Iasphelp::Open**](iasphelp-open.md) method must be called before the **Iasphelp::PageRate** property can be queried.

```
    Dim objPrinter, PtrPageRate
    strPrinter = Session("MS_printer")
    Set objPrinter = Server.CreateObject ("OlePrn.AspHelp")
    objPrinter.Open strPrinter
    PtrPageRate = objPrinter.PageRate
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


[**Iasphelp::PageRateUnit**](iasphelp-pagerateunit.md)

[**Iasphelp::Open**](iasphelp-open.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Iasphelp::get_PageRate%20method%20%20RELEASE:%20%281/8/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





