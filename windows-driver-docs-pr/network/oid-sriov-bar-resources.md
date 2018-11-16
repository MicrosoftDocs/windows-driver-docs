---
title: OID_SRIOV_BAR_RESOURCES
description: NDIS issues an object identifier (OID) method request of OID_SRIOV_BAR_RESOURCES to determine the memory resources that were allocated to a PCI Express (PCIe) Base Address Register (BAR) of a PCIe Virtual Function (VF).
ms.assetid: CA29591B-EBFB-4B12-A980-F3FAD65207E2
ms.date: 08/08/2017
keywords: 
 -OID_SRIOV_BAR_RESOURCES Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
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
<td><p>One or more of the members of the <a href="https://msdn.microsoft.com/library/windows/hardware/hh451675" data-raw-source="[&lt;strong&gt;NDIS_SRIOV_BAR_RESOURCES_INFO&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/hh451675)"><strong>NDIS_SRIOV_BAR_RESOURCES_INFO</strong></a> structure have invalid values.</p></td>
</tr>
<tr class="even">
<td><p>NDIS_STATUS_INVALID_LENGTH</p></td>
<td><p>The information buffer is less than (sizeof(<a href="https://msdn.microsoft.com/library/windows/hardware/hh451675" data-raw-source="[&lt;strong&gt;NDIS_SRIOV_BAR_RESOURCES_INFO&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/hh451675)"><strong>NDIS_SRIOV_BAR_RESOURCES_INFO</strong></a>) + sizeof(<a href="https://msdn.microsoft.com/library/windows/hardware/ff541977" data-raw-source="[&lt;strong&gt;CM_PARTIAL_RESOURCE_DESCRIPTOR&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff541977)"><strong>CM_PARTIAL_RESOURCE_DESCRIPTOR</strong></a>). The PF miniport driver must set the <strong>DATA.METHOD_INFORMATION.BytesNeeded</strong> member in the <a href="https://msdn.microsoft.com/library/windows/hardware/ff566710" data-raw-source="[&lt;strong&gt;NDIS_OID_REQUEST&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff566710)"><strong>NDIS_OID_REQUEST</strong></a> structure to the minimum buffer size that is required.</p></td>
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

 

 




