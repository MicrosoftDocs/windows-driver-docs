---
title: Deleting a Virtual Port
description: Deleting a Virtual Port
ms.assetid: CBE7AC59-D878-44BA-8FE6-168EC17A2D67
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Deleting a Virtual Port


An overlying driver issues an object identifier (OID) set request of [OID\_NIC\_SWITCH\_DELETE\_VPORT](https://msdn.microsoft.com/library/windows/hardware/hh451818) to delete a nondefault virtual port (VPort) on a network adapter's NIC switch. The overlying driver can only delete a VPort that it has previously created by issuing an OID method request of [OID\_NIC\_SWITCH\_CREATE\_VPORT](https://msdn.microsoft.com/library/windows/hardware/hh451816).

The **InformationBuffer** member of the [**NDIS\_OID\_REQUEST**](https://msdn.microsoft.com/library/windows/hardware/ff566710) structure contains a pointer to the [**NDIS\_NIC\_SWITCH\_DELETE\_VPORT\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/hh451577) structure.

An overlying driver, such as the virtualization stack, can delete a nondefault VPort that it has previously created. The overlying driver creates a VPort by issuing an OID method request of [OID\_NIC\_SWITCH\_CREATE\_VPORT](https://msdn.microsoft.com/library/windows/hardware/hh451816).

Before it issues the OID set request of [OID\_NIC\_SWITCH\_DELETE\_VPORT](https://msdn.microsoft.com/library/windows/hardware/hh451818), the overlying driver must do the following:

-   The overlying drivers must clear or move all receive filters that the driver previously set on the VPort before deleting the VPort. Receive filters are set through OID requests of [OID\_RECEIVE\_FILTER\_SET\_FILTER](https://msdn.microsoft.com/library/windows/hardware/ff569795) and are moved through OID requests of [OID\_RECEIVE\_FILTER\_MOVE\_FILTER](https://msdn.microsoft.com/library/windows/hardware/hh451845).

-   The overlying driver sets the **VPortId** member of the [**NDIS\_NIC\_SWITCH\_DELETE\_VPORT\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/hh451577) structure to the identifier of the nondefault VPort to be deleted.

    **Note**  The overlying driver must not set the **VPortId** member to **NDIS\_DEFAULT\_PORT\_NUMBER**. This VPort identifier is reserved for the default VPort that is attached to the PCI Express (PCIe) Physical Function (PF) on the network adapter. The default VPort always exists and is not deleted explicitly though an OID set request of [OID\_NIC\_SWITCH\_DELETE\_VPORT](https://msdn.microsoft.com/library/windows/hardware/hh451818).

     

The overlying driver calls [**NdisOidRequest**](https://msdn.microsoft.com/library/windows/hardware/ff563710) to issue the [OID\_NIC\_SWITCH\_DELETE\_VPORT](https://msdn.microsoft.com/library/windows/hardware/hh451818) request to the underlying PF miniport driver. When the miniport driver receives the OID\_NIC\_SWITCH\_DELETE\_VPORT request, the driver must do the following:

-   The driver must free the hardware and software resources that were allocated for the specified VPort.

-   The driver must detach the specified VPort from the PF or a PCIe Virtual Function (VF).

    If the VPort is attached to a VF, the virtualization stack ensures that the VF miniport driver that runs in the guest operating system has been previously paused and halted. As a result, all previouslyindicated receive packets from the VPort should have been returned to the VF miniport driver.

    If the VPort is attached to the PF, the PF miniport driver must stop any additional DMA to the shared memory associated with the VPort. The PF miniport driver must make sure that all previouslyindicated receive packets from the VPort are returned to the miniport. The PF miniport driver must not make any additional receive indications to NDIS that specify the VPort's identifier in the packet's [**NET\_BUFFER\_LIST**](https://msdn.microsoft.com/library/windows/hardware/ff568388) structure. After all of the indicated receive packets from the VPort are returned to the PF miniport driver, it must free the shared memory associated with the VPort by calling [**NdisFreeSharedMemory**](https://msdn.microsoft.com/library/windows/hardware/ff562601).

The following points apply to the deletion of VPorts:

-   The overlying protocol driver must delete all nondefault VPorts that it created before it calls [**NdisCloseAdapterEx**](https://msdn.microsoft.com/library/windows/hardware/ff561640).

-   The overlying filter driver must delete all nondefault VPorts that it created within its [*FilterDetach*](https://msdn.microsoft.com/library/windows/hardware/ff549918) function.

-   Before NDIS issues a set request of [OID\_NIC\_SWITCH\_DELETE\_SWITCH](https://msdn.microsoft.com/library/windows/hardware/hh451817) to delete a NIC switch on the network adapter, it guarantees that all nondefault VPorts are deleted from that switch.

-   Only nondefault VPorts can be explicitly deleted through OID requests of [OID\_NIC\_SWITCH\_DELETE\_SWITCH](https://msdn.microsoft.com/library/windows/hardware/hh451817). The default VPort is implicitly deleted when the PF miniport driver deletes the default NIC switch. For more information, see [Deleting a NIC Switch](deleting-a-nic-switch.md).

 

 





