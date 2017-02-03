---
title: NetRequestRetrieveInputOutputBuffer method
description: .
ms.assetid: b999f2bd-a9ba-471e-b053-a566743180c5
keywords: ["NetRequestRetrieveInputOutputBuffer method Network Drivers Starting with Windows Vista"]
topic_type:
- apiref
api_name:
- NetRequestRetrieveInputOutputBuffer
api_location:
- netrequest.h
api_type:
- HeaderDef
---

# NetRequestRetrieveInputOutputBuffer method


[!include[NetAdapterCx Beta Prerelease](../netcx-beta-prerelease.md)]

Syntax
------

```ManagedCPlusPlus
NTSTATUS NetRequestRetrieveInputOutputBuffer(
  _In_    NETREQUEST Request,
  _In_    UINT       MininumInputLengthRequired,
  _In_    UINT       MininumOutputLengthRequired,
  _Inout_ PVOID*     InputOutputBuffer,
  _Out_   PUINT      InputBufferLength,
  _Out_   PUINT      OutputBufferLength
);
```

Parameters
----------

*Request* \[in\]  
A handle to a network request object.

*MininumInputLengthRequired* \[in\]  

*MininumOutputLengthRequired* \[in\]  

*InputOutputBuffer* \[in, out\]  

*InputBufferLength* \[out\]  

*OutputBufferLength* \[out\]  

Return value
------------

(NTSTATUS) The method returns STATUS\_SUCCESS if the operation succeeds. Otherwise, this method may return an appropriate NTSTATUS error code.

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

 

 





