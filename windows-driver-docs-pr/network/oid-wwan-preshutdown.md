---
title: OID_WWAN_PRESHUTDOWN
ms.topic: reference
description: OID_WWAN_PRESHUTDOWN is sent to notify the modem that the system is entering the shutdown phase and the modem should finish its operations so it can be shut down properly.
ms.date: 08/08/2017
keywords: 
 -OID_WWAN_PRESHUTDOWN Network Drivers Starting with Windows Vista
---

# OID\_WWAN\_PRESHUTDOWN


OID\_WWAN\_PRESHUTDOWN is sent to notify the modem that the system is entering the shutdown phase and the modem should finish its operations so it can be shut down properly. It is only sent down with the port number corresponding to the physical MBB adapters. Virtual adapters that support multiple PDP contexts should not receive this OID.

Query requests are not supported.

Miniport drivers must process set requests asynchronously, initially returning **NDIS\_STATUS\_INDICATION\_REQUIRED** to the original request, and later sending a [**NDIS\_STATUS\_WWAN\_PRESHUTDOWN\_STATE**](./ndis-status-wwan-preshutdown-state.md) status notification when the MBB driver has finished all necessary modem operations prior to shutting down. The set request has a [**NDIS\_WWAN\_SET\_PRESHUTDOWN\_STATE**](/windows-hardware/drivers/ddi/ndiswwan/ns-ndiswwan-_ndis_wwan_set_preshutdown_state) structure.

Miniport drivers should return **NDIS\_STATUS\_NOT\_SUPPORTED** if they do not support this operation.

## Requirements

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Version</p></td>
<td><p>Available starting with Windows 10, version 1511.</p></td>
</tr>
<tr class="even">
<td><p>Header</p></td>
<td>Ntddndis.h (include Ndis.h)</td>
</tr>
</tbody>
</table>

## See also


[**NDIS\_STATUS\_WWAN\_PRESHUTDOWN\_STATE**](./ndis-status-wwan-preshutdown-state.md)

[**NDIS\_WWAN\_SET\_PRESHUTDOWN\_STATE**](/windows-hardware/drivers/ddi/ndiswwan/ns-ndiswwan-_ndis_wwan_set_preshutdown_state)

 

