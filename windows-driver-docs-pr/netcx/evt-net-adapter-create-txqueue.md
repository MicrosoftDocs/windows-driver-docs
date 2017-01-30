---
title: EVT_NET_ADAPTER_CREATE_TXQUEUE callback function
description: The client driver's implementation of the EVT\_NET\_ADAPTER\_CREATE\_TXQUEUE event callback function that sets up a transmit queue.
ms.assetid: 6597b92f-9e32-428e-bf3c-b12d1fcf3834
keywords: ["EvtNetAdapterCreateTxqueue callback function Network Drivers Starting with Windows Vista", "EVT_NET_ADAPTER_CREATE_TXQUEUE", "PFN_NET_ADAPTER_CREATE_TXQUEUE callback function pointer Network Drivers Starting with Windows Vista"]
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

The client driver's implementation of the *EVT\_NET\_ADAPTER\_CREATE\_TXQUEUE* event callback function that sets up a transmit queue.

Syntax
------

```ManagedCPlusPlus
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

*Adapter* \[in\]  
The NDIS adapter object that the client created in a prior call to [**NetAdapterCreate**](netadaptercreate.md).

*TxQueueInit* \[in, out\]  
A pointer to a NetAdapterCx-allocated **NETTXQUEUE\_INIT** structure. For more information, see the Remarks section.

Return value
------------

If the operation is successful, the callback function must return STATUS\_SUCCESS, or another status value for which NT\_SUCCESS(status) equals TRUE. Otherwise, an appropriate [NTSTATUS](https://msdn.microsoft.com/library/windows/hardware/ff557697) error code.

Remarks
-------

To register an *EVT\_NET\_ADAPTER\_CREATE\_TXQUEUE* callback function, the client driver must call [**NetAdapterCreate**](netadaptercreate.md).

The **NETTXQUEUE\_INIT** structure is an opaque structure that is defined and allocated by NetAdapterCx, similar to [WDFDEVICE\_INIT](https://msdn.microsoft.com/library/windows/hardware/ff546951).

For example, the client driver would call [**NetTxQueueInitGetQueueId**](nettxqueueinitgetqueueid.md) with *NetTxQueueInit* to retrieve the identifier of the transmit queue to set up.

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
<td align="left">Netadapter.h</td>
</tr>
<tr class="odd">
<td align="left"><p>IRQL</p></td>
<td align="left"><p>PASSIVE_LEVEL</p></td>
</tr>
</tbody>
</table>

 

 





