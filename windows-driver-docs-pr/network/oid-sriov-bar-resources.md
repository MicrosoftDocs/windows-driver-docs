---
title: OID\_SRIOV\_BAR\_RESOURCES
author: windows-driver-content
description: NDIS issues an object identifier (OID) method request of OID\_SRIOV\_BAR\_RESOURCES to determine the memory resources that were allocated to a PCI Express (PCIe) Base Address Register (BAR) of a PCIe Virtual Function (VF).
ms.assetid: CA29591B-EBFB-4B12-A980-F3FAD65207E2
ms.author: windowsdriverdev
ms.date: 08/08/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords: 
 -OID_SRIOV_BAR_RESOURCES Network Drivers Starting with Windows Vista
---

# OID\_SRIOV\_BAR\_RESOURCES


NDIS issues an object identifier (OID) method request of OID\_SRIOV\_BAR\_RESOURCES to determine the memory resources that were allocated to a PCI Express (PCIe) Base Address Register (BAR) of a PCIe Virtual Function (VF).

NDIS issues this OID method request to the miniport driver for the network adapter's PCIe Physical Function (PF). This OID method request is required for PF miniport drivers that support the single root I/O virtualization (SR-IOV) interface.

The **InformationBuffer** member of the [**NDIS\_OID\_REQUEST**](https://msdn.microsoft.com/library/windows/hardware/ff566710) structure contains a pointer to a buffer. This buffer contains the following structures:

-   An [**NDIS\_SRIOV\_BAR\_RESOURCES\_INFO**](https://msdn.microsoft.com/library/windows/hardware/hh451675) structure that specifies the VF and BAR for which the PF miniport driver returns resource information.

-   A [**CM\_PARTIAL\_RESOURCE\_DESCRIPTOR**](https://msdn.microsoft.com/library/windows/hardware/ff541977) structure which follows the [**NDIS\_SRIOV\_BAR\_RESOURCES\_INFO**](https://msdn.microsoft.com/library/windows/hardware/hh451675) structure. The **CM\_PARTIAL\_RESOURCE\_DESCRIPTOR** structure contains information about the memory resources that were allocated to the specified BAR.

Remarks
-------

NDIS issues an OID method request of OID\_SRIOV\_BAR\_RESOURCES to obtain the system physical address and length of the memory resources that were allocated to a VF BAR. Before it issues the OID method request, NDIS formats the [**NDIS\_SRIOV\_BAR\_RESOURCES\_INFO**](https://msdn.microsoft.com/library/windows/hardware/hh451675) structure in the following way:

-   NDIS sets the **VFId** member of the [**NDIS\_SRIOV\_BAR\_RESOURCES\_INFO**](https://msdn.microsoft.com/library/windows/hardware/hh451675) structure to the identifier associated with the VF.

-   NDIS sets the **BarIndex** member of the [**NDIS\_SRIOV\_BAR\_RESOURCES\_INFO**](https://msdn.microsoft.com/library/windows/hardware/hh451675) structure to the BAR index for the specified VF. The BAR index is the offset of the register within the table of BARs in the PCI configuration space.

-   NDIS sets the **BarResourcesOffset** member of the [**NDIS\_SRIOV\_BAR\_RESOURCES\_INFO**](https://msdn.microsoft.com/library/windows/hardware/hh451675) structure to the offset, in units of bytes, from the beginning of the **NDIS\_SRIOV\_BAR\_RESOURCES\_INFO** structure to a [**CM\_PARTIAL\_RESOURCE\_DESCRIPTOR**](https://msdn.microsoft.com/library/windows/hardware/ff541977) structure.

**Note**  Overlying drivers, such as protocol or filter drivers, cannot issue OID method requests of OID\_SRIOV\_BAR\_RESOURCES to the PF miniport driver.

 

When the PF miniport driver receives the OID method request, the driver returns the resources for the specified BAR by formatting the [**CM\_PARTIAL\_RESOURCE\_DESCRIPTOR**](https://msdn.microsoft.com/library/windows/hardware/ff541977) structure within the **InformationBuffer** member of the [**NDIS\_OID\_REQUEST**](https://msdn.microsoft.com/library/windows/hardware/ff566710) structure. The driver formats the **CM\_PARTIAL\_RESOURCE\_DESCRIPTOR** structure with the system hardware resources associated with the BAR for the specified VF.

**Note**  The driver must format the structure for a resource type of **CmResourceTypeMemory**.

 

### Return Status Codes

The PF miniport driver returns one of the following status codes for the method request of OID\_SRIOV\_BAR\_RESOURCES.

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
<td><p>One or more of the members of the [<strong>NDIS_SRIOV_BAR_RESOURCES_INFO</strong>](https://msdn.microsoft.com/library/windows/hardware/hh451675) structure have invalid values.</p></td>
</tr>
<tr class="even">
<td><p>NDIS_STATUS_INVALID_LENGTH</p></td>
<td><p>The information buffer is less than (sizeof([<strong>NDIS_SRIOV_BAR_RESOURCES_INFO</strong>](https://msdn.microsoft.com/library/windows/hardware/hh451675)) + sizeof([<strong>CM_PARTIAL_RESOURCE_DESCRIPTOR</strong>](https://msdn.microsoft.com/library/windows/hardware/ff541977)). The PF miniport driver must set the <strong>DATA.METHOD_INFORMATION.BytesNeeded</strong> member in the [<strong>NDIS_OID_REQUEST</strong>](https://msdn.microsoft.com/library/windows/hardware/ff566710) structure to the minimum buffer size that is required.</p></td>
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
[**CM\_PARTIAL\_RESOURCE\_DESCRIPTOR**](https://msdn.microsoft.com/library/windows/hardware/ff541977)

[**NDIS\_OID\_REQUEST**](https://msdn.microsoft.com/library/windows/hardware/ff566710)

[**NDIS\_SRIOV\_BAR\_RESOURCES\_INFO**](https://msdn.microsoft.com/library/windows/hardware/hh451675)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20OID_SRIOV_BAR_RESOURCES%20%20RELEASE:%20%288/8/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


