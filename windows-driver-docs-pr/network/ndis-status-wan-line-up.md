---
title: NDIS_STATUS_WAN_LINE_UP
description: The NDIS_STATUS_WAN_LINE_UP status indicates that a WAN-capable miniport driver has established a connection with a remote node.
ms.date: 07/18/2017
keywords:
 - NDIS_STATUS_WAN_LINE_UP Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# NDIS\_STATUS\_WAN\_LINE\_UP


The NDIS\_STATUS\_WAN\_LINE\_UP status indicates that a WAN-capable miniport driver has established a connection with a remote node.

## Remarks

NDIS 4.*x* and earlier NDIS WAN miniport drivers use this status indication. NDIS 5.0 and later WAN miniport drivers must use the CoNDIS WAN interface. For more information about the CoNDIS WAN interface, see [Implementing CoNDIS WAN Miniport Drivers (NDIS 5.1)](/previous-versions/windows/hardware/network/ff546752(v=vs.85)).

The *StatusBuffer* parameter of the [**NdisMIndicateStatus**](/previous-versions/windows/hardware/network/ff553538(v=vs.85)) function contains a pointer to an [**NDIS\_MAC\_LINE\_UP**](/previous-versions/windows/hardware/network/ff557058(v=vs.85)) structure.

For more information about NDIS\_STATUS\_WAN\_LINE\_UP, see [Line-Up Indication (NDIS 5.1)](/previous-versions/windows/hardware/network/ff549189(v=vs.85)) and [Indicating NDIS WAN Miniport Driver Status (NDIS 5.1)](/previous-versions/windows/hardware/network/ff546867(v=vs.85)).

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


[**NDIS\_MAC\_LINE\_UP**](/previous-versions/windows/hardware/network/ff557058(v=vs.85))

[**NdisMIndicateStatus**](/previous-versions/windows/hardware/network/ff553538(v=vs.85))

 

