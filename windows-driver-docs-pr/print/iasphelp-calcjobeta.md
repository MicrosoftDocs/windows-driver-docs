---
title: Iasphelp CalcJobETA method
author: windows-driver-content
description: The CalcJobETA method enables an ASP Web page to calculate the time at which a print job is to be completed.
MS-HAID:
- 'webfnc\_65577773-9d44-429e-a2fe-eb1a1475b7f6.xml'
- 'print.iasphelp\_calcjobeta'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: cdf4d590-c236-4ed7-a071-fd0ddbb78590
keywords: ["CalcJobETA method Print Devices", "CalcJobETA method Print Devices , Iasphelp interface", "Iasphelp interface Print Devices , CalcJobETA method"]
topic_type:
- apiref
api_name:
- Iasphelp.CalcJobETA
api_type:
- COM
---

# Iasphelp::CalcJobETA method


The **CalcJobETA** method enables an ASP Web page to calculate the time at which a print job is to be completed.

Syntax
------

```ManagedCPlusPlus
HRESULT CalcJobETA();
```

Parameters
----------

This method has no parameters.

Return value
------------

The following table shows possible return values for this method.

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
<td><p>The method succeeded.</p></td>
</tr>
<tr class="even">
<td><strong>E_HANDLE</strong></td>
<td><p>The <strong>Iasphelp::Open</strong> method has not been called.</p></td>
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

The **CalcJobETA** method calculates print job information that can be subsequently retrieved by using Iasphelp properties. Call **CalcJobETA** before getting any of the following properties:

[**Iasphelp::JobCompletionMinute**](iasphelp-jobcompletionminute.md)

[**Iasphelp::PendingJobCount**](iasphelp-pendingjobcount.md)

[**Iasphelp::AvgJobSize**](iasphelp-avgjobsize.md)

[**Iasphelp::AvgJobSizeUnit**](iasphelp-avgjobsizeunit.md)

Before **CalcJobETA** is called, the value of any of these properties is zero. If **CalcJobETA** determines that the printer rate is not available for the current printer, a subsequent call to JobCompletionMinute retrieves the value -1.

The [**Iasphelp::Open**](iasphelp-open.md) method must be called before the **CalcJobETA** method can be called.

```
    Dim objPrinter
    strPrinter = Session("MS_printer")
    Set objPrinter = Server.CreateObject ("OlePrn.AspHelp")
    objPrinter.Open strPrinter
    objPrinter.CalcJobETA
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


[**Iasphelp::JobCompletionMinute**](iasphelp-jobcompletionminute.md)

[**Iasphelp::PendingJobCount**](iasphelp-pendingjobcount.md)

[**Iasphelp::AvgJobSize**](iasphelp-avgjobsize.md)

[**Iasphelp::AvgJobSizeUnit**](iasphelp-avgjobsizeunit.md)

[**Iasphelp::Open**](iasphelp-open.md)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Iasphelp::CalcJobETA%20method%20%20RELEASE:%20%281/8/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


