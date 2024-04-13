---
title: NDIS_STATUS_QOS_REMOTE_PARAMETERS_CHANGE
ms.topic: reference
description: The miniport driver that supports NDIS Quality of Service (QoS) issues an NDIS_STATUS_QOS_REMOTE_PARAMETERS_CHANGE status indication when its remote NDIS QoS parameters are either received from a peer for the first time or change later.
ms.date: 03/02/2023
keywords:
 - NDIS_STATUS_QOS_REMOTE_PARAMETERS_CHANGE Network Drivers Starting with Windows Vista
---

# NDIS\_STATUS\_QOS\_REMOTE\_PARAMETERS\_CHANGE


The miniport driver that supports NDIS Quality of Service (QoS) issues an **NDIS\_STATUS\_QOS\_REMOTE\_PARAMETERS\_CHANGE** status indication when its remote NDIS QoS parameters are either received from a peer for the first time or change later. The miniport driver receives these QoS parameters from a remote peer through the IEEE 802.1Qaz Data Center Bridging Exchange (DCBX) protocol.

When the miniport driver makes this status indication, it sets the **StatusBuffer** member of the [**NDIS\_STATUS\_INDICATION**](/windows-hardware/drivers/ddi/ndis/ns-ndis-_ndis_status_indication) structure to a pointer to an [**NDIS\_QOS\_PARAMETERS**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_qos_parameters) structure. The driver initializes this structure with its remote NDIS QoS parameters.

**Note**  This NDIS status indication is valid only for miniport drivers that support the IEEE 802.1 Data Center Bridging (DCB) interface.

 

## Remarks

The miniport driver uses the DCBX protocol to receive the QoS parameters for a remote peer. The miniport driver resolves its operational NDIS QoS parameters based on its local and remote QoS settings. Once the operational parameters are resolved, the miniport driver configures the network adapter with these parameters for QoS packet transmission.

For more information about how the driver resolves its operational NDIS QoS parameter settings, see [Resolving Operational NDIS QoS Parameters](./resolving-operational-ndis-qos-parameters.md).

The miniport driver must follow these guidelines for issuing an **NDIS\_STATUS\_QOS\_REMOTE\_PARAMETERS\_CHANGE** status indication:

-   If the miniport driver has not received a DCBX frame from a remote peer, it must not issue an **NDIS\_STATUS\_QOS\_REMOTE\_PARAMETERS\_CHANGE** status indication.

-   The miniport driver must issue an **NDIS\_STATUS\_QOS\_REMOTE\_PARAMETERS\_CHANGE** status indication after it has first received the QoS settings from a remote peer.

    **Note**  The miniport driver must issue this status indication if the network adapter receives remote QoS parameter settings from a peer before the driver's local QoS parameters are set. For more information, see [Setting Local NDIS QoS Parameters](./setting-local-ndis-qos-parameters.md).

     

-   After this initial status indication, the miniport driver must only issue an **NDIS\_STATUS\_QOS\_REMOTE\_PARAMETERS\_CHANGE** status indication when it determines a change in the QoS settings on the remote peer.

    **Note**  Miniport drivers must not issue an **NDIS\_STATUS\_QOS\_REMOTE\_PARAMETERS\_CHANGE** status indication if there have been no changes to the remote NDIS QoS parameters. If the driver does make this type of status indication, NDIS may not pass the indication to overlying drivers.

     

**Note**  Overlying drivers can use the **NDIS\_STATUS\_QOS\_REMOTE\_PARAMETERS\_CHANGE** status indication to determine the remote NDIS QoS parameters. Alternatively, these drivers can also issue OID query requests of [OID\_QOS\_REMOTE\_PARAMETERS](./oid-qos-remote-parameters.md) to obtain the remote NDIS QoS parameters at any time.

 

For more information on how the miniport driver issues an **NDIS\_STATUS\_QOS\_REMOTE\_PARAMETERS\_CHANGE** status indication, see [Indicating Changes to the Remote NDIS QoS Parameters](./indicating-changes-to-the-remote-ndis-qos-parameters.md).

For more information about the remote NDIS QoS parameters, see [Overview of NDIS QoS Parameters](./overview-of-ndis-qos-parameters.md).

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
<td>Ndis.h (include Ndis.h)</td>
</tr>
</tbody>
</table>

## See also


****
[**NDIS\_STATUS\_INDICATION**](/windows-hardware/drivers/ddi/ndis/ns-ndis-_ndis_status_indication)

[**NDIS\_QOS\_PARAMETERS**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_qos_parameters)

[OID\_QOS\_REMOTE\_PARAMETERS](./oid-qos-remote-parameters.md)

 

