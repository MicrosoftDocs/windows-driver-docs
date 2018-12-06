---
title: OID_NIC_SWITCH_HARDWARE_CAPABILITIES
description: An overlying driver issues an object identifier (OID) query request of OID_NIC_SWITCH_HARDWARE_CAPABILITIES to obtain the hardware capabilities of the NIC switch in the network adapter.
ms.assetid: 2c417a16-68e1-4754-88a5-8bac4653e05d
ms.date: 08/08/2017
keywords: 
 -OID_NIC_SWITCH_HARDWARE_CAPABILITIES Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# OID\_NIC\_SWITCH\_HARDWARE\_CAPABILITIES


An overlying driver issues an object identifier (OID) query request of OID\_NIC\_SWITCH\_HARDWARE\_CAPABILITIES to obtain the hardware capabilities of the NIC switch in the network adapter.

After a successful return from the OID query request, the **InformationBuffer** member of the [**NDIS\_OID\_REQUEST**](https://msdn.microsoft.com/library/windows/hardware/ff566710) structure contains a pointer to an [**NDIS\_NIC\_SWITCH\_CAPABILITIES**](https://msdn.microsoft.com/library/windows/hardware/ff566583) structure.

Remarks
-------

The [**NDIS\_NIC\_SWITCH\_CAPABILITIES**](https://msdn.microsoft.com/library/windows/hardware/ff566583) structure contains information about the hardware capabilities of a NIC switch on the network adapter. These capabilities can include the hardware capabilities that are currently disabled by the INF file settings or through the **Advanced** properties page.

**Note**  All the capabilities of the specified NIC switch are returned through an OID query request of OID\_NIC\_SWITCH\_HARDWARE\_CAPABILITIES, regardless of whether a capability is enabled or disabled.

 

Starting with NDIS 6.20, miniport drivers supply the NIC switch hardware capabilities when its [*MiniportInitializeEx*](https://msdn.microsoft.com/library/windows/hardware/ff559389) function is called. The driver initializes an [**NDIS\_NIC\_SWITCH\_CAPABILITIES**](https://msdn.microsoft.com/library/windows/hardware/ff566583) structure with the NIC switch hardware capabilities and sets the **HardwareNicSwitchCapabilities** member of the [**NDIS\_MINIPORT\_ADAPTER\_HARDWARE\_ASSIST\_ATTRIBUTES**](https://msdn.microsoft.com/library/windows/hardware/ff565924) structure to a pointer to the **NDIS\_NIC\_SWITCH\_CAPABILITIES** structure. The miniport driver then calls the [**NdisMSetMiniportAttributes**](https://msdn.microsoft.com/library/windows/hardware/ff563672) function and sets the *MiniportAttributes* parameter to a pointer to an **NDIS\_MINIPORT\_ADAPTER\_HARDWARE\_ASSIST\_ATTRIBUTES** structure.

**Note**  Starting with NDIS 6.30, miniport drivers that support the single root I/O virtualization (SR-IOV) interface must register the hardware capabilities of the NIC switch. Drivers register these capabilities by calling [**NdisMSetMiniportAttributes**](https://msdn.microsoft.com/library/windows/hardware/ff563672).

 

### Return Status Codes

NDIS handles the OID query request of OID\_NIC\_SWITCH\_HARDWARE\_CAPABILITIES request for miniport drivers, and returns one of the following status codes:

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
<td><p>The request completed successfully. The <strong>InformationBuffer</strong> points to an <a href="https://msdn.microsoft.com/library/windows/hardware/ff566583" data-raw-source="[&lt;strong&gt;NDIS_NIC_SWITCH_CAPABILITIES&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff566583)"><strong>NDIS_NIC_SWITCH_CAPABILITIES</strong></a> structure.</p></td>
</tr>
<tr class="even">
<td><p>NDIS_STATUS_NOT_SUPPORTED</p></td>
<td><p>The miniport driver either does not support the single root I/O virtualization (SR-IOV) interface or is not enabled to use the interface.</p></td>
</tr>
<tr class="odd">
<td><p>NDIS_STATUS_INVALID_LENGTH</p></td>
<td><p>The length of the information buffer is less than sizeof(<a href="https://msdn.microsoft.com/library/windows/hardware/ff566583" data-raw-source="[&lt;strong&gt;NDIS_NIC_SWITCH_CAPABILITIES&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff566583)"><strong>NDIS_NIC_SWITCH_CAPABILITIES</strong></a>). NDIS sets the <strong>DATA.QUERY_INFORMATION.BytesNeeded</strong> member in the <a href="https://msdn.microsoft.com/library/windows/hardware/ff566710" data-raw-source="[&lt;strong&gt;NDIS_OID_REQUEST&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff566710)"><strong>NDIS_OID_REQUEST</strong></a> structure to the minimum buffer size that is required.</p></td>
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
<td><p>Supported in NDIS 6.20 and later.</p></td>
</tr>
<tr class="even">
<td><p>Header</p></td>
<td>Ntddndis.h (include Ndis.h)</td>
</tr>
</tbody>
</table>

## See also


[**NDIS\_BIND\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/ff564832)

[**NDIS\_MINIPORT\_ADAPTER\_HARDWARE\_ASSIST\_ATTRIBUTES**](https://msdn.microsoft.com/library/windows/hardware/ff565924)

[**NDIS\_NIC\_SWITCH\_CAPABILITIES**](https://msdn.microsoft.com/library/windows/hardware/ff566583)

[**NDIS\_OID\_REQUEST**](https://msdn.microsoft.com/library/windows/hardware/ff566710)

 

 




