---
title: OID\_SRIOV\_HARDWARE\_CAPABILITIES
author: windows-driver-content
description: An overlying driver issues an object identifier (OID) query request of OID\_SRIOV\_HARDWARE\_CAPABILITIES to obtain the single root I/O virtualization (SR-IOV) hardware capabilities of the network adapter.
ms.assetid: EEF99105-BBDC-4093-8B11-D27F13B1A3D0
ms.author: windowsdriverdev
ms.date: 08/08/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords: 
 -OID_SRIOV_HARDWARE_CAPABILITIES Network Drivers Starting with Windows Vista
---

# OID\_SRIOV\_HARDWARE\_CAPABILITIES


An overlying driver issues an object identifier (OID) query request of OID\_SRIOV\_HARDWARE\_CAPABILITIES to obtain the single root I/O virtualization (SR-IOV) hardware capabilities of the network adapter.

The **InformationBuffer** member of the [**NDIS\_OID\_REQUEST**](https://msdn.microsoft.com/library/windows/hardware/ff566710) structure contains a pointer to the [**NDIS\_SRIOV\_CAPABILITIES**](https://msdn.microsoft.com/library/windows/hardware/hh451677) structure.

Remarks
-------

The [**NDIS\_SRIOV\_CAPABILITIES**](https://msdn.microsoft.com/library/windows/hardware/hh451677) structure contains information about the hardware capabilities of the network adapter, such as whether the adapter supports SR-IOV and whether the miniport driver is managing the adapter's PCI Express (PCIe) Physical Function (PF) or Virtual Function (VF). These capabilities can include the hardware capabilities that are currently disabled by the INF file settings or through the **Advanced** properties page.

**Note**  All the SR-IOV capabilities of the network adapter are returned through an OID query request of OID\_SRIOV\_HARDWARE\_CAPABILITIES, regardless of whether a capability is enabled or disabled.

 

Starting with NDIS 6.30, miniport drivers supply the SR-IOV hardware capabilities when its [*MiniportInitializeEx*](https://msdn.microsoft.com/library/windows/hardware/ff559389) function is called. The driver initializes an [**NDIS\_SRIOV\_CAPABILITIES**](https://msdn.microsoft.com/library/windows/hardware/hh451677) structure with the SR-IOV hardware capabilities and sets the **HardwareSriovCapabilities** member of the [**NDIS\_MINIPORT\_ADAPTER\_HARDWARE\_ASSIST\_ATTRIBUTES**](https://msdn.microsoft.com/library/windows/hardware/ff565924) structure to a pointer to the **NDIS\_SRIOV\_CAPABILITIES** structure. The miniport driver then calls the [**NdisMSetMiniportAttributes**](https://msdn.microsoft.com/library/windows/hardware/ff563672) function and sets the *MiniportAttributes* parameter to a pointer to an **NDIS\_MINIPORT\_ADAPTER\_HARDWARE\_ASSIST\_ATTRIBUTES** structure.

### Return Status Codes

NDIS handles the OID query request of the OID\_SRIOV\_HARDWARE\_CAPABILITIES request for miniport drivers. The drivers will not be issued this OID request.

When NDIS handles the OID\_SRIOV\_HARDWARE\_CAPABILITIES request, it returns one of the following status codes.

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
[**NDIS\_BIND\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/ff564832)

[**NDIS\_FILTER\_ATTACH\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/ff565481)

[**NDIS\_OID\_REQUEST**](https://msdn.microsoft.com/library/windows/hardware/ff566710)

[**NDIS\_MINIPORT\_ADAPTER\_HARDWARE\_ASSIST\_ATTRIBUTES**](https://msdn.microsoft.com/library/windows/hardware/ff565924)

[**NDIS\_SRIOV\_CAPABILITIES**](https://msdn.microsoft.com/library/windows/hardware/hh451677)

[**NdisMSetMiniportAttributes**](https://msdn.microsoft.com/library/windows/hardware/ff563672)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20OID_SRIOV_HARDWARE_CAPABILITIES%20%20RELEASE:%20%288/8/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


