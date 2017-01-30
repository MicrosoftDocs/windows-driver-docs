---
title: NetTxQueueCreate method
description: Creates a net transmit queue object.
ms.assetid: 6b360b14-d104-4ffd-b0ef-e45cfa2b3ab2
keywords: ["NetTxQueueCreate method Network Drivers Starting with Windows Vista"]
topic_type:
- apiref
api_name:
- NetTxQueueCreate
api_location:
- nettxqueue.h
api_type:
- HeaderDef
---

# NetTxQueueCreate method


[!include[NetAdapterCx Beta Prerelease](../netcx-beta-prerelease.md)]

Creates a net transmit queue object.

Syntax
------

```ManagedCPlusPlus
NTSTATUS NetTxQueueCreate(
  _Inout_ PNETTXQUEUE_INIT       NetTxQueueInit,
  _In_    PWDF_OBJECT_ATTRIBUTES TxQueueAttributes,
  _In_    PNET_TXQUEUE_CONFIG    Configuration,
  _Out_   NETTXQUEUE             *TxQueue
);
```

Parameters
----------

*NetTxQueueInit* \[in, out\]  
A pointer to the **NETTXQUEUE\_INIT** structure that the client driver received in [*EVT\_NET\_ADAPTER\_CREATE\_TXQUEUE*](evt-net-adapter-create-txqueue.md).

*TxQueueAttributes* \[in\]  
A pointer to caller-allocated [**WDF\_OBJECT\_ATTRIBUTES**](https://msdn.microsoft.com/library/windows/hardware/ff552400) structure. The structure’s **ParentObject** must be NULL. The parameter is optional and can be WDF\_NO\_OBJECT\_ATTRIBUTES.

*Configuration* \[in\]  
A pointer to a caller-allocated [**NET\_TXQUEUE\_CONFIG**](net-txqueue-config.md) structure.

*TxQueue* \[out\]  
A pointer to a location that receives a handle to the new net receive queue object.

Return value
------------

The method returns STATUS\_SUCCESS if the operation succeeds. Otherwise, this method may return an appropriate NTSTATUS error code.

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
<td align="left">Nettxqueue.h (include Netadaptercx.h)</td>
</tr>
<tr class="odd">
<td align="left"><p>IRQL</p></td>
<td align="left"><p>PASSIVE_LEVEL</p></td>
</tr>
</tbody>
</table>

 

 





