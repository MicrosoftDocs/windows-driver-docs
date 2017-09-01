---
title: NET_PACKET structure
---

# NET_PACKET structure


[!include[NetAdapterCx Beta Prerelease](../netcx-beta-prerelease.md)]

Represents a single network packet.

Syntax
------

```cpp
typedef struct _NET_PACKET {
  NET_PACKET_FRAGMENT Data;

  NET_PACKET_LAYOUT   Layout;
  NET_PACKET_CHECKSUM Checksum;

  UINT16              IgnoreThisPacket          : 1;
  UINT16              AdvancedOffloadRequested  : 1;
  UINT16              Reserved1                 : 14;

  UINT32              Hash;

  UINT32              Reserved2;
  PVOID               Reserved3[2];
} NET_PACKET, *PNET_PACKET;
```

Members
-------

**Data**

A structure of type [**NET_PACKET_FRAGMENT**](net-packet-fragment.md) that describes the first fragment of the packet payload.  See the **LastFragmentOfFrame** member of the [**NET_PACKET_FRAGMENT**](net-packet-fragment.md) structure to determine if this packet is associated with additional fragments.

**Layout**  
A structure of type [**NET_PACKET_LAYOUT**](net-packet-layout.md).

* For transmit queues, if the host stack has enabled a task offload that uses a protocol header, specifies a read-only offset to each protocol field.  For example, if TCP checksum offload is enabled, this member specifies the offset to the TCP header.  Otherwise, this member is empty.

* For receive queues, this member is reserved.

**Checksum**  
A structure of type [**NET_PACKET_CHECKSUM**](net-packet-checksum.md).  

* For transmit queues, this member is read-only and specifies whether the client driver should perform checksum offload.

* For receive queues, if the NIC hardware performed a checksum validation, specifies the result of the validation.

**IgnoreThisPacket**  
* For receive queues, the client sets this bit to prevent the packet from being indicated to the host.
For example, if the hardware encountered a DMA error while writing bytes into this the data buffer for this packet, the client can set this bit to drop the partial packet.

* For transmit queues, this bit is read-only.  If set, it indicates that the client should not transmit the packet.

**AdvancedOffloadRequested**  
Reserved.
Do not read or write to this value.

**Reserved1**  
Reserved.
Do not read or write to this value.

**Hash**  
Reserved.
Do not read or write to this value.

**Reserved2**  
Reserved.
Do not read or write to this value.

**Reserved3**  
Reserved.
Do not read or write to this value.

Remarks
-------
Each [**NET_PACKET**](net-packet.md) structure represents a single network frame.

The **NET_PACKET** structure can be an element in a [**NET_RING_BUFFER**](net-ring-buffer.md) structure.

You can optionally use [**NetRingBufferGetPacketAtIndex**](netringbuffergetpacketatindex.md) or [**NetRingBufferGetNextPacket**](netringbuffergetnextpacket.md) to obtain a **NET_PACKET** from a ring buffer.

Requirements
------------

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p>Minimum KMDF version</p></td>
<td align="left"><p>1.21</p></td>
</tr>
<tr class="even">
<td align="left"><p>Minimum NetAdapterCx version</p></td>
<td align="left"><p>1.0</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Header</p></td>
<td align="left">Netpacket.h</td>
</tr>
</tbody>
</table>






