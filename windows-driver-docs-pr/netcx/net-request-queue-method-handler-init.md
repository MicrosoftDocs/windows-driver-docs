---
title: NET_REQUEST_QUEUE_METHOD_HANDLER_INIT method
description: Initializes the NET\_REQUEST\_QUEUE\_METHOD\_HANDLER structure.
ms.assetid: b4d004b6-7dad-4393-9c59-6274668f2d95
keywords: ["NET_REQUEST_QUEUE_METHOD_HANDLER_INIT method Network Drivers Starting with Windows Vista"]
topic_type:
- apiref
api_name:
- NET_REQUEST_QUEUE_METHOD_HANDLER_INIT
api_location:
- netrequestqueue.h
api_type:
- HeaderDef
---

# NET\_REQUEST\_QUEUE\_METHOD\_HANDLER\_INIT method


[!include[NetAdapterCx Beta Prerelease](../netcx-beta-prerelease.md)]

Initializes the [NET\_REQUEST\_QUEUE\_METHOD\_HANDLER](net-request-queue-method-handler.md) structure.

Syntax
------

```ManagedCPlusPlus
__inline
void NET_REQUEST_QUEUE_METHOD_HANDLER_INIT(
  _Out_ PNET_REQUEST_QUEUE_METHOD_HANDLER MethodHandler,
  _In_  NDIS_OID                          Oid,
  _In_  PFN_NET_REQUEST_METHOD            EvtRequestMethod,
  _In_  UINT                              MinimumInputLength,
  _In_  UINT                              MinimumOutputLength
);
```

Parameters
----------

*MethodHandler* \[out\]  
A pointer to the driver-allocated NET\_REQUEST\_QUEUE\_METHOD\_HANDLER structure.

*Oid* \[in\]  
The NDIS\_OID identifier for the request.

*EvtRequestMethod* \[in\]  
Pointer to the client driver's implementation of a [*EVT_NET_REQUEST_METHOD*](evt-net-request-method.md) event callback function.

*MinimumInputLength* \[in\]  
The needed minimum input length for the request.

*MinimumOutputLength* \[in\]  
The needed minimum output length for the request.

Return value
------------

This method does not return a value.

Requirements
------------

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p>Minimum supported client</p></td>
<td align="left"><p>Windows 10</p></td>
</tr>
<tr class="even">
<td align="left"><p>Minimum supported server</p></td>
<td align="left"><p>Windows Server 2016</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Header</p></td>
<td align="left">Netrequestqueue.h</td>
</tr>
<tr class="even">
<td align="left"><p>IRQL</p></td>
<td align="left"><p>PASSIVE_LEVEL</p></td>
</tr>
</tbody>
</table>

 

 





