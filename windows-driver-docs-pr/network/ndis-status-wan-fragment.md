---
title: NDIS_STATUS_WAN_FRAGMENT
ms.topic: reference
description: The NDIS_STATUS_WAN_FRAGMENT status indicates that a WAN-capable miniport driver has received a partial packet from a remote node.
ms.date: 03/02/2023
keywords:
 - NDIS_STATUS_WAN_FRAGMENT Network Drivers Starting with Windows Vista
---

# NDIS\_STATUS\_WAN\_FRAGMENT


The NDIS\_STATUS\_WAN\_FRAGMENT status indicates that a WAN-capable miniport driver has received a partial packet from a remote node.

## Remarks

NDIS 4.*x* and earlier NDIS WAN miniport drivers use this status indication. NDIS 5.0 and later miniport drivers should use the CoNDIS WAN interface. For more information about NDIS\_STATUS\_WAN\_FRAGMENT, see [**NDIS\_STATUS\_WAN\_CO\_FRAGMENT**](ndis-status-wan-co-fragment.md).

The *StatusBuffer* parameter of the [**NdisMIndicateStatus**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndismindicatestatus) function contains a pointer to an [**NDIS\_MAC\_FRAGMENT**](/previous-versions/windows/hardware/network/ff557055(v=vs.85)) structure. NDIS\_MAC\_FRAGMENT identifies a particular link and describes the reason that the partial packet was received.

For more information about NDIS\_STATUS\_WAN\_FRAGMENT, see [Indicating NDIS WAN Miniport Driver Status (NDIS 5.1)](/previous-versions/windows/hardware/network/ff546867(v=vs.85)).

## Requirements

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Version</p></td>
<td><p>Not supported for NDIS 6.0 drivers or NDIS 5.1 drivers in Windows Vista or Windows XP. Supported for NDIS 4.x drivers.</p></td>
</tr>
<tr class="even">
<td><p>Header</p></td>
<td>Ndis.h (include Ndis.h)</td>
</tr>
</tbody>
</table>

## See also


[**NDIS\_MAC\_FRAGMENT**](/previous-versions/windows/hardware/network/ff557055(v=vs.85))

[**NDIS\_STATUS\_WAN\_CO\_FRAGMENT**](ndis-status-wan-co-fragment.md)

[**NdisMIndicateStatus**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndismindicatestatus)

 

