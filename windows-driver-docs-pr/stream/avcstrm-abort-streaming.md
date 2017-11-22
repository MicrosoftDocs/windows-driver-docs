---
title: AVCSTRM\_ABORT\_STREAMING
description: AVCSTRM\_ABORT\_STREAMING
MS-HAID:
- 'avcsref\_516488e1-d3b2-4975-aa2e-62fa2bbc1442.xml'
- 'stream.avcstrm\_abort\_streaming'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 9a136511-c838-456f-87c5-a4639be0c299
keywords: ["AVCSTRM_ABORT_STREAMING Streaming Media Devices"]
topic_type:
- apiref
api_name:
- AVCSTRM_ABORT_STREAMING
api_type:
- NA
---

# AVCSTRM\_ABORT\_STREAMING


## <span id="ddk_avcstrm_abort_streaming_ks"></span><span id="DDK_AVCSTRM_ABORT_STREAMING_KS"></span>


The **AVCSTRM\_ABORT\_STREAMING** function code cancels *all* the pending data requests and frees the resources used.

### <span id="i_o_status_block"></span><span id="I_O_STATUS_BLOCK"></span>I/O Status Block

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

 

### <span id="comments"></span><span id="COMMENTS"></span>Comments

Note, this functionality cancels *all* streaming IRPs. To cancel an individual IRP, use [**IoCancelIrp**](https://msdn.microsoft.com/library/windows/hardware/ff548338).

A subunit should call this when its target device is removed or the original data IRP is canceled to stop stream operation.

This function does not use any member of the **CommandData** union in the AVC\_STREAM\_REQUEST\_BLOCK structure.

```
typedef struct _AVC_STREAM_REQUEST_BLOCK {
  ULONG  SizeOfThisBlock;
  ULONG  Version;
  AVCSTRM_FUNCTION  Function;
  .
  .
  PVOID AVCStreamContext;
  .
  .
} AVC_STREAM_REQUEST_BLOCK, *PAVC_STREAM_REQUEST_BLOCK;
```

### <span id="requirements"></span><span id="REQUIREMENTS"></span>Requirements

**Headers:** Declared in *avcstrm.h*. Include *avcstrm.h*.

### <span id="avc_stream_request_block_input"></span><span id="AVC_STREAM_REQUEST_BLOCK_INPUT"></span>AVC\_STREAM\_REQUEST\_BLOCK Input

<span id="SizeOfThisBlock__Version_and_Function"></span><span id="sizeofthisblock__version_and_function"></span><span id="SIZEOFTHISBLOCK__VERSION_AND_FUNCTION"></span>**SizeOfThisBlock, Version and Function**  
Use the [**INIT\_AVCSTRM\_HEADER**](https://msdn.microsoft.com/library/windows/hardware/ff560750) macro to initialize these members. Pass **AVCSTRM\_ABORT\_STREAMING** in the Request argument of the macro.

<span id="AVCStreamContext"></span><span id="avcstreamcontext"></span><span id="AVCSTREAMCONTEXT"></span>**AVCStreamContext**  
Specifies the stream context (handle) returned by an earlier **AVCSTRM\_OPEN** call that is the target for the data write operation.

A subunit driver must first allocate an IRP and an [**AVC\_STREAM\_REQUEST\_BLOCK**](https://msdn.microsoft.com/library/windows/hardware/ff554194) structure. Next, it should use the [**INIT\_AVCSTRM\_HEADER**](https://msdn.microsoft.com/library/windows/hardware/ff560750) macro to initialize the AVC\_STREAM\_REQUEST\_BLOCK structure, passing **AVCSTRM\_READ** as the Request argument to the macro. Next, the subunit driver sets the **AVCStreamContext** member to the stream context (handle) of the stream to abort streaming.

To send this request, a subunit submits an [**IRP\_MJ\_INTERNAL\_DEVICE\_CONTROL**](https://msdn.microsoft.com/library/windows/hardware/ff550766) IRP with the **IoControlCode** member of the IRP set to [**IOCTL\_AVCSTRM\_CLASS**](https://msdn.microsoft.com/library/windows/hardware/ff560778) and the **Argument1** member of the IRP set to the AVC\_STREAM\_REQUEST\_BLOCK structure that describes the abort streaming operation to take place.

This function code must be called at PASSIVE\_LEVEL. When a data IRP is being canceled, it can be executed at DISPATCH\_LEVEL. In this case, a subunit should start a work item and call this function in its work item routine, which is executing at the PASSIVE\_LEVEL.

### <span id="see_also"></span><span id="SEE_ALSO"></span>See Also

[**INIT\_AVCSTRM\_HEADER**](https://msdn.microsoft.com/library/windows/hardware/ff560750), [**IRP\_MJ\_INTERNAL\_DEVICE\_CONTROL**](https://msdn.microsoft.com/library/windows/hardware/ff550766), [**IOCTL\_AVCSTRM\_CLASS**](https://msdn.microsoft.com/library/windows/hardware/ff560778), [**AVCSTRM\_FUNCTION**](https://msdn.microsoft.com/library/windows/hardware/ff554120)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstream\stream%5D:%20AVCSTRM_ABORT_STREAMING%20%20RELEASE:%20%2811/22/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




