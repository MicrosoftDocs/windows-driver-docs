---
title: Deleting a NIC Switch
description: Deleting a NIC Switch
ms.assetid: BCC6A38B-F25B-483A-B9FF-D6FF73F9B2F3
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Deleting a NIC Switch


A network adapter that supports single root I/O virtualization (SR-IOV) must be able to delete a NIC switch. Only the miniport driver for the PCI Express (PCIe) Physical Function (PF) of the SR-IOV adapter can delete a NIC switch on the adapter.

**Note**  Starting with NDIS 6.30 in Windows Server 2012, the SR-IOV interface supports only one NIC switch on the network adapter. This switch is known as the *default NIC switch*, and is referenced by the NDIS\_DEFAULT\_SWITCH\_ID identifier.

 

Prior to halting the PF miniport driver, NDIS deletes the NIC switch by issuing an object identifier (OID) set request of [OID\_NIC\_SWITCH\_DELETE\_SWITCH](https://msdn.microsoft.com/library/windows/hardware/hh451817). The **InformationBuffer** member of the [**NDIS\_OID\_REQUEST**](https://msdn.microsoft.com/library/windows/hardware/ff566710) structure contains a pointer to an [**NDIS\_NIC\_SWITCH\_DELETE\_SWITCH\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/hh451575) structure that specifies the identifier of the switch being deleted.

NDIS enforces the following policies before issuing the OID set request of [OID\_NIC\_SWITCH\_DELETE\_SWITCH](https://msdn.microsoft.com/library/windows/hardware/hh451817) to the PF miniport driver:

-   NDIS guarantees that all receive filters have been cleared from the default and nondefault virtual ports (VPorts) on the NIC switch. Receive filters are cleared through an OID set request of [OID\_RECEIVE\_FILTER\_CLEAR\_FILTER](https://msdn.microsoft.com/library/windows/hardware/ff569785).

-   NDIS guarantees that all nondefault virtual ports (VPorts) created on the switch have been previously deleted. VPorts are deleted through an OID set request of [OID\_NIC\_SWITCH\_DELETE\_VPORT](https://msdn.microsoft.com/library/windows/hardware/hh451818).

-   NDIS guarantees that all the resources for PCIe Virtual Functions (VFs) attached to the NIC switch have been previously freed. VFs are freed through an OID set request of [OID\_NIC\_SWITCH\_FREE\_VF](https://msdn.microsoft.com/library/windows/hardware/hh451822).

When it receives the OID method request of [OID\_NIC\_SWITCH\_DELETE\_SWITCH](https://msdn.microsoft.com/library/windows/hardware/hh451817), the PF miniport driver must do the following:

1.  If the PF miniport driver supports static creation and configuration of NIC switches, it must free the software resources associated with the specified NIC switch. However, the driver can only free the hardware resources for the NIC switch when [*MiniportHaltEx*](https://msdn.microsoft.com/library/windows/hardware/ff559388) is called.

    For more information about static NIC switch creation, see [Static Creation of a NIC Switch](static-creation-of-a-nic-switch.md).

2.  If the PF miniport driver supports the dynamic creation and configuration of NIC switches, it must free the hardware and software resources associated with the specified NIC switch.

    For more information about dynamic NIC switch creation, see [Dynamic Creation of a NIC Switch](dynamic-creation-of-a-nic-switch.md).

3.  If the PF miniport driver supports the dynamic creation of NIC switches and all the NIC switches have been deleted on the network adapter, the driver must disable virtualization on the adapter by calling [**NdisMEnableVirtualization**](https://msdn.microsoft.com/library/windows/hardware/hh451481). To disable virtualization, the network adapter must set the *EnableVirtualization* parameter to FALSE and the *NumVFs* parameter to zero.

    [**NdisMEnableVirtualization**](https://msdn.microsoft.com/library/windows/hardware/hh451481) clears the **NumVFs** member and the **VF Enable** bit in the SR-IOV Extended Capability structure in the PCIe configuration space of the network adapter's PF.

    **Note**  If the PF miniport driver supports static creation and configuration of NIC switches, it must only call [**NdisMEnableVirtualization**](https://msdn.microsoft.com/library/windows/hardware/hh451481) when [*MiniportHaltEx*](https://msdn.microsoft.com/library/windows/hardware/ff559388) is called.

     

 

 





