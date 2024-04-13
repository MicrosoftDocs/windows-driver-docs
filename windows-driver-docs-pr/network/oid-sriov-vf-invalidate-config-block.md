---
title: OID_SRIOV_VF_INVALIDATE_CONFIG_BLOCK
ms.topic: reference
description: NDIS issues an object identifier (OID) method request of OID_SRIOV_VF_INVALIDATE_CONFIG_BLOCK to notify the miniport driver of a PCI Express (PCIe) Virtual Function (VF) that data within one or more configuration blocks has changed.
ms.date: 08/08/2017
keywords: 
 -OID_SRIOV_VF_INVALIDATE_CONFIG_BLOCK Network Drivers Starting with Windows Vista
---

# OID\_SRIOV\_VF\_INVALIDATE\_CONFIG\_BLOCK


NDIS issues an object identifier (OID) method request of OID\_SRIOV\_VF\_INVALIDATE\_CONFIG\_BLOCK to notify the miniport driver of a PCI Express (PCIe) Virtual Function (VF) that data within one or more configuration blocks has changed. NDIS issues this OID when the miniport driver for a PCIe Physical Function (PF) calls [**NdisMInvalidateConfigBlock**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndisminvalidateconfigblock).

The **InformationBuffer** member of the [**NDIS\_OID\_REQUEST**](/windows-hardware/drivers/ddi/oidrequest/ns-oidrequest-ndis_oid_request) structure contains a pointer to an [**NDIS\_SRIOV\_VF\_INVALIDATE\_CONFIG\_BLOCK\_INFO**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_sriov_vf_invalidate_config_block_info) structure. This structure specifies one or more Virtual Function (VF) configuration blocks whose data has been changed (*invalidated*) by the PF miniport driver.

## Remarks

A VF configuration block is used for backchannel communication between the PF and VF miniport drivers. The IHV can define one or more VF configuration blocks for the device. Each VF configuration block has an IHV-defined format, length, and block ID.

**Note**  Data from each VF configuration block is used only by the PF and VF miniport drivers.

 

VF configuration data is exchanged between the following drivers:

-   The VF driver, which runs in the guest operating system. This operating system runs within a Hyper-V child partition.

-   The PF driver, which runs in the management operating system. This operating system runs within the Hyper-V parent partition.

In order to handle notifications of invalid VF configuration data, NDIS and the miniport drivers perform the following steps:

1.  In the guest operating system, NDIS issues an I/O control request of [**IOCTL\_VPCI\_INVALIDATE\_BLOCK**](/windows-hardware/drivers/ddi/vpci/ni-vpci-ioctl_vpci_invalidate_block) request. When this IOCTL is completed, NDIS is notified that VF configuration data has changed.

2.  In the management operating system, the following steps occur:

    1.  The PF miniport driver calls the [**NdisMInvalidateConfigBlock**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndisminvalidateconfigblock) function to notify NDIS that VF configuration data has changed and is no longer valid. The driver sets the *BlockMask* parameter to a ULONGLONG bitmask that specifies which VF configuration blocks have changed. Each bit in the bitmask corresponds to a VF configuration block. If the bit is set to one, the data in the corresponding VF configuration block has changed.
    2.  NDIS signals the virtualization stack, which runs in the management operating system, about the change to VF configuration block data. The virtualization stack caches the *BlockMask* parameter data.

        **Note**  Each time that the PF miniport driver calls [**NdisMInvalidateConfigBlock**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndisminvalidateconfigblock), the virtualization stack ORs the *BlockMask* parameter data with the current value in its cache.

         

    3.  The virtualization stack notifies the virtual PCI (VPCI) driver, which runs in the guest operating system, about the invalidation of VF configuration data. The virtualization stack sends the cached *BlockMask* parameter data to the VPCI driver.

3.  In the Guest operating system, the following steps occur:

    1.  The VPCI driver saves the cached *BlockMask* parameter data in the **BlockMask** member of the [**VPCI\_INVALIDATE\_BLOCK\_OUTPUT**](/windows-hardware/drivers/ddi/vpci/ns-vpci-_vpci_invalidate_block_output) structure that is associated with the [**IOCTL\_VPCI\_INVALIDATE\_BLOCK**](/windows-hardware/drivers/ddi/vpci/ni-vpci-ioctl_vpci_invalidate_block) request.

    2.  The VPCI driver successfully completes the [**IOCTL\_VPCI\_INVALIDATE\_BLOCK**](/windows-hardware/drivers/ddi/vpci/ni-vpci-ioctl_vpci_invalidate_block) request. When this happens, NDIS issues an OID method request of OID\_SRIOV\_VF\_INVALIDATE\_CONFIG\_BLOCK to the VF miniport driver. An [**NDIS\_SRIOV\_VF\_INVALIDATE\_CONFIG\_BLOCK\_INFO**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_sriov_vf_invalidate_config_block_info) is passed along in the OID request. This structure contains the cached *BlockMask* parameter data.

        NDIS also issues another [**IOCTL\_VPCI\_INVALIDATE\_BLOCK**](/windows-hardware/drivers/ddi/vpci/ni-vpci-ioctl_vpci_invalidate_block) request to handle successive notifications of changes to VF configuration data.

    3.  When the VF driver handles the OID\_SRIOV\_VF\_INVALIDATE\_CONFIG\_BLOCK request, it reads data from the specified VF configuration blocks.

For more information about backchannel communication within the single root I/O virtualization (SR-IOV) interface, see [SR-IOV PF/VF Backchannel Communication](./sr-iov-pf-vf-backchannel-communication.md).

### Return Status Codes

The miniport driver returns one of the following status codes for the OID method request of OID\_SRIOV\_VF\_INVALIDATE\_CONFIG\_BLOCK.

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
<td><p>One or more of the members of the <a href="/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_sriov_vf_invalidate_config_block_info" data-raw-source="[&lt;strong&gt;NDIS_SRIOV_VF_INVALIDATE_CONFIG_BLOCK_INFO&lt;/strong&gt;](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_sriov_vf_invalidate_config_block_info)"><strong>NDIS_SRIOV_VF_INVALIDATE_CONFIG_BLOCK_INFO</strong></a> structure have invalid values.</p></td>
</tr>
<tr class="even">
<td><p>NDIS_STATUS_INVALID_LENGTH</p></td>
<td><p>The information buffer was too short. NDIS sets the <strong>DATA.SET_INFORMATION.BytesNeeded</strong> member in the <a href="/windows-hardware/drivers/ddi/ndis/ns-ndis-_ndis_oid_request" data-raw-source="[&lt;strong&gt;NDIS_OID_REQUEST&lt;/strong&gt;](/windows-hardware/drivers/ddi/oidrequest/ns-oidrequest-ndis_oid_request)"><strong>NDIS_OID_REQUEST</strong></a> structure to the size of the <a href="/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_sriov_vf_invalidate_config_block_info" data-raw-source="[&lt;strong&gt;NDIS_SRIOV_VF_INVALIDATE_CONFIG_BLOCK_INFO&lt;/strong&gt;](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_sriov_vf_invalidate_config_block_info)"><strong>NDIS_SRIOV_VF_INVALIDATE_CONFIG_BLOCK_INFO</strong></a> structure.</p></td>
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
[**IOCTL\_VPCI\_INVALIDATE\_BLOCK**](/windows-hardware/drivers/ddi/vpci/ni-vpci-ioctl_vpci_invalidate_block)

[**NDIS\_OID\_REQUEST**](/windows-hardware/drivers/ddi/oidrequest/ns-oidrequest-ndis_oid_request)

[**NDIS\_SRIOV\_VF\_INVALIDATE\_CONFIG\_BLOCK\_INFO**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_sriov_vf_invalidate_config_block_info)

[**NdisMInvalidateConfigBlock**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndisminvalidateconfigblock)

[OID\_SRIOV\_READ\_VF\_CONFIG\_SPACE](oid-sriov-read-vf-config-space.md)

[**VPCI\_INVALIDATE\_BLOCK\_OUTPUT**](/windows-hardware/drivers/ddi/vpci/ns-vpci-_vpci_invalidate_block_output)

