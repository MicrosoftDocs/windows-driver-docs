---
title: WDF Device Object Macros
description: This section documents macros that support WDF device objects.
ms.assetid: D91C16EB-5E31-4AB2-984E-A0B35C3B1BA1
ms.date: 08/23/2017
ms.localizationpriority: medium
---

# WDF Device Object Macros


This section documents macros that support WDF device objects.

## In this section


<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Topic</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p><a href="wdfdeviceresumeidlewithtag.md" data-raw-source="[&lt;strong&gt;WdfDeviceResumeIdleWithTag method&lt;/strong&gt;](wdfdeviceresumeidlewithtag.md)"><strong>WdfDeviceResumeIdleWithTag method</strong></a></p></td>
<td><div class="alert">
<strong>Note</strong>  Applies to KMDF and UMDF
</div>
<div>
 
</div>
<p>The <a href="wdfdeviceresumeidlewithtag.md" data-raw-source="[&lt;strong&gt;WdfDeviceResumeIdleWithTag&lt;/strong&gt;](wdfdeviceresumeidlewithtag.md)"><strong>WdfDeviceResumeIdleWithTag</strong></a> macro decrements the power reference count for a specified framework device object and assigns the driver&#39;s current file name and line number to the reference. The macro also assigns a tag value to the reference.</p></td>
</tr>
<tr class="even">
<td><p><a href="wdfdevicestopidlewithtag.md" data-raw-source="[&lt;strong&gt;WdfDeviceStopIdleWithTag method&lt;/strong&gt;](wdfdevicestopidlewithtag.md)"><strong>WdfDeviceStopIdleWithTag method</strong></a></p></td>
<td><div class="alert">
<strong>Note</strong>  Applies to KMDF and UMDF
</div>
<div>
 
</div>
<p>The <a href="wdfdevicestopidlewithtag.md" data-raw-source="[&lt;strong&gt;WdfDeviceStopIdleWithTag&lt;/strong&gt;](wdfdevicestopidlewithtag.md)"><strong>WdfDeviceStopIdleWithTag</strong></a> macro increments the power reference count for a specified framework device object and assigns the driver&#39;s current file name and line number to the reference. The macro also assigns a tag value to the reference.</p></td>
</tr>
</tbody>
</table>

 

 

 






