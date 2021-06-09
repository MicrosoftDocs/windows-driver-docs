---
title: WDI_TLV_LSO_V1_CAPABILITIES (0xCC)
description: WDI_TLV_LSO_V1_CAPABILITIES is a TLV that contains Large Send Offload V1 capabilities.
ms.date: 07/18/2017
keywords:
 - WDI_TLV_LSO_V1_CAPABILITIES (0xCC) Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# WDI\_TLV\_LSO\_V1\_CAPABILITIES (0xCC)


WDI\_TLV\_LSO\_V1\_CAPABILITIES is a TLV that contains Large Send Offload V1 capabilities.

Capability values are reported as documented in [**NDIS\_TCP\_IP\_CHECKSUM\_OFFLOAD**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_tcp_ip_checksum_offload). Use NDIS\_OFFLOAD\_NOT\_SUPPORTED and NDIS\_OFFLOAD\_SUPPORTED when indicating capabilities through [OID\_WDI\_GET\_ADAPTER\_CAPABILITIES](./oid-wdi-get-adapter-capabilities.md).

## TLV Type


0xCC

## Length


The sum (in bytes) of the sizes of all contained elements.

## Values


<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Type</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>UINT32</td>
<td>The encapsulation type. Valid values are:
<ul>
<li>WDI_ENCAPSULATION_IEEE_802_11</li>
</ul></td>
</tr>
<tr class="even">
<td>UINT32</td>
<td>The maximum offload size. Specified by the maximum number of bytes of TCP user data per packet.</td>
</tr>
<tr class="odd">
<td>UINT32</td>
<td>The minimum number of segments that a large TCP packet must be divisible by before the transport can offload it to the hardware for segmentation.</td>
</tr>
<tr class="even">
<td>UINT32</td>
<td>Specifies whether or not TCP options are supported for this offload.</td>
</tr>
<tr class="odd">
<td>UINT32</td>
<td>Specifies whether or not IP options are supported for this offload.</td>
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
<td><p>Minimum supported client</p></td>
<td><p>Windows 10</p></td>
</tr>
<tr class="even">
<td><p>Minimum supported server</p></td>
<td><p>Windows Server 2016</p></td>
</tr>
<tr class="odd">
<td><p>Header</p></td>
<td>Wditypes.hpp</td>
</tr>
</tbody>
</table>

 

