---
title: EVT_NET_REQUEST_DEFAULT_METHOD callback function
description: Implemented by the client driver to ... handler for method OIDs.
ms.assetid: 5e98a8fc-5d21-4940-bf08-bbc8fdd80af0
keywords: ["EvtNetRequestDefaultMethod callback function Network Drivers Starting with Windows Vista", "EVT_NET_REQUEST_DEFAULT_METHOD", "PFN_NET_REQUEST_DEFAULT_METHOD callback function pointer Network Drivers Starting with Windows Vista"]
topic_type:
- apiref
api_name:
- PFN_NET_REQUEST_DEFAULT_METHOD
api_location:
- netrequestqueue.h
api_type:
- UserDefined
---

# EVT\_NET\_REQUEST\_DEFAULT\_METHOD callback function

[!include[NetAdapterCx Beta Prerelease](../netcx-beta-prerelease.md)]

Implemented by the client driver to handle method OIDs.

Syntax
------

```ManagedCPlusPlus
EVT_NET_REQUEST_DEFAULT_METHOD EvtNetRequestDefaultMethod;

VOID EvtNetRequestDefaultMethod(
  _In_  NETREQUESTQUEUE RequestQueue,
  _In_  NETREQUEST      Request,
  _In_  NDIS_OID        Oid,
  _Out_ PVOID           InputOutputBuffer,
  _In_  UINT            InputBufferLength,
  _In_  UINT            OutputBufferLength
)
{ ... }

typedef EVT_NET_REQUEST_DEFAULT_METHOD PFN_NET_REQUEST_DEFAULT_METHOD;
```

Register your implementation of this callback function by setting the appropriate member of [**NET\_REQUEST\_QUEUE\_CONFIG**](net-request-queue-config.md) and then calling [**NetRequestQueueCreate**](netrequestqueuecreate.md).

Parameters
----------

*RequestQueue* \[in\]  

*Request* \[in\]  

*Oid* \[in\]  

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

 

 





