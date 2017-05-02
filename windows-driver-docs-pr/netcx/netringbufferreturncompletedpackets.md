---
title: NetRingBufferReturnCompletedPackets method
topic_type:
- apiref
api_name:
- NetRingBufferReturnCompletedPackets
api_location:
- netadapterpacket.h
api_type:
- HeaderDef
---

# NetRingBufferReturnCompletedPackets method

[!include[NetAdapterCx Beta Prerelease](../netcx-beta-prerelease.md)]

Returns all packets that have the **Completed** flag set.

Syntax
------

```cpp
void NetRingBufferReturnCompletedPackets(
  _In_ NET_RING_BUFFER *RingBuffer
);
```

Parameters
----------

*RingBuffer* [in]  
A pointer to a [**NET_RING_BUFFER**](net-ring-buffer.md).

Return value
------------

This method does not return a value.

Remarks
-----

The NetAdapter data path requires packets to be completed in the order that they are given to your driver.
If your driver can complete some packets out of order, you can use **NetRingBufferReturnCompletedPackets** to simplify your completion path.

To use this convenience function, first set the **Completed** flag on the first fragment of all packets with which your driver is finished, whether the packets were processed successfully or not.
Then, call **NetRingBufferReturnCompletedPackets** to batch the completion of all consecutive packets for which the first fragment has the **Completed** flag set.

**NetRingBufferReturnCompletedPackets** completes packets by writing a new value to the **BeginIndex** of the ring buffer.

If you always complete packets in order, it is more efficient to write to **BeginIndex** directly, rather than using the **Completed** flag with **NetRingBufferReturnCompletedPackets**.

When you use **NetRingBufferReturnCompletedPackets**, it is most efficient to flag all finished packets and call the routine just once.

Example
-------

This example shows how a simple data path can complete packets if the hardware completes I/O requests in the order in which they were issued.
Note that this data path just writes to **BeginIndex** directly.

```cpp
for (UINT i = ringBuffer->BeginIndex; 
     i != ringBuffer->EndIndex; 
     i = NetRingBufferIncrementIndex(ringBuffer, i))
{
  NET_PACKET *packet = NetRingBufferGetPacketAtIndex(ringBuffer, i);
  if (!MyHardwareIsDoneWithPacket(packet))
    break;

  // Complete the packet to the OS, simply by updating BeginIndex
  ringBuffer->BeginIndex = i;
}
```

But suppose that your hardware or lower edge completes packets out of order.
Now you cannot just assign the index of the most recently completed packet to **BeginIndex**.
Instead, use the **Completed** flag with **NetRingBufferReturnCompletedPackets** to return packets safely.

In this example, the lower edge returns a linked list of I/O completion blocks, and the list is not sorted in the order in which the I/O requests were issued.

```cpp
void MyPacketCompletionCallback(MY_IO_REQUEST *io)
{
  while (io) {
    NET_PACKET *packet = io->Packet;
    packet->Data.Completed = TRUE;

    // Walk the linked list
    io = io->Next;
  }

  // Complete any packets to the OS.  Updates BeginIndex for us.
  NetRingBufferReturnCompletedPackets(ringBuffer);
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

 

 





