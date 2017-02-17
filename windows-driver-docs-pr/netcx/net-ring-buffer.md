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
  _Field_size_(NumberOfElements * ElementStride) BYTE Buffer;
} NET_RING_BUFFER, *PNET_RING_BUFFER;
```

Members
-------

**OSReserved1**  
Reserved.

**ElementStride**  
The byte offset from the start of one packet to the start of the next.

**NumberOfElements**  
Indicates the number of packets in the ring buffer. 

**ElementIndexMask**  
TBD

**BeginIndex**  
Specifies an index value to the first packet in the ring buffer.

**NextIndex**  
Specifies an index value to the packet to be processed next.

**EndIndex**  
Specifies an index value to the last packet in the ring buffer.

**NetAdapterScratch**  
Reserved.

**OSReserved2**  
Reserved.

**Buffer**  
Pointer to the ring buffer.

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

 

 





