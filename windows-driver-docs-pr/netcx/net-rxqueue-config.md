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
  PCNET_CONTEXT_TYPE_INFO              ContextTypeInfo;
  ULONG                                AllocationSize;
  ULONG                                AlignmentRequirement;
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

**ContextTypeInfo**  
A pointer to a [**WDF_OBJECT_CONTEXT_TYPE_INFO**](https://msdn.microsoft.com/library/windows/hardware/ff552407) structure.

**AllocationSize**  
Size of each receive buffer. If the driver provides a non-zero value, receive buffers will be allocated on behalf of the client for each packet in the queue's ring buffer. If the queue provides a DMA enabler via [**NetRxQueueConfigureDmaAllocator**](netrxqueueconfiguredmaallocator.md), these receive buffers will be pre-mapped for the device. If **AllocationSize** is zero, the client must fill out each receive fragment with its own receive buffer.

**AlignmentRequirement**  
The alignment requirement for each receive buffer. This value must be one less than the alignment boundary. For example, 15 should be specified for a 16-byte alignment boundary and 31 for a 32-byte alignment boundary. You can also use one of the FILE_Xxxx_ALIGNMENT constants that are defined in Wdm.h. If unspecified, AlignmentRequirement defaults to the value returned by [**WdfDeviceGetAlignmentRequirement**](https://msdn.microsoft.com/en-us/library/windows/hardware/ff545953) for the adapter's associated device object.

Remarks
-------

Call [**NET_RXQUEUE_CONFIG_INIT**](net-rxqueue-config-init.md) to initialize this structure.

The **NET_RXQUEUE_CONFIG** structure is an input parameter to [**NetRxQueueCreate**](netrxqueuecreate.md). The client must use [**NET_RXQUEUE_CONFIG_INIT**](net-rxqueue-config-init.md) to initialize this structure.

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


[**NetRxQueueConfigureDmaAllocator**](netrxqueueconfiguredmaallocator.md)

 

 






