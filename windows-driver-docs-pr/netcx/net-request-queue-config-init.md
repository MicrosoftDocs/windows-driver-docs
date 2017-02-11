---
title: NET_REQUEST_QUEUE_CONFIG_INIT method
topic_type:
- apiref
api_name:
- NET_REQUEST_QUEUE_CONFIG_INIT
api_location:
- netrequestqueue.h
api_type:
- HeaderDef
---

# NET\_REQUEST\_QUEUE\_CONFIG\_INIT method


[!include[NetAdapterCx Beta Prerelease](../netcx-beta-prerelease.md)]

Initializes the caller-allocated [NET\_REQUEST\_QUEUE\_CONFIG](net-request-queue-config.md) structure.

Syntax
------

```ManagedCPlusPlus
__inline
void NET_REQUEST_QUEUE_CONFIG_INIT(
  _Out_ PNET_REQUEST_QUEUE_CONFIG NetRequestQueueConfig,
  _In_  NETADAPTER                Adapter,
  _In_  NET_REQUEST_QUEUE_TYPE    QueueType
);
```

Parameters
----------

*NetRequestQueueConfig* \[out\]  
A pointer to the driver-allocated NET\_REQUEST\_QUEUE\_CONFIG structure.

*Adapter* \[in\]  
The NDIS adapter object that the client created in a prior call to [**NetAdapterCreate**](netadaptercreate.md).

*QueueType* \[in\]  
A [NET_REQUEST_QUEUE_TYPE](net-request-queue-type.md) enumeration that specifies the type of queue.

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

 

 





