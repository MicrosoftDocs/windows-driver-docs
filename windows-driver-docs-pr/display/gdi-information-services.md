---
title: GDI Information Services
description: GDI Information Services
keywords:
- GDI WDK Windows 2000 display , information services
- graphics drivers WDK Windows 2000 display , information services
- drawing WDK GDI , information services
- time stamps WDK GDI
- counters WDK GDI
- performance counters WDK GDI
ms.date: 04/20/2017
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
<td align="left"><p><a href="/windows/win32/api/winddi/nf-winddi-engquerydeviceattribute" data-raw-source="[&lt;strong&gt;EngQueryDeviceAttribute&lt;/strong&gt;](/windows/win32/api/winddi/nf-winddi-engquerydeviceattribute)"><strong>EngQueryDeviceAttribute</strong></a></p></td>
<td align="left"><p>Allows the driver to query the system about particular attributes of the device.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows/win32/api/winddi/nf-winddi-engqueryfiletimestamp" data-raw-source="[&lt;strong&gt;EngQueryFileTimeStamp&lt;/strong&gt;](/windows/win32/api/winddi/nf-winddi-engqueryfiletimestamp)"><strong>EngQueryFileTimeStamp</strong></a></p></td>
<td align="left"><p>Returns the time stamp of a file.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows/win32/api/winddi/nf-winddi-engquerylocaltime" data-raw-source="[&lt;strong&gt;EngQueryLocalTime&lt;/strong&gt;](/windows/win32/api/winddi/nf-winddi-engquerylocaltime)"><strong>EngQueryLocalTime</strong></a></p></td>
<td align="left"><p>Queries the local time.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows/win32/api/winddi/nf-winddi-engqueryperformancecounter" data-raw-source="[&lt;strong&gt;EngQueryPerformanceCounter&lt;/strong&gt;](/windows/win32/api/winddi/nf-winddi-engqueryperformancecounter)"><strong>EngQueryPerformanceCounter</strong></a></p></td>
<td align="left"><p>Queries the performance counter.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows/win32/api/winddi/nf-winddi-engqueryperformancefrequency" data-raw-source="[&lt;strong&gt;EngQueryPerformanceFrequency&lt;/strong&gt;](/windows/win32/api/winddi/nf-winddi-engqueryperformancefrequency)"><strong>EngQueryPerformanceFrequency</strong></a></p></td>
<td align="left"><p>Queries the frequency of the performance counter.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows/win32/api/winddi/nf-winddi-engquerysystemattribute" data-raw-source="[&lt;strong&gt;EngQuerySystemAttribute&lt;/strong&gt;](/windows/win32/api/winddi/nf-winddi-engquerysystemattribute)"><strong>EngQuerySystemAttribute</strong></a></p></td>
<td align="left"><p>Queries processor or system-specific capabilities.</p></td>
</tr>
</tbody>
</table>

 

