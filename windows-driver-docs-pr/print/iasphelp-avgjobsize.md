---
title: Iasphelp get\_AvgJobSize method
description: The AvgJobSize property enables an ASP Web page to determine the average job size in a sequence of print jobs.
MS-HAID:
- 'webfnc\_de863905-eb8f-430a-a70b-7cb404dd3717.xml'
- 'print.iasphelp\_avgjobsize'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 3373376f-c904-47dd-8502-c2c26caed3be
keywords: ["get_AvgJobSize method Print Devices", "get_AvgJobSize method Print Devices , Iasphelp interface", "Iasphelp interface Print Devices , get_AvgJobSize method"]
topic_type:
- apiref
api_name:
- Iasphelp.get_AvgJobSize
api_type:
- COM
---

# Iasphelp::get\_AvgJobSize method


The **AvgJobSize** property enables an ASP Web page to determine the average job size in a sequence of print jobs.

Syntax
------

```ManagedCPlusPlus
HRESULT get_AvgJobSize(
  [out] long *pVal
);
```

Parameters
----------

*pVal* \[out\]  
A caller-supplied pointer to a memory location that receives the average job size. For more information about this parameter, see the following Remarks section.

Return value
------------

This method returns S\_OK on success.

### <span id="vbscript_example"></span><span id="VBSCRIPT_EXAMPLE"></span>VBScript Example

Remarks
-------

The average job size can be expressed as either the number of pages per job or the number of bytes per job. Use the [**Iasphelp::AvgJobSizeUnit**](iasphelp-avgjobsizeunit.md) property to determine which unit applies to the **Iasphelp::AvgJobSize** property.

Before you query this property, call the [**Iasphelp::CalcJobETA**](iasphelp-calcjobeta.md) method to initialize the property value.

```
    Dim objPrinter, strPrinter, JobSizeAvg
    strPrinter = Session("MS_printer")
    Set objPrinter = Server.CreateObject ("OlePrn.AspHelp")
    objPrinter.Open strPrinter
 objPrinter.CalcJobETA
    JobSizeAvg = objPrinter.AvgJobSize
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


[**Iasphelp::AvgJobSizeUnit**](iasphelp-avgjobsizeunit.md)

[**Iasphelp::CalcJobETA**](iasphelp-calcjobeta.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Iasphelp::get_AvgJobSize%20method%20%20RELEASE:%20%281/8/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





