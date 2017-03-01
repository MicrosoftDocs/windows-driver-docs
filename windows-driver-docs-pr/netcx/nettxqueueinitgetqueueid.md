---
title: NetTxQueueInitGetQueueId method
topic_type:
- apiref
api_name:
- NetTxQueueInitGetQueueId
api_location:
- nettxqueue.h
api_type:
- HeaderDef
---

# NetTxQueueInitGetQueueId method

[!include[NetAdapterCx Beta Prerelease](../netcx-beta-prerelease.md)]

Retrieves the identifier associated with a transmit queue.

Syntax
------

```cpp
ULONG NetTxQueueInitGetQueueId(
  _In_ PNETTXQUEUE_INIT NetTxQueueInit
);
```

Parameters
----------

*NetTxQueueInit* [in]  
A pointer to a NetAdapterCx-allocated **NETTXQUEUE_INIT** structure.  For more information, see the Remarks section.

Return value
------------

Returns a ULONG that identifies a transmit queue.

Remarks
-----
The client driver receives a pointer to a NETTXQUEUE_INIT structure in its [EVT_NET_ADAPTER_CREATE_TXQUEUE](evt-net-adapter-create-txqueue.md) callback function.

Starting with zero, NetAdapterCx assigns an unique identifier value for each transmit queue that it creates.  The client driver specifies the number of transmit queues that the network adapter supports in the **NumTxQueues** member of the [NET_ADAPTER_DATAPATH_CAPABILITIES](net-adapter-datapath-capabilities.md) structure.  The client driver passes this structure to [**NetAdapterSetDataPathCapabilities**](netadaptersetdatapathcapabilities.md).  Identifier values range from zero to the value of **NumTxQueues** minus one.

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
<td align="left">Nettxqueue.h (include Netadaptercx.h)</td>
</tr>
<tr class="odd">
<td align="left"><p>IRQL</p></td>
<td align="left"><p>PASSIVE_LEVEL</p></td>
</tr>
</tbody>
</table>

 

 





