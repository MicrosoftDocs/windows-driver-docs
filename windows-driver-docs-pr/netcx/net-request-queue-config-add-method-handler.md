---
title: NET_REQUEST_QUEUE_CONFIG_ADD_METHOD_HANDLER method
topic_type:
- apiref
api_name:
- NET_REQUEST_QUEUE_CONFIG_ADD_METHOD_HANDLER
api_location:
- netrequestqueue.h
api_type:
- HeaderDef
---

# NET_REQUEST_QUEUE_CONFIG_ADD_METHOD_HANDLER method


[!include[NetAdapterCx Beta Prerelease](../netcx-beta-prerelease.md)]

 This initializer adds a caller provided custom request callback to the Queue
    config.

Syntax
------

```ManagedCPlusPlus
FORCEINLINE
VOID
NET_REQUEST_QUEUE_CONFIG_ADD_METHOD_HANDLER(
    _In_ PNET_REQUEST_QUEUE_CONFIG NetRequestQueueConfig,
    _In_ NDIS_OID                  Oid,
    _In_ PFN_NET_REQUEST_METHOD    EvtRequestMethod,
    _In_ UINT                      MinimumInputLength,
    _In_ UINT                      MinimumOutputLength
)
```

Parameters
----------
  NetRequestQueueConfig - The pointer to the NET_REQUEST_QUEUE_CONFIG structure 
        to which the custom handler is being added.
 
    Oid - The NDIS_OID Identifier for which this handler is meant for.
 
    EvtRequestMethod - The Custom callback for the request
 
    MinimumInputLength - The needed minimum input length for the request.
 
    MinimumOutputLength - The needed minimum output length for the request.

*NetRequestQueueConfig* \[in\]  
A pointer to a driver-allocated [**NET\_REQUEST\_QUEUE\_CONFIG**](net-request-queue-config.md) structure to which the custom handler is being added.

*MethodHandler* \[in\]  
A pointer to a driver-allocated and initialized [**NET\_REQUEST\_QUEUE\_METHOD\_HANDLER**](net-request-queue-method-handler.md) structure.

Return value
------------

This method does not return a value.

Remarks
-------
This routine allocates memory, an operation that can fail. However to keep
    client interface simple this routine doesnt return an error. Instead a bit
    is set to track the error and thereby the subsequent call to NetRequestQueueCreate
    fails. 
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

 

 





