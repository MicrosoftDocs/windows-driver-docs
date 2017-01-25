---
title: NET_REQUEST_QUEUE_METHOD_HANDLER structure
description: Call NET\_REQUEST\_QUEUE\_METHOD\_HANDLER\_INIT to initialize this structure.
ms.assetid: f088cead-48e8-4c53-8178-e6408c387389
keywords: ["NET_REQUEST_QUEUE_METHOD_HANDLER structure Network Drivers Starting with Windows Vista", "PNET_REQUEST_QUEUE_METHOD_HANDLER structure pointer Network Drivers Starting with Windows Vista"]
topic_type:
- apiref
api_name:
- NET_REQUEST_QUEUE_METHOD_HANDLER
api_location:
- netrequestqueue.h
api_type:
- HeaderDef
---

# NET\_REQUEST\_QUEUE\_METHOD\_HANDLER structure


\[Some information relates to pre-released product which may be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here.\]

Call [NET\_REQUEST\_QUEUE\_METHOD\_HANDLER\_INIT](net-request-queue-method-handler-init.md) to initialize this structure.

Syntax
------

```ManagedCPlusPlus
typedef struct _NET_REQUEST_QUEUE_METHOD_HANDLER {
  PNET_REQUEST_QUEUE_METHOD_HANDLER Next;
  WDFMEMORY                         Memory;
  NDIS_OID                          Oid;
  PFN_NET_REQUEST_METHOD            EvtRequestMethod;
  UINT                              MinimumInputLength;
  UINT                              MinimumOutputLength;
} NET_REQUEST_QUEUE_METHOD_HANDLER, *PNET_REQUEST_QUEUE_METHOD_HANDLER;
```

Members
-------

**Next**  
Pointer to the Next Custom Handler

**Memory**  
The WDFMEMORY object backing this memory

**Oid**  
The Request Identifiver

**EvtRequestMethod**  
Pointer to the client driver's implementation of a [*EVT\_NET\_REQUEST\_METHOD*](evt-net-request-method.md) event callback function.

**MinimumInputLength**  
Minimum input length needed by the client for this request.

**MinimumOutputLength**  
Minimum output length needed by the client for this request.

Remarks
-------

Call [**NET\_REQUEST\_QUEUE\_METHOD\_HANDLER\_INIT**](net-request-queue-method-handler-init.md) to initialize this structure.

Call [**NET\_REQUEST\_QUEUE\_CONFIG\_ADD\_INITIALIZED\_METHOD\_HANDLER**](net-request-queue-config-add-initialized-method-handler.md) to add a caller-provided custom request handler to a [**NET\_REQUEST\_QUEUE\_CONFIG**](net-request-queue-config.md) structure.

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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20NET_REQUEST_QUEUE_METHOD_HANDLER%20structure%20%20RELEASE:%20%281/19/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




