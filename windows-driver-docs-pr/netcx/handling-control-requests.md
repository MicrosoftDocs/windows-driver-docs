---
title: Handling Control Requests
---

# Handling Control Requests

In the NetAdapterCx model, the client driver receives most control requests as NETREQUEST objects, each of which represents an OID (object identifier) request.  The client driver typically sets up one or two WDF queues (called NETREQUESTQUEUEs) to manage control requests.

The following table shows the parent-child hierarchy for these objects:

|Object|Parent|
|---|---|
|NETREQUESTQUEUE|NETADAPTER|
|NETREQUEST|NETREQUESTQUEUE|

To see all the default parent child relationships for NetAdapterCx, see [Summary of Objects](summary-of-objects.md).

The client driver calls [**NET_REQUEST_QUEUE_CONFIG_INIT_DEFAULT_SEQUENTIAL method**](net-request-queue-config-init-default-sequential.md) or [**NET_REQUEST_QUEUE_CONFIG_INIT_DEFAULT_PARALLEL method**](net-request-queue-config-init-default-parallel.md) to create a sequential queue or a parallel queue.

For info on the two queue types, see [Dispatching Methods for I/O Requests](../wdf/dispatching-methods-for-i-o-requests.md).

For each of the three main request types (query data, set data, and method), the client driver can provide a single default handler, or one or more OID-specific handlers.

You can use both approaches in the same driver, providing custom handlers for some OIDs while using a default handler with a switch statement for the remainder.

A client driver sets up OID handlers in its [*EvtDriverDeviceAdd*](https://msdn.microsoft.com/library/windows/hardware/ff541693) routine.

To register default handlers for all query OIDs and all set OIDs, provide an [*EVT_NET_REQUEST_DEFAULT_QUERY_DATA*](evt-net-request-default-query-data.md) event callback function and an [*EVT_NET_REQUEST_DEFAULT_SET_DATA*](evt-net-request-default-set-data.md) event callback function.

For requests of type other than query data, set data, and method, the client driver can provide an [*EVT_NET_REQUEST_DEFAULT*](evt-net-request-default.md) event callback function.

For example, if the protocol driver issues an OID request with `NDIS_REQUEST_TYPE = NdisRequestGeneric1`, NetAdapterCx calls [*EVT_NET_REQUEST_DEFAULT*](evt-net-request-default.md).  NetAdapterCx fails the request if the client driver has not provided such a handler.

```cpp
NTSTATUS status;
NET_REQUEST_QUEUE_CONFIG config;
NETREQUESTQUEUE requestQueue;

NET_REQUEST_QUEUE_CONFIG_INIT_DEFAULT_SEQUENTIAL(&config, NetAdapter);
config.EvtRequestDefaultQueryData = MyDefaultQueryData;
config.EvtRequestDefaultSetData = MyDefaultSetData;
config.EvtRequestDefaultMethod = MyDefaultMethod;

config.EvtRequestDefault = MyDefault;
```

If the client driver will receive direct OIDs, call [**NET_REQUEST_QUEUE_CONFIG_INIT_DEFAULT_PARALLEL**](net-request-queue-config-init-default-parallel.md) to add a second queue that is configured for parallel dispatching.

To add an OID-specific query data handler, call the [**NET_REQUEST_QUEUE_CONFIG_ADD_QUERY_DATA_HANDLER**](net-request-queue-config-add-query-data-handler.md) method with a pointer to the client driver's implementation of an [*EVT_NET_REQUEST_QUERY_DATA*](evt-net-request-query-data.md) event callback function:

```cpp
NET_REQUEST_QUEUE_CONFIG_ADD_QUERY_DATA_HANDLER(
    &config, OID_GEN_VENDOR_DESCRIPTION,
    EvtQueryGenVendorDescription, sizeof(NIC_VENDOR_DESC));
```

Once you've set up the OID queue the way you like, call [**NetRequestQueueCreate**](netrequestqueuecreate.md) to create the queue:

```cpp
status = NetRequestQueueCreate(&config, WDF_NO_OBJECT_ATTRIBUTES, NULL);

if(!NT_SUCCESS(status))
{
    return status;
}
```

NetAdapterCx can call the client driver's control request handlers as soon as [*EVT_WDF_DEVICE_PREPARE_HARDWARE*](https://msdn.microsoft.com/library/windows/hardware/ff540880) returns until the time it calls [*EVT_WDF_DEVICE_RELEASE_HARDWARE*](https://msdn.microsoft.com/library/windows/hardware/ff540890).

## Completing Requests

* To complete a control request and specify only completion status, call [**NetRequestCompleteWithoutInformation**](netrequestcompletewithoutinformation.md) from the OID handler.
    
    ```cpp
            NetRequestCompleteWithoutInformation(Request, NDIS_STATUS_INVALID_DATA);
    ```

* To complete a control request and specify data read or written, call one of the following:

    * [**NetRequestMethodComplete**](netrequestmethodcomplete.md)
    * [**NetRequestQueryDataComplete**](netrequestquerydatacomplete.md)
    * [**NetRequestSetDataComplete**](netrequestsetdatacomplete.md)
