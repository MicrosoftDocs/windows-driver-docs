---
title: GDI Information Services
description: GDI Information Services
ms.assetid: f3575d68-1d90-4ccd-adb1-5d2a26099397
keywords: ["GDI WDK Windows 2000 display , information services", "graphics drivers WDK Windows 2000 display , information services", "drawing WDK GDI , information services", "time stamps WDK GDI", "counters WDK GDI", "performance counters WDK GDI"]
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
<td align="left"><p>[<strong>EngQueryDeviceAttribute</strong>](https://msdn.microsoft.com/library/windows/hardware/ff564986)</p></td>
<td align="left"><p>Allows the driver to query the system about particular attributes of the device.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>EngQueryFileTimeStamp</strong>](https://msdn.microsoft.com/library/windows/hardware/ff564988)</p></td>
<td align="left"><p>Returns the time stamp of a file.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>EngQueryLocalTime</strong>](https://msdn.microsoft.com/library/windows/hardware/ff564990)</p></td>
<td align="left"><p>Queries the local time.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>EngQueryPerformanceCounter</strong>](https://msdn.microsoft.com/library/windows/hardware/ff564994)</p></td>
<td align="left"><p>Queries the performance counter.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>EngQueryPerformanceFrequency</strong>](https://msdn.microsoft.com/library/windows/hardware/ff564996)</p></td>
<td align="left"><p>Queries the frequency of the performance counter.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>EngQuerySystemAttribute</strong>](https://msdn.microsoft.com/library/windows/hardware/ff564997)</p></td>
<td align="left"><p>Queries processor or system-specific capabilities.</p></td>
</tr>
</tbody>
</table>

 

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20GDI%20Information%20Services%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




