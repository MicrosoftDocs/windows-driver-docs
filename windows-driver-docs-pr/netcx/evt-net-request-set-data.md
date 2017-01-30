---
title: EVT_NET_REQUEST_SET_DATA callback function
description: Implemented by the client driver to ... set handler callback.
ms.assetid: 1286c19b-ef24-4eaa-85f5-8049c864c3f7
keywords: ["EvtNetRequestSetData callback function Network Drivers Starting with Windows Vista", "EVT_NET_REQUEST_SET_DATA", "PFN_NET_REQUEST_SET_DATA callback function pointer Network Drivers Starting with Windows Vista"]
topic_type:
- apiref
api_name:
- PFN_NET_REQUEST_SET_DATA
api_location:
- netrequestqueue.h
api_type:
- UserDefined
---

# EVT\_NET\_REQUEST\_SET\_DATA callback function


[!include[NetAdapterCx Beta Prerelease](../netcx-beta-prerelease.md)]

Implemented by the client driver to ... custom set handler callback

Syntax
------

```ManagedCPlusPlus
EVT_NET_REQUEST_SET_DATA EvtNetRequestSetData;

void EvtNetRequestSetData(
  _In_ NETREQUESTQUEUE RequestQueue,
  _In_ NETREQUEST      Request,
  _In_ PVOID           InputBuffer,
  _In_ UINT            InputBufferLength
)
{ ... }

typedef EVT_NET_REQUEST_SET_DATA PFN_NET_REQUEST_SET_DATA;
```

Register your implementation of this callback function by setting the appropriate member of [**NET\_REQUEST\_QUEUE\_SET\_DATA\_HANDLER**](net-request-queue-set-data-handler.md) and then calling [**NET\_REQUEST\_QUEUE\_SET\_DATA\_HANDLER\_INIT**](net-request-queue-set-data-handler-init.md).

Parameters
----------

*RequestQueue* \[in\]  

*Request* \[in\]  

*InputBuffer* \[in\]  

*InputBufferLength* \[in\]  

Return value
------------

This callback function does not return a value.

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
<td align="left">Netrequestqueue.h</td>
</tr>
<tr class="odd">
<td align="left"><p>IRQL</p></td>
<td align="left"><p>PASSIVE_LEVEL</p></td>
</tr>
</tbody>
</table>

 

 





