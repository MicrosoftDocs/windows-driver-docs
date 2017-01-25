---
title: EVT_NET_REQUEST_SET_DATA callback function
description: Implemented by the client driver to ... set handler callback.
ms.assetid: 1286c19b-ef24-4eaa-85f5-8049c864c3f7
keywords: ["EvtNetRequestSetData callback function Network Drivers Starting with Windows Vista", "EVT_NET_REQUEST_SET_DATA", "PFN_NET_REQUEST_SET_DATA callback function pointer Network Drivers Starting with Windows Vista"]
topic_type:
- apiref
api_name:
- PFN_NET_REQUEST_SET_DATA
api_location:
- netrequestqueue.h
api_type:
- UserDefined
---

# EVT\_NET\_REQUEST\_SET\_DATA callback function


\[Some information relates to pre-released product which may be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here.\]

Implemented by the client driver to ... set handler callback

Syntax
------

```ManagedCPlusPlus
EVT_NET_REQUEST_SET_DATA EvtNetRequestSetData;

void EvtNetRequestSetData(
  _In_ NETREQUESTQUEUE RequestQueue,
  _In_ NETREQUEST      Request,
  _In_ PVOID           InputBuffer,
  _In_ UINT            InputBufferLength
)
{ ... }

typedef EVT_NET_REQUEST_SET_DATA PFN_NET_REQUEST_SET_DATA;
```

Register your implementation of this callback function by setting the appropriate member of [**NET\_REQUEST\_QUEUE\_SET\_DATA\_HANDLER**](net-request-queue-set-data-handler.md) and then calling [**NET\_REQUEST\_QUEUE\_SET\_DATA\_HANDLER\_INIT**](net-request-queue-set-data-handler-init.md).

Parameters
----------

*RequestQueue* \[in\]  

*Request* \[in\]  

*InputBuffer* \[in\]  

*InputBufferLength* \[in\]  

Return value
------------

This callback function does not return a value.

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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20EVT_NET_REQUEST_SET_DATA%20callback%20function%20%20RELEASE:%20%281/19/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




