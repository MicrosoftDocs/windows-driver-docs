---
title: EVT_NET_ADAPTER_CREATE_TXQUEUE callback function
topic_type:
- apiref
api_name:
- PFN_NET_ADAPTER_CREATE_TXQUEUE
api_location:
- netadapter.h
api_type:
- UserDefined
---

# EVT_NET_ADAPTER_CREATE_TXQUEUE callback function


[!include[NetAdapterCx Beta Prerelease](../netcx-beta-prerelease.md)]

The client driver's implementation of the *EVT_NET_ADAPTER_CREATE_TXQUEUE* event callback function that sets up a transmit queue.

Syntax
------

```cpp
EVT_NET_ADAPTER_CREATE_TXQUEUE EvtNetAdapterCreateTxqueue;

NTSTATUS EvtNetAdapterCreateTxqueue(
  _In_    NETADAPTER       Adapter,
  _Inout_ PNETTXQUEUE_INIT TxQueueInit
)
{ ... }

typedef EVT_NET_ADAPTER_CREATE_TXQUEUE PFN_NET_ADAPTER_CREATE_TXQUEUE;
```

Parameters
----------

*Adapter* [in]  
The network adapter object that the client created in a prior call to [**NetAdapterCreate**](netadaptercreate.md).

*TxQueueInit* [in, out]  
A pointer to a NetAdapterCx-allocated **NETTXQUEUE_INIT** structure. For more information, see the Remarks section.

Return value
------------

If the operation is successful, the callback function must return STATUS_SUCCESS, or another status value for which NT_SUCCESS(status) equals TRUE. Otherwise, an appropriate [NTSTATUS](https://msdn.microsoft.com/library/windows/hardware/ff557697) error code.

Remarks
-------

To register an *EVT_NET_ADAPTER_CREATE_TXQUEUE* callback function, the client driver must call [**NetAdapterCreate**](netadaptercreate.md).

The **NETTXQUEUE_INIT** structure is an opaque structure that is defined and allocated by NetAdapterCx, similar to [WDFDEVICE_INIT](https://msdn.microsoft.com/library/windows/hardware/ff546951).

In this callback, the client driver typically calls [**NetTxQueueInitGetQueueId**](nettxqueueinitgetqueueid.md) with *NetTxQueueInit* to retrieve the identifier of the transmit queue to set up.

Next, the client calls [**NetTxQueueCreate**](nettxqueuecreate.md) to allocate a queue.  If [**NetTxQueueCreate**](nettxqueuecreate.md) fails, the *EVT_NET_ADAPTER_CREATE_TXQUEUE* callback function should return an error code.

To retrieve the ring buffer associated with a given queue, call [**NetTxQueueGetRingBuffer**](nettxqueuegetringbuffer.md).

Example
-------

> [!TIP]
> This example transmit queue uses a driver-defined additonal packet context called MY_TCB to assist with transmit operations. For more info about setting up this example packet context and initializing it, see [NET_PACKET_CONTEXT_ATTRIBUTES_INIT_TYPE](net-packet-context-attributes-init-type.md).
>
> Error handling code has been excised from this example for brevity and clarity.

```cpp
NTSTATUS
EvtAdapterCreateTxQueue(
    _In_ NETADAPTER netAdapter,
    _Inout_ PNETTXQUEUE_INIT txQueueInit)
{
    NTSTATUS status = STATUS_SUCCESS;

    NET_TXQUEUE_CONFIG txConfig;
    NET_TXQUEUE_CONFIG_INIT(
        &txConfig,
        EvtTxQueueAdvance,
        EvtTxQueueSetNotificationEnabled,
        EvtTxQueueCancel);

    // Initialize the custom Transmit Control Block packet context

    NET_PACKET_CONTEXT_ATTRIBUTES packetContextAttributes;
    NET_PACKET_CONTEXT_ATTRIBUTES_INIT_TYPE(&packetContextAttributes, MY_TCB);

    // Add the TCB packet context to the queue

    status = NetTxQueueInitAddPacketContextAttributes(txQueueInit, &packetContextAttributes);

    // Create the transmit queue

    status = NetTxQueueCreate(
        txQueueInit,
        &txAttributes,
        &txConfig,
        &netAdapter->TxQueue);

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

 

 





