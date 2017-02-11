---
title: NET_REQUEST_QUEUE_METHOD_HANDLER_INIT method
topic_type:
- apiref
api_name:
- NET_REQUEST_QUEUE_METHOD_HANDLER_INIT
api_location:
- netrequestqueue.h
api_type:
- HeaderDef
---

# NET_REQUEST_QUEUE_METHOD_HANDLER_INIT method


[!include[NetAdapterCx Beta Prerelease](../netcx-beta-prerelease.md)]

Initializes the [NET_REQUEST_QUEUE_METHOD_HANDLER](net-request-queue-method-handler.md) structure.

Syntax
------

```ManagedCPlusPlus
__inline
void NET_REQUEST_QUEUE_METHOD_HANDLER_INIT(
  _Out_ PNET_REQUEST_QUEUE_METHOD_HANDLER MethodHandler,
  _In_  NDIS_OID                          Oid,
  _In_  PFN_NET_REQUEST_METHOD            EvtRequestMethod,
  _In_  UINT                              MinimumInputLength,
  _In_  UINT                              MinimumOutputLength
);
```

Parameters
----------

*MethodHandler* \[out\]  
A pointer to the driver-allocated NET_REQUEST_QUEUE_METHOD_HANDLER structure.

*Oid* \[in\]  
The NDIS_OID identifier for the request.

*EvtRequestMethod* \[in\]  
Pointer to the client driver's implementation of a [*EVT_NET_REQUEST_METHOD*](evt-net-request-method.md) event callback function.

*MinimumInputLength* \[in\]  
The needed minimum input length for the request.

*MinimumOutputLength* \[in\]  
The needed minimum output length for the request.

Return value
------------

This method does not return a value.

Requirements
------------

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p>Minimum supported client</p></td>
<td align="left"><p>Windows 10</p></td>
</tr>
<tr class="even">
<td align="left"><p>Minimum supported server</p></td>
<td align="left"><p>Windows Server 2016</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Header</p></td>
<td align="left">Netrequestqueue.h</td>
</tr>
<tr class="even">
<td align="left"><p>IRQL</p></td>
<td align="left"><p>PASSIVE_LEVEL</p></td>
</tr>
</tbody>
</table>

 

 





