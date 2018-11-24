---
title: Querying the PCI Configuration Space for a Virtual Function
description: Querying the PCI Configuration Space for a Virtual Function
ms.assetid: FFE7C946-4406-46A5-A9A7-CD0E2756C98E
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Querying the PCI Configuration Space for a Virtual Function

**Note** This method can only be used by overlying drivers that run in the management operating system of the Hyper-V parent partition.

The miniport driver for a PCI Express (PCIe) Virtual Function (VF) runs in the guest operating system of a Hyper-V child partition. Because of this, the VF miniport driver cannot directly access hardware resources, such as the VF's PCIe configuration space. Only the miniport driver for the PCIe Physical Function (PF) can access the PCIe configuration space for a VF. The PF miniport driver runs in the management operating system of a Hyper-V parent partition and has privileged access to the VF resources.

An overlying driver that runs in the management operating system issues an object identifier (OID) method request of [OID\_SRIOV\_READ\_VF\_CONFIG\_SPACE](https://msdn.microsoft.com/library/windows/hardware/hh451879) to read data from the PCIe configuration space for a specified VF on the network adapter.

For example, the virtualization stack that runs in the management operating system issues the OID method request of [OID\_SRIOV\_READ\_VF\_CONFIG\_SPACE](https://msdn.microsoft.com/library/windows/hardware/hh451879) when the VF miniport driver calls [**NdisMGetBusData**](https://msdn.microsoft.com/library/windows/hardware/ff563591) to read from its VF PCIe configuration space.

Before it issues this OID method request, the overlying driver must set the members of the[**NDIS\_SRIOV\_READ\_VF\_CONFIG\_SPACE\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/hh451681) structure in the following way:

-   The **VFId** member must be set to the identifier of the VF from which the information is to be read.

-   The **Offset** member must be set to the offset within the PCIe configuration space of the VF in which data will be read.

-   The **Length** member must be set to the number of bytes to read from the VF's PCIe configuration space.

-   The **BufferOffset** member must be set to the offset within the buffer (referenced by the **InformationBuffer** member) that will contain the data that is read from the specified VF's PCI configuration space. This offset is specified in units of bytes from the beginning of the [**NDIS\_SRIOV\_READ\_VF\_CONFIG\_SPACE\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/hh451681) structure.

When it handles the OID method request of [OID\_SRIOV\_READ\_VF\_CONFIG\_SPACE](https://msdn.microsoft.com/library/windows/hardware/hh451879), the PF miniport driver must follow these guidelines:

-   The miniport driver must verify that the VF, specified by the **VFId** member of the [**NDIS\_SRIOV\_READ\_VF\_CONFIG\_SPACE\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/hh451681) structure, has resources that have been previously allocated. The miniport driver allocates resources for a VF through an OID method request of [OID\_NIC\_SWITCH\_ALLOCATE\_VF](https://msdn.microsoft.com/library/windows/hardware/hh451814). If resources for the specified VF have not been allocated, the driver must fail the OID request.

-   The miniport driver must verify that the buffer (referenced by the **InformationBuffer** member of the [**NDIS\_OID\_REQUEST**](https://msdn.microsoft.com/library/windows/hardware/ff566710) structure) is large enough to return the requested PCIe configuration space data. If this is not true, the driver must fail the OID request.
-   The miniport driver typically calls [**NdisMGetVirtualFunctionBusData**](https://msdn.microsoft.com/library/windows/hardware/hh451484) to query the requested PCIe configuration space. However, the miniport driver can also return PCIe configuration space data for the VF that the driver has cached from previous read or write operations of the PCIe configuration space.

    **Note**  If an independent hardware vendor (IHV) provides a virtual bus driver (VBD) as part of its SR-IOV [driver package](https://msdn.microsoft.com/library/windows/hardware/ff544840), its miniport driver must not call [**NdisMGetVirtualFunctionBusData**](https://msdn.microsoft.com/library/windows/hardware/hh451484). Instead, the driver must interface with the VBD through a private communication channel, and request that the VBD call [*ReadVfConfigBlock*](https://msdn.microsoft.com/library/windows/hardware/hh439637). This function is exposed from the [GUID\_VPCI\_INTERFACE\_STANDARD](https://msdn.microsoft.com/library/windows/hardware/hh451146) interface that is supported by the underlying virtual PCI (VPCI) bus driver.

     

After a successful return from this OID method request, the **InformationBuffer** member of the [**NDIS\_OID\_REQUEST**](https://msdn.microsoft.com/library/windows/hardware/ff566710) structure contains a pointer to a caller-allocated buffer. This buffer is formatted to contain the following:

-   An [**NDIS\_SRIOV\_READ\_VF\_CONFIG\_SPACE\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/hh451681) structure that contains the parameters for a read operation of the PCIe configuration space of a VF.

-   Additional buffer space for the data to be read from the PCIe configuration space. The driver copies the data to the buffer at the offset specified by the**BufferOffset** member of the [**NDIS\_SRIOV\_READ\_VF\_CONFIG\_SPACE\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/hh451681) structure.

 

 





