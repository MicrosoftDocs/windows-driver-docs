---
title: NET_PACKET_DECLARE_CONTEXT_TYPE_WITH_NAME macro
topic_type:
- apiref
api_name:
- NET_PACKET_DECLARE_CONTEXT_TYPE_WITH_NAME
api_location:
- netadapterpacket.h
api_type:
- HeaderDef
---

# NET_PACKET_DECLARE_CONTEXT_TYPE_WITH_NAME macro


[!include[NetAdapterCx Beta Prerelease](../netcx-beta-prerelease.md)]

The NET_PACKET_DECLARE_CONTEXT_TYPE_WITH_NAME macro creates an accessor method with a specified name for a client driver's object-specific context space.

Syntax
------

```cpp
void NET_PACKET_DECLARE_CONTEXT_TYPE_WITH_NAME(
    _contexttype,
    _castingfunction
);
```

Parameters
----------

*_contexttype*   
The structure type name of a driver-defined structure that describes the contents of an object's context space.

*_castingfunction*   
A C-language routine name. The macro uses this name as the name for the accessor method that it creates for the object's context space.  You can put any name you like here; the macro will create a new function with this name.

Return value
------------

This macro does not return a value.

Remarks
-------

You can use NET_PACKET_DECLARE_CONTEXT_TYPE_WITH_NAME to define one context per packet.  The per-packet context area is optional.

You may find it helpful to store hardware-specific or bus-specific data in each packet.

NetAdapter automatically zeros the context area when the packet is created.
The context area is not zeroed out if a packet is reused.
If you need to initialize the context areas before the data path starts, initialize them in your [*EvtNetAdapterCreateTxQueue*](evt-net-adapter-create-txqueue.md) handler after calling [**NetTxQueueCreate**](nettxqueuecreate.md); or in the [*EvtNetAdapterCreateRxQueue*](evt-net-adapter-create-rxqueue.md) handler after calling [**NetRxQueueCreate**](netrxqueuecreate.md).

Example
-------

To declare a context area, use the NET_PACKET_DECLARE_CONTEXT_TYPE_WITH_NAME macro after declaring a structure in a header file:
```
typedef struct _MY_TX_PACKET_CONTEXT {
    ULONG MyFlags;
    VOID *MyDescriptor;
} MY_TX_PACKET_CONTEXT;

NET_PACKET_DECLARE_CONTEXT_TYPE_WITH_NAME(MY_TX_PACKET_CONTEXT, GetMyTxPacketContext);
```

Then, when the client creates a queue, associate the packet context with the queue:
```
NET_TXQUEUE_CONFIG txQueueConfig;
NET_TXQUEUE_CONFIG_INIT(&txQueueConfig, . . .);
NET_TXQUEUE_CONFIG_SET_DEFAULT_PACKET_CONTEXT_TYPE(&txQueueConfig, MY_TX_PACKET_CONTEXT);

status = NetTxQueueCreate(. . ., &txQueueConfig, . . .);

// Optional: Initialize the context area of each packet to a non-zero value.
NET_RING_BUFFER *ringBuffer = NetTxQueueGetRingBuffer(txQueue);
for (UINT i = 0; i < ringBuffer->NumberOfElements; i++) {
    NET_PACKET *packet = NetRingBufferGetPacketAtIndex(ringBuffer, i);
    MY_TX_PACKET_CONTEXT *context = GetMyTxPacketContext(packet);
    context->MyFlags = 0x1234;
}
```

While the data path is in operation, you can use the accessor method to get the context area of any packet:
```
NET_PACKET *packet = NetRingBufferGetNextPacket(ringBuffer);
MY_TX_PACKET_CONTEXT *context = GetMyTxPacketContext(packet);
```

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
</tbody>
</table>

## See also


[**NetPacketGetTypedContext**](netpacketgettypedcontext.md)

[**WDF_DECLARE_CONTEXT_TYPE_WITH_NAME**](https://msdn.microsoft.com/library/windows/hardware/ff551252)

 

 






