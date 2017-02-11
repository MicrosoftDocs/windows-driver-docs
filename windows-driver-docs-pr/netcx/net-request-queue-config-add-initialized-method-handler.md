---
title: NET_REQUEST_QUEUE_CONFIG_ADD_INITIALIZED_METHOD_HANDLER method
topic_type:
- apiref
api_name:
- NET_REQUEST_QUEUE_CONFIG_ADD_INITIALIZED_METHOD_HANDLER
api_location:
- netrequestqueue.h
api_type:
- HeaderDef
---

# NET\_REQUEST\_QUEUE\_CONFIG\_ADD\_INITIALIZED\_METHOD\_HANDLER method


[!include[NetAdapterCx Beta Prerelease](../netcx-beta-prerelease.md)]

Adds a pre-initialized custom request handler structure to a [**NET\_REQUEST\_QUEUE\_CONFIG**](net-request-queue-config.md) structure.

Syntax
------

```ManagedCPlusPlus
FORCEINLINE VOID NET_REQUEST_QUEUE_CONFIG_ADD_INITIALIZED_METHOD_HANDLER(
  _In_ PNET_REQUEST_QUEUE_CONFIG         NetRequestQueueConfig,
  _In_ PNET_REQUEST_QUEUE_METHOD_HANDLER MethodHandler
);
```

Parameters
----------

*NetRequestQueueConfig* \[in\]  
A pointer to a driver-allocated [**NET\_REQUEST\_QUEUE\_CONFIG**](net-request-queue-config.md) structure to which the custom handler is being added.

*MethodHandler* \[in\]  
A pointer to a driver-allocated and initialized [**NET\_REQUEST\_QUEUE\_METHOD\_HANDLER**](net-request-queue-method-handler.md) structure.

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

 

 





