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

An overlying driver that runs in the management operating system issues an object identifier (OID) method request of [OID\_SRIOV\_READ\_VF\_CONFIG\_SPACE](https://docs.microsoft.com/windows-hardware/drivers/network/oid-sriov-read-vf-config-space) to read data from the PCIe configuration space for a specified VF on the network adapter.

For example, the virtualization stack that runs in the management operating system issues the OID method request of [OID\_SRIOV\_READ\_VF\_CONFIG\_SPACE](https://docs.microsoft.com/windows-hardware/drivers/network/oid-sriov-read-vf-config-space) when the VF miniport driver calls [**NdisMGetBusData**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ndis/nf-ndis-ndismgetbusdata) to read from its VF PCIe configuration space.

Before it issues this OID method request, the overlying driver must set the members of the[**NDIS\_SRIOV\_READ\_VF\_CONFIG\_SPACE\_PARAMETERS**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ntddndis/ns-ntddndis-_ndis_sriov_read_vf_config_space_parameters) structure in the following way:

-   The **VFId** member must be set to the identifier of the VF from which the information is to be read.

-   The **Offset** member must be set to the offset within the PCIe configuration space of the VF in which data will be read.

-   The **Length** member must be set to the number of bytes to read from the VF's PCIe configuration space.

-   The **BufferOffset** member must be set to the offset within the buffer (referenced by the **InformationBuffer** member) that will contain the data that is read from the specified VF's PCI configuration space. This offset is specified in units of bytes from the beginning of the [**NDIS\_SRIOV\_READ\_VF\_CONFIG\_SPACE\_PARAMETERS**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ntddndis/ns-ntddndis-_ndis_sriov_read_vf_config_space_parameters) structure.

When it handles the OID method request of [OID\_SRIOV\_READ\_VF\_CONFIG\_SPACE](https://docs.microsoft.com/windows-hardware/drivers/network/oid-sriov-read-vf-config-space), the PF miniport driver must follow these guidelines:

-   The miniport driver must verify that the VF, specified by the **VFId** member of the [**NDIS\_SRIOV\_READ\_VF\_CONFIG\_SPACE\_PARAMETERS**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ntddndis/ns-ntddndis-_ndis_sriov_read_vf_config_space_parameters) structure, has resources that have been previously allocated. The miniport driver allocates resources for a VF through an OID method request of [OID\_NIC\_SWITCH\_ALLOCATE\_VF](https://docs.microsoft.com/windows-hardware/drivers/network/oid-nic-switch-allocate-vf). If resources for the specified VF have not been allocated, the driver must fail the OID request.

-   The miniport driver must verify that the buffer (referenced by the **InformationBuffer** member of the [**NDIS\_OID\_REQUEST**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ndis/ns-ndis-_ndis_oid_request) structure) is large enough to return the requested PCIe configuration space data. If this is not true, the driver must fail the OID request.
-   The miniport driver typically calls [**NdisMGetVirtualFunctionBusData**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ndis/nf-ndis-ndismgetvirtualfunctionbusdata) to query the requested PCIe configuration space. However, the miniport driver can also return PCIe configuration space data for the VF that the driver has cached from previous read or write operations of the PCIe configuration space.

    **Note**  If an independent hardware vendor (IHV) provides a virtual bus driver (VBD) as part of its SR-IOV [driver package](https://docs.microsoft.com/windows-hardware/drivers/install/driver-packages), its miniport driver must not call [**NdisMGetVirtualFunctionBusData**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ndis/nf-ndis-ndismgetvirtualfunctionbusdata). Instead, the driver must interface with the VBD through a private communication channel, and request that the VBD call [*ReadVfConfigBlock*](https://docs.microsoft.com/previous-versions/windows/hardware/drivers/hh439637(v=vs.85)). This function is exposed from the [GUID\_VPCI\_INTERFACE\_STANDARD](https://msdn.microsoft.com/library/windows/hardware/hh451146) interface that is supported by the underlying virtual PCI (VPCI) bus driver.

     

After a successful return from this OID method request, the **InformationBuffer** member of the [**NDIS\_OID\_REQUEST**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ndis/ns-ndis-_ndis_oid_request) structure contains a pointer to a caller-allocated buffer. This buffer is formatted to contain the following:

-   An [**NDIS\_SRIOV\_READ\_VF\_CONFIG\_SPACE\_PARAMETERS**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ntddndis/ns-ntddndis-_ndis_sriov_read_vf_config_space_parameters) structure that contains the parameters for a read operation of the PCIe configuration space of a VF.

-   Additional buffer space for the data to be read from the PCIe configuration space. The driver copies the data to the buffer at the offset specified by the**BufferOffset** member of the [**NDIS\_SRIOV\_READ\_VF\_CONFIG\_SPACE\_PARAMETERS**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ntddndis/ns-ntddndis-_ndis_sriov_read_vf_config_space_parameters) structure.

 

 





