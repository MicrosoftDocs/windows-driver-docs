---
title: NDIS_STATUS_TAPI_INDICATION
ms.topic: reference
description: The NDIS_STATUS_TAPI_INDICATION status indicates that a TAPI event occurred. A WAN-capable miniport driver can indicate TAPI status.
ms.date: 03/02/2023
keywords:
 - NDIS_STATUS_TAPI_INDICATION Network Drivers Starting with Windows Vista
---

# NDIS\_STATUS\_TAPI\_INDICATION


The NDIS\_STATUS\_TAPI\_INDICATION status indicates that a TAPI event occurred. A WAN-capable miniport driver can indicate TAPI status.

## Remarks

NDIS 4.*x* and earlier NDIS WAN miniport drivers use this status indication. NDIS 5.0 and later WAN miniport drivers must use the CoNDIS WAN interface. For more information about the CoNDIS WAN interface, see [Implementing CoNDIS WAN Miniport Drivers (NDIS 5.1)](/previous-versions/windows/hardware/network/ff546752(v=vs.85)).

The *StatusBuffer* parameter of the [**NdisMIndicateStatus**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndismindicatestatus) function contains a pointer to an [**NDIS\_TAPI\_EVENT**](/previous-versions/windows/hardware/network/ff558986(v=vs.85)) structure.The NDIS\_TAPI\_EVENT structure describes the TAPI line or call event that occurs (for example, changes in line and call states, the arrival of an incoming call, and the closing by a remote node or by the miniport driver of an existing call or line).

For more information about NDIS\_STATUS\_TAPI\_INDICATION, see [Indicating NDIS WAN Miniport Driver Status (NDIS 5.1)](/previous-versions/windows/hardware/network/ff546867(v=vs.85)).

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


[**NDIS\_TAPI\_EVENT**](/previous-versions/windows/hardware/network/ff558986(v=vs.85))

[**NdisMIndicateStatus**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndismindicatestatus)

 

