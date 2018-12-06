---
title: OID_SRIOV_READ_VF_CONFIG_BLOCK
description: An overlying driver issues an object identifier (OID) method request of OID_SRIOV_READ_VF_CONFIG_BLOCK to read data from a specified PCI Express (PCIe) Virtual Function (VF) configuration block.
ms.assetid: A7AC7A18-5DA2-4EE8-B635-04616ABFE08C
ms.date: 08/08/2017
keywords: 
 -OID_SRIOV_READ_VF_CONFIG_BLOCK Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# OID\_SRIOV\_READ\_VF\_CONFIG\_BLOCK


An overlying driver issues an object identifier (OID) method request of OID\_SRIOV\_READ\_VF\_CONFIG\_BLOCK to read data from a specified PCI Express (PCIe) Virtual Function (VF) configuration block.

Overlying drivers issue this OID method request to the miniport driver for the network adapter's PCIe Physical Function (PF). This OID method request is required for PF miniport drivers that support the single root I/O virtualization (SR-IOV) interface.

The **InformationBuffer** member of the [**NDIS\_OID\_REQUEST**](https://msdn.microsoft.com/library/windows/hardware/ff566710) structure contains a pointer to a caller-allocated buffer. This buffer is formatted to contain the following:

-   An [**NDIS\_SRIOV\_READ\_VF\_CONFIG\_BLOCK\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/hh451680) structure that contains the offset, in units of bytes, from the beginning of this structure to a location within the buffer that contains the data that is read from the VF configuration block.

-   Additional buffer space for the data to be read from the specified VF configuration block.

Remarks
-------

A VF configuration block is used for backchannel communication between the PF and VF miniport drivers. The IHV can define one or more VF configuration blocks for the miniport drivers. Each VF configuration block has an IHV-defined format, length, and block ID.

**Note**  Data from each VF configuration block is used only by the PF and VF miniport drivers.

 

Before it issues the OID method request of OID\_SRIOV\_READ\_VF\_CONFIG\_BLOCK, the overlying driver must set the members of [**NDIS\_SRIOV\_READ\_VF\_CONFIG\_BLOCK\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/hh451680) structure in the following way:

-   Set the **VFId** member to the identifier of the VF from which the information is to be read.

-   Set the **BlockId** member to the identifier of the VF configuration block from which the information is to be read.

-   Set the **Length** member to the number of bytes to read from the configuration block.

-   Set the **BufferOffset** member to the offset within the buffer (referenced by **InformationBuffer** member) that will contain the data that is read from the specified VF configuration block. This offset is specified in units of bytes from the beginning of the [**NDIS\_SRIOV\_READ\_VF\_CONFIG\_BLOCK\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/hh451680) structure.

When it handles the OID method request of OID\_SRIOV\_READ\_VF\_CONFIG\_BLOCK, the PF miniport driver must follow these guidelines:

-   The PF miniport driver must verify that the VF, specified by the **VFId** member of the [**NDIS\_SRIOV\_READ\_VF\_CONFIG\_BLOCK\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/hh451680) structure, has resources that have been previously allocated. The PF miniport driver allocates resources for a VF during an OID method request of [OID\_NIC\_SWITCH\_ALLOCATE\_VF](oid-nic-switch-allocate-vf.md). If resources for the specified VF have not been allocated, the driver must fail the OID request.

-   The PF miniport driver must verify that the **BlockId** member of the [**NDIS\_SRIOV\_READ\_VF\_CONFIG\_BLOCK\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/hh451680) structure specifies a valid VF configuration block. If not, the driver must fail the OID request.

For more information about backchannel communication within the single root I/O virtualization (SR-IOV) interface, see [SR-IOV PF/VF Backchannel Communication](https://msdn.microsoft.com/library/windows/hardware/hh440251).

### Return Status Codes

The PF miniport driver returns one of the following status codes for the method request of OID\_SRIOV\_READ\_VF\_CONFIG\_BLOCK.

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
<td><p>One or more of the members of the <a href="https://msdn.microsoft.com/library/windows/hardware/hh451680" data-raw-source="[&lt;strong&gt;NDIS_SRIOV_READ_VF_CONFIG_BLOCK_PARAMETERS&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/hh451680)"><strong>NDIS_SRIOV_READ_VF_CONFIG_BLOCK_PARAMETERS</strong></a> structure have invalid values.</p></td>
</tr>
<tr class="even">
<td><p>NDIS_STATUS_INVALID_LENGTH</p></td>
<td><p>The information buffer was too short. The miniport driver must set the <strong>DATA.METHOD_INFORMATION.BytesNeeded</strong> member in the <a href="https://msdn.microsoft.com/library/windows/hardware/ff566710" data-raw-source="[&lt;strong&gt;NDIS_OID_REQUEST&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff566710)"><strong>NDIS_OID_REQUEST</strong></a> structure to the minimum buffer size that is required.</p></td>
</tr>
<tr class="odd">
<td><p>NDIS_STATUS_FAILURE</p></td>
<td><p>The request failed for other reasons.</p></td>
</tr>
</tbody>
</table>

 

Requirements
------------

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
[**NDIS\_OID\_REQUEST**](https://msdn.microsoft.com/library/windows/hardware/ff566710)

[**NDIS\_SRIOV\_READ\_VF\_CONFIG\_BLOCK\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/hh451680)

[OID\_NIC\_SWITCH\_ALLOCATE\_VF](oid-nic-switch-allocate-vf.md)

[OID\_SRIOV\_READ\_VF\_CONFIG\_SPACE](oid-sriov-read-vf-config-space.md)

 

 




