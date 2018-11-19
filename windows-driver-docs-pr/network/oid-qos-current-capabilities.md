---
title: OID_QOS_CURRENT_CAPABILITIES
description: An overlying driver issues an object identifier (OID) query request of OID_QOS_CURRENT_CAPABILITIES to obtain the currently enabled NDIS Quality of Service (QoS) hardware capabilities of a network adapter.
ms.assetid: E9013EB2-5EDB-4BCB-BC1D-17345B85D1C4
ms.date: 08/08/2017
keywords: 
 -OID_QOS_CURRENT_CAPABILITIES Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# OID\_QOS\_CURRENT\_CAPABILITIES


An overlying driver issues an object identifier (OID) query request of OID\_QOS\_CURRENT\_CAPABILITIES to obtain the currently enabled NDIS Quality of Service (QoS) hardware capabilities of a network adapter.

After a successful return from the OID query request, the **InformationBuffer** member of the [**NDIS\_OID\_REQUEST**](https://msdn.microsoft.com/library/windows/hardware/ff566710) structure contains a pointer to an [**NDIS\_QOS\_CAPABILITIES**](https://msdn.microsoft.com/library/windows/hardware/hh451629) structure.

**Note**  This OID query request is handled by NDIS for miniport drivers that support the IEEE 802.1 Data Center Bridging (DCB) interface.

 

Remarks
-------

Miniport drivers register the currently-enabled NDIS QoS hardware capabilities of a network adapter when its [*MiniportInitializeEx*](https://msdn.microsoft.com/library/windows/hardware/ff559389) function is called. The driver registers these capabilities by following these steps:

1.  The driver initializes an [**NDIS\_QOS\_CAPABILITIES**](https://msdn.microsoft.com/library/windows/hardware/hh451629) structure with the enabled QoS hardware capabilities.

2.  The driver sets the **CurrentQosCapabilities** member of the [**NDIS\_MINIPORT\_ADAPTER\_HARDWARE\_ASSIST\_ATTRIBUTES**](https://msdn.microsoft.com/library/windows/hardware/ff565924) structure to a pointer to the [**NDIS\_QOS\_CAPABILITIES**](https://msdn.microsoft.com/library/windows/hardware/hh451629) structure.

3.  The miniport driver then calls the [**NdisMSetMiniportAttributes**](https://msdn.microsoft.com/library/windows/hardware/ff563672) function and sets the *MiniportAttributes* parameter to a pointer to an [**NDIS\_MINIPORT\_ADAPTER\_HARDWARE\_ASSIST\_ATTRIBUTES**](https://msdn.microsoft.com/library/windows/hardware/ff565924) structure.

**Note**  NDIS does not report the currently-enabled NDIS QoS hardware capabilities of a network adapter to overlying protocol and filter drivers during the bind or attach operations.

 

For more information on how to register NDIS QoS capabilities, see [Registering NDIS QoS Capabilities](https://msdn.microsoft.com/library/windows/hardware/hh440188).

### Return Status Codes

NDIS handles the OID query request of OID\_QOS\_CURRENT\_CAPABILITIES request for miniport drivers, and returns one of the following status codes.

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
<td><p>The miniport driver does not support the NDIS QoS interface.</p></td>
</tr>
<tr class="odd">
<td><p>NDIS_STATUS_INVALID_LENGTH</p></td>
<td><p>The length of the information buffer is less than sizeof(<a href="https://msdn.microsoft.com/library/windows/hardware/hh451629" data-raw-source="[&lt;strong&gt;NDIS_QOS_CAPABILITIES&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/hh451629)"><strong>NDIS_QOS_CAPABILITIES</strong></a>). NDIS sets the <strong>DATA.QUERY_INFORMATION.BytesNeeded</strong> member in the <a href="https://msdn.microsoft.com/library/windows/hardware/ff566710" data-raw-source="[&lt;strong&gt;NDIS_OID_REQUEST&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff566710)"><strong>NDIS_OID_REQUEST</strong></a> structure to the minimum buffer size that is required.</p></td>
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

[**NDIS\_MINIPORT\_ADAPTER\_HARDWARE\_ASSIST\_ATTRIBUTES**](https://msdn.microsoft.com/library/windows/hardware/ff565924)

[**NdisMSetMiniportAttributes**](https://msdn.microsoft.com/library/windows/hardware/ff563672)

[**NDIS\_OID\_REQUEST**](https://msdn.microsoft.com/library/windows/hardware/ff566710)

[**NDIS\_QOS\_CAPABILITIES**](https://msdn.microsoft.com/library/windows/hardware/hh451629)

 

 




