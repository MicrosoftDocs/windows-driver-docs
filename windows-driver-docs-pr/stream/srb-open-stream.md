---
title: SRB\_OPEN\_STREAM
description: SRB\_OPEN\_STREAM
ms.assetid: 53732add-e304-4128-9235-525ff073d777
keywords: ["SRB_OPEN_STREAM Streaming Media Devices"]
topic_type:
- apiref
api_name:
- SRB_OPEN_STREAM
api_type:
- NA
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# SRB\_OPEN\_STREAM


## <span id="ddk_srb_open_stream_ks"></span><span id="DDK_SRB_OPEN_STREAM_KS"></span>


The class driver sends this request to open a stream.

### <span id="return_value"></span><span id="RETURN_VALUE"></span>Return Value

The minidriver should set one of the following as the status in the SRB:

<span id="STATUS_SUCCESS"></span><span id="status_success"></span>STATUS\_SUCCESS  
Indicates successful completion of the command.

<span id="STATUS_NOT_IMPLEMENTED"></span><span id="status_not_implemented"></span>STATUS\_NOT\_IMPLEMENTED  
Indicates that the function is not supported by the minidriver.

<span id="STATUS_TOO_MANY_NODES"></span><span id="status_too_many_nodes"></span>STATUS\_TOO\_MANY\_NODES  
Indicates that there are not enough resources to open this stream.

<span id="STATUS_IO_DEVICE_ERROR"></span><span id="status_io_device_error"></span>STATUS\_IO\_DEVICE\_ERROR  
Indicates that a hardware failure occurred.

### Comments

The class driver provides a [**HW\_STREAM\_OBJECT**](https://msdn.microsoft.com/library/windows/hardware/ff559697) buffer in *pSrb*-&gt;**StreamObject**, with *pSrb*-&gt;**StreamObject**-&gt;**StreamNumber** set to the number of the stream to be opened. The *pSrb* pointer points to a [**HW\_STREAM\_REQUEST\_BLOCK**](https://msdn.microsoft.com/library/windows/hardware/ff559702) structure. **StreamNumber** corresponds to the offset of the stream within the [**HW\_STREAM\_DESCRIPTOR**](https://msdn.microsoft.com/library/windows/hardware/ff559686) structure the minidriver provides in response to a [**SRB\_GET\_STREAM\_INFO**](srb-get-stream-info.md) request. The class driver specifies the data format that the opened stream should provide in *pSrb*-&gt;**CommandData**-&gt;**OpenFormat**.

When the minidriver receives this request, it should determine if the specified stream can be opened at this time. The minidriver should also verify the [**KSDATAFORMAT**](https://msdn.microsoft.com/library/windows/hardware/ff561656) format passed in. the SRB's OpenFormat field. If the stream can be opened, the minidriver updates the HW\_STREAM\_OBJECT structure, and returns STATUS\_SUCCESS. If the maximum number of stream instances are already open, or the hardware resources necessary to open this stream are unavailable, the minidriver returns an appropriate error status.

**When the SRB\_OPEN\_STREAM command is received by the minidriver, the minidriver should:**

1.  Check that the maximum number of stream instances has not been exceeded and that the stream index value is valid.

2.  Check that the data format requested is valid for this stream.

3.  Set the format for the stream.

4.  Maintain an array of all the stream extension structures in the device extension so that IRPs can be canceled from any stream.

5.  Specify pointers, in the stream object, to the stream data handlers and control handlers.

6.  Set the DMA flag in the stream object if the device will perform DMA directly to the data buffer addresses passed into the **ReceiveDataPacket** routines. If the driver accesses data buffers passed in using logical addressing, also set the PIO flag in the stream object.

7.  If clock support is available on the stream, indicate this through the **HwClockObject** member in the stream object.

 

 





