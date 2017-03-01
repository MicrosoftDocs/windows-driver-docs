---
title: EVT_NET_REQUEST_METHOD callback function
topic_type:
- apiref
api_name:
- PFN_NET_REQUEST_METHOD
api_location:
- netrequestqueue.h
api_type:
- UserDefined
---

# EVT_NET_REQUEST_METHOD callback function

[!include[NetAdapterCx Beta Prerelease](../netcx-beta-prerelease.md)]

Implemented by the client driver to handle a specific OID method request.

Syntax
------

```cpp
EVT_NET_REQUEST_METHOD EvtNetRequestMethod;

VOID EvtNetRequestMethod(
  _In_  NETREQUESTQUEUE RequestQueue,
  _In_  NETREQUEST      Request,
  _Out_ PVOID           InputOutputBuffer,
  _In_  UINT            InputBufferLength,
  _In_  UINT            OutputBufferLength
)
{ ... }

typedef EVT_NET_REQUEST_METHOD PFN_NET_REQUEST_METHOD;
```

Parameters
----------

*RequestQueue* [in]  
A handle to a net request queue object.

*Request* [in]  
A handle to a network request object.

*InputOutputBuffer* [out]  
A pointer to a buffer into which the client driver or NetAdapterCx returns information for the specified request.

*InputBufferLength* [in]  
The length, in bytes, of the request's input buffer, if an input buffer is available.

*OutputBufferLength* [in]  
The length, in bytes, of the request's output buffer, if an output buffer is available.

Return value
------------

If the operation is successful, the callback function must return STATUS_SUCCESS, or another status value for which NT_SUCCESS(status) equals TRUE. Otherwise, an appropriate [NTSTATUS](https://msdn.microsoft.com/library/windows/hardware/ff557697) error code.

Remarks
---
Your client driver can provide one or more specialized handlers for specific OID method requests, or it can provide a single generic EVT_NET_REQUEST_DEFAULT_METHOD callback function.

To register an *EVT_NET_REQUEST_DEFAULT_METHOD* callback function, the client driver calls **NET_REQUEST_QUEUE_CONFIG_ADD_METHOD_HANDLER** or [**NET_REQUEST_QUEUE_CONFIG_ADD_INITIALIZED_METHOD_HANDLER**](net-request-queue-config-add-initialized-method-handler.md), and then calls [**NetRequestQueueCreate**](netrequestqueuecreate.md).

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

 

 





