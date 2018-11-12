---
title: GDI Information Services
description: GDI Information Services
ms.assetid: f3575d68-1d90-4ccd-adb1-5d2a26099397
keywords:
- GDI WDK Windows 2000 display , information services
- graphics drivers WDK Windows 2000 display , information services
- drawing WDK GDI , information services
- time stamps WDK GDI
- counters WDK GDI
- performance counters WDK GDI
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# GDI Information Services


## <span id="ddk_gdi_information_services_gg"></span><span id="DDK_GDI_INFORMATION_SERVICES_GG"></span>


GDI provides several services a driver can use to query the system about device and system attributes, a file's time stamp, and the performance counter. These services are listed in the following table.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Function</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff564986" data-raw-source="[&lt;strong&gt;EngQueryDeviceAttribute&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff564986)"><strong>EngQueryDeviceAttribute</strong></a></p></td>
<td align="left"><p>Allows the driver to query the system about particular attributes of the device.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff564988" data-raw-source="[&lt;strong&gt;EngQueryFileTimeStamp&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff564988)"><strong>EngQueryFileTimeStamp</strong></a></p></td>
<td align="left"><p>Returns the time stamp of a file.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff564990" data-raw-source="[&lt;strong&gt;EngQueryLocalTime&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff564990)"><strong>EngQueryLocalTime</strong></a></p></td>
<td align="left"><p>Queries the local time.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff564994" data-raw-source="[&lt;strong&gt;EngQueryPerformanceCounter&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff564994)"><strong>EngQueryPerformanceCounter</strong></a></p></td>
<td align="left"><p>Queries the performance counter.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff564996" data-raw-source="[&lt;strong&gt;EngQueryPerformanceFrequency&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff564996)"><strong>EngQueryPerformanceFrequency</strong></a></p></td>
<td align="left"><p>Queries the frequency of the performance counter.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff564997" data-raw-source="[&lt;strong&gt;EngQuerySystemAttribute&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff564997)"><strong>EngQuerySystemAttribute</strong></a></p></td>
<td align="left"><p>Queries processor or system-specific capabilities.</p></td>
</tr>
</tbody>
</table>

 

 

 





