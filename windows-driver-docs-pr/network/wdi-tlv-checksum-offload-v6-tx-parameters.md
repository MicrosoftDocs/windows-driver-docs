---
title: WDI_TLV_CHECKSUM_OFFLOAD_V6_TX_PARAMETERS (0xDC)
ms.topic: reference
description: WDI_TLV_CHECKSUM_OFFLOAD_V6_TX_PARAMETERS is a TLV that contains for Tx checksum offload for IPv6.
ms.date: 03/02/2023
keywords:
 - WDI_TLV_CHECKSUM_OFFLOAD_V6_TX_PARAMETERS (0xDC) Network Drivers Starting with Windows Vista
---

# WDI\_TLV\_CHECKSUM\_OFFLOAD\_V6\_TX\_PARAMETERS (0xDC)


WDI\_TLV\_CHECKSUM\_OFFLOAD\_V6\_TX\_PARAMETERS is a TLV that contains for Tx checksum offload for IPv6.

Capability values are reported as documented in [**NDIS\_TCP\_IP\_CHECKSUM\_OFFLOAD**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_tcp_ip_checksum_offload). Use NDIS\_OFFLOAD\_NOT\_SUPPORTED and NDIS\_OFFLOAD\_SUPPORTED when indicating capabilities through [OID\_WDI\_GET\_ADAPTER\_CAPABILITIES](./oid-wdi-get-adapter-capabilities.md).

## TLV Type


0xDC

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
<td>Encapsulation type. Valid values are:
<ul>
<li>WDI_ENCAPSULATION_IEEE_802_11</li>
</ul></td>
</tr>
<tr class="even">
<td>UINT32</td>
<td>Specifies if offload of checksum of packets with IP extension headers is supported.</td>
</tr>
<tr class="odd">
<td>UINT32</td>
<td>Specifies if offload of checksum with TCP options is supported.</td>
</tr>
<tr class="even">
<td>UINT32</td>
<td>Specifies if TCP checksum offload is enabled.</td>
</tr>
<tr class="odd">
<td>UINT32</td>
<td>Specifies if UDP offload is enabled.</td>
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

 

