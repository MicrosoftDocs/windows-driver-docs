---
title: NET_PACKET_FRAGMENT structure
---

# NET_PACKET_FRAGMENT structure


[!include[NetAdapterCx Beta Prerelease](../netcx-beta-prerelease.md)]

Represents one contiguous buffer in memory.

Syntax
------

```cpp
typedef struct _NET_PACKET_FRAGMENT {
  ULONG_PTR         LastFragmentOfFrame   : 1;
  ULONG_PTR         LastPacketOfChain     : 1;
#if _WIN64
  ULONG_PTR         Reserved              : 3;
  ULONG_PTR         NextFragment_Reserved : 59;
#else 
  ULONG_PTR         Reserved              : 1;
  ULONG_PTR         NextFragment_Reserved : 29;
#endif 
  
  union
  {
      MDL              *Mdl;
      PHYSICAL_ADDRESS DmaLogicalAddress;
      ULONG64          AsInteger;
  } Mapping;

  PVOID             VirtualAddress;

  UINT64            ValidLength           : 26;
  UINT64            Capacity              : 26;
  UINT64            Offset                : 10;
  UINT64            Completed             : 1;
  UINT64            Scratch               : 1;
} NET_PACKET_FRAGMENT, *PNET_PACKET_FRAGMENT;
```

Members
-------

**LastFragmentOfFrame**  
This bit field value specifies whether this is the last fragment in the current packet.  If it is not set, use **NET_PACKET_FRAGMENT_GET_NEXT** to get the next fragment in the chain.

**LastPacketOfChain**  
Reserved.
Client drivers must not read or write to this value.

**Reserved**  
Reserved.
Client drivers must not read or write to this value.

**NextFragment_Reserved**  
Reserved.
Client drivers must not read or write to this value.


**Mapping**  
TBD

**DmaLogicalAddress**  
For receive queues, contains a mapped DMA address that can be used to program NIC hardware.

For transmit queues, cast this value to an MDL pointer.

Do not modify this value.

**VirtualAddress**  
Points to the start of the packet buffer.
This address is mapped into the system address space.

For transmit queues, this value is read-only.

**ValidLength**  
Contains the length of packet payload.  This value is less than or equal to the value of **Capacity**.

For transmit queues, this value is read-only.

**Capacity**  
Contains the total length of the packet buffer.

For transmit queues, this value is read-only.

**Offset**  
Contains the offset from the start of the `VirtualAddress` and `DmaLogicalAddress` to the start of the valid packet payload.  This value is less than or equal to the value of **Capacity**.

For transmit queues, this value is read-only.

**Completed**  
A bit field value that, when set for the first fragment of a [**NET_PACKET**](net-packet.md), specifies that this packet should be completed when the client calls [**NetRingBufferReturnCompletedPackets**](netringbufferreturncompletedpackets.md).

Do not use this flag on fragments other than the first fragment of a packet.

**Scratch**  
A bit field value that the client may use for any purpose.  When the [**NET_PACKET**](net-packet.md) is reused, this value is reset to zero.

Remarks
-------

The **NET_PACKET_FRAGMENT** structure is similar in concept to a memory descriptor list (MDL).

A single [**NET_PACKET**](net-packet.md) structure contains references to one or more **NET_PACKET_FRAGMENT** structures.

While each fragment is a virtually contiguous buffer of memory, a packet that contains more than one fragment is virtually discontiguous.

The client driver should not unlink, append, or rearrange **NET_PACKET_FRAGMENT** structures within a [**NET_PACKET**](net-packet.md) structure.

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