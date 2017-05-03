---
title: NET_REQUEST_QUEUE_METHOD_HANDLER structure
topic_type:
- apiref
api_name:
- NET_REQUEST_QUEUE_METHOD_HANDLER
api_location:
- netrequestqueue.h
api_type:
- HeaderDef
---

# NET_REQUEST_QUEUE_METHOD_HANDLER structure

[!include[NetAdapterCx Beta Prerelease](../netcx-beta-prerelease.md)]

Call [NET_REQUEST_QUEUE_METHOD_HANDLER_INIT](net-request-queue-method-handler-init.md) to initialize this structure.

Syntax
------

```cpp
typedef struct _NET_REQUEST_QUEUE_METHOD_HANDLER {
  PNET_REQUEST_QUEUE_METHOD_HANDLER Next;
  WDFMEMORY                         Memory;
  NDIS_OID                          Oid;
  PFN_NET_REQUEST_METHOD            EvtRequestMethod;
  UINT                              MinimumInputLength;
  UINT                              MinimumOutputLength;
} NET_REQUEST_QUEUE_METHOD_HANDLER, *PNET_REQUEST_QUEUE_METHOD_HANDLER;
```

Members
-------

**Next**  
A pointer to the next custom handler.

**Memory**  
A handle to a WDFMEMORY object backing this memory.

**Oid**  
Specifies the object identifier of the requested operation. The value is an OID_XXX code. 

**EvtRequestMethod**  
Pointer to the client driver's implementation of a [*EVT_NET_REQUEST_METHOD*](evt-net-request-method.md) event callback function.

**MinimumInputLength**  
Minimum input length needed by the client for this request.

**MinimumOutputLength**  
Minimum output length needed by the client for this request.

Remarks
-------
The client driver must call [**NET_REQUEST_QUEUE_METHOD_HANDLER_INIT**](net-request-queue-method-handler-init.md) to initialize this structure.

Call [**NET_REQUEST_QUEUE_CONFIG_ADD_INITIALIZED_METHOD_HANDLER**](net-request-queue-config-add-initialized-method-handler.md) to add a caller-provided custom request handler to a [**NET_REQUEST_QUEUE_CONFIG**](net-request-queue-config.md) structure.

Requirements
------------

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p>Minimum KMDF version</p></td>
<td align="left"><p>1.21</p></td>
</tr>
<tr class="even">
<td align="left"><p>Minimum NetAdapterCx version</p></td>
<td align="left"><p>1.0</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Header</p></td>
<td align="left">Netrequestqueue.h</td>
</tr>
</tbody>
</table>

 

 





