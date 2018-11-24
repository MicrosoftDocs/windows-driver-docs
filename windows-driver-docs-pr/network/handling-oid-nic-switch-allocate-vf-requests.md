---
title: Handling OID_NIC_SWITCH_ALLOCATE_VF Requests
description: Handling OID_NIC_SWITCH_ALLOCATE_VF Requests
ms.assetid: B48A19D5-A768-4614-961D-1BD00762B6D0
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Handling OID\_NIC\_SWITCH\_ALLOCATE\_VF Requests


When the miniport driver for the PCI Express (PCIe) Physical Function (PF) on the network adapter handles the object identifier (OID) method request of [OID\_NIC\_SWITCH\_ALLOCATE\_VF](https://msdn.microsoft.com/library/windows/hardware/hh451814), it does the following:

-   The PF miniport driver allocates the software resources for a PCIe Virtual Function (VF) on the network adapter. These resources are configured based on the parameters that are specified in the [**NDIS\_NIC\_SWITCH\_VF\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/hh451593) structure.

-   The PF miniport driver assigns the VF to a NIC switch on the network adapter. The NIC switch is identified by the **SwitchId** member of the [**NDIS\_NIC\_SWITCH\_VF\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/hh451593) structure.

    For more information on a NIC switch, see [NIC Switches](nic-switches.md).

-   The PF miniport driver updates the **VFId** member with a VF identifier. This identifier is a zero-based index and must be unique across all VFs that are allocated on the NIC switch by the PF miniport driver.

    The overlying driver uses the value of the **VFId** member in successive OID requests of [OID\_NIC\_SWITCH\_FREE\_VF](https://msdn.microsoft.com/library/windows/hardware/hh451822) or [OID\_NIC\_SWITCH\_VF\_PARAMETERS](https://msdn.microsoft.com/library/windows/hardware/hh451824).

-   The PF miniport driver updates the **RequestorId** member with a PCIe Requestor Identifier (RID) for the VF.

    The miniport driver calls [**NdisMGetVirtualFunctionLocation**](https://msdn.microsoft.com/library/windows/hardware/hh451487) to get the RID information that corresponds to the VF. The driver then creates the RID by using the [**NDIS\_MAKE\_RID**](https://msdn.microsoft.com/library/windows/hardware/hh451557) macro based on the information returned by the call to **NdisMGetVirtualFunctionLocation**.

    The RID is used by the virtualization stack for remapping DMA and interrupts between the PF and VF. The RID also enables the hardware input/output memory management unit (IOMMU) to convert guest physical addresses to host physical addresses.

-   The PF miniport driver initializes and exposes the VF. This makes the VF ready for use by the virtualization stack.

If the PF miniport driver can successfully allocate the necessary software resources and initialize the VF, the driver completes the OID request with NDIS\_STATUS\_SUCCESS. The PF miniport driver must keep the VF IDs for each allocated VF. NDIS and the overlying drivers use the VF identifier in successive OID requests to the PF miniport driver for various actions, such as resetting or freeing the VF.

**Note**  When resources for the VF are allocated, the VF is in an unattached state because a virtual port (VPort) is not attached to the VF. The overlying driver can issue an OID request of [OID\_NIC\_SWITCH\_CREATE\_VPORT](https://msdn.microsoft.com/library/windows/hardware/hh451816) to create and attach a VPort to the VF. For more information, see [Creating a Virtual Port](creating-a-virtual-port.md).

 

 

 





