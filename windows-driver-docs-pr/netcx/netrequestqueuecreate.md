---
title: NetRequestQueueCreate method
description: Creates a net request queue object.
ms.assetid: f5bb6f56-d7cf-4f88-acd8-35da081f2edd
keywords: ["NetRequestQueueCreate method Network Drivers Starting with Windows Vista"]
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


\[Some information relates to pre-released product which may be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here.\]

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

*NetRequestQueueConfig* \[in\]  
A pointer to a caller-allocated [**NET\_REQUEST\_QUEUE\_CONFIG**](net-request-queue-config.md) structure.

*QueueAttributes* \[in, optional\]  
An optional pointer to a caller-allocated [**WDF\_OBJECT\_ATTRIBUTES**](wdf-wdf_object_attributes) structure that specifies attributes for the net request queue object.

*Queue* \[out, optional\]  
An optional pointer to a location that receives a handle to the new net request queue object.

Return value
------------

The method returns STATUS\_SUCCESS if the operation succeeds. Otherwise, this method may return an appropriate NTSTATUS error code.

Remarks
-------

The client driver typically calls this method from its [*EvtDriverDeviceAdd*](wdf-evtdriverdeviceadd) routine after the client has called [**WdfDeviceCreate**](wdf-wdfdevicecreate) and [**NetAdapterCreate**](netadaptercreate.md).

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
<td align="left">[Universal](http://go.microsoft.com/fwlink/p/?linkid=531356)</td>
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


[**NET\_REQUEST\_QUEUE\_CONFIG\_ADD\_INITIALIZED\_METHOD\_HANDLER**](net-request-queue-config-add-initialized-method-handler.md)

[**NET\_REQUEST\_QUEUE\_CONFIG\_ADD\_INITIALIZED\_QUERY\_DATA\_HANDLER**](net-request-queue-config-add-initialized-query-data-handler.md)

[**NET\_REQUEST\_QUEUE\_CONFIG\_INIT\_DEFAULT\_PARALLEL**](net-request-queue-config-init-default-parallel.md)

[**NET\_REQUEST\_QUEUE\_CONFIG\_INIT\_DEFAULT\_SEQUENTIAL**](net-request-queue-config-init-default-sequential.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20NetRequestQueueCreate%20method%20%20RELEASE:%20%281/19/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





