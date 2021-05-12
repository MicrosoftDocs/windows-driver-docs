---
title: OID_TCP_TASK_IPSEC_OFFLOAD_V2_DELETE_SA
description: As a set, the TCP/IP transport uses the OID_TCP_TASK_IPSEC_OFFLOAD_V2_DELETE_SA OID to request that a miniport driver delete the specified security associations (SAs) from a NIC.
ms.date: 08/08/2017
keywords: 
 -OID_TCP_TASK_IPSEC_OFFLOAD_V2_DELETE_SA Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# OID\_TCP\_TASK\_IPSEC\_OFFLOAD\_V2\_DELETE\_SA


\[The IPsec Task Offload feature is deprecated and should not be used.\]

As a set, the TCP/IP transport uses the OID\_TCP\_TASK\_IPSEC\_OFFLOAD\_V2\_DELETE\_SA OID to request that a miniport driver delete the specified security associations (SAs) from a NIC.

**Note**  NDIS supports this OID with the direct OID request interface. For more information about the direct OID request interface, see [NDIS 6.1 Direct OID Request Interface](/windows-hardware/drivers/ddi/_netvista/).

 

## Remarks

All NDIS 6.1 miniport drivers that support IPsec offload version 2 (IPsecOV2) must support this OID.

When a miniport driver receives this request, the driver should delete the specified SAs from the NIC and free any system resources that were allocated for the SAs.

The miniport driver receives an [**IPSEC\_OFFLOAD\_V2\_DELETE\_SA**](/windows-hardware/drivers/ddi/ndis/ns-ndis-_ipsec_offload_v2_delete_sa) structure that contains a handle to an SA bundle and a pointer to the next **IPSEC\_OFFLOAD\_V2\_DELETE\_SA** structure in a linked list.

The miniport driver can set **SaDeleteReq** in the [**NDIS\_IPSEC\_OFFLOAD\_V2\_NET\_BUFFER\_LIST\_INFO**](/windows-hardware/drivers/ddi/ndis/ns-ndis-_ndis_ipsec_offload_v2_net_buffer_list_info) structure for a receive [**NET\_BUFFER\_LIST**](/windows-hardware/drivers/ddi/ndis/ns-ndis-_net_buffer_list) structure. The TCP/IP transport subsequently issues OID\_TCP\_TASK\_IPSEC\_OFFLOAD\_V2\_DELETE\_SA once to delete the inbound SA that the packet was received over and once again to delete the outbound SA that corresponds to the deleted inbound SA. The NIC must not remove either of these SAs before receiving the corresponding OID\_TCP\_TASK\_IPSEC\_OFFLOAD\_V2\_DELETE\_SA request.

### Return status codes

The miniport driver's [*MiniportOidRequest*](/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_oid_request) function returns one of the following values for this request:

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Term</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p><strong>NDIS_STATUS_SUCCESS</strong></p></td>
<td><p>The miniport driver completed the request successfully.</p></td>
</tr>
<tr class="even">
<td><p><strong>NDIS_STATUS_PENDING</strong></p></td>
<td><p>The miniport driver will complete the request asynchronously. After the miniport driver has completed all processing, it must succeed the request by calling the <a href="/windows-hardware/drivers/ddi/ndis/nf-ndis-ndismoidrequestcomplete" data-raw-source="[&lt;strong&gt;NdisMOidRequestComplete&lt;/strong&gt;](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndismoidrequestcomplete)"><strong>NdisMOidRequestComplete</strong></a> function, passing <strong>NDIS_STATUS_SUCCESS</strong> for the <em>Status</em> parameter.</p></td>
</tr>
<tr class="odd">
<td><p><strong>NDIS_STATUS_NOT_ACCEPTED</strong></p></td>
<td><p>The miniport driver is resetting.</p></td>
</tr>
<tr class="even">
<td><p><strong>NDIS_STATUS_REQUEST_ABORTED</strong></p></td>
<td><p>The miniport driver stopped processing the request. For example, NDIS called the <a href="/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_reset" data-raw-source="[&lt;em&gt;MiniportResetEx&lt;/em&gt;](/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_reset)"><em>MiniportResetEx</em></a> function.</p></td>
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
<td><p>Supported in NDIS 6.1 and later.</p></td>
</tr>
<tr class="even">
<td><p>Header</p></td>
<td>Ntddndis.h (include Ndis.h)</td>
</tr>
</tbody>
</table>

## See also


[**IPSEC\_OFFLOAD\_V2\_DELETE\_SA**](/windows-hardware/drivers/ddi/ndis/ns-ndis-_ipsec_offload_v2_delete_sa)

[**NDIS\_IPSEC\_OFFLOAD\_V2\_NET\_BUFFER\_LIST\_INFO**](/windows-hardware/drivers/ddi/ndis/ns-ndis-_ndis_ipsec_offload_v2_net_buffer_list_info)

[**NET\_BUFFER\_LIST**](/windows-hardware/drivers/ddi/ndis/ns-ndis-_net_buffer_list)

