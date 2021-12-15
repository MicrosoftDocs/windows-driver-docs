---
title: Optional Network Wake Up OIDs
description: Optional Network Wake Up OIDs
keywords:
- Optional Network Wakeup OIDs
ms.date: 04/20/2017
---

# Optional Network Wake Up OIDs





To support network wake up events, a Remote NDIS device must additionally support the [OID\_PNP\_ENABLE\_WAKE\_UP](./oid-pnp-enable-wake-up.md) OID that is used by both the network protocols (TCP/IP) and NDIS to enable the wake up capabilities. Additionally, the options listed in the following table are available to enable specific types of wake up patterns. For further details, consult the Microsoft Windows 2000 Driver Development Kit (DDK).

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
<td align="left"><p><a href="/windows-hardware/drivers/network/oid-pnp-enable-wake-up" data-raw-source="[OID_PNP_ENABLE_WAKE_UP](./oid-pnp-enable-wake-up.md)">OID_PNP_ENABLE_WAKE_UP</a></p></td>
<td align="left"><p>The Remote NDIS device's wake-up capabilities that can be enabled</p></td>
</tr>
<tr class="even">
<td align="left"><p>Optional</p></td>
<td align="left"><p><a href="/windows-hardware/drivers/network/oid-pnp-add-wake-up-pattern" data-raw-source="[OID_PNP_ADD_WAKE_UP_PATTERN](./oid-pnp-add-wake-up-pattern.md)">OID_PNP_ADD_WAKE_UP_PATTERN</a></p></td>
<td align="left"><p>Wake-up patterns that the Remote NDIS miniport driver should load into the device</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Optional</p></td>
<td align="left"><p><a href="/windows-hardware/drivers/network/oid-pnp-remove-wake-up-pattern" data-raw-source="[OID_PNP_REMOVE_WAKE_UP_PATTERN](./oid-pnp-remove-wake-up-pattern.md)">OID_PNP_REMOVE_WAKE_UP_PATTERN</a></p></td>
<td align="left"><p>Wake-up patterns that the Remote NDIS miniport driver should remove from the device</p></td>
</tr>
</tbody>
</table>

 

