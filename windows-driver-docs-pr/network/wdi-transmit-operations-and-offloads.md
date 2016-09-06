---
title: WDI transmit operations and offloads
description: WDI operates in one of two Tx modes Port queuing and PeerTID queuing.
ms.assetid: 9ADBDAD5-4AFA-4AFA-A829-96EB28CEBAA1
---

# WDI transmit operations and offloads


WDI operates in one of two Tx modes: Port queuing and PeerTID queuing. The target sets the mode with the TargetPriorityQueueing capability (true = WDI Port queuing, false = WDI PeerTID queuing).

The host performs the following operations.

-   TX classification (only when **TargetPriorityQueueing** = false)
-   TX queuing (either at a Port level or a PeerTID level)
-   Transfer scheduling (scheduling frame download to the target)
-   Host-Target TX flow control

The following is a list of TX operations and offloads.

<table>
<colgroup>
<col width="25%" />
<col width="25%" />
<col width="25%" />
<col width="25%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Processing step</th>
<th align="left">Description</th>
<th align="left">Owner/Applicable offloads</th>
<th align="left">Notes</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>High-level protocol (task) offloads</p></td>
<td align="left"><p>Checksum, LSO.</p></td>
<td align="left"><p>Checksum is a configurable offload at boot-up. Each frame has flags to specify the applicable checksum operations.</p>
<p>WDI handles LSO segmentation transparently from the TAL/Target if applicable.</p></td>
<td align="left"><p>Checksum: The target passes to WDI its checksum offload capabilities as part of device caps during bringup. For capability information, see [<strong>NDIS_TCP_IP_CHECKSUM_OFFLOAD</strong>](https://msdn.microsoft.com/library/windows/hardware/ff567878).</p>
<p>WDI handles LSO segmentation transparently from the TAL/Target if applicable.</p></td>
</tr>
<tr class="even">
<td align="left"><p>TX encap</p></td>
<td align="left"><p>Update/replace the generic 802.11 header with the appropriate type of 802.11 frame header.</p></td>
<td align="left"><p>Target/TAL</p></td>
<td align="left"><p>The first contiguous buffer of the frame has space available at beginning (before the MAC header). This space is determined by the BackfillSize specified in the device parameters.</p>
<p>For Non-EAPOL packets, the first buffer contains the MAC and LLC/SNAP headers, but not the payload. The first contiguous buffer for an EAPOL packet may contain part (or all) of the payload.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>TX classification</p></td>
<td align="left"><p>Determine the TID. Determine the recipient based on unicast RA or DA.</p></td>
<td align="left"><p>WDI performs classification when <strong>TargetPriorityQueueing</strong> is false. WDI does not perform classification if <strong>TargetPriorityQueueing</strong> is true.</p></td>
<td align="left"></td>
</tr>
<tr class="even">
<td align="left"><p>TX queue</p></td>
<td align="left"><p>Store TX frames in separate queues.</p></td>
<td align="left"><p>WDI queues TX frames if needed.</p></td>
<td align="left"><p>WDI queues TX frames by port (<strong>TargetPriorityQueueing</strong> = true) or by recipient and traffic type (PeerId,TID) (<strong>TargetPriorityQueueing</strong> = false).</p></td>
</tr>
<tr class="odd">
<td align="left"><p>TX flow control</p></td>
<td align="left"><p>Prevent the overrunning of the TIL or target buffers with TX frames.</p></td>
<td align="left"><p>WDI/TIL/Target</p></td>
<td align="left"><p>See the section on Host-Target flow control.</p></td>
</tr>
<tr class="even">
<td align="left"><p>Transfer scheduling</p></td>
<td align="left"><p>Select the TX queue from which to transfer frames to the TAL/TIL when there are multiple backlogged queues.</p></td>
<td align="left"><p>WDI if it needs to queue TX frames.</p></td>
<td align="left"></td>
</tr>
<tr class="odd">
<td align="left"><p>A-MSDU aggregation</p></td>
<td align="left"><p>Determine which frames to group into an A-MSDU aggregate which must be maintained during retransmissions.</p></td>
<td align="left"><p>TAL/Target</p></td>
<td align="left"></td>
</tr>
<tr class="even">
<td align="left"><p>Fragmentation</p></td>
<td align="left"></td>
<td align="left"><p>TAL/Target</p></td>
<td align="left"></td>
</tr>
<tr class="odd">
<td align="left"><p>WLAN scheduling</p></td>
<td align="left"><p>Determine which recipient to transmit to next, which traffic type to send, and how many frames to send.</p></td>
<td align="left"><p>Target</p></td>
<td align="left"></td>
</tr>
<tr class="even">
<td align="left"><p>Encryption</p></td>
<td align="left"><p>Encrypt the frame contents using the security type and security key specified for the recipient (or sender, for multicast frames). Add security encapsulation where applicable.</p></td>
<td align="left"><p>Target</p></td>
<td align="left"><p>For systems supporting FIPS, the encryption is done within the host software. The target's encryption is bypassed.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>A-MPDU aggregation</p></td>
<td align="left"><p>Determine which frames to group into an A-MPDU aggregate, and which can be modified during a retransmission.</p></td>
<td align="left"><p>Target</p></td>
<td align="left"></td>
</tr>
<tr class="even">
<td align="left"><p>Retry</p></td>
<td align="left"><p>Retransmit MPDUs that are nacked or not acked by the recipient.</p></td>
<td align="left"><p>Target</p></td>
<td align="left"></td>
</tr>
</tbody>
</table>

 

## Operation in Host-Implemented FIPS mode


If the host provides FIPS for a given connection (host FIPS mode is set to true in [**WDI\_TLV\_CONNECTION\_SETTINGS**](https://msdn.microsoft.com/library/windows/hardware/dn926261)), the host encrypts the packets before they are submitted to the target. The target transmits the packets without additional changes that affect the data integrity of the packets. For example, the target must not perform transmit MSDU aggregation in this mode.

In the more common case where host-FIPS mode is not enabled (target-implemented encryption mode), the header 802.11 header is followed by the unencrypted payload data. If the packet requires encryption before transmission, the target encrypts the packet. It also performs QoS prioritization of packets, and may perform TCP layer offload operations (such as checksum or large send). For this send processing, the target may need to add additional headers into the packet (for example, QoS, HT headers, or IV).

## TX Encapsulation: Population of 802.11 TX Frame Headers


The network data is submitted in 802.11 packet format to the port (target device). Each transmitted frame starts with a 802.11 MAC header. The host sets some of the fields of the MAC header, while the target sets other fields. The table below describes which fields of the 802.11 MAC header and cipher headers are populated by the host, and which should be populated by the target device.

Field name
Subfield name
Target-implemented encryption mode
Host-implemented FIPS mode
Set by host
Set by target
Set by host
Set by target
Frame Control
Protocol Version
X
X
Frame Control
Type
X
X
Frame Control
Subtype
X
X
Frame Control
To DS
X
X
Frame Control
From DS
X
X
Frame Control
More Fragments
X
X
Frame Control
Retry
X
X
Frame Control
Pwr Mgmt
X
X
Frame Control
More Data
X
X
Frame Control
Protected Frame
X
X
Frame Control
Order
X
X
Duration/Id
X
X
Address 1
X
X
Address 2
X
X
Address 3
X
X
Sequence Control
Fragment Number
X
X
Sequence Control
Sequence Number
X
X
Address 4
X
X
QoS Control
Added/populated by target.
Added/populated by target in the case of 11n QoS association.
HT Control
Added/populated by target.
Added/populated by target.
 

## Related topics


[**NDIS\_TCP\_IP\_CHECKSUM\_OFFLOAD**](https://msdn.microsoft.com/library/windows/hardware/ff567878)

[WDI data transfer](wdi-data-transfer.md)

[**WDI\_TLV\_CONNECTION\_SETTINGS**](https://msdn.microsoft.com/library/windows/hardware/dn926261)

[**WDI\_TXRX\_CAPABILITIES**](https://msdn.microsoft.com/library/windows/hardware/dn898187)

 

 






