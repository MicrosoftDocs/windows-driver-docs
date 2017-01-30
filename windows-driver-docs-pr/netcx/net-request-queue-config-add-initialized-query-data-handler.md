---
title: NET_REQUEST_QUEUE_CONFIG_ADD_INITIALIZED_QUERY_DATA_HANDLER method
description: Adds a caller-provided query data handler to a NET\_REQUEST\_QUEUE\_CONFIG structure.
ms.assetid: 6495a861-cfdf-49c2-93ed-9f245d508e3b
keywords: ["NET_REQUEST_QUEUE_CONFIG_ADD_INITIALIZED_METHOD_HANDLER method Network Drivers Starting with Windows Vista"]
topic_type:
- apiref
api_name:
- NET_REQUEST_QUEUE_CONFIG_ADD_INITIALIZED_METHOD_HANDLER
api_location:
- netrequestqueue.h
api_type:
- HeaderDef
---

# NET\_REQUEST\_QUEUE\_CONFIG\_ADD\_INITIALIZED\_QUERY\_DATA\_HANDLER method


[!include[NetAdapterCx Beta Prerelease](../netcx-beta-prerelease.md)]

Adds a caller-provided query data handler to a [**NET\_REQUEST\_QUEUE\_CONFIG**](net-request-queue-config.md) structure.

Syntax
------

```ManagedCPlusPlus
FORCEINLINE VOID NET_REQUEST_QUEUE_CONFIG_ADD_INITIALIZED_METHOD_HANDLER(
  _In_ PNET_REQUEST_QUEUE_CONFIG             NetRequestQueueConfig,
  _In_ PNET_REQUEST_QUEUE_QUERY_DATA_HANDLER QueryDataHandler
);
```

Parameters
----------

*NetRequestQueueConfig* \[in\]  
A pointer to a driver-allocated [**NET\_REQUEST\_QUEUE\_CONFIG**](net-request-queue-config.md) structure to which the query data handler is being added.

*QueryDataHandler* \[in\]  
A pointer to a driver-allocated and initialized structure of type [**NET\_REQUEST\_QUEUE\_QUERY\_DATA\_HANDLER**](net-request-queue-query-data-handler.md).

Return value
------------

This method does not return a value.

Remarks
-------

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

## See also


[**NET\_REQUEST\_QUEUE\_CONFIG**](net-request-queue-config.md)

[**NET\_REQUEST\_QUEUE\_QUERY\_DATA\_HANDLER**](net-request-queue-query-data-handler.md)

 

 






