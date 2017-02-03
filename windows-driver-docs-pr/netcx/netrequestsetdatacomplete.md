---
title: NetRequestSetDataComplete method
description: .
ms.assetid: dd479305-fef9-4b5a-928e-4d9b80938bf9
keywords: ["NetRequestSetDataComplete method Network Drivers Starting with Windows Vista"]
topic_type:
- apiref
api_name:
- NetRequestSetDataComplete
api_location:
- netrequest.h
api_type:
- HeaderDef
---

# NetRequestSetDataComplete method

[!include[NetAdapterCx Beta Prerelease](../netcx-beta-prerelease.md)]

Completes a set data request.

Syntax
------

```ManagedCPlusPlus
VOID NetRequestSetDataComplete(
  _In_ NETREQUEST Request,
  _In_ NTSTATUS   CompletionStatus,
  _In_ UINT       BytesRead
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

*BytesRead* \[in\]  
The number of bytes that the client driver read from the buffer.

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

 

 





