---
title: General OIDs
description: General OIDs
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
<td align="left"><p><a href="/windows-hardware/drivers/network/oid-gen-supported-list" data-raw-source="[OID_GEN_SUPPORTED_LIST](./oid-gen-supported-list.md)">OID_GEN_SUPPORTED_LIST</a></p></td>
<td align="left"><p>List of supported OIDs.</p></td>
</tr>
<tr class="even">
<td align="left"><p>Required</p></td>
<td align="left"><p><a href="/windows-hardware/drivers/network/oid-gen-hardware-status" data-raw-source="[OID_GEN_HARDWARE_STATUS](./oid-gen-hardware-status.md)">OID_GEN_HARDWARE_STATUS</a></p></td>
<td align="left"><p>Hardware status.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Required</p></td>
<td align="left"><p><a href="/windows-hardware/drivers/network/oid-gen-media-supported" data-raw-source="[OID_GEN_MEDIA_SUPPORTED](./oid-gen-media-supported.md)">OID_GEN_MEDIA_SUPPORTED</a></p></td>
<td align="left"><p>Media types supported (encoded).</p></td>
</tr>
<tr class="even">
<td align="left"><p>Required</p></td>
<td align="left"><p><a href="/windows-hardware/drivers/network/oid-gen-media-in-use" data-raw-source="[OID_GEN_MEDIA_IN_USE](./oid-gen-media-in-use.md)">OID_GEN_MEDIA_IN_USE</a></p></td>
<td align="left"><p>Media types in use (encoded).</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Required</p></td>
<td align="left"><p><a href="/windows-hardware/drivers/network/oid-gen-maximum-frame-size" data-raw-source="[OID_GEN_MAXIMUM_FRAME_SIZE](./oid-gen-maximum-frame-size.md)">OID_GEN_MAXIMUM_FRAME_SIZE</a></p></td>
<td align="left"><p>Maximum frame size in bytes.</p></td>
</tr>
<tr class="even">
<td align="left"><p>Required</p></td>
<td align="left"><p><a href="/windows-hardware/drivers/network/oid-gen-link-speed" data-raw-source="[OID_GEN_LINK_SPEED](./oid-gen-link-speed.md)">OID_GEN_LINK_SPEED</a></p></td>
<td align="left"><p>Link speed in units of 100 bps.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Required</p></td>
<td align="left"><p><a href="/windows-hardware/drivers/network/oid-gen-transmit-block-size" data-raw-source="[OID_GEN_TRANSMIT_BLOCK_SIZE](./oid-gen-transmit-block-size.md)">OID_GEN_TRANSMIT_BLOCK_SIZE</a></p></td>
<td align="left"><p>Minimum amount of storage, in bytes, that a single packet occupies in the transmit buffer space of the NIC.</p></td>
</tr>
<tr class="even">
<td align="left"><p>Required</p></td>
<td align="left"><p><a href="/windows-hardware/drivers/network/oid-gen-receive-block-size" data-raw-source="[OID_GEN_RECEIVE_BLOCK_SIZE](./oid-gen-receive-block-size.md)">OID_GEN_RECEIVE_BLOCK_SIZE</a></p></td>
<td align="left"><p>Amount of storage, in bytes, that a single packet occupies in the receive buffer space of the NIC.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Required</p></td>
<td align="left"><p><a href="/windows-hardware/drivers/network/oid-gen-vendor-id" data-raw-source="[OID_GEN_VENDOR_ID](./oid-gen-vendor-id.md)">OID_GEN_VENDOR_ID</a></p></td>
<td align="left"><p>Vendor NIC code.</p></td>
</tr>
<tr class="even">
<td align="left"><p>Required</p></td>
<td align="left"><p><a href="/windows-hardware/drivers/network/oid-gen-vendor-description" data-raw-source="[OID_GEN_VENDOR_DESCRIPTION](./oid-gen-vendor-description.md)">OID_GEN_VENDOR_DESCRIPTION</a></p></td>
<td align="left"><p>Vendor network card description.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Required</p></td>
<td align="left"><p><a href="/windows-hardware/drivers/network/oid-gen-vendor-driver-version" data-raw-source="[OID_GEN_VENDOR_DRIVER_VERSION](./oid-gen-vendor-driver-version.md)">OID_GEN_VENDOR_DRIVER_VERSION</a></p></td>
<td align="left"><p>Vendor-assigned version number of driver.</p></td>
</tr>
<tr class="even">
<td align="left"><p>Required</p></td>
<td align="left"><p><a href="/windows-hardware/drivers/network/oid-gen-current-packet-filter" data-raw-source="[OID_GEN_CURRENT_PACKET_FILTER](./oid-gen-current-packet-filter.md)">OID_GEN_CURRENT_PACKET_FILTER</a></p></td>
<td align="left"><p>Current packet filter (encoded).</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Required</p></td>
<td align="left"><p><a href="/windows-hardware/drivers/network/oid-gen-maximum-total-size" data-raw-source="[OID_GEN_MAXIMUM_TOTAL_SIZE](./oid-gen-maximum-total-size.md)">OID_GEN_MAXIMUM_TOTAL_SIZE</a></p></td>
<td align="left"><p>Maximum total packet length in bytes.</p></td>
</tr>
<tr class="even">
<td align="left"><p>Optional</p></td>
<td align="left"><p><a href="/windows-hardware/drivers/network/oid-gen-rndis-config-parameter" data-raw-source="[OID_GEN_RNDIS_CONFIG_PARAMETER](./oid-gen-rndis-config-parameter.md)">OID_GEN_RNDIS_CONFIG_PARAMETER</a></p></td>
<td align="left"><p>Device-specific configuration parameter (set only).</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Optional</p></td>
<td align="left"><p><a href="/windows-hardware/drivers/network/oid-gen-physical-medium" data-raw-source="[OID_GEN_PHYSICAL_MEDIUM](./oid-gen-physical-medium.md)">OID_GEN_PHYSICAL_MEDIUM</a></p></td>
<td align="left"><p>Information about the underlying physical medium.</p></td>
</tr>
<tr class="even">
<td align="left"><p>Required</p></td>
<td align="left"><p><a href="/windows-hardware/drivers/network/oid-gen-media-connect-status" data-raw-source="[OID_GEN_MEDIA_CONNECT_STATUS](./oid-gen-media-connect-status.md)">OID_GEN_MEDIA_CONNECT_STATUS</a></p></td>
<td align="left"><p>Status of the NIC network connection.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Optional</p></td>
<td align="left"><p><a href="/windows-hardware/drivers/network/oid-gen-mac-options" data-raw-source="[OID_GEN_MAC_OPTIONS](./oid-gen-mac-options.md)">OID_GEN_MAC_OPTIONS</a></p></td>
<td align="left"><p>A bitmask that specifies optional properties of the NIC. Must be supported only by NICs that support <a href="/previous-versions/windows/hardware/network/ff562331(v=vs.85)" data-raw-source="[802.1p packet priority](/previous-versions/windows/hardware/network/ff562331(v=vs.85))">802.1p packet priority</a>.</p></td>
</tr>
</tbody>
</table>

 

