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


\[Some information relates to pre-released product which may be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here.\]

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
A handle to a DMA enabler object that the client driver obtained from a previous call to [**WdfDmaEnablerCreate**](wdf-wdfdmaenablercreate).

Return value
------------

The method returns STATUS\_SUCCESS if the operation succeeds. Otherwise, this method may return an appropriate NTSTATUS error code.

Remarks
-------

The client driver can choose to let NetAdapterCx manage the receive buffer on its behalf. To opt in, the client driver must first specify the size of its desired common buffer by setting the **AllocationSize** and **AlignmentRequirement** members of [**NET\_RXQUEUE\_CONFIG**](net-rxqueue-config.md).

Typically, from its [*EVT\_NET\_ADAPTER\_CREATE\_RXQUEUE*](evt-net-adapter-create-rxqueue.md) event callback function, the client driver calls [**WdfDmaEnablerCreate**](wdf-wdfdmaenablercreate), and then passes the initialized WDFDMAENABLER to **NetRxQueueConfigureDmaAllocator**.

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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20NetRxQueueConfigureDmaAllocator%20method%20%20RELEASE:%20%281/19/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





