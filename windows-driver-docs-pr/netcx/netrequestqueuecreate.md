---
title: NetRequestQueueCreate method
topic_type:
- apiref
api_name:
- NetRequestQueueCreate
api_location:
- NetAdapterCxStub.lib
- NetAdapterCxStub.dll
api_type:
- LibDef
---

# NetRequestQueueCreate method

[!include[NetAdapterCx Beta Prerelease](../netcx-beta-prerelease.md)]

Creates a net request queue object.

Syntax
------

```ManagedCPlusPlus
NTSTATUS NetRequestQueueCreate(
  _In_      PNET_REQUEST_QUEUE_CONFIG NetRequestQueueConfig,
  _In_opt_  PWDF_OBJECT_ATTRIBUTES    QueueAttributes,
  _Out_opt_ NETREQUESTQUEUE           *Queue
);
```

Parameters
----------

*NetRequestQueueConfig* [in]  
A pointer to a caller-allocated [**NET_REQUEST_QUEUE_CONFIG**](net-request-queue-config.md) structure.

*QueueAttributes* [in, optional]  
An optional pointer to a caller-allocated [**WDF_OBJECT_ATTRIBUTES**](https://msdn.microsoft.com/library/windows/hardware/ff552400) structure that specifies attributes for the net request queue object.

*Queue* [out, optional]  
An optional pointer to a location that receives a handle to the new net request queue object.

Return value
------------

The method returns STATUS_SUCCESS if the operation succeeds. Otherwise, this method may return an appropriate NTSTATUS error code.

Remarks
-------

The client driver typically calls this method from its [*EvtDriverDeviceAdd*](https://msdn.microsoft.com/library/windows/hardware/ff541693) routine after the client has called [**WdfDeviceCreate**](https://msdn.microsoft.com/library/windows/hardware/ff545926) and [**NetAdapterCreate**](netadaptercreate.md).

The NETREQUESTQUEUE object represents an OID queue in the traditional NDIS model.

Examples
--------

Typically, the client creates a queue for regular (sequential) OIDs, and may optionally also create a second queue for direct (parallel) OIDs. This example shows how to create a sequential queue.

```
    NET_REQUEST_QUEUE_CONFIG config;

    // Initialize the Queue Config
    NET_REQUEST_QUEUE_CONFIG_INIT_DEFAULT_SEQUENTIAL(&amp;config,
                                                     AdapterContext->GetNetAdapter());

    //
    // Register set and query handler
    //
    config.EvtRequestDefaultSetData = EvtNetRequestSetData;
    config.EvtRequestDefaultQueryData = EvtNetRequestQueryData;


    //
    // To add a custom request handler, call NET_REQUEST_QUEUE_CONFIG_ADD_INITIALIZED_QUERY_DATA_HANDLER
    //
    

    //
    // Create the default NETREQUESTQUEUE
    //
    status = NetRequestQueueCreate(&amp;config,
                                   WDF_NO_OBJECT_ATTRIBUTES,
                                   NULL);

```

Requirements
------------

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p>Target platform</p></td>
<td align="left">Universal</td>
</tr>
<tr class="even">
<td align="left"><p>Minimum KMDF version</p></td>
<td align="left"><p>1.21</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Minimum NetAdapterCx version</p></td>
<td align="left"><p>1.0</p></td>
</tr>
<tr class="even">
<td align="left"><p>Header</p></td>
<td align="left">Netrequestqueue.h (include Netadaptercx.h)</td>
</tr>
<tr class="odd">
<td align="left"><p>Library</p></td>
<td align="left">NetAdapterCxStub.lib</td>
</tr>
<tr class="even">
<td align="left"><p>IRQL</p></td>
<td align="left"><p>PASSIVE_LEVEL</p></td>
</tr>
</tbody>
</table>

## See also


[**NET_REQUEST_QUEUE_CONFIG_ADD_INITIALIZED_METHOD_HANDLER**](net-request-queue-config-add-initialized-method-handler.md)

[**NET_REQUEST_QUEUE_CONFIG_ADD_INITIALIZED_QUERY_DATA_HANDLER**](net-request-queue-config-add-initialized-query-data-handler.md)

[**NET_REQUEST_QUEUE_CONFIG_INIT_DEFAULT_PARALLEL**](net-request-queue-config-init-default-parallel.md)

[**NET_REQUEST_QUEUE_CONFIG_INIT_DEFAULT_SEQUENTIAL**](net-request-queue-config-init-default-sequential.md)

 

 






