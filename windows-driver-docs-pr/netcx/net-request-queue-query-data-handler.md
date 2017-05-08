---
title: NET_REQUEST_QUEUE_QUERY_DATA_HANDLER structure
topic_type:
- apiref
api_name:
- NET_REQUEST_QUEUE_QUERY_DATA_HANDLER
api_location:
- netrequestqueue.h
api_type:
- HeaderDef
---

# NET_REQUEST_QUEUE_QUERY_DATA_HANDLER structure

[!include[NetAdapterCx Beta Prerelease](../netcx-beta-prerelease.md)]

Reserved for internal use.  Call [**NET_REQUEST_QUEUE_CONFIG_ADD_QUERY_DATA_HANDLER**](net-request-queue-config-add-query-data-handler.md) to add a caller-provided handler for a specific OID query data request.

Syntax
------

```cpp
typedef struct _NET_REQUEST_QUEUE_QUERY_DATA_HANDLER {
  PNET_REQUEST_QUEUE_QUERY_DATA_HANDLER Next;
  WDFMEMORY                             Memory;
  NDIS_OID                              Oid;
  PFN_NET_REQUEST_QUERY_DATA            EvtRequestQueryData;
  UINT                                  MinimumInputLength;
  UINT                                  MinimumOutputLength;
} NET_REQUEST_QUEUE_QUERY_DATA_HANDLER, *PNET_REQUEST_QUEUE_QUERY_DATA_HANDLER;
```

Members
-------

**Next**  
A pointer to the next custom handler.

**Memory**  
Reserved for internal use.

**Oid**  
Specifies the object identifier of the requested operation. The value is an OID_XXX code. 

**EvtRequestQueryData**  
Pointer to the client driver's implementation of a [*EVT_NET_REQUEST_QUERY_DATA*](evt-net-request-query-data.md) event callback function.

**MinimumInputLength**  
Minimum input length needed by the client for this request.

**MinimumOutputLength**  
Minimum output length needed by the client for this request.

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

 

 





