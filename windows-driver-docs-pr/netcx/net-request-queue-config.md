---
title: NET_REQUEST_QUEUE_CONFIG structure
description: Call NET\_REQUEST\_QUEUE\_CONFIG\_INIT to initialize this structure.
ms.assetid: 16c23905-7192-4ab0-9eab-f3a6c39ed3d5
keywords: ["NET_REQUEST_QUEUE_CONFIG structure Network Drivers Starting with Windows Vista", "PNET_REQUEST_QUEUE_CONFIG structure pointer Network Drivers Starting with Windows Vista"]
topic_type:
- apiref
api_name:
- NET_REQUEST_QUEUE_CONFIG
api_location:
- netrequestqueue.h
api_type:
- HeaderDef
---

# NET\_REQUEST\_QUEUE\_CONFIG structure


[!include[NetAdapterCx Beta Prerelease](../netcx-beta-prerelease.md)]

Call [NET\_REQUEST\_QUEUE\_CONFIG\_INIT](net-request-queue-config-init.md) to initialize this structure.

Syntax
------

```ManagedCPlusPlus
typedef struct _NET_REQUEST_QUEUE_CONFIG {
  ULONG                                   Size;
  NETADAPTER                              Adapter;
  NET_REQUEST_QUEUE_TYPE                  Type;
  PFN_NET_REQUEST_DEFAULT_SET_DATA        EvtRequestDefaultSetData;
  PFN_NET_REQUEST_DEFAULT_QUERY_DATA      EvtRequestDefaultQueryData;
  PFN_NET_REQUEST_DEFAULT_METHOD          EvtRequestDefaultMethod;
  PFN_NET_REQUEST_DEFAULT                 EvtRequestDefault;
  NET_REQUEST_QUEUE_ADD_HANDLER_ERROR     AddHandlerError;
  ULONG                                   SizeOfSetDataHandler;
  ULONG                                   SizeOfQueryDataHandler;
  ULONG                                   SizeOfMethodHandler;
  PNET_REQUEST_QUEUE_SET_DATA_HANDLER     SetDataHandlers;
  PNET_REQUEST_QUEUE_QUERY_DATA_HANDLER   QueryDataHandlers;
  PNET_REQUEST_QUEUE_METHOD_HANDLER       MethodHandlers;
} NET_REQUEST_QUEUE_CONFIG, *PNET_REQUEST_QUEUE_CONFIG;
```

Members
-------

**Size**  
Size of the structure.

**Adapter**  
The NDIS adapter object that the client created in a prior call to [**NetAdapterCreate**](netadaptercreate.md).

**Type**  
A [NET_REQUEST_QUEUE_TYPE](net-request-queue-type.md) enumeration that specifies the type of queue.

**EvtRequestDefaultSetData**  
Pointer to the client driver's implementation of a [*EVT\_NET\_REQUEST\_DEFAULT\_SET\_DATA*](evt-net-request-default-set-data.md) event callback function.

**EvtRequestDefaultQueryData**  
Pointer to the client driver's implementation of a [*EVT\_NET\_REQUEST\_DEFAULT\_QUERY\_DATA*](evt-net-request-default-query-data.md) event callback function.

**EvtRequestDefaultMethod**  
Pointer to the client driver's implementation of a [*EVT\_NET\_REQUEST\_DEFAULT\_METHOD*](evt-net-request-default-method.md) event callback function.

**EvtRequestDefault**  
Pointer to the client driver's implementation of a [*EVT\_NET\_REQUEST\_DEFAULT*](evt-net-request-default.md) event callback function.

**AddHandlerError**  
A bit field tracking any errors encountered during Add custom handler operation.

**SizeOfSetDataHandler**  
A ULONG that specifies the size of the SetDataHandlers member.

**SizeOfQueryDataHandler**  
A ULONG that specifies the size of the QueryDataHandlers member.

**SizeOfMethodHandler**  
A ULONG that specifies the size of the MethodHandlers member.

**SetDataHandlers**  
Pointer to the first [**NET\_REQUEST\_QUEUE\_SET\_DATA\_HANDLER**](net-request-queue-set-data-handler.md) structure of the custom set handler list.

**QueryDataHandlers**  
Pointer to a [**NET\_REQUEST\_QUEUE\_QUERY\_DATA\_HANDLER**](net-request-queue-query-data-handler.md) structure of the custom query handler list.

**MethodHandlers**  
Pointer to a [**NET\_REQUEST\_QUEUE\_METHOD\_HANDLER**](net-request-queue-method-handler.md) structure of the custom method handler list.

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

 

 





