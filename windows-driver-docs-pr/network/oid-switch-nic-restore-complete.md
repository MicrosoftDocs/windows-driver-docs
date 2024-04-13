---
title: OID_SWITCH_NIC_RESTORE_COMPLETE
ms.topic: reference
description: The protocol edge of the Hyper-V extensible switch issues an object identifier (OID) set request of OID_SWITCH_NIC_RESTORE_COMPLETE to notify Hyper-V extensible switch extensions about the completion of the operation to restore run-time data.
ms.date: 08/08/2017
keywords: 
 -OID_SWITCH_NIC_RESTORE_COMPLETE Network Drivers Starting with Windows Vista
---

# OID\_SWITCH\_NIC\_RESTORE\_COMPLETE


The protocol edge of the Hyper-V extensible switch issues an object identifier (OID) set request of OID\_SWITCH\_NIC\_RESTORE\_COMPLETE to notify Hyper-V extensible switch extensions about the completion of the operation to restore run-time data. Through this operation, the extension restores its run-time data for a port and its associated network adapter connection.

The **InformationBuffer** member of the [**NDIS\_OID\_REQUEST**](/windows-hardware/drivers/ddi/oidrequest/ns-oidrequest-ndis_oid_request) structure contains a pointer to an [**NDIS\_SWITCH\_NIC\_SAVE\_STATE**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_switch_nic_save_state) structure. This structure is allocated by the protocol edge of the extensible switch.

## Remarks

When it receives the OID set request of OID\_SWITCH\_NIC\_RESTORE\_COMPLETE, the extension must follow these guidelines:

-   The extension must not modify the [**NDIS\_SWITCH\_NIC\_SAVE\_STATE**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_switch_nic_save_state) structure that is associated with the OID request.
-   The extension must call [**NdisFOidRequest**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndisfoidrequest) to forward this OID set request to underlying extensions in the extensible switch driver stack. The extension must not fail the OID request.

OID set requests of OID\_SWITCH\_NIC\_RESTORE\_COMPLETE are ultimately handled by the underlying miniport edge of the extensible switch. After this OID method request has been received by the miniport edge, it completes the OID request with NDIS\_STATUS\_SUCCESS. This notifies the protocol edge of the extensible switch that all extensions in the extensible switch driver stack have completed the save operation.

For more information on how to save run-time data for an extensible switch port, see [Saving Hyper-V Extensible Switch Run-Time Data](./managing-hyper-v-extensible-switch-run-time-data.md).

### Return Status Codes

If the extension completes the OID set request of [OID\_SWITCH\_NIC\_RESTORE\_COMPLETE](oid-switch-nic-restore.md), it returns one of the following status codes.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Status Code</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>NDIS_STATUS_SUCCESS</p></td>
<td><p>The OID request completed successfully.</p></td>
</tr>
</tbody>
</table>

 

## Requirements

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Version</p></td>
<td><p>Supported in NDIS 6.30 and later.</p></td>
</tr>
<tr class="even">
<td><p>Header</p></td>
<td>Ntddndis.h (include Ndis.h)</td>
</tr>
</tbody>
</table>

## See also


****
[**NDIS\_OID\_REQUEST**](/windows-hardware/drivers/ddi/oidrequest/ns-oidrequest-ndis_oid_request)

[**NDIS\_SWITCH\_NIC\_SAVE\_STATE**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_switch_nic_save_state)

 

