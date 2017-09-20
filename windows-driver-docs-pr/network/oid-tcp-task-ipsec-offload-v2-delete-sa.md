---
title: OID\_TCP\_TASK\_IPSEC\_OFFLOAD\_V2\_DELETE\_SA
author: windows-driver-content
description: As a set, the TCP/IP transport uses the OID\_TCP\_TASK\_IPSEC\_OFFLOAD\_V2\_DELETE\_SA OID to request that a miniport driver delete the specified security associations (SAs) from a NIC.
ms.assetid: 9b2c702c-beaa-4caf-97c5-d80a2632e4d3
ms.author: windowsdriverdev
ms.date: 08/08/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords: 
 -OID_TCP_TASK_IPSEC_OFFLOAD_V2_DELETE_SA Network Drivers Starting with Windows Vista
---

# OID\_TCP\_TASK\_IPSEC\_OFFLOAD\_V2\_DELETE\_SA


\[The IPsec Task Offload feature is deprecated and should not be used.\]

As a set, the TCP/IP transport uses the OID\_TCP\_TASK\_IPSEC\_OFFLOAD\_V2\_DELETE\_SA OID to request that a miniport driver delete the specified security associations (SAs) from a NIC.

**Note**  NDIS supports this OID with the direct OID request interface. For more information about the direct OID request interface, see [NDIS 6.1 Direct OID Request Interface](https://msdn.microsoft.com/library/windows/hardware/ff564736).

 

Remarks
-------

All NDIS 6.1 miniport drivers that support IPsec offload version 2 (IPsecOV2) must support this OID.

When a miniport driver receives this request, the driver should delete the specified SAs from the NIC and free any system resources that were allocated for the SAs.

The miniport driver receives an [**IPSEC\_OFFLOAD\_V2\_DELETE\_SA**](https://msdn.microsoft.com/library/windows/hardware/ff556979) structure that contains a handle to an SA bundle and a pointer to the next **IPSEC\_OFFLOAD\_V2\_DELETE\_SA** structure in a linked list.

The miniport driver can set **SaDeleteReq** in the [**NDIS\_IPSEC\_OFFLOAD\_V2\_NET\_BUFFER\_LIST\_INFO**](https://msdn.microsoft.com/library/windows/hardware/ff565818) structure for a receive [**NET\_BUFFER\_LIST**](https://msdn.microsoft.com/library/windows/hardware/ff568388) structure. The TCP/IP transport subsequently issues OID\_TCP\_TASK\_IPSEC\_OFFLOAD\_V2\_DELETE\_SA once to delete the inbound SA that the packet was received over and once again to delete the outbound SA that corresponds to the deleted inbound SA. The NIC must not remove either of these SAs before receiving the corresponding OID\_TCP\_TASK\_IPSEC\_OFFLOAD\_V2\_DELETE\_SA request.

### Return status codes

The miniport driver's [*MiniportOidRequest*](https://msdn.microsoft.com/library/windows/hardware/ff559416) function returns one of the following values for this request:

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
<td><p>The miniport driver will complete the request asynchronously. After the miniport driver has completed all processing, it must succeed the request by calling the [<strong>NdisMOidRequestComplete</strong>](https://msdn.microsoft.com/library/windows/hardware/ff563622) function, passing <strong>NDIS_STATUS_SUCCESS</strong> for the <em>Status</em> parameter.</p></td>
</tr>
<tr class="odd">
<td><p><strong>NDIS_STATUS_NOT_ACCEPTED</strong></p></td>
<td><p>The miniport driver is resetting.</p></td>
</tr>
<tr class="even">
<td><p><strong>NDIS_STATUS_REQUEST_ABORTED</strong></p></td>
<td><p>The miniport driver stopped processing the request. For example, NDIS called the [<em>MiniportResetEx</em>](https://msdn.microsoft.com/library/windows/hardware/ff559432) function.</p></td>
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
<td><p>Supported in NDIS 6.1 and later.</p></td>
</tr>
<tr class="even">
<td><p>Header</p></td>
<td>Ntddndis.h (include Ndis.h)</td>
</tr>
</tbody>
</table>

## See also


[**IPSEC\_OFFLOAD\_V2\_DELETE\_SA**](https://msdn.microsoft.com/library/windows/hardware/ff556979)

[**NDIS\_IPSEC\_OFFLOAD\_V2\_NET\_BUFFER\_LIST\_INFO**](https://msdn.microsoft.com/library/windows/hardware/ff565818)

[**NET\_BUFFER\_LIST**](https://msdn.microsoft.com/library/windows/hardware/ff568388)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20OID_TCP_TASK_IPSEC_OFFLOAD_V2_DELETE_SA%20%20RELEASE:%20%288/8/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


