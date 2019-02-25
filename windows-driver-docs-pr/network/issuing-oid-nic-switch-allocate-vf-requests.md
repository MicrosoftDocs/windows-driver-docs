---
title: Issuing OID_NIC_SWITCH_ALLOCATE_VF Requests
description: Issuing OID_NIC_SWITCH_ALLOCATE_VF Requests
ms.assetid: 72285E72-DEC7-4578-9B6C-E616FECD6F41
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Issuing OID\_NIC\_SWITCH\_ALLOCATE\_VF Requests


Before it issues the object identifier (OID) method request of [OID\_NIC\_SWITCH\_ALLOCATE\_VF](https://msdn.microsoft.com/library/windows/hardware/hh451814) to the miniport driver for the PCI Express (PCIe) Physical Function (PF), the overlying driver formats an [**NDIS\_NIC\_SWITCH\_VF\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/hh451593) structure. This structure contains the configuration parameters for the resources to be allocated for a PCIe Virtual Function (VF) on the network adapter. The overlying driver must set the members of this structure in the following way:

-   The **SwitchId** member must be set to the identifier of a NIC switch that was previously created on the network adapter. A NIC switch is created through an OID method request of [OID\_NIC\_SWITCH\_CREATE\_SWITCH](https://msdn.microsoft.com/library/windows/hardware/hh451815).

    When it handles the OID method request of [OID\_NIC\_SWITCH\_ALLOCATE\_VF](https://msdn.microsoft.com/library/windows/hardware/hh451814), the miniport driver for the PCIe Physical Function (PF) allocates resources for the VF. If resources are allocated successfully, the PF miniport driver assigns the VF to the specified NIC switch.

    **Note**  Starting with NDIS 6.30 in Windows Server 2012, the SR-IOV interface only supports the default NIC switch on the network adapter. The value of the **SwitchId** member must be set to NDIS\_DEFAULT\_SWITCH\_ID.

    For more information on a NIC switch, see [NIC Switches](nic-switches.md).

-   The **VFId** member must be set to NDIS\_INVALID\_VF\_FUNCTION\_ID.

-   The **RequestorId** member must be set to NDIS\_INVALID\_RID.

-   The **VMFriendlyName** and **VMName** members must be set to the parameters of a Hyper-V child partition. The PF miniport driver uses these members only for informational purposes.

    **Note**  The Hyper-V child partition is also known as a *virtual machine (VM)*.

    The VF is associated with the specified VM before the overlying driver issues the [OID\_NIC\_SWITCH\_CREATE\_SWITCH](https://msdn.microsoft.com/library/windows/hardware/hh451815) request.

-   The **NicName** member must be set to the identifier of the virtual machine (VM) network adapter. This virtual adapter is exposed in the guest operating system that runs in the VM. The PF miniport driver uses this member only for informational purposes.

    When resources are allocated for the VF and it is attached to the child partition, a VF network adapter is exposed in the guest operating system. The VM network adapter teams with the VF network adapter for packet transfer over the hardware-based VF data path.

    However, the VF could be detached from the child partition, such as during Live Migration. When this happens, the packet transfer occurs over the software-based synthetic data path. For more information on these data paths, see [SR-IOV Data Paths](sr-iov-data-paths.md).

-   The **PermanentMacAddress** and **CurrentMacAddress** members must be set to the media access control (MAC) addresses for the virtual network adapter of the VF. These addresses are exposed to the network stack that runs in the guest operating system of the Hyper-V child partition.

The overlying driver issues the OID method request of [OID\_NIC\_SWITCH\_ALLOCATE\_VF](https://msdn.microsoft.com/library/windows/hardware/hh451814) by following these steps:

1.  The overlying driver initializes an [**NDIS\_OID\_REQUEST**](https://msdn.microsoft.com/library/windows/hardware/ff566710) structure for the OID method request. The driver sets the **InformationBuffer** member to a pointer to an initialized [**NDIS\_NIC\_SWITCH\_VF\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/hh451593) structure.

2.  The overlying driver calls [**NdisOidRequest**](https://msdn.microsoft.com/library/windows/hardware/ff563710) to issue the OID request to the underlying PF miniport driver.

    **Note**  When the overlying driver calls [**NdisOidRequest**](https://msdn.microsoft.com/library/windows/hardware/ff563710), NDIS intercepts the OID request and verifies the VF parameters specified in the [**NDIS\_NIC\_SWITCH\_VF\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/hh451593) structure. If the parameters are verified successfully, NDIS forwards the OID to the PF miniport driver. Otherwise, NDIS fails the OID request with NDIS\_STATUS\_INVALID\_PARAMETER.

After an overlying driver requests resource allocation for a VF, that driver is the only component that can request the freeing of the resources for the same VF. The overlying driver must issue an OID set request of [OID\_NIC\_SWITCH\_FREE\_VF](https://msdn.microsoft.com/library/windows/hardware/hh451822) to free the VF resources. Before the overlying driver can be halted, it must free the resources for each VF that was allocated by the driver's [OID\_NIC\_SWITCH\_ALLOCATE\_VF](https://msdn.microsoft.com/library/windows/hardware/hh451814) request.