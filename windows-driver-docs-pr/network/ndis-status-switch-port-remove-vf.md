---
title: NDIS_STATUS_SWITCH_PORT_REMOVE_VF
description: The NDIS_STATUS_SWITCH_PORT_REMOVE_VF status indication is issued by a Hyper-V extensible switch forwarding extension to remove the binding between a virtual machine (VM) network adapter and a PCI Express (PCIe) virtual function (VF).
ms.date: 07/18/2017
keywords:
 - NDIS_STATUS_SWITCH_PORT_REMOVE_VF Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# NDIS\_STATUS\_SWITCH\_PORT\_REMOVE\_VF


The **NDIS\_STATUS\_SWITCH\_PORT\_REMOVE\_VF** status indication is issued by a Hyper-V extensible switch forwarding extension to remove the binding between a virtual machine (VM) network adapter and a PCI Express (PCIe) virtual function (VF). The VF is exposed and supported by an underlying physical network adapter that supports the single root I/O virtualization (SR-IOV) interface.

In order to issue the **NDIS\_STATUS\_SWITCH\_PORT\_REMOVE\_VF** status indication, the forwarding extension must encapsulate the indication in an [**NDIS\_SWITCH\_NIC\_STATUS\_INDICATION**](/windows-hardware/drivers/ddi/ndis/ns-ndis-_ndis_switch_nic_status_indication) structure and issue an [**NDIS\_STATUS\_SWITCH\_NIC\_STATUS**](ndis-status-switch-nic-status.md) status indication.

For more information on this process, see [Guidelines for Issuing an **NDIS\_STATUS\_SWITCH\_PORT\_REMOVE\_VF** Status Indication](#issuing).

## Remarks

A PCIe VF is created and allocated by an underlying physical adapter that supports the SR-IOV interface. Once created, the virtualization stack attaches, or *assigns*, the VF to a Hyper-V child partition. The guest operating system that runs in this partition exposes a virtual machine (VM) network adapter that is bound to the VF of the underlying SR-IOV physical adapter.

After the virtual and physical network adapters are assigned, packets are routed directly between the VF and the VM network adapter. However, because the extensible switch is not involved in packet delivery, extensible switch port policies are not applied to these packets. This includes port policies for access control lists (ACLs) and quality of service (QoS).

An extensible switch forwarding extension can remove the assignment of the VF to the child partition by issuing an **NDIS\_STATUS\_SWITCH\_PORT\_REMOVE\_VF** status indication. This indication causes the packets to be delivered through an extensible switch port instead of directly between the VM network adapter and the VF of the underlying SR-IOV physical adapter. This allows the extensible switch port policies to be applied to packets that are received or sent over the extensible switch port.

When the forwarding extension makes the **NDIS\_STATUS\_SWITCH\_PORT\_REMOVE\_VF** status indication, it specifies the extensible switch port to which the VM network adapter is connected.

For more information about extensible switch forwarding extensions, see [Forwarding Extensions](./forwarding-extensions.md).

### <a href="" id="issuing"></a>Guidelines for Issuing an NDIS\_STATUS\_SWITCH\_PORT\_REMOVE\_VF Status Indication

In order to issue the **NDIS\_STATUS\_SWITCH\_PORT\_REMOVE\_VF** status indication, the forwarding extension must follow these steps:

1.  The forwarding extension initializes an [**NDIS\_STATUS\_INDICATION**](/windows-hardware/drivers/ddi/ndis/ns-ndis-_ndis_status_indication) structure for the **NDIS\_STATUS\_SWITCH\_PORT\_REMOVE\_VF** indication. For this indication, the forwarding extensions sets the following members of the **NDIS\_STATUS\_INDICATION** structure:

    -   The **StatusCode** member must be set to **NDIS\_STATUS\_SWITCH\_PORT\_REMOVE\_VF**.

    -   The **StatusBuffer** member must be set to **NULL**.

    -   The **StatusBufferSize** must be set to zero.

2.  The forwarding extension initializes an [**NDIS\_SWITCH\_NIC\_STATUS\_INDICATION**](/windows-hardware/drivers/ddi/ndis/ns-ndis-_ndis_switch_nic_status_indication) structure. In order to remove a VF assignment, the forwarding extension must set the members in the following way:

    -   The **DestinationPortId** member must be set to the identifier of an extensible switch port to which the VM network adapter is connected.

    -   The **DestinationNicIndex** member must be set to the index value of the VM network adapter that is connected to the specified port.

    -   The **SourcePortId** member must be set to **NDIS\_SWITCH\_DEFAULT\_PORT\_ID**.

    -   The **SourceNicIndex** member must be set to **NDIS\_SWITCH\_DEFAULT\_NIC\_INDEX**.

    -   The **StatusIndication** member must be set to the address of the [**NDIS\_STATUS\_INDICATION**](/windows-hardware/drivers/ddi/ndis/ns-ndis-_ndis_status_indication) structure for the **NDIS\_STATUS\_SWITCH\_PORT\_REMOVE\_VF** indication.

3.  The forwarding extension initializes an [**NDIS\_STATUS\_INDICATION**](/windows-hardware/drivers/ddi/ndis/ns-ndis-_ndis_status_indication) structure for the [**NDIS\_SWITCH\_NIC\_STATUS\_INDICATION**](/windows-hardware/drivers/ddi/ndis/ns-ndis-_ndis_switch_nic_status_indication) indication. For this indication, the forwarding extension sets the following members of the **NDIS\_STATUS\_INDICATION** structure:

    -   The **StatusCode** member must be set to [**NDIS\_STATUS\_SWITCH\_NIC\_STATUS**](ndis-status-switch-nic-status.md).

    -   The **StatusBuffer** member must be set to the address of the [**NDIS\_SWITCH\_NIC\_STATUS\_INDICATION**](/windows-hardware/drivers/ddi/ndis/ns-ndis-_ndis_switch_nic_status_indication) structure.

    -   The **StatusBufferSize** must be set to the length, in bytes, of the [**NDIS\_SWITCH\_NIC\_STATUS\_INDICATION**](/windows-hardware/drivers/ddi/ndis/ns-ndis-_ndis_switch_nic_status_indication) structure and the [**NDIS\_STATUS\_INDICATION**](/windows-hardware/drivers/ddi/ndis/ns-ndis-_ndis_status_indication) structure for the **NDIS\_STATUS\_SWITCH\_PORT\_REMOVE\_VF** indication.

4.  The forwarding extension must call [*ReferenceSwitchNic*](/windows-hardware/drivers/ddi/ndis/nc-ndis-ndis_switch_reference_switch_nic) to increment a reference counter for the VM network adapter. If *ReferenceSwitchNic* does not complete with NDIS\_STATUS\_SUCCESS, the forwarding extension must not forward the status indication.

    **Note**  If the forwarding extension has received an [OID\_SWITCH\_NIC\_DISCONNECT](./oid-switch-nic-disconnect.md) set request for the VM adapter, it must not call [*ReferenceSwitchNic*](/windows-hardware/drivers/ddi/ndis/nc-ndis-ndis_switch_reference_switch_nic) nor forward the status indication.

     

5.  The forwarding extension calls [**NdisFIndicateStatus**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndisfindicatestatus) to forward the [**NDIS\_STATUS\_INDICATION**](/windows-hardware/drivers/ddi/ndis/ns-ndis-_ndis_status_indication) to overlying extensions in the extensible switch driver stack. When the forwarding extension calls this function, it sets the *StatusIndication* parameter to a pointer to the **NDIS\_STATUS\_INDICATION** structure for the [**NDIS\_STATUS\_SWITCH\_NIC\_STATUS**](ndis-status-switch-nic-status.md) indication.

6.  After [**NdisFIndicateStatus**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndisfindicatestatus) returns, the forwarding extension must call [*DereferenceSwitchNic*](/windows-hardware/drivers/ddi/ndis/nc-ndis-ndis_switch_dereference_switch_nic) to decrement the reference counter for the VM network adapter.

**Note**  The forwarding extension must follow the previous steps for each VF assignment that the forwarding extension is removing.

 

For more information on how a forwarding extension forwards status indications, see [Filter Module Status Indications](./filter-module-status-indications.md).

### Guidelines for Determining VF Assignments

The forwarding extension can enumerate the current VF assignments for virtual network adapters by issuing an OID query request of [OID\_SWITCH\_NIC\_ARRAY](./oid-switch-nic-array.md). This request returns an [**NDIS\_SWITCH\_NIC\_ARRAY**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_switch_nic_array) structure that contains an array of [**NDIS\_SWITCH\_NIC\_PARAMETERS**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_switch_nic_parameters) structures. Each **NDIS\_SWITCH\_NIC\_PARAMETERS** structure specifies the parameters of a network adapter that is exposed in one of the following environments:

-   The management operating system that runs in the Hyper-V parent partition.

    Network adapters that are exposed in this operating system are specified with an [**NDIS\_SWITCH\_NIC\_TYPE**](/windows-hardware/drivers/ddi/ntddndis/ne-ntddndis-_ndis_switch_nic_type) enumeration value of **NdisSwitchNicTypeExternal** or **NdisSwitchNicTypeInternal**.

-   The guest operating system that runs in a Hyper-V child partition.

    Network adapters that are exposed in this operating system are specified with an [**NDIS\_SWITCH\_NIC\_TYPE**](/windows-hardware/drivers/ddi/ntddndis/ne-ntddndis-_ndis_switch_nic_type) enumeration value of **NdisSwitchNicTypeSynthetic** or **NdisSwitchNicTypeEmulated**.

If the OID query request of [OID\_SWITCH\_NIC\_ARRAY](./oid-switch-nic-array.md) completes with a status of NDIS\_STATUS\_SUCCESS, the forwarding extension can determine VF assignments by inspecting each [**NDIS\_SWITCH\_NIC\_PARAMETERS**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_switch_nic_parameters) structure in the returned array. If the **VFAssigned** member of the **NDIS\_SWITCH\_NIC\_PARAMETERS** structure is set to **TRUE**, the network adapter that corresponds to the **NDIS\_SWITCH\_NIC\_PARAMETERS** structure is assigned to a VF.

The forwarding extension can remove the assignment by issuing an **NDIS\_STATUS\_SWITCH\_PORT\_REMOVE\_VF** status indication. In this case, the forwarding extension must set the **DestinationPortId** member of the [**NDIS\_SWITCH\_NIC\_STATUS\_INDICATION**](/windows-hardware/drivers/ddi/ndis/ns-ndis-_ndis_switch_nic_status_indication) to the value of the **PortId** member of the [**NDIS\_SWITCH\_NIC\_PARAMETERS**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_switch_nic_parameters) structure.

For more information on how to issue an **NDIS\_STATUS\_SWITCH\_PORT\_REMOVE\_VF** status indication, see [Guidelines for Issuing an **NDIS\_STATUS\_SWITCH\_PORT\_REMOVE\_VF** Status Indication](#issuing).

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
[**NdisFIndicateStatus**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndisfindicatestatus)

[**NDIS\_STATUS\_INDICATION**](/windows-hardware/drivers/ddi/ndis/ns-ndis-_ndis_status_indication)

[**NDIS\_STATUS\_SWITCH\_NIC\_STATUS**](ndis-status-switch-nic-status.md)

[**NDIS\_SWITCH\_NIC\_ARRAY**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_switch_nic_array)

[**NDIS\_SWITCH\_NIC\_PARAMETERS**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_switch_nic_parameters)

[**NDIS\_SWITCH\_NIC\_TYPE**](/windows-hardware/drivers/ddi/ntddndis/ne-ntddndis-_ndis_switch_nic_type)

[OID\_SWITCH\_NIC\_ARRAY](./oid-switch-nic-array.md)

 

