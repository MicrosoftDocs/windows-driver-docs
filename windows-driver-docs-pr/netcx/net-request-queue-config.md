---
title: NET_REQUEST_QUEUE_CONFIG structure
description: Call NET\_REQUEST\_QUEUE\_CONFIG\_INIT to initialize this structure.
ms.assetid: 16c23905-7192-4ab0-9eab-f3a6c39ed3d5
keywords: ["NET_REQUEST_QUEUE_CONFIG structure Network Drivers Starting with Windows Vista", "PNET_REQUEST_QUEUE_CONFIG structure pointer Network Drivers Starting with Windows Vista"]
topic_type:
- apiref
api_name:
- NET_REQUEST_QUEUE_CONFIG
api_location:
- netrequestqueue.h
api_type:
- HeaderDef
---

# NET\_REQUEST\_QUEUE\_CONFIG structure


[!include[NetAdapterCx Beta Prerelease](../netcx-beta-prerelease.md)]

Call [NET\_REQUEST\_QUEUE\_CONFIG\_INIT](net-request-queue-config-init.md) to initialize this structure.

Syntax
------

```ManagedCPlusPlus
typedef struct _NET_REQUEST_QUEUE_CONFIG {
  ULONG                                   Size;
  NETADAPTER                              Adapter;
  NET_REQUEST_QUEUE_TYPE                  Type;
  PFN_NET_REQUEST_DEFAULT_SET_DATA        EvtRequestDefaultSetData;
  PFN_NET_REQUEST_DEFAULT_QUERY_DATA      EvtRequestDefaultQueryData;
  PFN_NET_REQUEST_DEFAULT_METHOD          EvtRequestDefaultMethod;
  PFN_NET_REQUEST_DEFAULT                 EvtRequestDefault;
  NET_REQUEST_QUEUE_ADD_HANDLER_ERROR     AddHandlerError;
  ULONG                                   SizeOfSetDataHandler;
  ULONG                                   SizeOfQueryDataHandler;
  ULONG                                   SizeOfMethodHandler;
  PNET_REQUEST_QUEUE_SET_DATA_HANDLER     SetDataHandlers;
  PNET_REQUEST_QUEUE_QUERY_DATA_HANDLER   QueryDataHandlers;
  PNET_REQUEST_QUEUE_METHOD_HANDLER       MethodHandlers;
} NET_REQUEST_QUEUE_CONFIG, *PNET_REQUEST_QUEUE_CONFIG;
```

Members
-------

**Size**  

**Adapter**  

**Type**  

**EvtRequestDefaultSetData**  
Pointer to the client driver's implementation of a [*EVT\_NET\_REQUEST\_DEFAULT\_SET\_DATA*](evt-net-request-default-set-data.md) event callback function.

**EvtRequestDefaultQueryData**  
Pointer to the client driver's implementation of a [*EVT\_NET\_REQUEST\_DEFAULT\_QUERY\_DATA*](evt-net-request-default-query-data.md) event callback function.

**EvtRequestDefaultMethod**  
Pointer to the client driver's implementation of a [*EVT\_NET\_REQUEST\_DEFAULT\_METHOD*](evt-net-request-default-method.md) event callback function.

**EvtRequestDefault**  
Pointer to the client driver's implementation of a [*EVT\_NET\_REQUEST\_DEFAULT*](evt-net-request-default.md) event callback function.

**AddHandlerError**  

**SizeOfSetDataHandler**  

**SizeOfQueryDataHandler**  

**SizeOfMethodHandler**  

**SetDataHandlers**  
Pointer to a [**NET\_REQUEST\_QUEUE\_SET\_DATA\_HANDLER**](net-request-queue-set-data-handler.md) structure.

**QueryDataHandlers**  
Pointer to a [**NET\_REQUEST\_QUEUE\_QUERY\_DATA\_HANDLER**](net-request-queue-query-data-handler.md) structure.

**MethodHandlers**  
Pointer to a [**NET\_REQUEST\_QUEUE\_METHOD\_HANDLER**](net-request-queue-method-handler.md) structure.

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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20NET_REQUEST_QUEUE_CONFIG%20structure%20%20RELEASE:%20%281/19/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




