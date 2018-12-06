---
title: AVCSTRM\_READ
description: AVCSTRM\_READ
ms.assetid: 0bc0c8ae-15b8-4f52-b081-f3eb31ac4478
keywords: ["AVCSTRM_READ Streaming Media Devices"]
topic_type:
- apiref
api_name:
- AVCSTRM_READ
api_type:
- NA
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# AVCSTRM\_READ


## <span id="ddk_avcstrm_read_ks"></span><span id="DDK_AVCSTRM_READ_KS"></span>


The **AVCSTRM\_READ** function code is used to submit a data buffer *avcstrm.sys* that is filled with data from the specified stream.

### I/O Status Block

If successful, *avcstrm.sys* sets **Irp-&gt;IoStatus.Status** to STATUS\_SUCCESS.

Possible error return values include:

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Error Status</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>STATUS_DEVICE_REMOVED</p></td>
<td><p>The device corresponding to the <strong>AVCSTRM_READ</strong> operation no longer exists.</p></td>
</tr>
<tr class="even">
<td><p>STATUS_CANCELLED</p></td>
<td><p>The request was unable to be completed.</p></td>
</tr>
<tr class="odd">
<td><p>STATUS_INVALID_PARAMETER</p></td>
<td><p>A parameter specified in the IRP is incorrect,</p></td>
</tr>
<tr class="even">
<td><p>STATUS_INSUFFICIENT_RESOURCES</p></td>
<td><p>There were not sufficient system resources to complete the request.</p></td>
</tr>
<tr class="odd">
<td><p>STATUS_PENDING</p></td>
<td><p>The request has been received but requires further processing. The I/O completion routine will handle the final response.</p></td>
</tr>
</tbody>
</table>

 

### Comments

This function uses the **BufferStruct** member of the **CommandData** union in the AVC\_STREAM\_REQUEST\_BLOCK structure as shown below.

```cpp
typedef struct _AVC_STREAM_REQUEST_BLOCK {
  ULONG  SizeOfThisBlock;
  ULONG  Version;
  AVCSTRM_FUNCTION  Function;
  .
  .
  PVOID AVCStreamContext;
  .
  .
  union _tagCommandData {
    .
    .
    AVCSTRM_BUFFER_STRUCT  BufferStruct;
    .
    .
  } CommandData;
} AVC_STREAM_REQUEST_BLOCK, *PAVC_STREAM_REQUEST_BLOCK;
```

### Requirements

**Headers:** Declared in *avcstrm.h*. Include *avcstrm.h*.

### <span id="avc_stream_request_block_input"></span><span id="AVC_STREAM_REQUEST_BLOCK_INPUT"></span>AVC\_STREAM\_REQUEST\_BLOCK Input

<span id="SizeOfThisBlock__Version_and_Function"></span><span id="sizeofthisblock__version_and_function"></span><span id="SIZEOFTHISBLOCK__VERSION_AND_FUNCTION"></span>**SizeOfThisBlock, Version and Function**  
Use the [**INIT\_AVCSTRM\_HEADER**](https://msdn.microsoft.com/library/windows/hardware/ff560750) macro to initialize these members. Pass **AVCSTRM\_READ** in the Request argument of the macro.

<span id="AVCStreamContext"></span><span id="avcstreamcontext"></span><span id="AVCSTREAMCONTEXT"></span>**AVCStreamContext**  
Specifies the stream context (handle) returned by an earlier **AVCSTRM\_OPEN** call that is the source of data for the read operation.

<span id="BufferStruct"></span><span id="bufferstruct"></span><span id="BUFFERSTRUCT"></span>**BufferStruct**  
Specifies the buffer the read operation should place data in.

A subunit driver must first allocate an IRP and an [**AVC\_STREAM\_REQUEST\_BLOCK**](https://msdn.microsoft.com/library/windows/hardware/ff554194) structure. Next, it should use the [**INIT\_AVCSTRM\_HEADER**](https://msdn.microsoft.com/library/windows/hardware/ff560750) macro to initialize the AVC\_STREAM\_REQUEST\_BLOCK structure, passing **AVCSTRM\_READ** as the Request argument to the macro. Next, the subunit driver sets the **AVCStreamContext** member to the stream context (handle) of the stream that provides the data to be read. Finally, the subunit driver sets the **BufferStruct** member of the **CommandData** union that describes the buffer the read operation places data into.

To send this request, a subunit submits an [**IRP\_MJ\_INTERNAL\_DEVICE\_CONTROL**](https://msdn.microsoft.com/library/windows/hardware/ff550766) IRP with the **IoControlCode** member of the IRP set to [**IOCTL\_AVCSTRM\_CLASS**](https://msdn.microsoft.com/library/windows/hardware/ff560778) and the **Argument1** member of the IRP set to the AVC\_STREAM\_REQUEST\_BLOCK structure that describes the read operation to take place.

This command completes asynchronously. When it is completed, the I/O completion routine set in the IRP is called.

This function code must be called at IRQL = PASSIVE\_LEVEL.

### See Also

[**AVC\_STREAM\_REQUEST\_BLOCK**](https://msdn.microsoft.com/library/windows/hardware/ff554194), [**INIT\_AVCSTRM\_HEADER**](https://msdn.microsoft.com/library/windows/hardware/ff560750), [**IRP\_MJ\_INTERNAL\_DEVICE\_CONTROL**](https://msdn.microsoft.com/library/windows/hardware/ff550766), [**IOCTL\_AVCSTRM\_CLASS**](https://msdn.microsoft.com/library/windows/hardware/ff560778), [**AVCSTRM\_BUFFER\_STRUCT**](https://msdn.microsoft.com/library/windows/hardware/ff554108), [**AVCSTRM\_FUNCTION**](https://msdn.microsoft.com/library/windows/hardware/ff554120)

 

 





