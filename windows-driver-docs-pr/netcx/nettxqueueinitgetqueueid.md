---
title: NetTxQueueInitGetQueueId method
description: .
ms.assetid: 73d29f02-9f2c-42b1-8c1d-53aa8c60f3ab
keywords: ["NetTxQueueInitGetQueueId method Network Drivers Starting with Windows Vista"]
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

Syntax
------

```ManagedCPlusPlus
ULONG NetTxQueueInitGetQueueId(
  _In_ PNETTXQUEUE_INIT NetTxQueueInit
);
```

Parameters
----------

*NetTxQueueInit* \[in\]  

Return value
------------

A ULONG that...

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

 

 





