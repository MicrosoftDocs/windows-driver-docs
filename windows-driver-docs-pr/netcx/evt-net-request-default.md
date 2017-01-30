---
title: EVT_NET_REQUEST_DEFAULT callback function
description: The client driver's implementation of the EVT\_NET\_REQUEST\_DEFAULT event callback function to handle an object identifier (OID) request to query or set information in the driver.
ms.assetid: 34be105b-c952-4dfe-9889-ef2ed444f8ac
keywords: ["EvtNetRequestDefault callback function Network Drivers Starting with Windows Vista", "EVT_NET_REQUEST_DEFAULT", "PFN_NET_REQUEST_DEFAULT callback function pointer Network Drivers Starting with Windows Vista"]
topic_type:
- apiref
api_name:
- PFN_NET_REQUEST_DEFAULT
api_location:
- netrequestqueue.h
api_type:
- UserDefined
---

# EVT\_NET\_REQUEST\_DEFAULT callback function


[!include[NetAdapterCx Beta Prerelease](../netcx-beta-prerelease.md)]

The client driver's implementation of the *EVT\_NET\_REQUEST\_DEFAULT* event callback function to handle an object identifier (OID) request to query or set information in the driver.

Syntax
------

```ManagedCPlusPlus
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

Register your implementation of this callback function by setting the appropriate member of [**NET\_REQUEST\_QUEUE\_CONFIG**](net-request-queue-config.md) and then calling [**NetRequestQueueCreate**](netrequestqueuecreate.md).

Parameters
----------

*RequestQueue* \[in\]  
A handle to the net request queue object that is associated with the I/O request.

*Request* \[in\]  
A handle to a network request object.

*RequestType* \[in\]  
The request type as one of the [**NDIS\_REQUEST\_TYPE**](https://msdn.microsoft.com/library/windows/hardware/ff567250) enumeration values.

*Oid* \[in\]  
The object identifier of the requested operation. The value is an OID\_ *XXX* code.

*InputOutputBuffer* \[in, out\]  
A pointer to a buffer into which the client driver or NetAdapterCx returns information for the specified request.

*InputBufferLength* \[in\]  
The length, in bytes, of the request's input buffer, if an input buffer is available.

*OutputBufferLength* \[in\]  
The length, in bytes, of the request's output buffer, if an output buffer is available.

Return value
------------

This callback function does not return a value.

Remarks
-------

To register an *EVT\_NET\_REQUEST\_DEFAULT* callback function, the client driver must call [**NetRequestQueueCreate**](netrequestqueuecreate.md).

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
<td align="left">Netrequestqueue.h</td>
</tr>
<tr class="odd">
<td align="left"><p>IRQL</p></td>
<td align="left"><p>PASSIVE_LEVEL</p></td>
</tr>
</tbody>
</table>

## See also


[*MiniportOidRequest*](https://msdn.microsoft.com/library/windows/hardware/ff559416)

[**NDIS\_OID\_REQUEST**](https://msdn.microsoft.com/library/windows/hardware/ff566710)

 

 






