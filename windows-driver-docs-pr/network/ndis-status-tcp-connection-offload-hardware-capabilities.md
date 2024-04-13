---
title: NDIS_STATUS_TCP_CONNECTION_OFFLOAD_HARDWARE_CAPABILITIES
ms.topic: reference
description: MUX intermediate drivers use the NDIS_STATUS_TCP_CONNECTION_OFFLOAD_HARDWARE_CAPABILITIES CAPABILITIES status indication to notify NDIS and overlying drivers that there has been change in the connection offload characteristics of the underlying hardware.
ms.date: 03/02/2023
keywords:
 - NDIS_STATUS_TCP_CONNECTION_OFFLOAD_HARDWARE_CAPABILITIES Network Drivers Starting with Windows Vista
---

# NDIS\_STATUS\_TCP\_CONNECTION\_OFFLOAD\_HARDWARE\_CAPABILITIES


MUX intermediate drivers use the NDIS\_STATUS\_TCP\_CONNECTION\_OFFLOAD\_HARDWARE\_CAPABILITIES CAPABILITIES status indication to notify NDIS and overlying drivers that there has been change in the connection offload characteristics of the underlying hardware.

## Remarks

If an underlying NIC is added or deleted, the overall set of hardware capabilities that is associated with a MUX intermediate driver can change.

The **StatusBuffer** member of the [**NDIS\_STATUS\_INDICATION**](/windows-hardware/drivers/ddi/ndis/ns-ndis-_ndis_status_indication) structure contains an [**NDIS\_TCP\_CONNECTION\_OFFLOAD**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_tcp_connection_offload) structure. NDIS\_TCP\_CONNECTION\_OFFLOAD specifies the task offload hardware capabilities.

For more information about task offload hardware capabilities, see [OID\_TCP\_CONNECTION\_OFFLOAD\_HARDWARE\_CAPABILITIES](./oid-tcp-connection-offload-hardware-capabilities.md).

## Requirements

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Version</p></td>
<td><p>Supported in NDIS 6.0 and later.</p></td>
</tr>
<tr class="even">
<td><p>Header</p></td>
<td>Ndis.h (include Ndis.h)</td>
</tr>
</tbody>
</table>

## See also


[**NDIS\_STATUS\_INDICATION**](/windows-hardware/drivers/ddi/ndis/ns-ndis-_ndis_status_indication)

[**NDIS\_TCP\_CONNECTION\_OFFLOAD**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_tcp_connection_offload)

[OID\_TCP\_CONNECTION\_OFFLOAD\_HARDWARE\_CAPABILITIES](./oid-tcp-connection-offload-hardware-capabilities.md)

 

