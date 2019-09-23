---
title: Setting the PCI Configuration Data of a Virtual Function
description: Setting the PCI Configuration Data of a Virtual Function
ms.assetid: 74CAAD8B-7009-4C79-A496-93B4A3DA0B43
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Setting the PCI Configuration Data of a Virtual Function


The miniport driver for a PCI Express (PCIe) Virtual Function (VF) runs in the guest operating system of a Hyper-V child partition. Because of this, the VF miniport driver cannot directly access hardware resources, such as the VF's PCI configuration space. Only the miniport driver for the PCIe Physical Function (PF) can access the PCI configuration space for a VF. The PF miniport driver runs in the management operating system of a Hyper-V parent partition and has privileged access to the VF resources.

The overlying driver, such as the virtualization stack, issues the OID set request of [OID\_SRIOV\_WRITE\_VF\_CONFIG\_SPACE](https://docs.microsoft.com/windows-hardware/drivers/network/oid-sriov-write-vf-config-space) when the VF miniport driver calls [**NdisMSetBusData**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ndis/nf-ndis-ndismsetbusdata) to write to its PCI configuration space.

Before it issues this OID set request, the overlying driver must set the members of the[**NDIS\_SRIOV\_WRITE\_VF\_CONFIG\_SPACE\_PARAMETERS**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ntddndis/ns-ntddndis-_ndis_sriov_write_vf_config_space_parameters) structure in the following way:

-   Set the **VFId** member to the identifier of the VF for which the information is to be written.

-   Set the **Offset** member to the offset within the PCI configuration space of the VF in which data will be written.

-   Set the **Length** member to the number of bytes to write to the VF's PCI configuration space.

-   Set the **BufferOffset** member to the offset within the buffer (referenced by the**InformationBuffer** member) that will contain the data that is written to the specified VF's PCI configuration space. This offset is specified in units of bytes from the beginning of the [**NDIS\_SRIOV\_WRITE\_VF\_CONFIG\_SPACE\_PARAMETERS**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ntddndis/ns-ntddndis-_ndis_sriov_write_vf_config_space_parameters) structure.

When it handles the OID method request of [OID\_SRIOV\_WRITE\_VF\_CONFIG\_SPACE](https://docs.microsoft.com/windows-hardware/drivers/network/oid-sriov-write-vf-config-space), the PF miniport driver must follow these guidelines:

-   The PF miniport driver must verify that the VF, specified by the **VFId** member of the [**NDIS\_SRIOV\_WRITE\_VF\_CONFIG\_SPACE\_PARAMETERS**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ntddndis/ns-ntddndis-_ndis_sriov_write_vf_config_space_parameters) structure, has resources that have been previously allocated. The PF miniport driver allocates resources for a VF through an OID method request of [OID\_NIC\_SWITCH\_ALLOCATE\_VF](https://docs.microsoft.com/windows-hardware/drivers/network/oid-nic-switch-allocate-vf).

    If resources for the specified VF have not been allocated, the driver must fail the OID request.

-   The PF miniport driver calls [**NdisMSetVirtualFunctionBusData**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ndis/nf-ndis-ndismsetvirtualfunctionbusdata) to write to the requested PCI configuration space. However, the PF miniport driver can also return PCI configuration space data for the VF that the driver has cached from previous read or write operations of the PCI configuration space.

    **Note**  If an independent hardware vendor (IHV) provides a virtual bus driver (VBD) as part of its SR-IOV [driver package](https://docs.microsoft.com/windows-hardware/drivers/install/driver-packages), its PF miniport driver must not call [**NdisMSetVirtualFunctionBusData**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ndis/nf-ndis-ndismsetvirtualfunctionbusdata). Instead, the driver must interface with the VBD through a private communication channel, and request that the VBD call [*SetVirtualFunctionData*](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/nc-wdm-set_virtual_device_data). This function is exposed from the [GUID\_VPCI\_INTERFACE\_STANDARD](https://msdn.microsoft.com/library/windows/hardware/hh451146) interface that is supported by the underlying virtual PCI (VPCI) bus driver.

     

If the PF miniport driver can successfully complete the OID request, the driver must copy the requested PCI configuration space data to the buffer referenced by the **InformationBuffer** member of the [**NDIS\_OID\_REQUEST**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ndis/ns-ndis-_ndis_oid_request) structure. The driver copies the data to the buffer at the offset specified by the**BufferOffset** member of the [**NDIS\_SRIOV\_READ\_VF\_CONFIG\_SPACE\_PARAMETERS**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ntddndis/ns-ntddndis-_ndis_sriov_read_vf_config_space_parameters) structure.

 

 





