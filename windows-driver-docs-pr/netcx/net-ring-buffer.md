---
title: NET_RING_BUFFER structure
topic_type:
- apiref
api_name:
- NET_RING_BUFFER
api_location:
- netringbuffer.h
api_type:
- HeaderDef
---

# NET_RING_BUFFER structure


[!include[NetAdapterCx Beta Prerelease](../netcx-beta-prerelease.md)]

Specifies a buffer comprised of one or more [**NET_PACKET**](net-packet.md) structures.

Syntax
------

```ManagedCPlusPlus
typedef struct _NET_RING_BUFFER {
  UINT16                                              OSReserved1;
  UINT16                                              ElementStride;
  UINT32                                              NumberOfElements;
  UINT32                                              ElementIndexMask;
  UINT32                                              BeginIndex;
  UINT32                                              NextIndex;
  UINT32                                              EndIndex;
  VOID                                                *NetAdapterScratch[2];
  VOID                                                *OSReserved2[3];
  _Field_size_(NumberOfElements * ElementStride) BYTE Buffer[];
} NET_RING_BUFFER, *PNET_RING_BUFFER;
```

Members
-------

**OSReserved1**  
Reserved.
Client drivers must not read or write to this value.

**ElementStride**  
The byte offset from the start of one **NET_PACKET** to the start of the next.
Read-only: client drivers may read this value, but must not modify it.

**NumberOfElements**  
Indicates the number of packets in the ring buffer.
NumberOfElements is guaranteed to be a power of two.
Read-only: client drivers may read this value, but must not modify it.

**ElementIndexMask**  
A mask that is defined as (`NumberOfElements`-1).
The mask can be used to efficiently calculate an index that wraps around the ring buffer.
Read-only: client drivers may read this value, but must not modify it.

**BeginIndex**  
Specifies the index of the first element owned by the client driver.
`BeginIndex` must have a value in the inclusive range [0, `NumberOfElements`-1].
Read-write: client drivers may read or write to this value.
Typically, a client driver would use helper routines like [**NetRingBufferReturnCompletedPackets**](netringbufferreturncompletedpackets.md) to write to this field.

**NextIndex**  
Client drivers may use this value to track the index of the next element that needs processing.
Typically, a client driver would use [**NetRingBufferAdvanceNextPacket**](netringbufferadvancenextpacket.md) to read and update this field.
Read-write: client drivers may read or write to this value.

**EndIndex**  
Specifies the index of the last element that is owned by the client driver.
`EndIndex` is guaranteed to have a value in the inclusive range [0, `NumberOfElements`-1].
Read-only: client drivers may read this value, but must not modify it.

**NetAdapterScratch**  
Client drivers may use this for any purpose.
Read-write: client drivers may read or write to this value.

**OSReserved2**  
Reserved.
Client drivers must not read or write to this value.

**Buffer**  
Start of the array of elements.
Typically, a client driver would use [**NetRingBufferGetPacketAtIndex**](netringbuffergetpacketatindex.md) to access elements in this array.

Remarks
-------

The `NET_RING_BUFFER` is a generic ring buffer, optimized for efficient access from a single thread.
In the current version of Windows, a `NET_RING_BUFFER` can only contain `NET_PACKET` elements.

A `NET_RING_BUFFER` is organized around ownership of elements: the client driver owns every element from `BeginIndex` to `EndIndex`.
For example, if `BeginIndex` is 2 and `EndIndex` is 5, then the client driver owns three elements: the elements with index 2, 3, and 4.
If `BeginIndex == EndIndex`, then zero elements are owned by the client driver.

The NetAdapter framework adds elements to the ring buffer by incrementing `EndIndex`.
A client driver returns ownership of the elements by incrementing `BeginIndex`.

The client driver may optionally use `NextIndex` to track elements that have been partially-processed, but which are still not ready to be returned back to the OS.
For example, a driver may use `NextIndex` to track which packets have been submitted to the hardware.

Although a client driver may access the `NET_RING_BUFFER` directly, a client driver typically uses higher-level helper routines, like `NetRingBufferReturnCompletedPackets`.
These high-level routines hide the details of the ring buffer.

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
<td align="left">Netringbuffer.h</td>
</tr>
</tbody>
</table>

 

 





