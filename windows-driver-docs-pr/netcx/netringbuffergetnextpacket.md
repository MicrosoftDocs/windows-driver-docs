---
title: NetRingBufferGetNextPacket method
topic_type:
- apiref
api_name:
- NetRingBufferGetNextPacket
api_location:
- netadapterpacket.h
api_type:
- HeaderDef
---

# NetRingBufferGetNextPacket method


[!include[NetAdapterCx Beta Prerelease](../netcx-beta-prerelease.md)]

Returns a pointer to the net packet at the NextIndex value of the ring buffer.

Syntax
------

```cpp
__inline
NET_PACKET* NetRingBufferGetNextPacket(
  _In_ NET_RING_BUFFER *RingBuffer
);
```

Parameters
----------

*RingBuffer* [in]  
A pointer to a [**NET_RING_BUFFER**](net-ring-buffer.md).

Return value
------------

A pointer to a [**NET_PACKET**](net-packet.md) at the **NextIndex** value of the ring buffer, or NULL if the value of **NextIndex** equals the value of **EndIndex**.

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

 

 





