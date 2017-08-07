---
title: OID\_SRIOV\_VF\_INVALIDATE\_CONFIG\_BLOCK
author: windows-driver-content
description: NDIS issues an object identifier (OID) method request of OID\_SRIOV\_VF\_INVALIDATE\_CONFIG\_BLOCK to notify the miniport driver of a PCI Express (PCIe) Virtual Function (VF) that data within one or more configuration blocks has changed.
ms.assetid: CF73E0DA-20DA-49A0-80B0-0F5A56DCEF5D
ms.author: windowsdriverdev
ms.date: 08/08/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords:
 - OID_SRIOV_VF_INVALIDATE_CONFIG_BLOCK Network Drivers Starting with Windows Vista
---

# OID\_SRIOV\_VF\_INVALIDATE\_CONFIG\_BLOCK


NDIS issues an object identifier (OID) method request of OID\_SRIOV\_VF\_INVALIDATE\_CONFIG\_BLOCK to notify the miniport driver of a PCI Express (PCIe) Virtual Function (VF) that data within one or more configuration blocks has changed. NDIS issues this OID when the miniport driver for a PCIe Physical Function (PF) calls [**NdisMInvalidateConfigBlock**](ndisminvalidateconfigblock.md).

The **InformationBuffer** member of the [**NDIS\_OID\_REQUEST**](ndis-oid-request.md) structure contains a pointer to an [**NDIS\_SRIOV\_VF\_INVALIDATE\_CONFIG\_BLOCK\_INFO**](ndis-sriov-vf-invalidate-config-block-info.md) structure. This structure specifies one or more Virtual Function (VF) configuration blocks whose data has been changed (*invalidated*) by the PF miniport driver.

Remarks
-------

A VF configuration block is used for backchannel communication between the PF and VF miniport drivers. The IHV can define one or more VF configuration blocks for the device. Each VF configuration block has an IHV-defined format, length, and block ID.

**Note**  Data from each VF configuration block is used only by the PF and VF miniport drivers.

 

VF configuration data is exchanged between the following drivers:

-   The VF driver, which runs in the guest operating system. This operating system runs within a Hyper-V child partition.

-   The PF driver, which runs in the management operating system. This operating system runs within the Hyper-V parent partition.

In order to handle notifications of invalid VF configuration data, NDIS and the miniport drivers perform the following steps:

1.  In the guest operating system, NDIS issues an I/O control request of [**IOCTL\_VPCI\_INVALIDATE\_BLOCK**](https://msdn.microsoft.com/library/windows/hardware/hh439301) request. When this IOCTL is completed, NDIS is notified that VF configuration data has changed.

2.  In the management operating system, the following steps occur:

    1.  The PF miniport driver calls the [**NdisMInvalidateConfigBlock**](ndisminvalidateconfigblock.md) function to notify NDIS that VF configuration data has changed and is no longer valid. The driver sets the *BlockMask* parameter to a ULONGLONG bitmask that specifies which VF configuration blocks have changed. Each bit in the bitmask corresponds to a VF configuration block. If the bit is set to one, the data in the corresponding VF configuration block has changed.
    2.  NDIS signals the virtualization stack, which runs in the management operating system, about the change to VF configuration block data. The virtualization stack caches the *BlockMask* parameter data.

        **Note**  Each time that the PF miniport driver calls [**NdisMInvalidateConfigBlock**](ndisminvalidateconfigblock.md), the virtualization stack ORs the *BlockMask* parameter data with the current value in its cache.

         

    3.  The virtualization stack notifies the virtual PCI (VPCI) driver, which runs in the guest operating system, about the invalidation of VF configuration data. The virtualization stack sends the cached *BlockMask* parameter data to the VPCI driver.

3.  In the Guest operating system, the following steps occur:

    1.  The VPCI driver saves the cached *BlockMask* parameter data in the **BlockMask** member of the [**VPCI\_INVALIDATE\_BLOCK\_OUTPUT**](https://msdn.microsoft.com/library/windows/hardware/hh451586) structure that is associated with the [**IOCTL\_VPCI\_INVALIDATE\_BLOCK**](https://msdn.microsoft.com/library/windows/hardware/hh439301) request.

    2.  The VPCI driver successfully completes the [**IOCTL\_VPCI\_INVALIDATE\_BLOCK**](https://msdn.microsoft.com/library/windows/hardware/hh439301) request. When this happens, NDIS issues an OID method request of OID\_SRIOV\_VF\_INVALIDATE\_CONFIG\_BLOCK to the VF miniport driver. An [**NDIS\_SRIOV\_VF\_INVALIDATE\_CONFIG\_BLOCK\_INFO**](ndis-sriov-vf-invalidate-config-block-info.md) is passed along in the OID request. This structure contains the cached *BlockMask* parameter data.

        NDIS also issues another [**IOCTL\_VPCI\_INVALIDATE\_BLOCK**](https://msdn.microsoft.com/library/windows/hardware/hh439301) request to handle successive notifications of changes to VF configuration data.

    3.  When the VF driver handles the OID\_SRIOV\_VF\_INVALIDATE\_CONFIG\_BLOCK request, it reads data from the specified VF configuration blocks.

For more information about backchannel communication within the single root I/O virtualization (SR-IOV) interface, see [SR-IOV PF/VF Backchannel Communication](https://msdn.microsoft.com/library/windows/hardware/hh440251).

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
<td><p>One or more of the members of the [<strong>NDIS_SRIOV_VF_INVALIDATE_CONFIG_BLOCK_INFO</strong>](ndis-sriov-vf-invalidate-config-block-info.md) structure have invalid values.</p></td>
</tr>
<tr class="even">
<td><p>NDIS_STATUS_INVALID_LENGTH</p></td>
<td><p>The information buffer was too short. NDIS sets the <strong>DATA.SET_INFORMATION.BytesNeeded</strong> member in the [<strong>NDIS_OID_REQUEST</strong>](ndis-oid-request.md) structure to the size of the [<strong>NDIS_SRIOV_VF_INVALIDATE_CONFIG_BLOCK_INFO</strong>](ndis-sriov-vf-invalidate-config-block-info.md) structure.</p></td>
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
[**IOCTL\_VPCI\_INVALIDATE\_BLOCK**](https://msdn.microsoft.com/library/windows/hardware/hh439301)

[**NDIS\_OID\_REQUEST**](ndis-oid-request.md)

[**NDIS\_SRIOV\_VF\_INVALIDATE\_CONFIG\_BLOCK\_INFO**](ndis-sriov-vf-invalidate-config-block-info.md)

[**NdisMInvalidateConfigBlock**](ndisminvalidateconfigblock.md)

[OID\_SRIOV\_READ\_VF\_CONFIG\_SPACE](oid-sriov-read-vf-config-space.md)

[**VPCI\_INVALIDATE\_BLOCK\_OUTPUT**](https://msdn.microsoft.com/library/windows/hardware/hh451586)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20OID_SRIOV_VF_INVALIDATE_CONFIG_BLOCK%20%20RELEASE:%20%288/3/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


