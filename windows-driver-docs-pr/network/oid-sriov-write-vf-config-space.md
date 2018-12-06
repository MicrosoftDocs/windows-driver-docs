---
title: OID_SRIOV_WRITE_VF_CONFIG_SPACE
description: An overlying driver issues an object identifier (OID) set request of OID_SRIOV_WRITE_VF_CONFIG_SPACE to write data to the PCI Express (PCIe) configuration space for a specified PCIe Virtual Function (VF) on the network adapter.
ms.assetid: 0D9866A6-A8C6-4B0A-8D17-A632E1AE37BF
ms.date: 08/08/2017
keywords: 
 -OID_SRIOV_WRITE_VF_CONFIG_SPACE Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# OID\_SRIOV\_WRITE\_VF\_CONFIG\_SPACE


An overlying driver issues an object identifier (OID) set request of OID\_SRIOV\_WRITE\_VF\_CONFIG\_SPACE to write data to the PCI Express (PCIe) configuration space for a specified PCIe Virtual Function (VF) on the network adapter.

Overlying drivers issue this OID set request to the miniport driver for the network adapter's PCIe Physical Function (PF). This OID method request is required for PF miniport drivers that support the single root I/O virtualization (SR-IOV) interface.

The **InformationBuffer** member of the [**NDIS\_OID\_REQUEST**](https://msdn.microsoft.com/library/windows/hardware/ff566710) structure contains a pointer to a caller-allocated buffer. This buffer is formatted to contain the following:

-   An [**NDIS\_SRIOV\_WRITE\_VF\_CONFIG\_SPACE\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/hh451688) structure that contains the parameters for a write operation of the PCI configuration space of a VF.

-   Additional buffer space that contains the data to be written to the PCI configuration space.

Remarks
-------

The VF miniport driver runs in the guest operating system of a Hyper-V child partition. Because of this, the VF miniport driver cannot directly access hardware resources, such as the VF's PCI configuration space. Only the PF miniport driver, which runs in the management operating system of a Hyper-V parent partition, can access the PCI configuration space for a VF.

The overlying driver, such as the virtualization stack, issues the OID set request of OID\_SRIOV\_WRITE\_VF\_CONFIG\_SPACE when the VF miniport driver calls [**NdisMSetBusData**](https://msdn.microsoft.com/library/windows/hardware/ff563670) to write to its PCI configuration space.

When it handles the OID method request of OID\_SRIOV\_WRITE\_VF\_CONFIG\_SPACE, the PF miniport driver must follow these guidelines:

-   The PF miniport driver must verify that the VF, specified by the **VFId** member of the [**NDIS\_SRIOV\_WRITE\_VF\_CONFIG\_SPACE\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/hh451688) structure, has resources that have been previously allocated. The PF miniport driver allocates resources for a VF through an OID method request of [OID\_NIC\_SWITCH\_ALLOCATE\_VF](oid-nic-switch-allocate-vf.md).

    If resources for the specified VF have not been allocated, the driver must fail the OID request.

-   The PF miniport driver calls [**NdisMSetVirtualFunctionBusData**](https://msdn.microsoft.com/library/windows/hardware/hh451526) to write to the requested PCI configuration space. However, the PF miniport driver can also return PCI configuration space data for the VF that the driver has cached from previous read or write operations of the PCI configuration space.

    **Note**  If an independent hardware vendor (IHV) provides a virtual bus driver (VBD) as part of its SR-IOV [driver package](https://msdn.microsoft.com/library/windows/hardware/ff544840), its PF miniport driver must not call [**NdisMSetVirtualFunctionBusData**](https://msdn.microsoft.com/library/windows/hardware/hh451526). Instead, the driver must interface with the VBD through a private communication channel, and request that the VBD call [*SetVirtualFunctionData*](https://msdn.microsoft.com/library/windows/hardware/hh451552). This function is exposed from the [GUID\_VPCI\_INTERFACE\_STANDARD](https://msdn.microsoft.com/library/windows/hardware/hh451146) interface that is supported by the underlying virtual PCI (VPCI) bus driver.

     

If the PF miniport driver can successfully complete the OID request, the driver must copy the requested PCI configuration space data to the buffer referenced by the **InformationBuffer** member of the [**NDIS\_OID\_REQUEST**](https://msdn.microsoft.com/library/windows/hardware/ff566710) structure. The driver copies the data to the buffer at the offset specified by **BufferOffset** member of the [**NDIS\_SRIOV\_READ\_VF\_CONFIG\_SPACE\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/hh451681) structure.

For more information, see [Setting the PCI Configuration Data of a Virtual Function](https://msdn.microsoft.com/library/windows/hardware/hh440229).

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
<td><p>One or more of the members of the <a href="https://msdn.microsoft.com/library/windows/hardware/hh451688" data-raw-source="[&lt;strong&gt;NDIS_SRIOV_WRITE_VF_CONFIG_SPACE_PARAMETERS&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/hh451688)"><strong>NDIS_SRIOV_WRITE_VF_CONFIG_SPACE_PARAMETERS</strong></a> structure have invalid values.</p></td>
</tr>
<tr class="even">
<td><p>NDIS_STATUS_INVALID_LENGTH</p></td>
<td><p>The information buffer was too short. NDIS sets the <strong>DATA.SET_INFORMATION.BytesNeeded</strong> member in the <a href="https://msdn.microsoft.com/library/windows/hardware/ff566710" data-raw-source="[&lt;strong&gt;NDIS_OID_REQUEST&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff566710)"><strong>NDIS_OID_REQUEST</strong></a> structure to the minimum buffer size that is required.</p></td>
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
[GUID\_VPCI\_INTERFACE\_STANDARD](https://msdn.microsoft.com/library/windows/hardware/hh451146)

[**NDIS\_OID\_REQUEST**](https://msdn.microsoft.com/library/windows/hardware/ff566710)

[**NDIS\_SRIOV\_WRITE\_VF\_CONFIG\_SPACE\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/hh451688)

[**NdisMSetBusData**](https://msdn.microsoft.com/library/windows/hardware/ff563670)

[**NdisMSetVirtualFunctionBusData**](https://msdn.microsoft.com/library/windows/hardware/hh451526)

[OID\_NIC\_SWITCH\_ALLOCATE\_VF](oid-nic-switch-allocate-vf.md)

[OID\_SRIOV\_READ\_VF\_CONFIG\_SPACE](oid-sriov-read-vf-config-space.md)

[*SetVirtualFunctionData*](https://msdn.microsoft.com/library/windows/hardware/hh451552)

 

 




