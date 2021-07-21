---
title: NDIS_STATUS_RING_STATUS
description: The NDIS_STATUS_RING_STATUS status indicates the ring status of a line. A WAN-capable miniport driver can use this status to report a ring failure.
ms.date: 07/18/2017
keywords:
 - NDIS_STATUS_RING_STATUS Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# NDIS\_STATUS\_RING\_STATUS


The NDIS\_STATUS\_RING\_STATUS status indicates the ring status of a line. A WAN-capable miniport driver can use this status to report a ring failure.

## Remarks

NDIS 4.*x* and earlier NDIS WAN miniport drivers use this status indication. NDIS 5.0 and later WAN miniport drivers must use the CoNDIS WAN interface. For more information about the CoNDIS WAN interface, see [Implementing CoNDIS WAN Miniport Drivers (NDIS 5.1)](/previous-versions/windows/hardware/network/ff546752(v=vs.85)).

The *StatusBuffer* parameter of the [**NdisMIndicateStatus**](/previous-versions/windows/hardware/network/ff553538(v=vs.85)) function contains a ULONG value with one of the following status values:

NDIS\_RING\_LOBE\_WIRE\_FAULT

NDIS\_RING\_HARD\_ERROR

NDIS\_RING\_SIGNAL\_LOSS

These values specify ring conditions that are the reason for the status indication. For more information about NDIS\_STATUS\_RING\_STATUS, see [Reporting Hardware Status (NDIS 5.1)](/previous-versions/windows/hardware/network/ff564044(v=vs.85)).

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


[**NdisMIndicateStatus**](/previous-versions/windows/hardware/network/ff553538(v=vs.85))

 

