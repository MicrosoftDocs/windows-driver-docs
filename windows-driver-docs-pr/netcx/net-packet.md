---
title: NET_PACKET structure
---

# NET_PACKET structure


[!include[NetAdapterCx Beta Prerelease](../netcx-beta-prerelease.md)]

Represents a single network packet.

Syntax
------

```ManagedCPlusPlus
typedef struct _NET_PACKET {
  NET_PACKET_FRAGMENT Data;
  NET_PACKET_LAYOUT   Layout;
  NET_PACKET_CHECKSUM Checksum;
  UINT16              IgnoreThisPacket  :1;
  UINT16              AdvancedOffloadRequested  :1;
  UINT16              Reserved1  :14;
  UINT32              Hash;
  UINT32              Reserved2;
  PVOID               Reserved3;
} NET_PACKET, *PNET_PACKET;
```

Members
-------

**Data**  
A structure of type [**NET_PACKET_FRAGMENT**](net-packet-fragment.md) that describes the first fragment of the packet payload.

**Layout**  
A structure of type [**NET_PACKET_LAYOUT**](net-packet-layout.md).  

For Tx queues, describes the layout of the packet.
If the OS requests a task offload that involves a protocol header, the OS will write the offsets to each protocol field to the `Layout` field.
For example, if the OS requests TCP checksum offload, the OS will write the offset to the TCP header.
The `Layout` field may be empty if the OS does not request any features that involve protocol headers.
For Tx queues, this field is read-only.

For Rx queues, this field is Reserved.

**Checksum**  
A structure of type [**NET_PACKET_CHECKSUM**](net-packet-checksum.md).  

For Tx queues, client drivers read the Checksum field to determine whether to enable checksum offload.
For Tx queues, this field is read-only.

For Rx queues, if the NIC hardware performed a checksum validation, the client driver writes the result of the validation in the Checksum field.

**IgnoreThisPacket**  
For Rx queues, client drivers may set this to `TRUE` to prevent the packet from being indicated to the OS.
For example, if the hardware encountered a DMA error while writing bytes into this packet's data buffer, the client driver can set `IgnoreThisPacket` to drop the partial packet.

For Tx queues, client drivers should not attempt to transmit packets where `IgnoreThisPacket` is `TRUE`.
This field is read-only for Tx queues.

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
The **NET_PACKET** structure can be an element in a [**NET_RING_BUFFER**](net-ring-buffer.md) structure.

A single **NET_PACKET** has one or more [**NET_PACKET_FRAGMENT**](net-packet-fragment.md) structures linked into it.

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






