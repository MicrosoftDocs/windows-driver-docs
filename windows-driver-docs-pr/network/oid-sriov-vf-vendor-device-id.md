---
title: OID\_SRIOV\_VF\_VENDOR\_DEVICE\_ID
author: windows-driver-content
description: An overlying driver issues an object identifier (OID) method request of OID\_SRIOV\_VF\_VENDOR\_DEVICE\_ID to query the PCI Express (PCIe) device identifier (DeviceID) and vendor identifier (VendorID) for a PCI Express (PCIe) Virtual Function (VF) network adapter. This virtual network adapter is exposed in the Hyper-V child partition that is attached to the VF.Overlying drivers issue this OID method request to the miniport driver of the PCI Express (PCIe) Physical Function (PF) of the network adapter. This OID method request is required for PF miniport drivers that support the single root I/O virtualization (SR-IOV) interface.
ms.assetid: 19D98264-325B-4EA4-83BF-BBFECD185E55
ms.author: windowsdriverdev
ms.date: 08/08/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords: 
 -OID_SRIOV_VF_VENDOR_DEVICE_ID Network Drivers Starting with Windows Vista
---

# OID\_SRIOV\_VF\_VENDOR\_DEVICE\_ID


An overlying driver issues an object identifier (OID) method request of OID\_SRIOV\_VF\_VENDOR\_DEVICE\_ID to query the PCI Express (PCIe) device identifier (DeviceID) and vendor identifier (VendorID) for a PCI Express (PCIe) Virtual Function (VF) network adapter. This virtual network adapter is exposed in the Hyper-V child partition that is attached to the VF.

Overlying drivers issue this OID method request to the miniport driver of the PCI Express (PCIe) Physical Function (PF) of the network adapter. This OID method request is required for PF miniport drivers that support the single root I/O virtualization (SR-IOV) interface.

The **InformationBuffer** member of the [**NDIS\_OID\_REQUEST**](https://msdn.microsoft.com/library/windows/hardware/ff566710) structure contains a pointer to an [**NDIS\_SRIOV\_VF\_VENDOR\_DEVICE\_ID\_INFO**](https://msdn.microsoft.com/library/windows/hardware/hh451686) structure.

Remarks
-------

Before it issues this OID method request, the overlying driver must initialize an [**NDIS\_SRIOV\_VF\_VENDOR\_DEVICE\_ID\_INFO**](https://msdn.microsoft.com/library/windows/hardware/hh451686) structure and must set the **VFId** member to the identifier of the VF from which the information is to be read.

When it handles this OID request, the PF miniport driver must verify that the specified VF has resources that have been previously allocated. The PF miniport driver allocates resources for a VF during an OID method request of [OID\_NIC\_SWITCH\_ALLOCATE\_VF](oid-nic-switch-allocate-vf.md). If resources for the specified VF have not been allocated, the driver must fail the OID request.

For more information, see [Querying the PCI Vendor and Device Identifiers for a Virtual Function](https://msdn.microsoft.com/library/windows/hardware/hh440185).

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
<td><p>One or more of the members of the [<strong>NDIS_SRIOV_VF_VENDOR_DEVICE_ID_INFO</strong>](https://msdn.microsoft.com/library/windows/hardware/hh451686) structure have invalid values.</p></td>
</tr>
<tr class="even">
<td><p>NDIS_STATUS_INVALID_LENGTH</p></td>
<td><p>The information buffer was too short. NDIS sets the <strong>DATA.METHOD_INFORMATION.BytesNeeded</strong> member in the [<strong>NDIS_OID_REQUEST</strong>](https://msdn.microsoft.com/library/windows/hardware/ff566710) structure to the minimum buffer size that is required.</p></td>
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

[**NDIS\_SRIOV\_VF\_VENDOR\_DEVICE\_ID\_INFO**](https://msdn.microsoft.com/library/windows/hardware/hh451686)

[OID\_NIC\_SWITCH\_ALLOCATE\_VF](oid-nic-switch-allocate-vf.md)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20OID_SRIOV_VF_VENDOR_DEVICE_ID%20%20RELEASE:%20%288/8/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


