---
title: EVT_NET_REQUEST_DEFAULT_QUERY_DATA callback function
topic_type:
- apiref
api_name:
- PFN_NET_REQUEST_DEFAULT_QUERY_DATA
api_location:
- netrequestqueue.h
api_type:
- UserDefined
---

# EVT_NET_REQUEST_DEFAULT_QUERY_DATA callback function


[!include[NetAdapterCx Beta Prerelease](../netcx-beta-prerelease.md)]

Implemented by the client driver as the default handler for object identifier (OID) requests of type query data.

Syntax
------

```cpp
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

Register your implementation of this callback function by setting the appropriate member of [**NET_REQUEST_QUEUE_CONFIG**](net-request-queue-config.md) and then calling [**NetRequestQueueCreate**](netrequestqueuecreate.md).

Parameters
----------

*RequestQueue* [in]  
A handle to a net request queue object.

*Request* [in]  
A handle to a network request object.

*Oid* [in]  
The object identifier of the requested operation. The value is an OID_ *XXX* code.

*OutputBuffer* [out]  
A pointer to a caller-supplied buffer.

*OutputBufferLength* [in]  
The length, in bytes, of the request's output buffer, if an output buffer is available.

Return value
------------

This callback function does not return a value.

Remarks
---
To register an *EVT_NET_REQUEST_DEFAULT_QUERY_DATA* callback function, the client driver calls [**NetRequestQueueCreate**](netrequestqueuecreate.md).

NetAdapterCx calls the client driver's *EVT_NET_REQUEST_DEFAULT_QUERY_DATA* handler when it receives an OID query data request for which the client driver has not provided a specialized *EVT_NET_REQUEST_QUERY_DATA* handler.

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

 

 





