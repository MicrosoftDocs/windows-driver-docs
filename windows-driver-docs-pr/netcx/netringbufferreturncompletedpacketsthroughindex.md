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

Sets the BeginIndex value of the specified ring buffer to the first packet that is not completed.

Syntax
------

```cpp
__inline
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
The index of the last [**NET_PACKET**](net-packet.md) in the client's ring buffer window that is programmed for transmission or receive.

Return value
------------

This method does not return a value.

Remarks
-------

When the device driver completes transmission or reception of a [**NET_PACKET**](net-packet.md), it marks the packet as completed by setting the **Completed** flag in the starting fragment of the packet.

The client can call **NetRingBufferReturnCompletedPacketsThroughIndex** from [*EVT_RXQUEUE_ADVANCE*](evt-rxqueue-advance.md) or [*EVT_TXQUEUE_ADVANCE*](evt-txqueue-advance.md) to transfer ownership of completed packets in the ring buffer back to NetAdapterCx.

NetAdapterCx updates the packet's **BeginIndex** field to the index of the first non-completed packet or to **EndIndex**, whichever comes first. **EndIndex** should indicate the last [**NET_PACKET**](net-packet.md) that the client has programmed to transmit or receive data.

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

 

 





