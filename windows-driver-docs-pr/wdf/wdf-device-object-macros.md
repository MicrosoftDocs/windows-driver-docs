---
title: WDF Device Object Macros
author: windows-driver-content
description: This section documents macros that support WDF device objects.
ms.assetid: D91C16EB-5E31-4AB2-984E-A0B35C3B1BA1
ms.author: windowsdriverdev
ms.date: 08/23/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
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
<td><p>[<strong>WdfDeviceResumeIdleWithTag method</strong>](wdfdeviceresumeidlewithtag.md)</p></td>
<td><div class="alert">
<strong>Note</strong>  Applies to KMDF and UMDF
</div>
<div>
 
</div>
<p>The [<strong>WdfDeviceResumeIdleWithTag</strong>](wdfdeviceresumeidlewithtag.md) macro decrements the power reference count for a specified framework device object and assigns the driver's current file name and line number to the reference. The macro also assigns a tag value to the reference.</p></td>
</tr>
<tr class="even">
<td><p>[<strong>WdfDeviceStopIdleWithTag method</strong>](wdfdevicestopidlewithtag.md)</p></td>
<td><div class="alert">
<strong>Note</strong>  Applies to KMDF and UMDF
</div>
<div>
 
</div>
<p>The [<strong>WdfDeviceStopIdleWithTag</strong>](wdfdevicestopidlewithtag.md) macro increments the power reference count for a specified framework device object and assigns the driver's current file name and line number to the reference. The macro also assigns a tag value to the reference.</p></td>
</tr>
</tbody>
</table>

 

 

 






