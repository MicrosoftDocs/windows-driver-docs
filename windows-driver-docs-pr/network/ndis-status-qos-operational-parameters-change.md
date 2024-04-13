---
title: NDIS_STATUS_QOS_OPERATIONAL_PARAMETERS_CHANGE
ms.topic: reference
description: The miniport driver that supports NDIS Quality of Service (QoS) issues an NDIS_STATUS_QOS_OPERATIONAL_PARAMETERS_CHANGE status indication when its operational NDIS QoS parameters are either resolved for the first time or changed later.
ms.date: 03/02/2023
keywords:
 - NDIS_STATUS_QOS_OPERATIONAL_PARAMETERS_CHANGE Network Drivers Starting with Windows Vista
---

# NDIS\_STATUS\_QOS\_OPERATIONAL\_PARAMETERS\_CHANGE


The miniport driver that supports NDIS Quality of Service (QoS) issues an **NDIS\_STATUS\_QOS\_OPERATIONAL\_PARAMETERS\_CHANGE** status indication when its operational NDIS QoS parameters are either resolved for the first time or changed later. The miniport driver configures the network adapter with these operational parameters to perform QoS packet transmission.

When the miniport driver makes this status indication, it sets the **StatusBuffer** member of the [**NDIS\_STATUS\_INDICATION**](/windows-hardware/drivers/ddi/ndis/ns-ndis-_ndis_status_indication) structure to a pointer to an [**NDIS\_QOS\_PARAMETERS**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_qos_parameters) structure. The driver initializes this structure with its operational NDIS QoS parameters.

**Note**  This NDIS status indication is valid only for miniport drivers that support the IEEE 802.1 Data Center Bridging (DCB) interface.

 

## Remarks

The miniport driver issues an **NDIS\_STATUS\_QOS\_OPERATIONAL\_PARAMETERS\_CHANGE** status indication under the following conditions:

-   The miniport driver must issue an **NDIS\_STATUS\_QOS\_OPERATIONAL\_PARAMETERS\_CHANGE** status indication after it has initially resolved its operational NDIS QoS parameters and configured the network adapter with them.

-   After this initial status indication, the miniport driver must issue an **NDIS\_STATUS\_QOS\_OPERATIONAL\_PARAMETERS\_CHANGE** status indication when its operational NDIS QoS parameters are changed. This can happen when either the local or remote NDIS QoS parameters are changed.

-   Miniport drivers obtain the local NDIS QoS parameters from the Windows operating system when the Data Center Bridging (DCB) component (Msdcb.sys) issues an object identifier (OID) method request of [OID\_QOS\_PARAMETERS](./oid-qos-parameters.md). This OID request contains an [**NDIS\_QOS\_PARAMETERS**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_qos_parameters) structure that specifies the local NDIS QoS parameters.

    There may be situations when the miniport driver has to override the local NDIS QoS parameters when it resolves its operational NDIS QoS parameters. This is especially true if the local QoS parameters compromise the operational QoS parameters that are being used by any underlying protocols or technologies that are currently enabled on the network adapter. For example, the driver can override the local QoS parameters if the network adapter is enabled for remote boot through the Fibre Channel over Ethernet (FCoE) protocol.

    The miniport driver notifies NDIS and overlying drivers of its intention to override the local NDIS QoS parameters by issuing an **NDIS\_STATUS\_QOS\_OPERATIONAL\_PARAMETERS\_CHANGE** status indication.

    For more information, see [Managing NDIS QoS Parameters](overview-of-ndis-qos-parameters.md).

**Note**  Overlying drivers can use the **NDIS\_STATUS\_QOS\_OPERATIONAL\_PARAMETERS\_CHANGE** status indication to determine the operational NDIS QoS parameters. Alternatively, these drivers can also issue OID query requests of [OID\_QOS\_OPERATIONAL\_PARAMETERS](./oid-qos-operational-parameters.md) to obtain the operational NDIS QoS parameters at any time.

 

For information on how the miniport driver issues an **NDIS\_STATUS\_QOS\_OPERATIONAL\_PARAMETERS\_CHANGE** status indication, see [Indicating Changes to the Operational NDIS QoS Parameters](./indicating-changes-to-the-operational-ndis-qos-parameters.md).

For more information about the various types of NDIS QoS parameters, see [Overview of NDIS QoS Parameters](./overview-of-ndis-qos-parameters.md).

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

[OID\_QOS\_OPERATIONAL\_PARAMETERS](./oid-qos-operational-parameters.md)

 

