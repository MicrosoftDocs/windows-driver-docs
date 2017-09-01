---
title: NET_RXQUEUE_CONFIG structure
topic_type:
- apiref
api_name:
- NET_RXQUEUE_CONFIG
api_location:
- netrxqueue.h
api_type:
- HeaderDef
---

# NET_RXQUEUE_CONFIG structure

[!include[NetAdapterCx Beta Prerelease](../netcx-beta-prerelease.md)]

Describes the configuration options for a NetAdapterCx client driver's receive queue.

Syntax
------

```cpp
typedef struct _NET_RXQUEUE_CONFIG {
  ULONG                                Size;
  PFN_RXQUEUE_CANCEL                   EvtRxQueueCancel;
  PFN_RXQUEUE_SET_NOTIFICATION_ENABLED EvtRxQueueSetNotificationEnabled;
  PFN_RXQUEUE_ADVANCE                  EvtRxQueueAdvance;
  ULONG                                AllocationSize;
  ULONG                                AlignmentRequirement;
  ULONG                                RingBufferNumberOfElementsHint;
} NET_RXQUEUE_CONFIG, *PNET_RXQUEUE_CONFIG;
```

Members
-------

**Size**  
The size, in bytes, of this structure.

**EvtRxQueueCancel**  
A pointer to the client driver's [*EVT_RXQUEUE_CANCEL*](evt-rxqueue-cancel.md) event callback function. This callback function is required.

**EvtRxQueueSetNotificationEnabled**  
A pointer to the client driver's [*EVT_RXQUEUE_SET_NOTIFICATION_ENABLED*](evt-rxqueue-set-notification-enabled.md) event callback function. This callback function is required.

**EvtRxQueueAdvance**  
A pointer to the client driver's [*EVT_RXQUEUE_ADVANCE*](evt-rxqueue-advance.md) event callback function. This callback function is required.

**AllocationSize**  
Size of each receive buffer. If non-zero, NetAdapterCx allocates receive buffers for each packet in the queue's ring buffer. If the client initialized a [NET_RXQUEUE_DMA_ALLOCATOR_CONFIG](net-rxqueue-dma-allocator-config.md) structure by calling [NET_RXQUEUE_DMA_ALLOCATOR_CONFIG_INIT](net-rxqueue-dma-allocator-config-init.md), NetAdapterCx pre-maps virtual addresses in the receive buffers to fixed physical addresses. If zero, the client provides a receive buffer for each receive fragment.

**AlignmentRequirement**  
The alignment requirement, in bytes, for each receive buffer. This value must be one less than the alignment boundary. For example, specify 15 for a 16-byte alignment boundary. You can also use one of the FILE_Xxxx_ALIGNMENT constants that are defined in Wdm.h. If unspecified, **AlignmentRequirement** defaults to the value returned by [**WdfDeviceGetAlignmentRequirement**](https://msdn.microsoft.com/en-us/library/windows/hardware/ff545953) for the adapter's associated device object.

**RingBufferNumberOfElementsHint**  


Remarks
-------

Call [**NET_RXQUEUE_CONFIG_INIT**](net-rxqueue-config-init.md) to initialize this structure.

The **NET_RXQUEUE_CONFIG** structure is an input parameter to [**NetRxQueueCreate**](netrxqueuecreate.md). The client must use [**NET_RXQUEUE_CONFIG_INIT**](net-rxqueue-config-init.md) to initialize this structure.

In NetAdapterCx 1.1, the **ContextTypeInfo** member from version 1.0 was removed. The **RingBufferNumberOfElementsHint** member was added in version 1.1.

Requirements
------------

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p>Minimum KMDF version</p></td>
<td align="left"><p>1.21</p></td>
</tr>
<tr class="even">
<td align="left"><p>Minimum NetAdapterCx version</p></td>
<td align="left"><p>1.0</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Header</p></td>
<td align="left">Netrxqueue.h</td>
</tr>
</tbody>
</table>

## See also


[**NetRxQueueQueryAllocatorCacheEnabled**](netrxqueuequeryallocatorcacheenabled.md)

 

 






