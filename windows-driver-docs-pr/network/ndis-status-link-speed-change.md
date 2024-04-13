---
title: NDIS_STATUS_LINK_SPEED_CHANGE
ms.topic: reference
description: The NDIS_STATUS_LINK_SPEED_CHANGE status indicates a link speed change.
ms.date: 03/02/2023
keywords:
 - NDIS_STATUS_LINK_SPEED_CHANGE Network Drivers Starting with Windows Vista
---

# NDIS\_STATUS\_LINK\_SPEED\_CHANGE


The NDIS\_STATUS\_LINK\_SPEED\_CHANGE status indicates a link speed change.

## Remarks

NDIS translates NDIS\_STATUS\_LINK\_SPEED\_CHANGE status indications to [**NDIS\_STATUS\_LINK\_STATE**](ndis-status-link-state.md) status indications for overlying NDIS 6.0 drivers. When NDIS receives an NDIS\_STATUS\_LINK\_SPEED\_CHANGE status, NDIS issues an OID query request of [OID\_GEN\_LINK\_SPEED](./oid-gen-link-speed.md). NDIS uses the results of the OID\_GEN\_LINK\_SPEED query to issue an NDIS\_STATUS\_LINK\_STATE status to overlying NDIS 6.0 drivers.

The NDIS 5.*x* or earlier miniport driver supplies a DWORD-type value at the *StatusBuffer* parameter of the [**NdisMIndicateStatus**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndismindicatestatus) function. For more information about NDIS\_STATUS\_LINK\_SPEED\_CHANGE, see [OID\_IRDA\_RATE\_SNIFF](/previous-versions/windows/hardware/network/ff560287(v=vs.85)).

## Requirements

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Version</p></td>
<td><p>Not supported in NDIS 6.0 and later (use <a href="ndis-status-link-state.md" data-raw-source="[&lt;strong&gt;NDIS_STATUS_LINK_STATE&lt;/strong&gt;](ndis-status-link-state.md)"><strong>NDIS_STATUS_LINK_STATE</strong></a> instead). Supported only for NDIS 5.1 drivers in Windows Vista and Windows XP.</p></td>
</tr>
<tr class="even">
<td><p>Header</p></td>
<td>Ndis.h (include Ndis.h)</td>
</tr>
</tbody>
</table>

## See also


[**NDIS\_STATUS\_LINK\_STATE**](ndis-status-link-state.md)

[**NdisMIndicateStatus**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndismindicatestatus)

[OID\_GEN\_LINK\_SPEED](./oid-gen-link-speed.md)

[OID\_IRDA\_RATE\_SNIFF](/previous-versions/windows/hardware/network/ff560287(v=vs.85))

 

