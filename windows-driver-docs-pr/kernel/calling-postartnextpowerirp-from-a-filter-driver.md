---
title: Calling PoStartNextPowerIrp from a Filter Driver
description: Calling PoStartNextPowerIrp from a Filter Driver
ms.assetid: 6005f107-8f90-4530-91c2-9f0947cacb0a
keywords: ["power IRPs WDK kernel , PoStartNextPowerIrp", "PoStartNextPowerIrp", "filter drivers WDK power management"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# Calling PoStartNextPowerIrp from a Filter Driver


Beginning with Windows Vista, calling [**PoStartNextPowerIrp**](https://msdn.microsoft.com/library/windows/hardware/ff559776) is not required and call to this routine performs no power management operation. However, in Windows Server 2003, Windows XP, and Windows 2000, a filter driver must call **PoStartNextPowerIrp** once for every [**IRP\_MN\_QUERY\_POWER**](https://msdn.microsoft.com/library/windows/hardware/ff551699) or [**IRP\_MN\_SET\_POWER**](https://msdn.microsoft.com/library/windows/hardware/ff551744) request that the driver receives. When the call occurs depends on the type of request and whether the driver will fail or succeed the request, as the following table shows.

<table>
<colgroup>
<col width="33%" />
<col width="33%" />
<col width="33%" />
</colgroup>
<thead>
<tr class="header">
<th>Type of request</th>
<th>If driver succeeds the request, the call occurs:</th>
<th>If driver fails the request, the call occurs:</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p><strong>IRP_MN_QUERY_POWER</strong> (device power state)</p></td>
<td><p>In an <a href="https://msdn.microsoft.com/library/windows/hardware/ff548354" data-raw-source="[&lt;em&gt;IoCompletion&lt;/em&gt;](https://msdn.microsoft.com/library/windows/hardware/ff548354)"><em>IoCompletion</em></a> routine, immediately before returning.</p></td>
<td><p>In <a href="https://msdn.microsoft.com/library/windows/hardware/ff543354" data-raw-source="[&lt;em&gt;DispatchPower&lt;/em&gt;](https://msdn.microsoft.com/library/windows/hardware/ff543354)"><em>DispatchPower</em></a> routine, before calling <strong>IoCompleteRequest</strong>.</p></td>
</tr>
<tr class="even">
<td><p><strong>IRP_MN_QUERY_POWER</strong> (system power state)</p></td>
<td><p>In <em>DispatchPower</em> routine, after acquiring remove lock and before setting IRP stack location.</p></td>
<td><p>In <em>DispatchPower</em> routine, before calling <a href="https://msdn.microsoft.com/library/windows/hardware/ff548343" data-raw-source="[&lt;strong&gt;IoCompleteRequest&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff548343)"><strong>IoCompleteRequest</strong></a>.</p></td>
</tr>
<tr class="odd">
<td><p><strong>IRP_MN_SET_POWER</strong> (device power state)</p></td>
<td><p>In an <em>IoCompletion</em> routine, immediately before returning.</p></td>
<td><p>Not allowed.</p></td>
</tr>
<tr class="even">
<td><p><strong>IRP_MN_SET_POWER</strong> (system power state)</p></td>
<td><p>In <em>DispatchPower</em> routine, after acquiring remove lock and before setting IRP stack location.</p></td>
<td><p>Not allowed.</p></td>
</tr>
</tbody>
</table>

 

 

 




