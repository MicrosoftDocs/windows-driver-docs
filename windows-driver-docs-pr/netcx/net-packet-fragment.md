---
title: NET_PACKET_FRAGMENT structure
---

# NET_PACKET_FRAGMENT structure


[!include[NetAdapterCx Beta Prerelease](../netcx-beta-prerelease.md)]

Represents one contiguous buffer in memory

Syntax
------

```ManagedCPlusPlus
typedef struct _NET_PACKET_FRAGMENT {
  ULONG_PTR         LastFragmentOfFrame  :1;
  ULONG_PTR         LastPacketOfChain  :1;
#if _WIN64
  ULONG_PTR         Reserved  :3;
  ULONG_PTR         NextFragment_Reserved  :59;
#else 
  ULONG_PTR         Reserved  :1;
  ULONG_PTR         NextFragment_Reserved  :29;
#endif 
  PHYSICAL_ADDRESS  DmaLogicalAddress;
  PVOID             VirtualAddress;
  UINT64            ValidLength  :26;
  UINT64            Capacity  :26;
  UINT64            Offset  :10;
  UINT64            Completed  :1;
  UINT64            Scratch  :1;
} NET_PACKET_FRAGMENT, *PNET_PACKET_FRAGMENT;
```

Members
-------

**LastFragmentOfFrame**  
`TRUE` if this is the last fragment in the current packet.
If `FALSE`, use `NET_PACKET_FRAGMENT_GET_NEXT` to get the next fragment in the chain.

**LastPacketOfChain**  
Reserved.
Client drivers must not read or write to this value.

**Reserved**  
Reserved.
Client drivers must not read or write to this value.

**NextFragment_Reserved**  
Reserved.
Client drivers must not read or write to this value.

**DmaLogicalAddress**  
For Rx queues, contains a mapped DMA address that can be used to program NIC hardware.

For Tx queues, cast this value to an MDL pointer.

This value is read-only: client drivers must not modify this value.

**VirtualAddress**  
Points to the start of the packet buffer.
This address is mapped into the system address space.

For Tx queues, this value is read-only.

**ValidLength**  
Contains the length of packet payload.
The `ValidLength` is guaranteed to be less than or equal to `Capacity`.

For Tx queues, this value is read-only.

**Capacity**  
Contains the total length of the packet buffer.

For Tx queues, this value is read-only.

**Offset**  
Contains the offset from the start of the `VirtualAddress` and `DmaLogicalAddress` to the start of the valid packet payload.
The `Offset` is guaranteed to be less than or equal to `Capacity`.

For Tx queues, this value is read-only.

**Completed**  
Client drivers may use this flag in conjunction with [**NetRingBufferReturnCompletedPackets**](netringbufferreturncompletedpackets.md) to complete packets back to the OS.
The client driver sets the `Completed` flag to `TRUE` on the first fragment of a `NET_PACKET`.

This flag is Reserved on fragments other than the first fragment of a packet.

**Scratch**  
Client drivers may use this value for any purpose.  
It will be reset to 0 when the `NET_PACKET` is reused.

 
Members
-------

A `NET_PACKET_FRAGMENT` is similar in concept to an `MDL`.
The `NET_PACKET_FRAGMENT` is optimized for efficient advance/retreat operations, and efficient use with DMA.

A single `NET_PACKET` has one or more `NET_PACKET_FRAGMENT` structures linked into it.
Each fragment is a virtually-contiguous buffer of memory; the packet itself is the sum of each virtually-contiguous buffer.
Therefore, a packet can be virtually-discontiguous; if so, the packet has more than one fragment attached to it.

In NetAdapterCx version 1.0, each `NET_PACKET` represents a single network frame, and the `LastPacketOfChain` field is not used.

In NetAdapterCx version 1.0, the client driver cannot unlink, append, or rearrange `NET_PACKET_FRAGMENT` structures from a `NET_PACKET` structure.

The buffer layout fields must always obey this identity: `Capacity` &geq; `ValidLength` + `Offset`.
