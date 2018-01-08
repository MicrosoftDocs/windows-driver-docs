---
title: Iasphelp get\_AvgJobSizeUnit method
author: windows-driver-content
description: The AvgJobSizeUnit property enables an ASP Web page to determine the units of the average job size.
MS-HAID:
- 'webfnc\_b7542526-ad13-46d7-a1c1-e02d7832dfb6.xml'
- 'print.iasphelp\_avgjobsizeunit'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: f5a701ff-270f-45f5-8c6e-ecf1b8afab20
keywords: ["get_AvgJobSizeUnit method Print Devices", "get_AvgJobSizeUnit method Print Devices , Iasphelp interface", "Iasphelp interface Print Devices , get_AvgJobSizeUnit method"]
topic_type:
- apiref
api_name:
- Iasphelp.get_AvgJobSizeUnit
api_type:
- COM
---

# Iasphelp::get\_AvgJobSizeUnit method


The **AvgJobSizeUnit** property enables an ASP Web page to determine the units of the average job size.

Syntax
------

```ManagedCPlusPlus
HRESULT get_AvgJobSizeUnit(
  [out] long *pVal
);
```

Parameters
----------

*pVal* \[out\]  
A caller-supplied pointer to a memory location that receives one of the values in the following table. The value indicates the units that are associated with the average job size.

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
<td><p>Units of average job size are in pages per job.</p></td>
</tr>
<tr class="even">
<td><p>2</p></td>
<td><p>Units of average job size are in bytes per job.</p></td>
</tr>
</tbody>
</table>

 

Return value
------------

This method returns S\_OK on success.

### <span id="vbscript_example"></span><span id="VBSCRIPT_EXAMPLE"></span>VBScript Example

Remarks
-------

Query the **Iasphelp::AvgJobSizeUnit** property to determine the units in which the [**Iasphelp::AvgJobSize**](iasphelp-avgjobsize.md) property value is expressed.

Before you query this property, call the [**Iasphelp::CalcJobETA**](iasphelp-calcjobeta.md) method to initialize the property value.

```
    Dim objPrinter, strPrinter, JobUnits
    strPrinter = Session("MS_printer")
    Set objPrinter = Server.CreateObject ("OlePrn.AspHelp")
    objPrinter.Open strPrinter
 objPrinter.CalcJobETA
    JobUnits = objPrinter.AvgJobSizeUnit
    &#39; If JobUnits = 1 then job size is in units of pages
    &#39; If JobUnits = 2 then job size is in units of bytes
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


[**Iasphelp::AvgJobSize**](iasphelp-avgjobsize.md)

[**Iasphelp::CalcJobETA**](iasphelp-calcjobeta.md)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Iasphelp::get_AvgJobSizeUnit%20method%20%20RELEASE:%20%281/8/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


