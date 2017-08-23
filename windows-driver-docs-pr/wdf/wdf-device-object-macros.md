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

 

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bwdf\wdf%5D:%20WDF%20Device%20Object%20Macros%20%20RELEASE:%20%288/22/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


