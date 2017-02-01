---
title: EVT_NET_REQUEST_DEFAULT_QUERY_DATA callback function
description: Implemented by the client driver to ... handler for query OIDs.
ms.assetid: 48211125-072e-49ac-a9d6-c81503ae1370
keywords: ["EvtNetRequestDefaultQueryData callback function Network Drivers Starting with Windows Vista", "EVT_NET_REQUEST_DEFAULT_QUERY_DATA", "PFN_NET_REQUEST_DEFAULT_QUERY_DATA callback function pointer Network Drivers Starting with Windows Vista"]
topic_type:
- apiref
api_name:
- PFN_NET_REQUEST_DEFAULT_QUERY_DATA
api_location:
- netrequestqueue.h
api_type:
- UserDefined
---

# EVT\_NET\_REQUEST\_DEFAULT\_QUERY\_DATA callback function


[!include[NetAdapterCx Beta Prerelease](../netcx-beta-prerelease.md)]

Implemented by the client driver to ... handler for query OIDs

Syntax
------

```ManagedCPlusPlus
EVT_NET_REQUEST_DEFAULT_QUERY_DATA EvtNetRequestDefaultQueryData;

void EvtNetRequestDefaultQueryData(
  _In_  NETREQUESTQUEUE RequestQueue,
  _In_  NETREQUEST      Request,
  _In_  NDIS_OID        Oid,
  _Out_ PVOID           OutputBuffer,
  _In_  UINT            OutputBufferLength
)
{ ... }

typedef EVT_NET_REQUEST_DEFAULT_QUERY_DATA PFN_NET_REQUEST_DEFAULT_QUERY_DATA;
```

Register your implementation of this callback function by setting the appropriate member of [**NET\_REQUEST\_QUEUE\_CONFIG**](net-request-queue-config.md) and then calling [**NetRequestQueueCreate**](netrequestqueuecreate.md).

Parameters
----------

*RequestQueue* \[in\]  

*Request* \[in\]  

*Oid* \[in\]  

*OutputBuffer* \[out\]  

*OutputBufferLength* \[in\]  

Return value
------------

This callback function does not return a value.

Remarks
---
To register an *EVT\_NET\_REQUEST\_DEFAULT* callback function, the client driver calls [**NetRequestQueueCreate**](netrequestqueuecreate.md).

If NDIS_REQUEST_TYPE is not query, set, or method, NetAdapterCx calls the client driver's EVT_NET_REQUEST_DEFAULT handler with the request. If the client driver has not provided this callback, the request fails.

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

 

 





