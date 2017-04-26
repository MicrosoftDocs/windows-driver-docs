---
title: NetRingBufferAdvanceNextPacket method
topic_type:
- apiref
api_name:
- NetRingBufferAdvanceNextPacket
api_location:
- netadapterpacket.h
api_type:
- HeaderDef
---

# NetRingBufferAdvanceNextPacket method


[!include[NetAdapterCx Beta Prerelease](../netcx-beta-prerelease.md)]

Increments the NextIndex value of the ring buffer and then returns a pointer to the net packet at the new NextIndex value.

Syntax
------

```cpp
__inline
NET_PACKET* NetRingBufferAdvanceNextPacket(
  _In_ NET_RING_BUFFER *RingBuffer
);
```

Parameters
----------

*RingBuffer* [in]  
A pointer to a [**NET_RING_BUFFER**](net-ring-buffer.md).

Return value
------------

Returns NULL if the value of NextIndex equals the value of EndIndex for the specified ring buffer. Otherwise, increments NextIndex and returns a pointer to the NET_PACKET at the new NextIndex value of the ring buffer.

Remarks
-----

For more info, see [Transferring Network Data](transferring-network-data.md).

Requirements
------------

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p>Target platform</p></td>
<td align="left">Universal</td>
</tr>
<tr class="even">
<td align="left"><p>Minimum KMDF version</p></td>
<td align="left"><p>1.21</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Minimum NetAdapterCx version</p></td>
<td align="left"><p>1.0</p></td>
</tr>
<tr class="even">
<td align="left"><p>Header</p></td>
<td align="left">Netadapterpacket.h (include Netadaptercx.h)</td>
</tr>
<tr class="odd">
<td align="left"><p>IRQL</p></td>
<td align="left"><p>&lt;=DISPATCH_LEVEL</p></td>
</tr>
</tbody>
</table>

 

 





