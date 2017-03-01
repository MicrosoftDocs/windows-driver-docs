---
title: NetRequestRetrieveInputOutputBuffer method
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

Retrieves the input/output buffer associated with a NETREQUEST object.

Syntax
------

```cpp
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

*Request* [in]  
A handle to a network request object.

*MininumInputLengthRequired* [in]  
The minimum input length needed for *InputOutputBuffer*. If the buffer's *InputOutputBuffer* is less than the minimum required, this routine returns STATUS_BUFFER_TOO_SMALL.

*MininumOutputLengthRequired* [in]  
The minimum output length needed for *InputOutputBuffer*. If the buffer's *OutputBufferLength* is less than the minimum required, this routine returns STATUS_BUFFER_TOO_SMALL.

*InputOutputBuffer* [in, out]  
Address to a location that receives a pointer to the buffer.

*InputBufferLength* [out]  
Address to a location that receives the actual input length of *InputOutputBuffer*.

*OutputBufferLength* [out]  
Address to a location that receives the actual output length of *InputOutputBuffer*.

Return value
------------

The method returns STATUS_SUCCESS if the operation succeeds. Otherwise, this method may return an appropriate NTSTATUS error code.

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

 

 





