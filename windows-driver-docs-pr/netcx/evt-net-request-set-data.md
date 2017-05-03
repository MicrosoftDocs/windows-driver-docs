---
title: EVT_NET_REQUEST_SET_DATA callback function
topic_type:
- apiref
api_name:
- PFN_NET_REQUEST_SET_DATA
api_location:
- netrequestqueue.h
api_type:
- UserDefined
---

# EVT_NET_REQUEST_SET_DATA callback function


[!include[NetAdapterCx Beta Prerelease](../netcx-beta-prerelease.md)]

Implemented by the client driver to handle a specific OID set data request.

Syntax
------

```cpp
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

Parameters
----------

*RequestQueue* [in]  
A handle to a net request queue object.

*Request* [in]  
A handle to a network request object.

*InputBuffer* [in]  
A pointer to a caller-supplied buffer.

*InputBufferLength* [in]  
The length, in bytes, of the request's input buffer, if an input buffer is available.

Return value
------------

This callback function does not return a value.

Remarks
---
Your client driver can provide one or more specialized handlers for specific OID query data requests.  In addition, it can also provide a generic *EVT_NET_REQUEST_DEFAULT_SET_DATA* callback function.

To register an *EVT_NET_REQUEST_DEFAULT_SET_DATA* callback function, the client driver calls **NET_REQUEST_QUEUE_CONFIG_ADD_SET_DATA_HANDLER** or [**NET_REQUEST_QUEUE_CONFIG_ADD_INITIALIZED_SET_DATA_HANDLER**](net-request-queue-config-add-initialized-set-data-handler.md), and then calls [**NetRequestQueueCreate**](netrequestqueuecreate.md).

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

 

 





