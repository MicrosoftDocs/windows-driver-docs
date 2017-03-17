---
title: EVT_NET_REQUEST_DEFAULT callback function
topic_type:
- apiref
api_name:
- PFN_NET_REQUEST_DEFAULT
api_location:
- netrequestqueue.h
api_type:
- UserDefined
---

# EVT_NET_REQUEST_DEFAULT callback function


[!include[NetAdapterCx Beta Prerelease](../netcx-beta-prerelease.md)]

Implemented by the client driver as the default handler for object identifier (OID) requests that are not query, set, or method requests.

Syntax
------

```cpp
EVT_NET_REQUEST_DEFAULT EvtNetRequestDefault;

void EvtNetRequestDefault(
  _In_    NETREQUESTQUEUE   RequestQueue,
  _In_    NETREQUEST        Request,
  _In_    NDIS_REQUEST_TYPE RequestType,
  _In_    NDIS_OID          Oid,
  _Inout_ PVOID             InputOutputBuffer,
  _In_    UINT              InputBufferLength,
  _In_    UINT              OutputBufferLength
)
{ ... }

typedef EVT_NET_REQUEST_DEFAULT PFN_NET_REQUEST_DEFAULT;
```

Register your implementation of this callback function by setting the appropriate member of [**NET_REQUEST_QUEUE_CONFIG**](net-request-queue-config.md) and then calling [**NetRequestQueueCreate**](netrequestqueuecreate.md).

Parameters
----------

*RequestQueue* [in]  
A handle to the net request queue object that is associated with the I/O request.

*Request* [in]  
A handle to a network request object.

*RequestType* [in]  
The request type as one of the [**NDIS_REQUEST_TYPE**](https://msdn.microsoft.com/library/windows/hardware/ff567250) enumeration values.

*Oid* [in]  
The object identifier of the requested operation. The value is an OID_ *XXX* code.

*InputOutputBuffer* [in, out]  
A pointer to a buffer into which the client driver or NetAdapterCx returns information for the specified request.

*InputBufferLength* [in]  
The length, in bytes, of the request's input buffer, if an input buffer is available.

*OutputBufferLength* [in]  
The length, in bytes, of the request's output buffer, if an output buffer is available.

Return value
------------

This callback function does not return a value.

Remarks
-------

To register an *EVT_NET_REQUEST_DEFAULT* callback function, the client driver calls [**NetRequestQueueCreate**](netrequestqueuecreate.md).

If NDIS_REQUEST_TYPE is not query, set, or method, NetAdapterCx calls the client driver's EVT_NET_REQUEST_DEFAULT handler with the request. If the client driver has not provided this callback, the request fails.

The contents of the *InputOutputBuffer*, *InputBufferLength*, and *OutputBufferLength* parameters are specific to NDIS_REQUEST_TYPE.

Requirements
------------
_Target platform: Universal_  
_Minimum KMDF version: 1.21_  
_Minimum NetAdapterCx version: 1.0_  
_Header: Netrequestqueue.h_  
_IRQL: PASSIVE_LEVEL_

## See also


[*MiniportOidRequest*](https://msdn.microsoft.com/library/windows/hardware/ff559416)

[**NDIS_OID_REQUEST**](https://msdn.microsoft.com/library/windows/hardware/ff566710)

 

 






