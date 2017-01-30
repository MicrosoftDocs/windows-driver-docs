---
title: NET_REQUEST_QUEUE_SET_DATA_HANDLER structure
description: Call NET\_REQUEST\_QUEUE\_SET\_DATA\_HANDLER\_INIT to initialize this structure.
ms.assetid: e3cd863a-f798-4841-af71-936515c7aab1
keywords: ["NET_REQUEST_QUEUE_SET_DATA_HANDLER structure Network Drivers Starting with Windows Vista", "PNET_REQUEST_QUEUE_SET_DATA_HANDLER structure pointer Network Drivers Starting with Windows Vista"]
topic_type:
- apiref
api_name:
- NET_REQUEST_QUEUE_SET_DATA_HANDLER
api_location:
- netrequestqueue.h
api_type:
- HeaderDef
---

# NET\_REQUEST\_QUEUE\_SET\_DATA\_HANDLER structure


[!include[NetAdapterCx Beta Prerelease](../netcx-beta-prerelease.md)]

Call [NET\_REQUEST\_QUEUE\_SET\_DATA\_HANDLER\_INIT](net-request-queue-set-data-handler-init.md) to initialize this structure.

Syntax
------

```ManagedCPlusPlus
typedef struct _NET_REQUEST_QUEUE_SET_DATA_HANDLER {
  PNET_REQUEST_QUEUE_SET_DATA_HANDLER Next;
  WDFMEMORY                           Memory;
  NDIS_OID                            Oid;
  PFN_NET_REQUEST_SET_DATA            EvtRequestSetData;
  UINT                                MinimumInputLength;
  UINT                                MinimumOutputLength;
} NET_REQUEST_QUEUE_SET_DATA_HANDLER, *PNET_REQUEST_QUEUE_SET_DATA_HANDLER;
```

Members
-------

**Next**  

**Memory**  

**Oid**  

**EvtRequestSetData**  
Pointer to the client driver's implementation of a [*EVT\_NET\_REQUEST\_SET\_DATA*](evt-net-request-set-data.md) event callback function.

**MinimumInputLength**  

**MinimumOutputLength**  

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

 

 





