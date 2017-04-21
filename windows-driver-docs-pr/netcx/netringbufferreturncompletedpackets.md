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

The NetAdapter datapath requires packets to be completed in the order that they are given to your driver.
If your driver can complete some packets out-of-order, then you may use **NetRingBufferReturnCompletedPackets** to simplify your completion path.

To use this convenience function, first set the **Completed** flag on all packets that your driver is done with, whether they were processed successfully or not.
Then, call **NetRingBufferReturnCompletedPackets** to batch the completion of all consecutive packets that have the **Completed** flag.

**NetRingBufferReturnCompletedPackets** completes packets by writing a new value to the **BeginIndex** of the ring buffer.

If you always complete packets in order, it is more efficient to just write to **BeginIndex** directly, rather than to use the **Completed** flag with **NetRingBufferReturnCompletedPackets**.

When you use **NetRingBufferReturnCompletedPackets**, it is most efficient to batch it.

Example
-------

This example shows how a simple datapath can complete packets, if the hardware completes IOs in the same order that they were issued.
Note that this datapath just writes to **BeginIndex** directly.
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

But suppose that your hardware or lower edge completes packets out-of-order.
Now you cannot just assign the index of the most recently-completed packet to **BeginIndex**.
Instead, you can use use the **Completed** flag with **NetRingBufferReturnCompletedPackets** to safely return packets.

In this example, the lower edge returns a linked list of IO completion blocks, and the list is not sorted in the order that the IOs were issued.

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

For more info, see [Handling I/O Requests](handling-i-o-requests.md).

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

 

 





