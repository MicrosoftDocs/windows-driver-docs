---
title: Iasphelp get\_AvgJobSize method
author: windows-driver-content
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
ms.localizationpriority: medium
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

```cpp
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

## See also


[**Iasphelp::AvgJobSizeUnit**](iasphelp-avgjobsizeunit.md)

[**Iasphelp::CalcJobETA**](iasphelp-calcjobeta.md)

 

 




