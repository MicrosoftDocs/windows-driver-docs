---
title: NetRingBufferReturnCompletedPacketsThroughIndex method
topic_type:
- apiref
api_name:
- NetRingBufferReturnCompletedPacketsThroughIndex
api_location:
- netadapterpacket.h
api_type:
- HeaderDef
---

# NetRingBufferReturnCompletedPacketsThroughIndex method


[!include[NetAdapterCx Beta Prerelease](../netcx-beta-prerelease.md)]

Returns all packets that have the **Completed** flag set, up to a specified range.

Syntax
------

```cpp
void NetRingBufferReturnCompletedPacketsThroughIndex(
  _In_ NET_RING_BUFFER *RingBuffer,
  _In_ UINT32          EndIndex
);
```

Parameters
----------

*RingBuffer* [in]  
A pointer to a [**NET_RING_BUFFER**](net-ring-buffer.md).

*EndIndex* [in]  
The index of the last [**NET_PACKET**](net-packet.md) to be considered for completion.
This index is exclusive of the range, so the packet at this index value will not be completed.

Return value
------------

This method does not return a value.

Remarks
-------

The NetAdapter data path requires packets to be completed in the order in which they are given to your driver.
If your driver can complete some packets out of order, you can use **NetRingBufferReturnCompletedPacketsThroughIndex** to simplify your completion path.

To use this convenience function, first set the **Completed** flag on the first fragment of all packets with which your driver is finished, whether the packets were processed successfully or not.
Then, call **NetRingBufferReturnCompletedPacketsThroughIndex** to batch the completion of all consecutive packets  for which the first fragment has the **Completed** flag set.

**NetRingBufferReturnCompletedPacketsThroughIndex** completes packets by writing a new value to the **BeginIndex** of the ring buffer.

If you always complete packets in order, it is more efficient to write to **BeginIndex** directly, rather than using the **Completed** flag with **NetRingBufferReturnCompletedPacketsThroughIndex**.

Typically you would call **NetRingBufferReturnCompletedPacketsThroughIndex** once just before returning from [*EVT_RXQUEUE_ADVANCE*](evt-rxqueue-advance.md) or [*EVT_TXQUEUE_ADVANCE*](evt-txqueue-advance.md).
There's no advantage to calling **NetRingBufferReturnCompletedPacketsThroughIndex** more than once per Advance call; the API is designed for batching.

The [**NetRingBufferReturnCompletedPackets**](netringbufferreturncompletedpackets.md) routine is similar, but examines all packets owned by your driver.
**NetRingBufferReturnCompletedPacketsThroughIndex** allows you to limit the search to a specific range of packets owned by your driver.
If you don't need to control the exact range of packets that are completed, you can use the simpler method [**NetRingBufferReturnCompletedPackets**](netringbufferreturncompletedpackets.md) instead of **NetRingBufferReturnCompletedPacketsThroughIndex**.

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

 

 





