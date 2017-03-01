---
title: NET_REQUEST_QUEUE_SET_DATA_HANDLER_INIT method
topic_type:
- apiref
api_name:
- NET_REQUEST_QUEUE_SET_DATA_HANDLER_INIT
api_location:
- netrequestqueue.h
api_type:
- HeaderDef
---

# NET_REQUEST_QUEUE_SET_DATA_HANDLER_INIT method


[!include[NetAdapterCx Beta Prerelease](../netcx-beta-prerelease.md)]

Initializes the [NET_REQUEST_QUEUE_SET_DATA_HANDLER](net-request-queue-set-data-handler.md) structure.

Syntax
------

```cpp
__inline
void NET_REQUEST_QUEUE_SET_DATA_HANDLER_INIT(
  _Out_ PNET_REQUEST_QUEUE_SET_DATA_HANDLER SetDataHandler,
  _In_  NDIS_OID                            Oid,
  _In_  PFN_NET_REQUEST_SET_DATA            EvtRequestSetData,
  _In_  UINT                                MinimumInputLength
);
```

Parameters
----------

*SetDataHandler* [out]  
A pointer to the driver-allocated NET_REQUEST_QUEUE_SET_DATA_HANDLER structure.

*Oid* [in]  
The NDIS_OID identifier for the request.

*EvtRequestSetData* [in]  
Pointer to the custom set request handler.

*MinimumInputLength* [in]  
The needed minimum input length for the request.

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

 

 





