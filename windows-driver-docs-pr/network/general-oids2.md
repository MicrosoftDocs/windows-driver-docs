---
title: General OIDs
description: General OIDs
ms.assetid: fcd0e7fe-d1ab-4ec3-9c47-0bfb0ce63572
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# General OIDs





The following table lists the general OIDs for Remote NDIS Ethernet devices.

<table>
<colgroup>
<col width="33%" />
<col width="33%" />
<col width="33%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Support</th>
<th align="left">OID</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>Required</p></td>
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff569642" data-raw-source="[OID_GEN_SUPPORTED_LIST](https://msdn.microsoft.com/library/windows/hardware/ff569642)">OID_GEN_SUPPORTED_LIST</a></p></td>
<td align="left"><p>List of supported OIDs.</p></td>
</tr>
<tr class="even">
<td align="left"><p>Required</p></td>
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff569585" data-raw-source="[OID_GEN_HARDWARE_STATUS](https://msdn.microsoft.com/library/windows/hardware/ff569585)">OID_GEN_HARDWARE_STATUS</a></p></td>
<td align="left"><p>Hardware status.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Required</p></td>
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff569609" data-raw-source="[OID_GEN_MEDIA_SUPPORTED](https://msdn.microsoft.com/library/windows/hardware/ff569609)">OID_GEN_MEDIA_SUPPORTED</a></p></td>
<td align="left"><p>Media types supported (encoded).</p></td>
</tr>
<tr class="even">
<td align="left"><p>Required</p></td>
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff569607" data-raw-source="[OID_GEN_MEDIA_IN_USE](https://msdn.microsoft.com/library/windows/hardware/ff569607)">OID_GEN_MEDIA_IN_USE</a></p></td>
<td align="left"><p>Media types in use (encoded).</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Required</p></td>
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff569598" data-raw-source="[OID_GEN_MAXIMUM_FRAME_SIZE](https://msdn.microsoft.com/library/windows/hardware/ff569598)">OID_GEN_MAXIMUM_FRAME_SIZE</a></p></td>
<td align="left"><p>Maximum frame size in bytes.</p></td>
</tr>
<tr class="even">
<td align="left"><p>Required</p></td>
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff569593" data-raw-source="[OID_GEN_LINK_SPEED](https://msdn.microsoft.com/library/windows/hardware/ff569593)">OID_GEN_LINK_SPEED</a></p></td>
<td align="left"><p>Link speed in units of 100 bps.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Required</p></td>
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff569644" data-raw-source="[OID_GEN_TRANSMIT_BLOCK_SIZE](https://msdn.microsoft.com/library/windows/hardware/ff569644)">OID_GEN_TRANSMIT_BLOCK_SIZE</a></p></td>
<td align="left"><p>Minimum amount of storage, in bytes, that a single packet occupies in the transmit buffer space of the NIC.</p></td>
</tr>
<tr class="even">
<td align="left"><p>Required</p></td>
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff569633" data-raw-source="[OID_GEN_RECEIVE_BLOCK_SIZE](https://msdn.microsoft.com/library/windows/hardware/ff569633)">OID_GEN_RECEIVE_BLOCK_SIZE</a></p></td>
<td align="left"><p>Amount of storage, in bytes, that a single packet occupies in the receive buffer space of the NIC.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Required</p></td>
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff569651" data-raw-source="[OID_GEN_VENDOR_ID](https://msdn.microsoft.com/library/windows/hardware/ff569651)">OID_GEN_VENDOR_ID</a></p></td>
<td align="left"><p>Vendor NIC code.</p></td>
</tr>
<tr class="even">
<td align="left"><p>Required</p></td>
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff569649" data-raw-source="[OID_GEN_VENDOR_DESCRIPTION](https://msdn.microsoft.com/library/windows/hardware/ff569649)">OID_GEN_VENDOR_DESCRIPTION</a></p></td>
<td align="left"><p>Vendor network card description.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Required</p></td>
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff569650" data-raw-source="[OID_GEN_VENDOR_DRIVER_VERSION](https://msdn.microsoft.com/library/windows/hardware/ff569650)">OID_GEN_VENDOR_DRIVER_VERSION</a></p></td>
<td align="left"><p>Vendor-assigned version number of driver.</p></td>
</tr>
<tr class="even">
<td align="left"><p>Required</p></td>
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff569575" data-raw-source="[OID_GEN_CURRENT_PACKET_FILTER](https://msdn.microsoft.com/library/windows/hardware/ff569575)">OID_GEN_CURRENT_PACKET_FILTER</a></p></td>
<td align="left"><p>Current packet filter (encoded).</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Required</p></td>
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff569601" data-raw-source="[OID_GEN_MAXIMUM_TOTAL_SIZE](https://msdn.microsoft.com/library/windows/hardware/ff569601)">OID_GEN_MAXIMUM_TOTAL_SIZE</a></p></td>
<td align="left"><p>Maximum total packet length in bytes.</p></td>
</tr>
<tr class="even">
<td align="left"><p>Optional</p></td>
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff569639" data-raw-source="[OID_GEN_RNDIS_CONFIG_PARAMETER](https://msdn.microsoft.com/library/windows/hardware/ff569639)">OID_GEN_RNDIS_CONFIG_PARAMETER</a></p></td>
<td align="left"><p>Device-specific configuration parameter (set only).</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Optional</p></td>
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff569621" data-raw-source="[OID_GEN_PHYSICAL_MEDIUM](https://msdn.microsoft.com/library/windows/hardware/ff569621)">OID_GEN_PHYSICAL_MEDIUM</a></p></td>
<td align="left"><p>Information about the underlying physical medium.</p></td>
</tr>
<tr class="even">
<td align="left"><p>Required</p></td>
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff569604" data-raw-source="[OID_GEN_MEDIA_CONNECT_STATUS](https://msdn.microsoft.com/library/windows/hardware/ff569604)">OID_GEN_MEDIA_CONNECT_STATUS</a></p></td>
<td align="left"><p>Status of the NIC network connection.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Optional</p></td>
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff569597" data-raw-source="[OID_GEN_MAC_OPTIONS](https://msdn.microsoft.com/library/windows/hardware/ff569597)">OID_GEN_MAC_OPTIONS</a></p></td>
<td align="left"><p>A bitmask that specifies optional properties of the NIC. Must be supported only by NICs that support <a href="https://msdn.microsoft.com/library/windows/hardware/ff562331" data-raw-source="[802.1p packet priority](https://msdn.microsoft.com/library/windows/hardware/ff562331)">802.1p packet priority</a>.</p></td>
</tr>
</tbody>
</table>

 

 

 





