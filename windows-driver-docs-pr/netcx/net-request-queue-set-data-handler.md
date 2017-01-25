---
title: NET_REQUEST_QUEUE_SET_DATA_HANDLER structure
description: Call NET\_REQUEST\_QUEUE\_SET\_DATA\_HANDLER\_INIT to initialize this structure.
ms.assetid: e3cd863a-f798-4841-af71-936515c7aab1
keywords: ["NET_REQUEST_QUEUE_SET_DATA_HANDLER structure Network Drivers Starting with Windows Vista", "PNET_REQUEST_QUEUE_SET_DATA_HANDLER structure pointer Network Drivers Starting with Windows Vista"]
topic_type:
- apiref
api_name:
- NET_REQUEST_QUEUE_SET_DATA_HANDLER
api_location:
- netrequestqueue.h
api_type:
- HeaderDef
---

# NET\_REQUEST\_QUEUE\_SET\_DATA\_HANDLER structure


[!include[NetAdapterCx Beta Prerelease](../netcx-beta-prerelease.md)]

Call [NET\_REQUEST\_QUEUE\_SET\_DATA\_HANDLER\_INIT](net-request-queue-set-data-handler-init.md) to initialize this structure.

Syntax
------

```ManagedCPlusPlus
typedef struct _NET_REQUEST_QUEUE_SET_DATA_HANDLER {
  PNET_REQUEST_QUEUE_SET_DATA_HANDLER Next;
  WDFMEMORY                           Memory;
  NDIS_OID                            Oid;
  PFN_NET_REQUEST_SET_DATA            EvtRequestSetData;
  UINT                                MinimumInputLength;
  UINT                                MinimumOutputLength;
} NET_REQUEST_QUEUE_SET_DATA_HANDLER, *PNET_REQUEST_QUEUE_SET_DATA_HANDLER;
```

Members
-------

**Next**  

**Memory**  

**Oid**  

**EvtRequestSetData**  
Pointer to the client driver's implementation of a [*EVT\_NET\_REQUEST\_SET\_DATA*](evt-net-request-set-data.md) event callback function.

**MinimumInputLength**  

**MinimumOutputLength**  

Requirements
------------

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p>Minimum KMDF version</p></td>
<td align="left"><p>1.21</p></td>
</tr>
<tr class="even">
<td align="left"><p>Minimum NetAdapterCx version</p></td>
<td align="left"><p>1.0</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Header</p></td>
<td align="left">Netrequestqueue.h</td>
</tr>
</tbody>
</table>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20NET_REQUEST_QUEUE_SET_DATA_HANDLER%20structure%20%20RELEASE:%20%281/19/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




