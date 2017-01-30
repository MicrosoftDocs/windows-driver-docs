---
title: EVT_NET_REQUEST_QUERY_DATA callback function
description: Implemented by the client driver to ... custom query handler callback.
ms.assetid: 2a1ade3a-571d-402d-bfda-40de75b67164
keywords: ["EvtNetRequestQueryData callback function Network Drivers Starting with Windows Vista", "EVT_NET_REQUEST_QUERY_DATA", "PFN_NET_REQUEST_QUERY_DATA callback function pointer Network Drivers Starting with Windows Vista"]
topic_type:
- apiref
api_name:
- PFN_NET_REQUEST_QUERY_DATA
api_location:
- netrequestqueue.h
api_type:
- UserDefined
---

# EVT\_NET\_REQUEST\_QUERY\_DATA callback function


[!include[NetAdapterCx Beta Prerelease](../netcx-beta-prerelease.md)]

Implemented by the client driver to ... custom query handler callback

Syntax
------

```ManagedCPlusPlus
EVT_NET_REQUEST_QUERY_DATA EvtNetRequestQueryData;

VOID EvtNetRequestQueryData(
  _In_  NETREQUESTQUEUE RequestQueue,
  _In_  NETREQUEST      Request,
  _Out_ PVOID           OutputBuffer,
  _In_  UINT            OutputBufferLength
)
{ ... }

typedef EVT_NET_REQUEST_QUERY_DATA PFN_NET_REQUEST_QUERY_DATA;
```

Register your implementation of this callback function by setting the appropriate member of [**NET\_REQUEST\_QUEUE\_QUERY\_DATA\_HANDLER**](net-request-queue-query-data-handler.md) and then calling [**NET\_REQUEST\_QUEUE\_QUERY\_DATA\_HANDLER\_INIT**](net-request-queue-query-data-handler-init.md).

Parameters
----------

*RequestQueue* \[in\]  

*Request* \[in\]  

*OutputBuffer* \[out\]  

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

 

 





