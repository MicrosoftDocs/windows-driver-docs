---
title: EVT\_NET\_REQUEST\_DEFAULT callback function
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


\[Some information relates to pre-released product which may be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here.\]

\[NetAdapterCx is preview only in the next major update to Windows 10\]

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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20EVT_NET_REQUEST_DEFAULT%20callback%20function%20%20RELEASE:%20%281/19/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





