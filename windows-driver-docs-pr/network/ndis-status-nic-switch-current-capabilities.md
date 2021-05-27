---
title: NDIS_STATUS_NIC_SWITCH_CURRENT_CAPABILITIES
description: The NDIS_STATUS_NIC_SWITCH_CURRENT_CAPABILITIES status indicates to NDIS and overlying drivers that the currently enabled hardware capabilities of the NIC switch in a network adapter have changed.
ms.date: 08/08/2017
keywords: 
 -NDIS_STATUS_NIC_SWITCH_CURRENT_CAPABILITIES Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# NDIS\_STATUS\_NIC\_SWITCH\_CURRENT\_CAPABILITIES


The **NDIS\_STATUS\_NIC\_SWITCH\_CURRENT\_CAPABILITIES** status indicates to NDIS and overlying drivers that the currently enabled hardware capabilities of the NIC switch in a network adapter have changed.

The status indication is made by the miniport driver of the network adapter's PCI Express (PCIe) Physical Function (PF). The PF miniport driver runs in the management operating system of the Hyper-V parent partition.

## Remarks

The PF miniport driver must issue an **NDIS\_STATUS\_NIC\_SWITCH\_CURRENT\_CAPABILITIES** status indication whenever it detects a change to the currently enabled hardware capabilities of the NIC switch on the network adapter. These capabilities could change when one of the following conditions is true:

-   The currently enabled NIC switch hardware capabilities are changed through a management application developed by the independent hardware vendor (IHV).

-   The currently enabled NIC switch hardware capabilities change for one or more network adapters that belong to a load balancing failover (LBFO) team managed by a MUX intermediate driver. For more information, see [NDIS MUX Intermediate Drivers](./ndis-mux-intermediate-drivers.md).

When the PF miniport driver issues the **NDIS\_STATUS\_NIC\_SWITCH\_CURRENT\_CAPABILITIES** status indication, it must follow these steps:

1.  The miniport driver initializes an [**NDIS\_NIC\_SWITCH\_CAPABILITIES**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_nic_switch_capabilities) structure with the currently enabled hardware capabilities of the network adapter's NIC switch.
2.  The miniport driver initializes an [**NDIS\_STATUS\_INDICATION**](/windows-hardware/drivers/ddi/ndis/ns-ndis-_ndis_status_indication) structure in the following way:

    -   The **StatusCode** member must be set to **NDIS\_STATUS\_NIC\_SWITCH\_CURRENT\_CAPABILITIES**.

    -   The **StatusBuffer** member must be set to the pointer to a [**NDIS\_NIC\_SWITCH\_CAPABILITIES**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_nic_switch_capabilities) structure. This structure contains the currently enabled hardware capabilities of the NIC switch.

    -   The **StatusBufferSize** member must be set to sizeof([**NDIS\_NIC\_SWITCH\_CAPABILITIES**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_nic_switch_capabilities)).

3.  The PF miniport driver issues the status notification by calling [**NdisMIndicateStatusEx**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndismindicatestatusex). The driver must pass a pointer to the [**NDIS\_STATUS\_INDICATION**](/windows-hardware/drivers/ddi/ndis/ns-ndis-_ndis_status_indication) structure to the *StatusIndication* parameter.

Overlying drivers can use the **NDIS\_STATUS\_NIC\_SWITCH\_CURRENT\_CAPABILITIES** status indication to determine the currently enabled NIC switch capabilities on the network adapter. Alternatively, these drivers can also issue OID query requests of [OID\_NIC\_SWITCH\_CURRENT\_CAPABILITIES](oid-nic-switch-current-capabilities.md) to obtain these capabilities at any time.

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
<td>Ndis.h</td>
</tr>
</tbody>
</table>

## See also


****
[**NDIS\_NIC\_SWITCH\_CAPABILITIES**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_nic_switch_capabilities)

[**NDIS\_STATUS\_INDICATION**](/windows-hardware/drivers/ddi/ndis/ns-ndis-_ndis_status_indication)

[OID\_NIC\_SWITCH\_CURRENT\_CAPABILITIES](oid-nic-switch-current-capabilities.md)

 

