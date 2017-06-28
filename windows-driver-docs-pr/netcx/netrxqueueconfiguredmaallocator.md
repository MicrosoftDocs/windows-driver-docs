---
title: NetRxQueueConfigureDmaAllocator method
topic_type:
- apiref
api_name:
- NetRxQueueConfigureDmaAllocator
api_location:
- NetAdapterCxStub.lib
- NetAdapterCxStub.dll
api_type:
- LibDef
---

# NetRxQueueConfigureDmaAllocator method

[!include[NetAdapterCx Beta Prerelease](../netcx-beta-prerelease.md)]

Associates a WDFDMAENABLER object with a receive queue.

Syntax
------

```cpp
NTSTATUS NetRxQueueConfigureDmaAllocator(
  _In_ NETRXQUEUE    RxQueue,
  _In_ WDFDMAENABLER Enabler
);
```

Parameters
----------

*RxQueue* [in]  
The receive queue object that the client driver obtained from a previous call to [**NetRxQueueCreate**](netrxqueuecreate.md).

*Enabler* [in]  
A handle to a DMA enabler object that the client driver obtained from a previous call to [**WdfDmaEnablerCreate**](https://msdn.microsoft.com/library/windows/hardware/ff546983).

Return value
------------

The method returns STATUS_SUCCESS if the operation succeeds. Otherwise, this method may return an appropriate NTSTATUS error code.

Remarks
-------

The client driver can choose to let NetAdapterCx manage the receive buffer.  To opt in:

  1.  Set the **AllocationSize** and **AlignmentRequirement** members of [**NET_RXQUEUE_CONFIG**](net-rxqueue-config.md).
  2.  Call [**WdfDmaEnablerCreate**](https://msdn.microsoft.com/library/windows/hardware/ff546983), typically from the [*EVT_NET_ADAPTER_CREATE_RXQUEUE*](evt-net-adapter-create-rxqueue.md) event callback function.
  3.  Call **NetRxQueueConfigureDmaAllocator** with the initialized WDFDMAENABLER.

NetAdapterCx uses the queue's DMA enabler to allocate pre-mapped buffers for each packet in the queue's [**NET_RING_BUFFER**](net-ring-buffer.md) structure, and updates the **VirtualAddress** and **DmaLogicalAddress** members of each [**NET_PACKET_FRAGMENT**](net-packet-fragment.md) to point to each premapped buffer.

The client driver retrieves a pointer to the ring buffer by calling [**NetTxQueueGetRingBuffer**](nettxqueuegetringbuffer.md) or [**NetRxQueueGetRingBuffer**](netrxqueuegetringbuffer.md).

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
<td align="left">NetRxQueue.h</td>
</tr>
<tr class="odd">
<td align="left"><p>Library</p></td>
<td align="left">NetAdapterCxStub.lib</td>
</tr>
<tr class="even">
<td align="left"><p>IRQL</p></td>
<td align="left"><p>PASSIVE_LEVEL</p></td>
</tr>
</tbody>
</table>

## See also


[**NET_RXQUEUE_CONFIG**](net-rxqueue-config.md)

 

 






