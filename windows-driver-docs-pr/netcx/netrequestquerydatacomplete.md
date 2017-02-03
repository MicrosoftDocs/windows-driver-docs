---
title: NetRequestQueryDataComplete method
description: .
ms.assetid: 0883bc93-dcd3-4145-91fd-c8845095b8b4
keywords: ["NetRequestQueryDataComplete method Network Drivers Starting with Windows Vista"]
topic_type:
- apiref
api_name:
- NetRequestQueryDataComplete
api_location:
- netrequest.h
api_type:
- HeaderDef
---

# NetRequestQueryDataComplete method

[!include[NetAdapterCx Beta Prerelease](../netcx-beta-prerelease.md)]

Completes a query data request.

Syntax
------

```ManagedCPlusPlus
VOID NetRequestQueryDataComplete(
  _In_ NETREQUEST Request,
  _In_ NTSTATUS   CompletionStatus,
  _In_ UINT       BytesWritten
);
```

Parameters
----------

*Request* \[in\]  
A handle to a network request object.

*CompletionStatus* \[in\]  
An NTSTATUS value that represents the completion status of the request.  Valid status values include, but are not limited to, the following:

|Return code|Description|
|--|--|
|STATUS_SUCCESS|The driver successfully completed the request.|
|STATUS_CANCELLED|The driver canceled the request.|
|STATUS_UNSUCCESSFUL|The driver encountered an error while processing the request.|

*BytesWritten* \[in\]  
The number of bytes that the client driver wrote to the buffer.

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
<td align="left">Netrequest.h (include Netadaptercx.h)</td>
</tr>
<tr class="odd">
<td align="left"><p>IRQL</p></td>
<td align="left"><p>DISPATCH_LEVEL</p></td>
</tr>
</tbody>
</table>

 

 





