---
title: Combining Types of Task Offloads
description: Combining Types of Task Offloads
ms.assetid: 33f8ba3c-09ab-4041-9641-d4207b98c8b7
keywords:
- task offload WDK TCP/IP transport , combining offload types
- combining task offload types WDK TCP/IP offload
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Combining Types of Task Offloads





The following restrictions determine which combinations of NDIS 6.0 and later task offload services can be active on the system:

-   A task offload-capable miniport adapter can support checksum offload alone.

-   A large send offload version 1 (LSOV1)-capable network interface card (NIC) must support V4 TCP and IPv4 checksum transmit offload services. If an LSOV1-capable miniport adapter also supports Internet protocol security (IPsec) offload, NDIS will configure the adapter to offload either IPsec or LSOV1, but not both.

-   A large send offload version 2 (LSOV2)-capable miniport adapter must support TCP and IP Checksum transmit offload. If a LSOV2-capable miniport adapter also supports IPsec offload, NDIS will configure it to offload IPsec or LSOV2, but not both.

Miniport drivers are not required to support both IPv4 and IPv6. All NDIS 6.0 and later miniport drivers must support Ethernet 802.3 encapsulations with the ability to support Ethernet 802.1Q tags. The following table describes the hardware requirements when the miniport driver reports support for various offload capabilities.

<table>
<colgroup>
<col width="33%" />
<col width="33%" />
<col width="33%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Type of offload</th>
<th align="left">IPv4</th>
<th align="left">IpV6</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Checksum Offload</strong></p></td>
<td align="left"></td>
<td align="left"></td>
</tr>
<tr class="even">
<td align="left"><p>UDP Checksum</p></td>
<td align="left"><p>Optional</p></td>
<td align="left"><p>Optional</p></td>
</tr>
<tr class="odd">
<td align="left"><p>TCP Checksum</p></td>
<td align="left"><p>Optional</p></td>
<td align="left"><p>Optional</p></td>
</tr>
<tr class="even">
<td align="left"><p>TCP Options</p></td>
<td align="left"><p>Optional</p></td>
<td align="left"><p>Required (for TCP Checksum)</p></td>
</tr>
<tr class="odd">
<td align="left"><p>IP Checksum</p></td>
<td align="left"><p>Optional</p></td>
<td align="left"><p>Not Applicable</p></td>
</tr>
<tr class="even">
<td align="left"><p>IP Options</p></td>
<td align="left"><p>Required (for TCP checksum)</p></td>
<td align="left"><p>Not Applicable</p></td>
</tr>
<tr class="odd">
<td align="left"><p>IP Extension Header</p></td>
<td align="left"><p>Not Applicable</p></td>
<td align="left"><p>Required (128 bytes)</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Large Send Offload version 1 (LSOv1)</strong></p></td>
<td align="left"></td>
<td align="left"></td>
</tr>
<tr class="odd">
<td align="left"><p>Max Offload Size</p></td>
<td align="left"><p>&lt;= 64K</p></td>
<td align="left"><p>Not Applicable</p></td>
</tr>
<tr class="even">
<td align="left"><p>TCP Options</p></td>
<td align="left"><p>Required</p></td>
<td align="left"><p>Not Applicable</p></td>
</tr>
<tr class="odd">
<td align="left"><p>IP Options</p></td>
<td align="left"><p>Required</p></td>
<td align="left"><p>Not Applicable</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Large Send Offload version 2 (LSOv2)</strong></p></td>
<td align="left"></td>
<td align="left"></td>
</tr>
<tr class="odd">
<td align="left"><p>Max Offload Size</p></td>
<td align="left"><p>Unlimited</p></td>
<td align="left"><p>Unlimited</p></td>
</tr>
<tr class="even">
<td align="left"><p>IP Options</p></td>
<td align="left"><p>Required</p></td>
<td align="left"><p>Required (128 bytes)</p></td>
</tr>
<tr class="odd">
<td align="left"><p>IP ID Support</p></td>
<td align="left"><p>0x0000 to 0xffff</p></td>
<td align="left"><p>0x0000 to 0x7fff reserved for segmentation offload</p></td>
</tr>
</tbody>
</table>

 

 

 





