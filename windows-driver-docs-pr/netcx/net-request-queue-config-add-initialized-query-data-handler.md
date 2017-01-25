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


\[Some information relates to pre-released product which may be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here.\]

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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20NET_REQUEST_QUEUE_CONFIG_ADD_INITIALIZED_QUERY_DATA_HANDLER%20method%20%20RELEASE:%20%281/19/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





