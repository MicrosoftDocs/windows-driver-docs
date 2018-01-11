---
title: Iasphelp get\_JobCompletionMinute method
author: windows-driver-content
description: The JobCompletionMinute property enables an ASP Web page to determine when the print jobs that are currently pending will be finished.
MS-HAID:
- 'webfnc\_63bca3eb-0ead-4430-8e82-9014d58c133b.xml'
- 'print.iasphelp\_jobcompletionminute'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: e3dba870-84b4-4959-8ed4-102ac82be14b
keywords: ["get_JobCompletionMinute method Print Devices", "get_JobCompletionMinute method Print Devices , Iasphelp interface", "Iasphelp interface Print Devices , get_JobCompletionMinute method"]
topic_type:
- apiref
api_name:
- Iasphelp.get_JobCompletionMinute
api_type:
- COM
---

# Iasphelp::get\_JobCompletionMinute method


The **JobCompletionMinute** property enables an ASP Web page to determine when the print jobs that are currently pending will be finished.

Syntax
------

```ManagedCPlusPlus
HRESULT get_JobCompletionMinute(
  [out] long *pVal
);
```

Parameters
----------

*pVal* \[out\]  
A caller-supplied pointer to a memory location that receives the required time, in minutes, for all print jobs that are currently pending completion.

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

Before you query this property, call the [**Iasphelp::CalcJobETA**](iasphelp-calcjobeta.md) method to initialize the property value. To determine the number of pending print jobs, query the [**Iasphelp::PendingJobCount**](iasphelp-pendingjobcount.md) property.

```
    Dim objPrinter, EndMinute
    strPrinter = Session("MS_printer")
    Set objPrinter = Server.CreateObject ("OlePrn.AspHelp")
    objPrinter.Open strPrinter
    objPrinter.CalcJobETA
    EndMinute = objPrinter.JobCompletionMinute
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

[**Iasphelp::CalcJobETA**](iasphelp-calcjobeta.md)

[**Iasphelp::PendingJobCount**](iasphelp-pendingjobcount.md)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Iasphelp::get_JobCompletionMinute%20method%20%20RELEASE:%20%281/8/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


