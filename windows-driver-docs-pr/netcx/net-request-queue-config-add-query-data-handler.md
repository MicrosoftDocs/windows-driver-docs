---
title: NET_REQUEST_QUEUE_CONFIG_ADD_QUERY_DATA_HANDLER method
topic_type:
- apiref
api_name:
- NET_REQUEST_QUEUE_CONFIG_ADD_QUERY_DATA_HANDLER
api_location:
- netrequestqueue.h
api_type:
- HeaderDef
---

# NET_REQUEST_QUEUE_CONFIG_ADD_QUERY_DATA_HANDLER method


[!include[NetAdapterCx Beta Prerelease](../netcx-beta-prerelease.md)]

Adds a caller-provided handler for a specific OID query data request to a [**NET\_REQUEST\_QUEUE\_CONFIG**](net-request-queue-config.md) structure.

Syntax
------

```ManagedCPlusPlus
FORCEINLINE
VOID
NET_REQUEST_QUEUE_CONFIG_ADD_QUERY_DATA_HANDLER(
    _In_ PNET_REQUEST_QUEUE_CONFIG  NetRequestQueueConfig,
    _In_ NDIS_OID                   Oid,
    _In_ PFN_NET_REQUEST_QUERY_DATA EvtRequestQueryData,
    _In_ UINT                       MinimumOutputLength
)
```

Parameters
----------
*NetRequestQueueConfig* \[in\]  
A pointer to a driver-allocated [**NET\_REQUEST\_QUEUE\_CONFIG**](net-request-queue-config.md) structure to which the custom handler is being added.

*Oid* \[in\]  
The object identifier of the requested operation. The value is an OID\_ *XXX* code.

*EvtRequestQueryData* \[in\]
Pointer to the client driver's implementation of a [*EVT_NET_REQUEST_QUERY_DATA*](evt-net-request-query-data.md) event callback function.

*MinimumOutputLength*  \[in\]
A UINT specifying the minimum output length for the request.

Return value
------------

This method does not return a value.

Remarks
-------
When the client driver has finished adding custom handlers, it registers them with NetAdapterCx by calling [**NetRequestQueueCreate**](netrequestqueuecreate.md).

If the memory allocation for this method fails, the subsequent call to [**NetRequestQueueCreate**](netrequestqueuecreate.md) returns a failure code.

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

 

 





