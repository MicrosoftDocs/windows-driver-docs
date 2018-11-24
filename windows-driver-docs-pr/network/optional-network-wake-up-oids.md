---
title: Optional Network Wake Up OIDs
description: Optional Network Wake Up OIDs
ms.assetid: 0e9b4844-1623-4bfd-8e73-ebbd970c7e95
keywords:
- Optional Network Wakeup OIDs
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Optional Network Wake Up OIDs





To support network wake up events, a Remote NDIS device must additionally support the [OID\_PNP\_ENABLE\_WAKE\_UP](https://msdn.microsoft.com/library/windows/hardware/ff569775) OID that is used by both the network protocols (TCP/IP) and NDIS to enable the wake up capabilities. Additionally, the options listed in the following table are available to enable specific types of wake up patterns. For further details, consult the Microsoft Windows 2000 Driver Development Kit (DDK).

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
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff569775" data-raw-source="[OID_PNP_ENABLE_WAKE_UP](https://msdn.microsoft.com/library/windows/hardware/ff569775)">OID_PNP_ENABLE_WAKE_UP</a></p></td>
<td align="left"><p>The Remote NDIS device&#39;s wake-up capabilities that can be enabled</p></td>
</tr>
<tr class="even">
<td align="left"><p>Optional</p></td>
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff569773" data-raw-source="[OID_PNP_ADD_WAKE_UP_PATTERN](https://msdn.microsoft.com/library/windows/hardware/ff569773)">OID_PNP_ADD_WAKE_UP_PATTERN</a></p></td>
<td align="left"><p>Wake-up patterns that the Remote NDIS miniport driver should load into the device</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Optional</p></td>
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff569779" data-raw-source="[OID_PNP_REMOVE_WAKE_UP_PATTERN](https://msdn.microsoft.com/library/windows/hardware/ff569779)">OID_PNP_REMOVE_WAKE_UP_PATTERN</a></p></td>
<td align="left"><p>Wake-up patterns that the Remote NDIS miniport driver should remove from the device</p></td>
</tr>
</tbody>
</table>

 

 

 





