---
title: EVT\_NET\_REQUEST\_METHOD callback function
description: Implemented by the client driver to ... custom method handler callback.
ms.assetid: 9dc17107-8e42-4853-be11-bc8031e21e2b
keywords: ["EvtNetRequestMethod callback function Network Drivers Starting with Windows Vista", "EVT_NET_REQUEST_METHOD", "PFN_NET_REQUEST_METHOD callback function pointer Network Drivers Starting with Windows Vista"]
topic_type:
- apiref
api_name:
- PFN_NET_REQUEST_METHOD
api_location:
- netrequestqueue.h
api_type:
- UserDefined
---

# EVT\_NET\_REQUEST\_METHOD callback function


\[Some information relates to pre-released product which may be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here.\]

Implemented by the client driver to ... custom method handler callback

Syntax
------

```ManagedCPlusPlus
EVT_NET_REQUEST_METHOD EvtNetRequestMethod;

VOID EvtNetRequestMethod(
  _In_  NETREQUESTQUEUE RequestQueue,
  _In_  NETREQUEST      Request,
  _Out_ PVOID           InputOutputBuffer,
  _In_  UINT            InputBufferLength,
  _In_  UINT            OutputBufferLength
)
{ ... }

typedef EVT_NET_REQUEST_METHOD PFN_NET_REQUEST_METHOD;
```

Register your implementation of this callback function by setting the appropriate member of [**NET\_REQUEST\_QUEUE\_METHOD\_HANDLER**](net-request-queue-method-handler.md) and then calling [**NET\_REQUEST\_QUEUE\_METHOD\_HANDLER\_INIT**](net-request-queue-method-handler-init.md).

Parameters
----------

*RequestQueue* \[in\]  

*Request* \[in\]  

*InputOutputBuffer* \[out\]  

*InputBufferLength* \[in\]  

*OutputBufferLength* \[in\]  

Return value
------------

(NTSTATUS) If the operation is successful, the callback function must return STATUS\_SUCCESS, or another status value for which NT\_SUCCESS(status) equals TRUE. Otherwise, an appropriate [NTSTATUS](https://msdn.microsoft.com/library/windows/hardware/ff557697) error code.

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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20EVT_NET_REQUEST_METHOD%20callback%20function%20%20RELEASE:%20%281/19/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




