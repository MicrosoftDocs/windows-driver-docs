---
title: OID_SRIOV_PF_LUID
description: An overlying driver issues an object identifier (OID) query request of OID_SRIOV_PF_LUID to receive the locally unique identifier (LUID) associated with the PCI Express (PCIe) Physical Function (PF) of the network adapter.
ms.assetid: 363D308D-CE88-4F3B-81FF-37A2D86CB7BC
ms.date: 08/08/2017
keywords: 
 -OID_SRIOV_PF_LUID Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# OID\_SRIOV\_PF\_LUID


An overlying driver issues an object identifier (OID) query request of OID\_SRIOV\_PF\_LUID to receive the locally unique identifier (LUID) associated with the PCI Express (PCIe) Physical Function (PF) of the network adapter.

The **InformationBuffer** member of the [**NDIS\_OID\_REQUEST**](https://msdn.microsoft.com/library/windows/hardware/ff566710) structure contains a pointer to the [**NDIS\_SRIOV\_PF\_LUID\_INFO**](https://msdn.microsoft.com/library/windows/hardware/hh451678) structure.

Remarks
-------

NDIS generates a LUID for the PF before NDIS calls the [*MiniportInitializeEx*](https://msdn.microsoft.com/library/windows/hardware/ff559389) function of the miniport driver for the PF. This LUID is valid until NDIS calls the [*MiniportHaltEx*](https://msdn.microsoft.com/library/windows/hardware/ff559388) function of the driver.

**Note**  The value of the **Luid** member differs from the **NetLuid** member of the [**NDIS\_MINIPORT\_INIT\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/ff565972) structure. This structure is passed to the miniport driver through the *MiniportInitParameters* parameter of [*MiniportInitializeEx*](https://msdn.microsoft.com/library/windows/hardware/ff559389).

 

### Return Status Codes

NDIS handles the OID query request of OID\_SRIOV\_PF\_LUID request for miniport drivers. The drivers will not be issued this OID request.

When NDIS handles the OID\_SRIOV\_PF\_LUID request, it returns one of the following status codes.

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
<td><p>NDIS_STATUS_INVALID_LENGTH</p></td>
<td><p>The information buffer was too short. The miniport driver must set the <strong>DATA.QUERY_INFORMATION.BytesNeeded</strong> member in the <a href="https://msdn.microsoft.com/library/windows/hardware/ff566710" data-raw-source="[&lt;strong&gt;NDIS_OID_REQUEST&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff566710)"><strong>NDIS_OID_REQUEST</strong></a> structure to the minimum buffer size that is required.</p></td>
</tr>
<tr class="even">
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
[*MiniportInitializeEx*](https://msdn.microsoft.com/library/windows/hardware/ff559389)

[**NDIS\_OID\_REQUEST**](https://msdn.microsoft.com/library/windows/hardware/ff566710)

[**NDIS\_SRIOV\_PF\_LUID\_INFO**](https://msdn.microsoft.com/library/windows/hardware/hh451678)

 

 




