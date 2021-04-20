---
title: Calling PoStartNextPowerIrp from a Filter Driver
description: Calling PoStartNextPowerIrp from a Filter Driver
keywords: ["power IRPs WDK kernel , PoStartNextPowerIrp", "PoStartNextPowerIrp", "filter drivers WDK power management"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# Calling PoStartNextPowerIrp from a Filter Driver


Beginning with Windows Vista, calling [**PoStartNextPowerIrp**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-postartnextpowerirp) is not required and call to this routine performs no power management operation. However, in Windows Server 2003, Windows XP, and Windows 2000, a filter driver must call **PoStartNextPowerIrp** once for every [**IRP\_MN\_QUERY\_POWER**](./irp-mn-query-power.md) or [**IRP\_MN\_SET\_POWER**](./irp-mn-set-power.md) request that the driver receives. When the call occurs depends on the type of request and whether the driver will fail or succeed the request, as the following table shows.

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
<td><p>In an <a href="/windows-hardware/drivers/ddi/wdm/nc-wdm-io_completion_routine" data-raw-source="[&lt;em&gt;IoCompletion&lt;/em&gt;](/windows-hardware/drivers/ddi/wdm/nc-wdm-io_completion_routine)"><em>IoCompletion</em></a> routine, immediately before returning.</p></td>
<td><p>In <a href="/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_dispatch" data-raw-source="[&lt;em&gt;DispatchPower&lt;/em&gt;](/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_dispatch)"><em>DispatchPower</em></a> routine, before calling <strong>IoCompleteRequest</strong>.</p></td>
</tr>
<tr class="even">
<td><p><strong>IRP_MN_QUERY_POWER</strong> (system power state)</p></td>
<td><p>In <em>DispatchPower</em> routine, after acquiring remove lock and before setting IRP stack location.</p></td>
<td><p>In <em>DispatchPower</em> routine, before calling <a href="/windows-hardware/drivers/ddi/wdm/nf-wdm-iocompleterequest" data-raw-source="[&lt;strong&gt;IoCompleteRequest&lt;/strong&gt;](/windows-hardware/drivers/ddi/wdm/nf-wdm-iocompleterequest)"><strong>IoCompleteRequest</strong></a>.</p></td>
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

 

