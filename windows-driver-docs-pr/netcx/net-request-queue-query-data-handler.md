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

# NET\_REQUEST\_QUEUE\_QUERY\_DATA\_HANDLER structure


[!include[NetAdapterCx Beta Prerelease](../netcx-beta-prerelease.md)]

Call [NET\_REQUEST\_QUEUE\_QUERY\_DATA\_HANDLER\_INIT](net-request-queue-query-data-handler-init.md) to initialize this structure.

Syntax
------

```ManagedCPlusPlus
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

**Memory**  

**Oid**  

**EvtRequestQueryData**  
Pointer to the client driver's implementation of a [*EVT\_NET\_REQUEST\_QUERY\_DATA*](evt-net-request-query-data.md) event callback function.

**MinimumInputLength**  

**MinimumOutputLength**  

Remarks
-------
Call [**NET_REQUEST_QUEUE_QUERY_DATA_HANDLER_INIT**](net-request-queue-query-data-handler-init.md) to initialize this structure.

Call [**NET_REQUEST_QUEUE_CONFIG_ADD_INITIALIZED_QUERY_DATA_HANDLER**](net-request-queue-config-add-initialized-query-data-handler.md) to add a caller-provided custom request handler to a [**NET_REQUEST_QUEUE_CONFIG**](net-request-queue-config.md) structure.

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

 

 





