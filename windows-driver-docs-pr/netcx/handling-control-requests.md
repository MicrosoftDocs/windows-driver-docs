---
title: Handling Control Requests
---

# Handling Control Requests

In the NetAdapterCx model, the client driver receives most control requests as NETREQUEST objects, each of which represents an OID (object identifier) request.  The client driver typically sets up one or two WDF queues (called NETREQUESTQUEUEs) to manage control requests.

The NETREQUESTQUEUE object is the parent of each NETREQUEST that it manages.  Because the queue is a child of the NETADAPTER object, WDF automatically deletes each queue and any associated requests when the adapter is deleted.

To see all the default parent child relationships for NetAdapterCx, see [Summary of Objects](summary-of-objects.md).

## Creating queue objects

In the NetAdapterCx model, the client uses a sequential queue for serial OIDs, and a parallel queue for direct OIDs.  Call these methods to create queues:

*  [**NET_REQUEST_QUEUE_CONFIG_INIT_DEFAULT_SEQUENTIAL**](net-request-queue-config-init-default-sequential.md)
*  [**NET_REQUEST_QUEUE_CONFIG_INIT_DEFAULT_PARALLEL**](net-request-queue-config-init-default-parallel.md)

For more info on these dispatching methods, see [Dispatching Methods for I/O Requests](../wdf/dispatching-methods-for-i-o-requests.md).


## Registering handlers

For each of the three main request types (query data, set data, and method), the client driver can provide a single default handler, or one or more OID-specific handlers.

You can use both approaches in the same driver, providing custom handlers for some OIDs while using a default handler with a switch statement for the remainder.

A client driver registers OID handlers in its [*EvtDriverDeviceAdd*](https://msdn.microsoft.com/library/windows/hardware/ff541693) routine.

Here are the control request handlers the client can provide:

* [*EVT_NET_REQUEST_METHOD*](evt-net-request-method.md)
* [*EVT_NET_REQUEST_QUERY_DATA*](evt-net-request-query-data.md)
* [*EVT_NET_REQUEST_SET_DATA*](evt-net-request-set-data.md)
* [*EVT_NET_REQUEST_DEFAULT_METHOD*](evt-net-request-default-method.md)
* [*EVT_NET_REQUEST_DEFAULT_QUERY_DATA*](evt-net-request-default-query-data.md)
* [*EVT_NET_REQUEST_DEFAULT_SET_DATA*](evt-net-request-default-set-data.md)

For each of the three main request types, the OID-specific handlers take precedence over the default handlers.  If the client provides neither for a given OID, NetAdapterCx fails the request.

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

To add an OID-specific handlers, use these methods:

* [**NET_REQUEST_QUEUE_CONFIG_ADD_QUERY_DATA_HANDLER**](net-request-queue-config-add-query-data-handler.md)
* [**NET_REQUEST_QUEUE_CONFIG_ADD_SET_DATA_HANDLER**](net-request-queue-config-add-set-data-handler.md)
* [**NET_REQUEST_QUEUE_CONFIG_ADD_METHOD_HANDLER**](net-request-queue-config-add-method-handler.md)

The following example calls [**NET_REQUEST_QUEUE_CONFIG_ADD_QUERY_DATA_HANDLER**](net-request-queue-config-add-query-data-handler.md) with a pointer to the client's [*EVT_NET_REQUEST_QUERY_DATA*](evt-net-request-query-data.md) event callback function:

```cpp
NET_REQUEST_QUEUE_CONFIG_ADD_QUERY_DATA_HANDLER(
    &config, OID_GEN_VENDOR_DESCRIPTION,
    EvtQueryGenVendorDescription, sizeof(NIC_VENDOR_DESC));
```

## Creating the queue

Once you've set up each OID queue the way you like, call [**NetRequestQueueCreate**](netrequestqueuecreate.md) to create the queue:

```cpp
status = NetRequestQueueCreate(&config, WDF_NO_OBJECT_ATTRIBUTES, NULL);

if(!NT_SUCCESS(status))
{
    return status;
}
```

NetAdapterCx can call the client driver's control request handlers as soon as [*EVT_WDF_DEVICE_PREPARE_HARDWARE*](https://msdn.microsoft.com/library/windows/hardware/ff540880) returns until the time it calls [*EVT_WDF_DEVICE_RELEASE_HARDWARE*](https://msdn.microsoft.com/library/windows/hardware/ff540890).

## Completing Requests

The client driver must complete each NETREQUEST that it receives.  Otherwise, the control request is left in a pending state.

* To complete a control request and specify only completion status, call [**NetRequestCompleteWithoutInformation**](netrequestcompletewithoutinformation.md) from the OID handler.
    
    ```cpp
            NetRequestCompleteWithoutInformation(Request, NDIS_STATUS_INVALID_DATA);
    ```

* To complete a control request and specify data read or written, call one of the following:

    * [**NetRequestMethodComplete**](netrequestmethodcomplete.md)
    * [**NetRequestQueryDataComplete**](netrequestquerydatacomplete.md)
    * [**NetRequestSetDataComplete**](netrequestsetdatacomplete.md)

