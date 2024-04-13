---
title: OID_SRIOV_READ_VF_CONFIG_SPACE
ms.topic: reference
description: An overlying driver issues an object identifier (OID) method request of OID_SRIOV_READ_VF_CONFIG_SPACE to read data from the PCI Express (PCIe) configuration space for a specified PCIe Virtual Function (VF) on the network adapter.
ms.date: 08/08/2017
keywords: 
 -OID_SRIOV_READ_VF_CONFIG_SPACE Network Drivers Starting with Windows Vista
---

# OID\_SRIOV\_READ\_VF\_CONFIG\_SPACE


An overlying driver issues an object identifier (OID) method request of OID\_SRIOV\_READ\_VF\_CONFIG\_SPACE to read data from the PCI Express (PCIe) configuration space for a specified PCIe Virtual Function (VF) on the network adapter.

After a successful return from this OID method request, the **InformationBuffer** member of the [**NDIS\_OID\_REQUEST**](/windows-hardware/drivers/ddi/oidrequest/ns-oidrequest-ndis_oid_request) structure contains a pointer to a caller-allocated buffer. This buffer is formatted to contain the following:

-   An [**NDIS\_SRIOV\_READ\_VF\_CONFIG\_SPACE\_PARAMETERS**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_sriov_read_vf_config_space_parameters) structure that contains the parameters for a read operation of the PCI configuration space of a VF.

-   Additional buffer space for the data to be read from the PCI configuration space.

## Remarks

The VF miniport driver runs in the guest operating system of a Hyper-V child partition. Because of this, the VF miniport driver cannot directly access hardware resources, such as the VF's PCI configuration space. Only the miniport driver for the PCIe Physical Function (PF) can access the PCI configuration space for a VF. The PF miniport driver runs in the management operating system of a Hyper-V parent partition and has privileged access to the VF resources.

In order to read the VF PCI configuration space, overlying drivers that run in the management operating system issue the OID method request of OID\_SRIOV\_READ\_VF\_CONFIG\_SPACE to the PF miniport driver. This OID method request is required for PF miniport drivers that support the single root I/O virtualization (SR-IOV) interface.

For example, the virtualization stack that runs in the management operating system issues the OID method request of OID\_SRIOV\_READ\_VF\_CONFIG\_SPACE when the VF miniport driver calls [**NdisMGetBusData**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndismgetbusdata) to read from its VF PCI configuration space.

When it handles the OID method request of OID\_SRIOV\_READ\_VF\_CONFIG\_SPACE, the PF miniport driver must follow these guidelines:

-   The miniport driver must verify that the VF, specified by the **VFId** member of the [**NDIS\_SRIOV\_READ\_VF\_CONFIG\_SPACE\_PARAMETERS**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_sriov_read_vf_config_space_parameters) structure, has resources that have been previously allocated. The miniport driver allocates resources for a VF through an OID method request of [OID\_NIC\_SWITCH\_ALLOCATE\_VF](oid-nic-switch-allocate-vf.md). If resources for the specified VF have not been allocated, the driver must fail the OID request.

-   The miniport driver must verify that the buffer (referenced by the **InformationBuffer** member of the [**NDIS\_OID\_REQUEST**](/windows-hardware/drivers/ddi/oidrequest/ns-oidrequest-ndis_oid_request) structure) is large enough to return the requested PCIe configuration space data. If this is not true, the driver must fail the OID request.
-   The miniport driver typically calls [**NdisMGetVirtualFunctionBusData**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndismgetvirtualfunctionbusdata) to query the requested PCIe configuration space. However, the miniport driver can also return PCIe configuration space data for the VF that the driver has cached from previous read or write operations of the PCIe configuration space.

    **Note**  If an independent hardware vendor (IHV) provides a virtual bus driver (VBD) as part of its SR-IOV [driver package](../install/driver-packages.md), its miniport driver must not call [**NdisMGetVirtualFunctionBusData**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndismgetvirtualfunctionbusdata). Instead, the driver must interface with the VBD through a private communication channel, and request that the VBD call [*ReadVfConfigBlock*](/previous-versions/windows/hardware/drivers/hh439637(v=vs.85)). This function is exposed from the [GUID\_VPCI\_INTERFACE\_STANDARD](/previous-versions/windows/hardware/drivers/hh451580(v=vs.85)) interface that is supported by the underlying virtual PCI (VPCI) bus driver.

     

If the PF miniport driver can successfully complete the OID request, the driver must copy the requested PCI configuration space data to the buffer referenced by the **InformationBuffer** member of the [**NDIS\_OID\_REQUEST**](/windows-hardware/drivers/ddi/oidrequest/ns-oidrequest-ndis_oid_request) structure. The driver copies the data to the buffer at the offset specified by **BufferOffset** member of [**NDIS\_SRIOV\_READ\_VF\_CONFIG\_SPACE\_PARAMETERS**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_sriov_read_vf_config_space_parameters) structure.

For more information, see [Querying the PCI Configuration Data of a Virtual Function](querying-the-pci-configuration-space-for-a-virtual-function.md).

### Return Status Codes

The PF miniport driver returns one of the following status codes for the OID method request of OID\_SRIOV\_READ\_VF\_CONFIG\_SPACE.

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
<td><p>The miniport driver either does not support the single root I/O virtualization (SR-IOV) interface or is not enabled to use the interface.</p></td>
</tr>
<tr class="odd">
<td><p>NDIS_STATUS_INVALID_PARAMETER</p></td>
<td><p>One or more of the members of the <a href="/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_sriov_read_vf_config_space_parameters" data-raw-source="[&lt;strong&gt;NDIS_SRIOV_READ_VF_CONFIG_SPACE_PARAMETERS&lt;/strong&gt;](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_sriov_read_vf_config_space_parameters)"><strong>NDIS_SRIOV_READ_VF_CONFIG_SPACE_PARAMETERS</strong></a> structure have invalid values.</p></td>
</tr>
<tr class="even">
<td><p>NDIS_STATUS_INVALID_LENGTH</p></td>
<td><p>The information buffer was too short. The miniport driver must set the <strong>DATA.METHOD_INFORMATION.BytesNeeded</strong> member in the <a href="/windows-hardware/drivers/ddi/ndis/ns-ndis-_ndis_oid_request" data-raw-source="[&lt;strong&gt;NDIS_OID_REQUEST&lt;/strong&gt;](/windows-hardware/drivers/ddi/oidrequest/ns-oidrequest-ndis_oid_request)"><strong>NDIS_OID_REQUEST</strong></a> structure to the minimum buffer size that is required.</p></td>
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
[GUID\_VPCI\_INTERFACE\_STANDARD](/previous-versions/windows/hardware/drivers/hh451580(v=vs.85))

[**NDIS\_OID\_REQUEST**](/windows-hardware/drivers/ddi/oidrequest/ns-oidrequest-ndis_oid_request)

[**NDIS\_SRIOV\_READ\_VF\_CONFIG\_SPACE\_PARAMETERS**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_sriov_read_vf_config_space_parameters)

[**NdisMGetBusData**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndismgetbusdata)

[**NdisMGetVirtualFunctionBusData**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndismgetvirtualfunctionbusdata)

[OID\_NIC\_SWITCH\_ALLOCATE\_VF](oid-nic-switch-allocate-vf.md)

[*ReadVfConfigBlock*](/previous-versions/windows/hardware/drivers/hh439637(v=vs.85))

