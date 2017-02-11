---
title: NetRxQueueInitGetQueueId method
topic_type:
- apiref
api_name:
- NetRxQueueInitGetQueueId
api_location:
- netrxqueue.h
api_type:
- HeaderDef
---

# NetRxQueueInitGetQueueId method

[!include[NetAdapterCx Beta Prerelease](../netcx-beta-prerelease.md)]

Retrieves the identifier of the receive queue associated with a receive queue.

Syntax
------

```ManagedCPlusPlus
ULONG NetRxQueueInitGetQueueId(
  _In_ PNETRXQUEUE_INIT NetRxQueueInit
);
```

Parameters
----------

*NetRxQueueInit* \[in\]  
A pointer to a NetAdapterCx-allocated **NETRXQUEUE_INIT** structure. For more information, see the Remarks section.

Return value
------------

Returns a ULONG that identifies a receive queue.

Remarks
---
The client driver receives a pointer to a NETRXQUEUE_INIT structure in its [EVT_NET_ADAPTER_CREATE_RXQUEUE](evt-net-adapter-create-rxqueue.md) callback function.

Starting with zero, NetAdapterCx assigns an unique identifier value for each receive queue that it creates.  The client driver specifies the number of receive queues that the network adapter supports in the **NumRxQueues** member of the [NET_ADAPTER_DATAPATH_CAPABILITIES](net-adapter-datapath-capabilities.md) structure.  The client driver passes this structure to [**NetAdapterSetDataPathCapabilities**](netadaptersetdatapathcapabilities.md).  Identifier values range from zero to the value of **NumRxQueues** minus one.

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
<td align="left">Netrxqueue.h (include Netadaptercx.h)</td>
</tr>
<tr class="odd">
<td align="left"><p>IRQL</p></td>
<td align="left"><p>PASSIVE_LEVEL</p></td>
</tr>
</tbody>
</table>

 

 





