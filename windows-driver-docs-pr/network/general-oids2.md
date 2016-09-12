---
title: General OIDs
description: General OIDs
ms.assetid: fcd0e7fe-d1ab-4ec3-9c47-0bfb0ce63572
---

# General OIDs


## <a href="" id="ddk-general-oids-ng"></a>


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
<td align="left"><p>[OID_GEN_SUPPORTED_LIST](https://msdn.microsoft.com/library/windows/hardware/ff569642)</p></td>
<td align="left"><p>List of supported OIDs.</p></td>
</tr>
<tr class="even">
<td align="left"><p>Required</p></td>
<td align="left"><p>[OID_GEN_HARDWARE_STATUS](https://msdn.microsoft.com/library/windows/hardware/ff569585)</p></td>
<td align="left"><p>Hardware status.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Required</p></td>
<td align="left"><p>[OID_GEN_MEDIA_SUPPORTED](https://msdn.microsoft.com/library/windows/hardware/ff569609)</p></td>
<td align="left"><p>Media types supported (encoded).</p></td>
</tr>
<tr class="even">
<td align="left"><p>Required</p></td>
<td align="left"><p>[OID_GEN_MEDIA_IN_USE](https://msdn.microsoft.com/library/windows/hardware/ff569607)</p></td>
<td align="left"><p>Media types in use (encoded).</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Required</p></td>
<td align="left"><p>[OID_GEN_MAXIMUM_FRAME_SIZE](https://msdn.microsoft.com/library/windows/hardware/ff569598)</p></td>
<td align="left"><p>Maximum frame size in bytes.</p></td>
</tr>
<tr class="even">
<td align="left"><p>Required</p></td>
<td align="left"><p>[OID_GEN_LINK_SPEED](https://msdn.microsoft.com/library/windows/hardware/ff569593)</p></td>
<td align="left"><p>Link speed in units of 100 bps.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Required</p></td>
<td align="left"><p>[OID_GEN_TRANSMIT_BLOCK_SIZE](https://msdn.microsoft.com/library/windows/hardware/ff569644)</p></td>
<td align="left"><p>Minimum amount of storage, in bytes, that a single packet occupies in the transmit buffer space of the NIC.</p></td>
</tr>
<tr class="even">
<td align="left"><p>Required</p></td>
<td align="left"><p>[OID_GEN_RECEIVE_BLOCK_SIZE](https://msdn.microsoft.com/library/windows/hardware/ff569633)</p></td>
<td align="left"><p>Amount of storage, in bytes, that a single packet occupies in the receive buffer space of the NIC.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Required</p></td>
<td align="left"><p>[OID_GEN_VENDOR_ID](https://msdn.microsoft.com/library/windows/hardware/ff569651)</p></td>
<td align="left"><p>Vendor NIC code.</p></td>
</tr>
<tr class="even">
<td align="left"><p>Required</p></td>
<td align="left"><p>[OID_GEN_VENDOR_DESCRIPTION](https://msdn.microsoft.com/library/windows/hardware/ff569649)</p></td>
<td align="left"><p>Vendor network card description.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Required</p></td>
<td align="left"><p>[OID_GEN_VENDOR_DRIVER_VERSION](https://msdn.microsoft.com/library/windows/hardware/ff569650)</p></td>
<td align="left"><p>Vendor-assigned version number of driver.</p></td>
</tr>
<tr class="even">
<td align="left"><p>Required</p></td>
<td align="left"><p>[OID_GEN_CURRENT_PACKET_FILTER](https://msdn.microsoft.com/library/windows/hardware/ff569575)</p></td>
<td align="left"><p>Current packet filter (encoded).</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Required</p></td>
<td align="left"><p>[OID_GEN_MAXIMUM_TOTAL_SIZE](https://msdn.microsoft.com/library/windows/hardware/ff569601)</p></td>
<td align="left"><p>Maximum total packet length in bytes.</p></td>
</tr>
<tr class="even">
<td align="left"><p>Optional</p></td>
<td align="left"><p>[OID_GEN_RNDIS_CONFIG_PARAMETER](https://msdn.microsoft.com/library/windows/hardware/ff569639)</p></td>
<td align="left"><p>Device-specific configuration parameter (set only).</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Optional</p></td>
<td align="left"><p>[OID_GEN_PHYSICAL_MEDIUM](https://msdn.microsoft.com/library/windows/hardware/ff569621)</p></td>
<td align="left"><p>Information about the underlying physical medium.</p></td>
</tr>
<tr class="even">
<td align="left"><p>Required</p></td>
<td align="left"><p>[OID_GEN_MEDIA_CONNECT_STATUS](https://msdn.microsoft.com/library/windows/hardware/ff569604)</p></td>
<td align="left"><p>Status of the NIC network connection.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Optional</p></td>
<td align="left"><p>[OID_GEN_MAC_OPTIONS](https://msdn.microsoft.com/library/windows/hardware/ff569597)</p></td>
<td align="left"><p>A bitmask that specifies optional properties of the NIC. Must be supported only by NICs that support [802.1p packet priority](https://msdn.microsoft.com/library/windows/hardware/ff562331).</p></td>
</tr>
</tbody>
</table>

 

 

 





