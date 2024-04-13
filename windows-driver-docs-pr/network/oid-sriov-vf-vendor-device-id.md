---
title: OID_SRIOV_VF_VENDOR_DEVICE_ID
ms.topic: reference
description: An overlying driver issues an object identifier (OID) method request of OID_SRIOV_VF_VENDOR_DEVICE_ID to query the PCI Express (PCIe) device identifier (DeviceID) and vendor identifier (VendorID) for a PCI Express (PCIe) Virtual Function (VF) network adapter. This virtual network adapter is exposed in the Hyper-V child partition that is attached to the VF.Overlying drivers issue this OID method request to the miniport driver of the PCI Express (PCIe) Physical Function (PF) of the network adapter. This OID method request is required for PF miniport drivers that support the single root I/O virtualization (SR-IOV) interface.
ms.date: 08/08/2017
keywords: 
 -OID_SRIOV_VF_VENDOR_DEVICE_ID Network Drivers Starting with Windows Vista
---

# OID\_SRIOV\_VF\_VENDOR\_DEVICE\_ID


An overlying driver issues an object identifier (OID) method request of OID\_SRIOV\_VF\_VENDOR\_DEVICE\_ID to query the PCI Express (PCIe) device identifier (DeviceID) and vendor identifier (VendorID) for a PCI Express (PCIe) Virtual Function (VF) network adapter. This virtual network adapter is exposed in the Hyper-V child partition that is attached to the VF.

Overlying drivers issue this OID method request to the miniport driver of the PCI Express (PCIe) Physical Function (PF) of the network adapter. This OID method request is required for PF miniport drivers that support the single root I/O virtualization (SR-IOV) interface.

The **InformationBuffer** member of the [**NDIS\_OID\_REQUEST**](/windows-hardware/drivers/ddi/oidrequest/ns-oidrequest-ndis_oid_request) structure contains a pointer to an [**NDIS\_SRIOV\_VF\_VENDOR\_DEVICE\_ID\_INFO**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_sriov_vf_vendor_device_id_info) structure.

## Remarks

Before it issues this OID method request, the overlying driver must initialize an [**NDIS\_SRIOV\_VF\_VENDOR\_DEVICE\_ID\_INFO**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_sriov_vf_vendor_device_id_info) structure and must set the **VFId** member to the identifier of the VF from which the information is to be read.

When it handles this OID request, the PF miniport driver must verify that the specified VF has resources that have been previously allocated. The PF miniport driver allocates resources for a VF during an OID method request of [OID\_NIC\_SWITCH\_ALLOCATE\_VF](oid-nic-switch-allocate-vf.md). If resources for the specified VF have not been allocated, the driver must fail the OID request.

For more information, see [Querying the PCI Vendor and Device Identifiers for a Virtual Function](./querying-the-pci-vendor-and-device-identifiers-for-a-virtual-function.md).

### Return Status Codes

The PF miniport driver returns one of the following status codes for the OID method request of OID\_SRIOV\_VF\_VENDOR\_DEVICE\_ID.

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
<td><p>One or more of the members of the <a href="/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_sriov_vf_vendor_device_id_info" data-raw-source="[&lt;strong&gt;NDIS_SRIOV_VF_VENDOR_DEVICE_ID_INFO&lt;/strong&gt;](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_sriov_vf_vendor_device_id_info)"><strong>NDIS_SRIOV_VF_VENDOR_DEVICE_ID_INFO</strong></a> structure have invalid values.</p></td>
</tr>
<tr class="even">
<td><p>NDIS_STATUS_INVALID_LENGTH</p></td>
<td><p>The information buffer was too short. NDIS sets the <strong>DATA.METHOD_INFORMATION.BytesNeeded</strong> member in the <a href="/windows-hardware/drivers/ddi/ndis/ns-ndis-_ndis_oid_request" data-raw-source="[&lt;strong&gt;NDIS_OID_REQUEST&lt;/strong&gt;](/windows-hardware/drivers/ddi/oidrequest/ns-oidrequest-ndis_oid_request)"><strong>NDIS_OID_REQUEST</strong></a> structure to the minimum buffer size that is required.</p></td>
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
[**NDIS\_OID\_REQUEST**](/windows-hardware/drivers/ddi/oidrequest/ns-oidrequest-ndis_oid_request)

[**NDIS\_SRIOV\_VF\_VENDOR\_DEVICE\_ID\_INFO**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_sriov_vf_vendor_device_id_info)

[OID\_NIC\_SWITCH\_ALLOCATE\_VF](oid-nic-switch-allocate-vf.md)

