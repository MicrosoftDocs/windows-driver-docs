---
title: Handling Control Requests
---

# Handling Control Requests

In the NetAdapterCx model, the client driver receives most control requests as NETREQUEST objects, each of which represents an OID (object identifier) request.  The client driver typically sets up one or two WDF queues (called NETREQUESTQUEUEs) to manage control requests.

The NETREQUESTQUEUE object is the parent of each NETREQUEST that it manages.  Because the queue is a child of the NETADAPTER object, WDF automatically deletes each queue and any associated requests when the adapter is deleted.

To see all the default parent child relationships for NetAdapterCx, see [Summary of Objects](summary-of-objects.md).

## Creating queue objects

In the NetAdapterCx model, the client can use two types of queues for handling requests (OIDs):
*  a sequential queue for normal requests (OIDs). Requests received from upper layers in this queue are always dispatched to client driver by NetAdapterCx in serialized fashion.
*  a parallel queue for direct requests (OIDs). Requests received from upper layers may be dispatched to client driver by NetAdapterCx in a parallel fashion.

Call these methods to create queues:

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

A detailed flow digram is shown as follow:


<img src="images/netcx-adapter-request-handling-flow.png" alt="Drawing" style="width: 800px;"/>

A client driver shall use the following code snippet to setup its default handlers.

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

The following example calls [**NET_REQUEST_QUEUE_CONFIG_ADD_QUERY_DATA_HANDLER**](net-request-queue-config-add-query-data-handler.md) with a pointer to the client's [*EVT_NET_REQUEST_QUERY_DATA*](evt-net-request-query-data.md) event callback function to register a handler for a specific OID (OID_GEN_VENDOR_DESCRIPTION):

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

The client driver must complete each NETREQUEST that it receives.  Otherwise, the control request is left in a pending state. If the request can not be handled synchronously, the client driver must later complete the pending NETREQUEST. Forget to complete a pending request will cause the client driver to hang during its unbinding process.

If the original request did not contain a large enough buffer, call [**NetRequestSetBytesNeeded**](netrequestsetbytesneeded.md), and then one of the following.

* To complete a control request and specify only completion status, call [**NetRequestCompleteWithoutInformation**](netrequestcompletewithoutinformation.md) from the OID handler.
    
    ```cpp
            NetRequestCompleteWithoutInformation(Request, NDIS_STATUS_INVALID_DATA);
    ```

If the original request did contain a large enough buffer for read/write, the client driver shall call [**NetRequestRetrieveInputOutputBuffer**](NetRequestRetrieveInputOutputBuffer.md) to retrieve the input/output buffer. Then perform neccessary memory transfer and complete the request using:

* To complete a control request and specify data read or written, call one of the following based on the request type:

    * [**NetRequestMethodComplete**](netrequestmethodcomplete.md)
    * [**NetRequestQueryDataComplete**](netrequestquerydatacomplete.md)
    * [**NetRequestSetDataComplete**](netrequestsetdatacomplete.md)