---
title: NET_REQUEST_QUEUE_METHOD_HANDLER structure
description: Call NET\_REQUEST\_QUEUE\_METHOD\_HANDLER\_INIT to initialize this structure.
ms.assetid: f088cead-48e8-4c53-8178-e6408c387389
keywords: ["NET_REQUEST_QUEUE_METHOD_HANDLER structure Network Drivers Starting with Windows Vista", "PNET_REQUEST_QUEUE_METHOD_HANDLER structure pointer Network Drivers Starting with Windows Vista"]
topic_type:
- apiref
api_name:
- NET_REQUEST_QUEUE_METHOD_HANDLER
api_location:
- netrequestqueue.h
api_type:
- HeaderDef
---

# NET\_REQUEST\_QUEUE\_METHOD\_HANDLER structure


[!include[NetAdapterCx Beta Prerelease](../netcx-beta-prerelease.md)]

Call [NET\_REQUEST\_QUEUE\_METHOD\_HANDLER\_INIT](net-request-queue-method-handler-init.md) to initialize this structure.

Syntax
------

```ManagedCPlusPlus
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
Pointer to the Next Custom Handler

**Memory**  
The WDFMEMORY object backing this memory

**Oid**  
The Request Identifiver

**EvtRequestMethod**  
Pointer to the client driver's implementation of a [*EVT\_NET\_REQUEST\_METHOD*](evt-net-request-method.md) event callback function.

**MinimumInputLength**  
Minimum input length needed by the client for this request.

**MinimumOutputLength**  
Minimum output length needed by the client for this request.

Remarks
-------

Call [**NET\_REQUEST\_QUEUE\_METHOD\_HANDLER\_INIT**](net-request-queue-method-handler-init.md) to initialize this structure.

Call [**NET\_REQUEST\_QUEUE\_CONFIG\_ADD\_INITIALIZED\_METHOD\_HANDLER**](net-request-queue-config-add-initialized-method-handler.md) to add a caller-provided custom request handler to a [**NET\_REQUEST\_QUEUE\_CONFIG**](net-request-queue-config.md) structure.

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

 

 





