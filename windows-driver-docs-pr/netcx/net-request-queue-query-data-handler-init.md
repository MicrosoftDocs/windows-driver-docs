---
title: NET_REQUEST_QUEUE_QUERY_DATA_HANDLER_INIT method
description: Initializes the NET\_REQUEST\_QUEUE\_QUERY\_DATA\_HANDLER structure.
ms.assetid: d766afb0-46aa-4d79-8a40-c23c0e014d68
keywords: ["NET_REQUEST_QUEUE_QUERY_DATA_HANDLER_INIT method Network Drivers Starting with Windows Vista"]
topic_type:
- apiref
api_name:
- NET_REQUEST_QUEUE_QUERY_DATA_HANDLER_INIT
api_location:
- netrequestqueue.h
api_type:
- HeaderDef
---

# NET\_REQUEST\_QUEUE\_QUERY\_DATA\_HANDLER\_INIT method


[!include[NetAdapterCx Beta Prerelease](../netcx-beta-prerelease.md)]

Initializes the [NET\_REQUEST\_QUEUE\_QUERY\_DATA\_HANDLER](net-request-queue-query-data-handler.md) structure.

Syntax
------

```ManagedCPlusPlus
__inline
void NET_REQUEST_QUEUE_QUERY_DATA_HANDLER_INIT(
  _Out_ PNET_REQUEST_QUEUE_QUERY_DATA_HANDLER QueryDataHandler,
  _In_  NDIS_OID                              Oid,
  _In_  PFN_NET_REQUEST_QUERY_DATA            EvtRequestQueryData,
  _In_  UINT                                  MinimumOutputLength
);
```

Parameters
----------

*QueryDataHandler* \[out\]  
A pointer to the driver-allocated NET\_REQUEST\_QUEUE\_QUERY\_DATA\_HANDLER structure.

*Oid* \[in\]  
The NDIS\_OID identifier for the request.

*EvtRequestQueryData* \[in\]  
Pointer to the custom query request handler.

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

 

 





