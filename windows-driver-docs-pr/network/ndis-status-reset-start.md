---
title: NDIS_STATUS_RESET_START
description: The NDIS_STATUS_RESET_START status indicates that a miniport adapter is being reset.
ms.date: 07/18/2017
keywords:
 - NDIS_STATUS_RESET_START Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# NDIS\_STATUS\_RESET\_START


The NDIS\_STATUS\_RESET\_START status indicates that a miniport adapter is being reset.

## Remarks

Miniport drivers should not call the [**NdisMIndicateStatusEx**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndismindicatestatusex) function to signal the start and finish of each reset operation because NDIS notifies overlying drivers when a reset operation begins and ends.

A miniport driver resets a miniport adapter when NDIS calls the miniport driver's [*MiniportResetEx*](/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_reset) function. NDIS calls the [*ProtocolStatusEx*](/windows-hardware/drivers/ddi/ndis/nc-ndis-protocol_status_ex) function of each bound protocol and intermediate driver and the [*FilterStatus*](/windows-hardware/drivers/ddi/ndis/nc-ndis-filter_status) function of the overlying filter modules with a status of NDIS\_STATUS\_RESET\_START. When the miniport driver completes the reset, NDIS notifies the overlying drivers with a status of [**NDIS\_STATUS\_RESET\_END**](ndis-status-reset-end.md).

When a protocol driver receives an NDIS\_STATUS\_RESET\_START status indication, it should:

-   Hold any data that is ready to transmit until its *ProtocolStatusEx* function receives an NDIS\_STATUS\_RESET\_END status indication.

-   Not make any NDIS calls that are directed to the underlying miniport driver, except calls to return resources such as received data buffers with the [**NdisReturnNetBufferLists**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndisreturnnetbufferlists) function.

## Requirements

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Version</p></td>
<td><p>Supported for NDIS 6.0 and NDIS 5.1 drivers in Windows Vista. Supported for NDIS 5.1 drivers in Windows XP.</p></td>
</tr>
<tr class="even">
<td><p>Header</p></td>
<td>Ndis.h (include Ndis.h)</td>
</tr>
</tbody>
</table>

## See also


[*FilterStatus*](/windows-hardware/drivers/ddi/ndis/nc-ndis-filter_status)

[*MiniportResetEx*](/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_reset)

[**NDIS\_STATUS\_RESET\_END**](ndis-status-reset-end.md)

[**NdisMIndicateStatusEx**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndismindicatestatusex)

[**NdisReturnNetBufferLists**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndisreturnnetbufferlists)

[*ProtocolStatusEx*](/windows-hardware/drivers/ddi/ndis/nc-ndis-protocol_status_ex)

 

