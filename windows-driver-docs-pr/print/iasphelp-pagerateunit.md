---
title: Iasphelp get\_PageRateUnit method
description: The PageRateUnit enables an ASP Web page to determine the units in which the page rate is expressed.
MS-HAID:
- 'webfnc\_c3c557fb-2ce9-4260-838a-4bd0e56fb63d.xml'
- 'print.iasphelp\_pagerateunit'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 1b528527-a03a-4fab-b118-5c744759a0a1
keywords: ["get_PageRateUnit method Print Devices", "get_PageRateUnit method Print Devices , Iasphelp interface", "Iasphelp interface Print Devices , get_PageRateUnit method"]
topic_type:
- apiref
api_name:
- Iasphelp.get_PageRateUnit
api_type:
- COM
---

# Iasphelp::get\_PageRateUnit method


The **PageRateUnit** enables an ASP Web page to determine the units in which the page rate is expressed.

Syntax
------

```ManagedCPlusPlus
HRESULT get_PageRateUnit(
  [out] long *pVal
);
```

Parameters
----------

*pVal* \[out\]  
A caller-supplied pointer to a memory location that receives a value that indicates the units used in the page rate. The four possible values are shown in the following table.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Value</th>
<th>Meaning</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>1</p></td>
<td><p>Print rate units are pages per minute.</p></td>
</tr>
<tr class="even">
<td><p>2</p></td>
<td><p>Print rate units are characters per second.</p></td>
</tr>
<tr class="odd">
<td><p>3</p></td>
<td><p>Print rate units are lines per minute.</p></td>
</tr>
<tr class="even">
<td><p>4</p></td>
<td><p>Print rate units are inches per minute.</p></td>
</tr>
</tbody>
</table>

 

These values correspond to the constants PRINTRATEUNIT\_PPM, PRINTRATEUNIT\_CPS, PRINTRATEUNIT\_LPM, and PRINTRATEUNIT\_IPM, which are defined in the Wingdi.h header file. For more information about these constants, see the description of the **DeviceCapabilities** function in the Windows SDK documentation.

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

 

### <span id="vbscript_example"></span><span id="VBSCRIPT_EXAMPLE"></span>VBScript Example

Remarks
-------

Query this property to determine the units in which the [**Iasphelp::PageRate**](iasphelp-pagerate.md) property value is expressed.

The [**Iasphelp::Open**](iasphelp-open.md) method must be called before the **Iasphelp::PageRateUnit** property can be queried.

```
    Dim objPrinter, PtrPageRateUnit
    strPrinter = Session("MS_printer")
    Set objPrinter = Server.CreateObject ("OlePrn.AspHelp")
    objPrinter.Open strPrinter
    PtrPageRate = objPrinter.PageRateUnit
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


[**Iasphelp::PageRate**](iasphelp-pagerate.md)

[**Iasphelp::Open**](iasphelp-open.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Iasphelp::get_PageRateUnit%20method%20%20RELEASE:%20%281/8/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





