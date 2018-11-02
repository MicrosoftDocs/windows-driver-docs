---
title: Optional Power Management OIDs
description: Optional Power Management OIDs
ms.assetid: 31c8ec45-ecb2-42e2-be4d-2b89fe02a908
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Optional Power Management OIDs





For NDIS to consider a device power-management -- aware, it must respond to the three power management OIDs listed in the following table. If the device returns a failure status code in response to a query for [OID\_PNP\_CAPABILITIES](https://msdn.microsoft.com/library/windows/hardware/ff569774), then the host will consider the device as not being power manageable. NDIS decides whether to query this OID based on the underlying bus technology that the Remote NDIS device is connected to. Some buses are power-manageable, such as USB, so it is expected that these types of Remote NDIS devices will support the minimal OIDs to be considered power-manageable.

<table>
<colgroup>
<col width="33%" />
<col width="33%" />
<col width="33%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Support</th>
<th align="left">OID</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>Optional</p></td>
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff569774" data-raw-source="[OID_PNP_CAPABILITIES](https://msdn.microsoft.com/library/windows/hardware/ff569774)">OID_PNP_CAPABILITIES</a></p></td>
<td align="left"><p>The NIC&#39;s Power Management abilities</p></td>
</tr>
<tr class="even">
<td align="left"><p>Optional</p></td>
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff569778" data-raw-source="[OID_PNP_QUERY_POWER](https://msdn.microsoft.com/library/windows/hardware/ff569778)">OID_PNP_QUERY_POWER</a></p></td>
<td align="left"><p>A query to determine whether the device can transition to a specific power state.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Optional</p></td>
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff569780" data-raw-source="[OID_PNP_SET_POWER](https://msdn.microsoft.com/library/windows/hardware/ff569780)">OID_PNP_SET_POWER</a></p></td>
<td align="left"><p>A command to set the device to specified power state</p></td>
</tr>
</tbody>
</table>

 

 

 





