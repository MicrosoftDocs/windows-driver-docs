---
title: NetRxQueueConfigureDmaAllocator method
description: Associates a WDFDMAENABLER object with a receive queue.
ms.assetid: f0eac676-0f0c-4be2-b514-db03d3eb7067
keywords: ["NetRxQueueConfigureDmaAllocator method Network Drivers Starting with Windows Vista"]
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

```ManagedCPlusPlus
NTSTATUS NetRxQueueConfigureDmaAllocator(
  _In_ NETRXQUEUE    RxQueue,
  _In_ WDFDMAENABLER Enabler
);
```

Parameters
----------

*RxQueue* \[in\]  
The receive queue object that the client driver obtained from a previous call to [**NetRxQueueCreate**](netrxqueuecreate.md).

*Enabler* \[in\]  
A handle to a DMA enabler object that the client driver obtained from a previous call to [**WdfDmaEnablerCreate**](https://msdn.microsoft.com/library/windows/hardware/ff546983).

Return value
------------

The method returns STATUS\_SUCCESS if the operation succeeds. Otherwise, this method may return an appropriate NTSTATUS error code.

Remarks
-------

The client driver can choose to let NetAdapterCx manage the receive buffer on its behalf. To opt in, the client driver must first specify the size of its desired common buffer by setting the **AllocationSize** and **AlignmentRequirement** members of [**NET\_RXQUEUE\_CONFIG**](net-rxqueue-config.md).

Typically, from its [*EVT\_NET\_ADAPTER\_CREATE\_RXQUEUE*](evt-net-adapter-create-rxqueue.md) event callback function, the client driver calls [**WdfDmaEnablerCreate**](https://msdn.microsoft.com/library/windows/hardware/ff546983), and then passes the initialized WDFDMAENABLER to **NetRxQueueConfigureDmaAllocator**.

The client driver does not need to delete the common buffer. NetAdapterCx handles this on the driver's behalf.

NetAdapterCx allocates DMA common buffers and stores them in a [**NET\_RING\_BUFFER**](net-ring-buffer.md) structure. The client driver retrieves a pointer to the ring buffer by calling [**NetTxQueueGetRingBuffer**](nettxqueuegetringbuffer.md) and [**NetRxQueueGetRingBuffer**](netrxqueuegetringbuffer.md).

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
<td align="left">[Universal](http://go.microsoft.com/fwlink/p/?linkid=531356)</td>
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


[**NET\_RXQUEUE\_CONFIG**](net-rxqueue-config.md)

 

 






