---
title: WDI receive operations and offloads
description: These main categories of operation offloads are configurable.MSDU-level receive operationsFrame forwarding (forwarding decision and actuation)Protocol/Task offloads.
ms.assetid: 7D2648BC-05F2-4F75-BA01-E0385C83E0E8
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# WDI receive operations and offloads


These main categories of operation offloads are configurable.

-   MSDU-level receive operations
-   Frame forwarding (forwarding decision and actuation)
-   Protocol/Task offloads

The following is a list of RX operations and offloads.

<table>
<colgroup>
<col width="25%" />
<col width="25%" />
<col width="25%" />
<col width="25%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Function</th>
<th align="left">Description</th>
<th align="left">Ownership</th>
<th align="left">Notes</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>Decryption</p></td>
<td align="left"><p>Decrypt the frame contents using the security type and security key specified for the sender.</p></td>
<td align="left"><p>Target</p></td>
<td align="left"><p>In host-implemented FIPS mode, the decryption is done within the host software. The target&#39;s decryption is bypassed.</p></td>
</tr>
<tr class="even">
<td align="left"><p>A-MPDU deaggregation</p></td>
<td align="left"><p>Decompose an RX A-MPDU into individual MPDUs.</p></td>
<td align="left"><p>Target</p></td>
<td align="left"></td>
</tr>
<tr class="odd">
<td align="left"><p>A-MSDU deaggregation</p></td>
<td align="left"><p>Decompose an RX A-MSDU into individual MSDUs.</p></td>
<td align="left"><p>Target/TAL</p></td>
<td align="left"><p>Each RX MSDU is placed into a separate buffer.</p></td>
</tr>
<tr class="even">
<td align="left"><p>MSDU Security decap and de-MIC</p></td>
<td align="left"><p>For security types that involve an MSDU-level MIC, verify the received MIC. Decapsulate the security header and footer.</p></td>
<td align="left"><p>Target/TAL</p></td>
<td align="left"><p>The operating system performs countermeasures if needed.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Rx decap</p></td>
<td align="left"><p>Replace non-initial A-MSDU subframe headers with 802.11 headers, using the 802.11 header fields from the initial A-MSDU subframe as appropriate.</p></td>
<td align="left"><p>Target/TAL</p></td>
<td align="left"><p>During A-MSDU deaggregation, the non-initial MSDUs of the A-MSDU need their 802.3 header replaced by a generic 802.11 header. WDI always expects 802.11 headers.</p></td>
</tr>
<tr class="even">
<td align="left"><p>Rx reordering logic</p></td>
<td align="left"><p>For each RX MPDU, determine which slot of the Rx reordering array it goes to. Determine when a series of in-order frames is present. Determine when to release pending frames even if their preceding frames have not arrived.</p></td>
<td align="left"><p>Target/TAL</p></td>
<td align="left"></td>
</tr>
<tr class="odd">
<td align="left"><p>Rx discard logic</p></td>
<td align="left"><p>Determine which Rx frames need to be discarded:</p>
<ol>
<li>If it does not match any of the receive packet filters.</li>
<li>If the frame is encrypted, discard if:
<ul>
<li>A cipher key is not available to decrypt the packet.</li>
<li>The packet payload fails to decrypt successfully.</li>
<li>The packet payload fails the MIC verification.</li>
<li>The packet fails the replay mechanism defined for the cipher algorithm (see Rx PN/replay check).</li>
<li>A privacy exemption is defined for the packet&#39;s ether type that specifies an <strong>WDI_EXEMPT_ ALWAYS</strong> action.</li>
</ul></li>
<li>If the frame is unencrypted, discard if:
<ul>
<li>A cipher key is available to decrypt the packet and a privacy exemption is defined for the packet&#39;s Ethertype that specifies a <strong>WDI_EXEMPT_ON_ KEY_UNAVAILABLE</strong> action.</li>
<li>The dot11ExcludeUnencrypted MIB is set to true.</li>
</ul></li>
</ol></td>
<td align="left"><p>Target/TAL makes all discard decisions.</p></td>
<td align="left"></td>
</tr>
<tr class="even">
<td align="left"><p>Rx PN/replay check</p></td>
<td align="left"><p>Confirm that each MPDU has a distinct Packet Number that is larger than prior PNs.</p></td>
<td align="left"><p>This is a mandatory and always enabled offload except for streams associated with a reorder queue and reordering queue management is not fully offloaded to the target.</p></td>
<td align="left"></td>
</tr>
<tr class="odd">
<td align="left"><p>Chatter offload</p></td>
<td align="left"><p>Avoid interrupting the host for each deferrable &quot;noise&quot; Rx frame. Instead, group the Rx noise frames and use a single interrupt to deliver all such frames.</p></td>
<td align="left"><p>Target</p></td>
<td align="left"></td>
</tr>
<tr class="even">
<td align="left"><p>Defragmentation</p></td>
<td align="left"><p>Reassemble 802.11 fragments into their original MSDU.</p></td>
<td align="left"><p>Target/TAL</p></td>
<td align="left"></td>
</tr>
<tr class="odd">
<td align="left"><p>Rx reorder queuing</p></td>
<td align="left"><p>Store out-of-order Rx MPDUs until the missing prior MPDUs from the flow arrive.</p></td>
<td align="left"><p>Target/TAL</p></td>
<td align="left"></td>
</tr>
<tr class="even">
<td align="left"><p>Rx discard actuation</p></td>
<td align="left"><p>Discard Rx frames based on the specifications flagged by the Rx discard logic run at the target.</p></td>
<td align="left"><p>Target/TAL</p></td>
<td align="left"></td>
</tr>
<tr class="odd">
<td align="left"><p>Higher-level protocol (task) offloads</p></td>
<td align="left"><p>Checksum</p></td>
<td align="left"><p>Checksum: Configurable offload at boot-up if required.</p></td>
<td align="left"><p>Checksum: The target passes its checksum offload capabilities as part of device caps to WDI during bring-up. For information about capabilities, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff567878" data-raw-source="[&lt;strong&gt;NDIS_TCP_IP_ CHECKSUM_OFFLOAD&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff567878)"><strong>NDIS_TCP_IP_ CHECKSUM_OFFLOAD</strong></a>.</p></td>
</tr>
</tbody>
</table>

 

## Receive operations in Host-Implemented FIPS mode


In this mode, the target may indicate the received frame with either an 802.11 header or an 802.3 header. The frame must not be decrypted before indication.

If discard logic is offloaded to the target, it must mark received frames for discard if they meet any of the following criteria.

-   Frames that have a bad CRC.
-   Duplicate frames.
-   Frames that do not match the configured packet filters.

The target must increment the appropriate MAC and PHY statistics for packets that are either received successfully or discarded by the port.

In addition, the target must perform discard actuation if offloaded.

The target should not strip the QoS flag from the 802.11 header on the RX path when operating in Host-implemented FIPS mode. The target should indicate the frame without modifying the QoS header.

For the case of fragmented packets, the payload type reported by the LE for FIPS mode is always **WDI\_FRAME\_MSDU\_FRAGMENT** as the host is doing the defragmentation process. However, in non-FIPS mode, the reported payload type should be **WDI\_FRAME\_MSDU** as the Target/TAL is performing the defragmentation.

## Related topics


[**NDIS\_TCP\_IP\_CHECKSUM\_OFFLOAD**](https://msdn.microsoft.com/library/windows/hardware/ff567878)

[WDI data transfer](wdi-data-transfer.md)

[**WDI\_EXEMPTION\_ACTION\_TYPE**](https://msdn.microsoft.com/library/windows/hardware/dn897820)

[**WDI\_FRAME\_PAYLOAD\_TYPE**](https://msdn.microsoft.com/library/windows/hardware/dn897831)

 

 






