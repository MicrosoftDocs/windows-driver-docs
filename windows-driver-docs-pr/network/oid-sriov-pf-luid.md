---
title: OID_SRIOV_PF_LUID
author: windows-driver-content
description: An overlying driver issues an object identifier (OID) query request of OID_SRIOV_PF_LUID to receive the locally unique identifier (LUID) associated with the PCI Express (PCIe) Physical Function (PF) of the network adapter.
ms.assetid: 363D308D-CE88-4F3B-81FF-37A2D86CB7BC
ms.author: windowsdriverdev
ms.date: 08/08/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords: 
 -OID_SRIOV_PF_LUID Network Drivers Starting with Windows Vista
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
<td><p>The information buffer was too short. The miniport driver must set the <strong>DATA.QUERY_INFORMATION.BytesNeeded</strong> member in the [<strong>NDIS_OID_REQUEST</strong>](https://msdn.microsoft.com/library/windows/hardware/ff566710) structure to the minimum buffer size that is required.</p></td>
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

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20OID_SRIOV_PF_LUID%20%20RELEASE:%20%288/8/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


