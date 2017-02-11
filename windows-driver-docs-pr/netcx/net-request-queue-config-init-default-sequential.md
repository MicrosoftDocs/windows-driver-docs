---
title: NET_REQUEST_QUEUE_CONFIG_INIT_DEFAULT_SEQUENTIAL method
topic_type:
- apiref
api_name:
- NET_REQUEST_QUEUE_CONFIG_ADD_INITIALIZED_METHOD_HANDLER
api_location:
- netrequestqueue.h
api_type:
- HeaderDef
---

# NET_REQUEST_QUEUE_CONFIG_INIT_DEFAULT_SEQUENTIAL method


[!include[NetAdapterCx Beta Prerelease](../netcx-beta-prerelease.md)]

Initializes the caller-allocated [**NET_REQUEST_QUEUE_CONFIG**](net-request-queue-config.md) structure to create a default request queue.

Syntax
------

```ManagedCPlusPlus
FORCEINLINE VOID NET_REQUEST_QUEUE_CONFIG_ADD_INITIALIZED_METHOD_HANDLER(
  _Out_ PNET_REQUEST_QUEUE_CONFIG NetRequestQueueConfig,
  _In_  NETADAPTER                Adapter
);
```

Parameters
----------

*NetRequestQueueConfig* \[out\]  
A pointer to a driver-allocated [**NET_REQUEST_QUEUE_CONFIG**](net-request-queue-config.md) structure.

*Adapter* \[in\]  
The NDIS adapter object that the client created in a prior call to [**NetAdapterCreate**](netadaptercreate.md).

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

 

 





