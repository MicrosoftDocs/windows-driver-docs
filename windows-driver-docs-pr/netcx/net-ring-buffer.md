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

```cpp
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
A read-only byte offset from the start of one **NET_PACKET** to the start of the next.  Use `((BYTE*)p + ElementStride)` to obtain the address of the next element.

**NumberOfElements**  
A read-only value that indicates the number of packets in the ring buffer, which is always a power of two, and greater than one.

**ElementIndexMask**  
A read-only UINT32 mask that is defined as (**NumberOfElements**-1).  The client can use this value to calculate an index that wraps around the ring buffer.  Use the identity `(x % NumberofElements) == (x & ElementIndexMask)`.

**BeginIndex**  
Specifies the index of the first element owned by the client driver in the inclusive range [0, **NumberOfElements**-1].
While a client driver can modify this value directly, it typically uses helper routines like [**NetRingBufferReturnCompletedPackets**](netringbufferreturncompletedpackets.md) instead.

**NextIndex**  
Specifies the index of the next element that needs processing.  For optional use by the client driver.
While a client driver can modify this value directly, it typically calls [**NetRingBufferAdvanceNextPacket**](netringbufferadvancenextpacket.md) instead.

**EndIndex**  
Specifies the read-only index of the last element that is owned by the client driver in the inclusive range [0, **NumberOfElements**-1].

**NetAdapterScratch**  
A pointer to a buffer that the client driver may use for any purpose.

**OSReserved2**  
Reserved.
Client drivers must not read or write to this value.

**Buffer**  
A byte array that contains the packets in the ring buffer.
Typically, a client driver calls [**NetRingBufferGetPacketAtIndex**](netringbuffergetpacketatindex.md) to access packets in the ring buffer.

Remarks
-------

The **NET_RING_BUFFER** is a generic ring buffer, optimized for efficient access from a single thread.
A **NET_RING_BUFFER** contains elements of type [**NET_PACKET**](net-packet.md).

For more info about the ring buffer, see [Handling I/O Requests](handling-i-o-requests.md#using-the-ring-buffer).

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

 

 





