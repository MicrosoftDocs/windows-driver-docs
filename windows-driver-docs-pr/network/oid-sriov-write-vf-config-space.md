---
title: OID_SRIOV_WRITE_VF_CONFIG_SPACE
description: An overlying driver issues an object identifier (OID) set request of OID_SRIOV_WRITE_VF_CONFIG_SPACE to write data to the PCI Express (PCIe) configuration space for a specified PCIe Virtual Function (VF) on the network adapter.
ms.date: 08/08/2017
keywords: 
 -OID_SRIOV_WRITE_VF_CONFIG_SPACE Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# OID\_SRIOV\_WRITE\_VF\_CONFIG\_SPACE


An overlying driver issues an object identifier (OID) set request of OID\_SRIOV\_WRITE\_VF\_CONFIG\_SPACE to write data to the PCI Express (PCIe) configuration space for a specified PCIe Virtual Function (VF) on the network adapter.

Overlying drivers issue this OID set request to the miniport driver for the network adapter's PCIe Physical Function (PF). This OID method request is required for PF miniport drivers that support the single root I/O virtualization (SR-IOV) interface.

The **InformationBuffer** member of the [**NDIS\_OID\_REQUEST**](/windows-hardware/drivers/ddi/oidrequest/ns-oidrequest-ndis_oid_request) structure contains a pointer to a caller-allocated buffer. This buffer is formatted to contain the following:

-   An [**NDIS\_SRIOV\_WRITE\_VF\_CONFIG\_SPACE\_PARAMETERS**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_sriov_write_vf_config_space_parameters) structure that contains the parameters for a write operation of the PCI configuration space of a VF.

-   Additional buffer space that contains the data to be written to the PCI configuration space.

## Remarks

The VF miniport driver runs in the guest operating system of a Hyper-V child partition. Because of this, the VF miniport driver cannot directly access hardware resources, such as the VF's PCI configuration space. Only the PF miniport driver, which runs in the management operating system of a Hyper-V parent partition, can access the PCI configuration space for a VF.

The overlying driver, such as the virtualization stack, issues the OID set request of OID\_SRIOV\_WRITE\_VF\_CONFIG\_SPACE when the VF miniport driver calls [**NdisMSetBusData**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndismsetbusdata) to write to its PCI configuration space.

When it handles the OID method request of OID\_SRIOV\_WRITE\_VF\_CONFIG\_SPACE, the PF miniport driver must follow these guidelines:

-   The PF miniport driver must verify that the VF, specified by the **VFId** member of the [**NDIS\_SRIOV\_WRITE\_VF\_CONFIG\_SPACE\_PARAMETERS**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_sriov_write_vf_config_space_parameters) structure, has resources that have been previously allocated. The PF miniport driver allocates resources for a VF through an OID method request of [OID\_NIC\_SWITCH\_ALLOCATE\_VF](oid-nic-switch-allocate-vf.md).

    If resources for the specified VF have not been allocated, the driver must fail the OID request.

-   The PF miniport driver calls [**NdisMSetVirtualFunctionBusData**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndismsetvirtualfunctionbusdata) to write to the requested PCI configuration space. However, the PF miniport driver can also return PCI configuration space data for the VF that the driver has cached from previous read or write operations of the PCI configuration space.

    **Note**  If an independent hardware vendor (IHV) provides a virtual bus driver (VBD) as part of its SR-IOV [driver package](../install/driver-packages.md), its PF miniport driver must not call [**NdisMSetVirtualFunctionBusData**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndismsetvirtualfunctionbusdata). Instead, the driver must interface with the VBD through a private communication channel, and request that the VBD call [*SetVirtualFunctionData*](/windows-hardware/drivers/ddi/wdm/nc-wdm-set_virtual_device_data). This function is exposed from the [GUID\_VPCI\_INTERFACE\_STANDARD](https://msdn.microsoft.com/library/windows/hardware/hh451146) interface that is supported by the underlying virtual PCI (VPCI) bus driver.

     

If the PF miniport driver can successfully complete the OID request, the driver must copy the requested PCI configuration space data to the buffer referenced by the **InformationBuffer** member of the [**NDIS\_OID\_REQUEST**](/windows-hardware/drivers/ddi/oidrequest/ns-oidrequest-ndis_oid_request) structure. The driver copies the data to the buffer at the offset specified by **BufferOffset** member of the [**NDIS\_SRIOV\_READ\_VF\_CONFIG\_SPACE\_PARAMETERS**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_sriov_read_vf_config_space_parameters) structure.

For more information, see [Setting the PCI Configuration Data of a Virtual Function](./setting-the-pci-configuration-data-of-a-virtual-function.md).

### Return Status Codes

The PF miniport driver returns one of the following status codes for the OID set request of OID\_SRIOV\_WRITE\_VF\_CONFIG\_SPACE.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Status Code</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>NDIS_STATUS_SUCCESS</p></td>
<td><p>The OID request completed successfully.</p></td>
</tr>
<tr class="even">
<td><p>NDIS_STATUS_NOT_SUPPORTED</p></td>
<td><p>The PF miniport driver either does not support the single root I/O virtualization (SR-IOV) interface or is not enabled to use the interface.</p></td>
</tr>
<tr class="odd">
<td><p>NDIS_STATUS_INVALID_PARAMETER</p></td>
<td><p>One or more of the members of the <a href="/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_sriov_write_vf_config_space_parameters" data-raw-source="[&lt;strong&gt;NDIS_SRIOV_WRITE_VF_CONFIG_SPACE_PARAMETERS&lt;/strong&gt;](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_sriov_write_vf_config_space_parameters)"><strong>NDIS_SRIOV_WRITE_VF_CONFIG_SPACE_PARAMETERS</strong></a> structure have invalid values.</p></td>
</tr>
<tr class="even">
<td><p>NDIS_STATUS_INVALID_LENGTH</p></td>
<td><p>The information buffer was too short. NDIS sets the <strong>DATA.SET_INFORMATION.BytesNeeded</strong> member in the <a href="/windows-hardware/drivers/ddi/ndis/ns-ndis-_ndis_oid_request" data-raw-source="[&lt;strong&gt;NDIS_OID_REQUEST&lt;/strong&gt;](/windows-hardware/drivers/ddi/oidrequest/ns-oidrequest-ndis_oid_request)"><strong>NDIS_OID_REQUEST</strong></a> structure to the minimum buffer size that is required.</p></td>
</tr>
<tr class="odd">
<td><p>NDIS_STATUS_FAILURE</p></td>
<td><p>The request failed for other reasons.</p></td>
</tr>
</tbody>
</table>

 

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
<td>Ntddndis.h (include Ndis.h)</td>
</tr>
</tbody>
</table>

## See also


****
[GUID\_VPCI\_INTERFACE\_STANDARD](https://msdn.microsoft.com/library/windows/hardware/hh451146)

[**NDIS\_OID\_REQUEST**](/windows-hardware/drivers/ddi/oidrequest/ns-oidrequest-ndis_oid_request)

[**NDIS\_SRIOV\_WRITE\_VF\_CONFIG\_SPACE\_PARAMETERS**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_sriov_write_vf_config_space_parameters)

[**NdisMSetBusData**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndismsetbusdata)

[**NdisMSetVirtualFunctionBusData**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndismsetvirtualfunctionbusdata)

[OID\_NIC\_SWITCH\_ALLOCATE\_VF](oid-nic-switch-allocate-vf.md)

[OID\_SRIOV\_READ\_VF\_CONFIG\_SPACE](oid-sriov-read-vf-config-space.md)

[*SetVirtualFunctionData*](/windows-hardware/drivers/ddi/wdm/nc-wdm-set_virtual_device_data)

