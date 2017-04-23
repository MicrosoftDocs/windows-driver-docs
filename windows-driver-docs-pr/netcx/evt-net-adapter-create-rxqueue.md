---
title: EVT_NET_ADAPTER_CREATE_RXQUEUE callback function
topic_type:
- apiref
api_name:
- PFN_NET_ADAPTER_CREATE_RXQUEUE
api_location:
- netadapter.h
api_type:
- UserDefined
---

# EVT_NET_ADAPTER_CREATE_RXQUEUE callback function


[!include[NetAdapterCx Beta Prerelease](../netcx-beta-prerelease.md)]

The client driver's implementation of the *EVT_NET_ADAPTER_CREATE_RXQUEUE* event callback function that sets up a receive queue.

Syntax
------

```cpp
EVT_NET_ADAPTER_CREATE_RXQUEUE EvtNetAdapterCreateRxqueue;

NTSTATUS EvtNetAdapterCreateRxqueue(
  _In_    NETADAPTER       Adapter,
  _Inout_ PNETRXQUEUE_INIT RxQueueInit
)
{ ... }

typedef EVT_NET_ADAPTER_CREATE_RXQUEUE PFN_NET_ADAPTER_CREATE_RXQUEUE;
```

Parameters
----------

*Adapter* [in]  
The NetAdapter object that was created by [**NetAdapterCreate**](netadaptercreate.md).

*RxQueueInit* [in, out]  
A pointer to a NetAdapterCx-allocated **NETRXQUEUE_INIT** structure. For more information, see the Remarks section.

Return value
------------

If the operation is successful, the callback function must return STATUS_SUCCESS, or another status value for which NT_SUCCESS(status) equals TRUE. Otherwise, an appropriate [NTSTATUS](https://msdn.microsoft.com/library/windows/hardware/ff557697) error code.

Remarks
-------

To register an *EVT_NET_ADAPTER_CREATE_RXQUEUE* callback function, the client driver must call [**NetAdapterCreate**](netadaptercreate.md).

The **NETRXQUEUE_INIT** structure is an opaque structure that is defined and allocated by NetAdapterCx, similar to [WDFDEVICE_INIT](https://msdn.microsoft.com/library/windows/hardware/ff546951).

In this callback, the client driver might call [**NetRxQueueInitGetQueueId**](netrxqueueinitgetqueueid.md) to retrieve the identifier of the receive queue to set up.

The NetRxQueue's ring buffer is allocated in NetRxQueueCreate, so it can be retrieved via [**NetRxQueueGetRingBuffer**](netrxqueuegetringbuffer.md) after queue creation. You can use this as an opportunity to allocate any per-packet resources.

If AllocationSize is specified, the receive buffers are not allocated until after this function returns.

Example
-----

```cpp
NTSTATUS
EvtAdapterCreateRxQueue(
    _In_ NETADAPTER netAdapter,
    _Inout_ PNETRXQUEUE_INIT rxQueueInit)
{
    NTSTATUS status = STATUS_SUCCESS;

    NET_RXQUEUE_CONFIG rxConfig;
    NET_RXQUEUE_CONFIG_INIT(
        &rxConfig,
        EvtRxQueueAdvance,
        EvtRxQueueSetNotificationEnabled,
        EvtRxQueueCancel);

    // Specify buffer size required per packet so the OS can preallocate

    rxConfig.AlignmentRequirement = 64;
    rxConfig.AllocationSize = NIC_MAX_PACKET_SIZE + FRAME_CRC_SIZE + RSVD_BUF_SIZE;

    // Assign fixed size data type as per packet context

    NET_RXQUEUE_CONFIG_SET_DEFAULT_PACKET_CONTEXT_TYPE(&rxConfig, MY_RXQUEUE_PACKET_CONTEXT);

    NTSTATUS status = NetRxQueueCreate(
        rxQueueInit,
        &rxAttributes,
        &rxConfig,
        &adapter->RxQueue);

    // Specify that the OS use a WDFDMAENABLER to allocate the receive buffers

    status = NetRxQueueConfigureDmaAllocator(
        adapter->RxQueue,
        adapter->DmaEnabler);

     return status;
}
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
<td align="left">NetAdapter.h</td>
</tr>
<tr class="odd">
<td align="left"><p>IRQL</p></td>
<td align="left"><p>PASSIVE_LEVEL</p></td>
</tr>
</tbody>
</table>

 

 





