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

Returns a pointer to the packet in a ring buffer at the ring buffer's **NextIndex** index value.

Syntax
------

```cpp
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

Returns **NULL** if the ring buffer's **NextIndex** equals its **EndIndex**, meaning there are no more unprocessed packets.
Otherwise, this routine returns a pointer to the [**NET_PACKET**](net-packet.md) at the new **NextIndex** value of the ring buffer.

Remarks
-----

This routine is similar to [**NetRingBufferAdvanceNextPacket**](netringbufferadvancenextpacket.md).
The difference is that this routine does not modify the ring buffer's **NextIndex** field; the ring buffer is not modified.

Typically, your driver would use **NetRingBufferGetNextPacket** to get the next packet to program into hardware.
Because **NetRingBufferGetNextPacket** does not increment **NextIndex**, you'll also eventually need to increment the index.
For example:

```cpp
NET_PACKET *nextPacket;
while (NULL != (nextPacket = NetRingBufferGetNextPacket(ringBuffer))) {
  if (!EnoughMemoryAvailableForPacket(nextPacket))
    break;

    ProgramPacketToMyHardware(nextPacket);
    NetRingBufferAdvanceNextPacket(ringBuffer);
}
```

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
<td align="left"><p>PASSIVE_LEVEL</p></td>
</tr>
</tbody>
</table>

 

 





