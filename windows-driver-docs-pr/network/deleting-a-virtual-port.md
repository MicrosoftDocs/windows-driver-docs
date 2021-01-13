---
title: Deleting a Virtual Port
description: Deleting a Virtual Port
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Deleting a Virtual Port


An overlying driver issues an object identifier (OID) set request of [OID\_NIC\_SWITCH\_DELETE\_VPORT](./oid-nic-switch-delete-vport.md) to delete a nondefault virtual port (VPort) on a network adapter's NIC switch. The overlying driver can only delete a VPort that it has previously created by issuing an OID method request of [OID\_NIC\_SWITCH\_CREATE\_VPORT](./oid-nic-switch-create-vport.md).

The **InformationBuffer** member of the [**NDIS\_OID\_REQUEST**](/windows-hardware/drivers/ddi/oidrequest/ns-oidrequest-ndis_oid_request) structure contains a pointer to the [**NDIS\_NIC\_SWITCH\_DELETE\_VPORT\_PARAMETERS**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_nic_switch_delete_vport_parameters) structure.

An overlying driver, such as the virtualization stack, can delete a nondefault VPort that it has previously created. The overlying driver creates a VPort by issuing an OID method request of [OID\_NIC\_SWITCH\_CREATE\_VPORT](./oid-nic-switch-create-vport.md).

Before it issues the OID set request of [OID\_NIC\_SWITCH\_DELETE\_VPORT](./oid-nic-switch-delete-vport.md), the overlying driver must do the following:

-   The overlying drivers must clear or move all receive filters that the driver previously set on the VPort before deleting the VPort. Receive filters are set through OID requests of [OID\_RECEIVE\_FILTER\_SET\_FILTER](./oid-receive-filter-set-filter.md) and are moved through OID requests of [OID\_RECEIVE\_FILTER\_MOVE\_FILTER](./oid-receive-filter-move-filter.md).

-   The overlying driver sets the **VPortId** member of the [**NDIS\_NIC\_SWITCH\_DELETE\_VPORT\_PARAMETERS**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_nic_switch_delete_vport_parameters) structure to the identifier of the nondefault VPort to be deleted.

    **Note**  The overlying driver must not set the **VPortId** member to **NDIS\_DEFAULT\_PORT\_NUMBER**. This VPort identifier is reserved for the default VPort that is attached to the PCI Express (PCIe) Physical Function (PF) on the network adapter. The default VPort always exists and is not deleted explicitly though an OID set request of [OID\_NIC\_SWITCH\_DELETE\_VPORT](./oid-nic-switch-delete-vport.md).

     

The overlying driver calls [**NdisOidRequest**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndisoidrequest) to issue the [OID\_NIC\_SWITCH\_DELETE\_VPORT](./oid-nic-switch-delete-vport.md) request to the underlying PF miniport driver. When the miniport driver receives the OID\_NIC\_SWITCH\_DELETE\_VPORT request, the driver must do the following:

-   The driver must free the hardware and software resources that were allocated for the specified VPort.

-   The driver must detach the specified VPort from the PF or a PCIe Virtual Function (VF).

    If the VPort is attached to a VF, the virtualization stack ensures that the VF miniport driver that runs in the guest operating system has been previously paused and halted. As a result, all previouslyindicated receive packets from the VPort should have been returned to the VF miniport driver.

    If the VPort is attached to the PF, the PF miniport driver must stop any additional DMA to the shared memory associated with the VPort. The PF miniport driver must make sure that all previouslyindicated receive packets from the VPort are returned to the miniport. The PF miniport driver must not make any additional receive indications to NDIS that specify the VPort's identifier in the packet's [**NET\_BUFFER\_LIST**](/windows-hardware/drivers/ddi/nbl/ns-nbl-net_buffer_list) structure. After all of the indicated receive packets from the VPort are returned to the PF miniport driver, it must free the shared memory associated with the VPort by calling [**NdisFreeSharedMemory**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndisfreesharedmemory).

The following points apply to the deletion of VPorts:

-   The overlying protocol driver must delete all nondefault VPorts that it created before it calls [**NdisCloseAdapterEx**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndiscloseadapterex).

-   The overlying filter driver must delete all nondefault VPorts that it created within its [*FilterDetach*](/windows-hardware/drivers/ddi/ndis/nc-ndis-filter_detach) function.

-   Before NDIS issues a set request of [OID\_NIC\_SWITCH\_DELETE\_SWITCH](./oid-nic-switch-delete-switch.md) to delete a NIC switch on the network adapter, it guarantees that all nondefault VPorts are deleted from that switch.

-   Only nondefault VPorts can be explicitly deleted through OID requests of [OID\_NIC\_SWITCH\_DELETE\_SWITCH](./oid-nic-switch-delete-switch.md). The default VPort is implicitly deleted when the PF miniport driver deletes the default NIC switch. For more information, see [Deleting a NIC Switch](deleting-a-nic-switch.md).

 

