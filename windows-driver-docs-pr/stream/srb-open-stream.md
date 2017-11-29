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
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
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

### <span id="comments"></span><span id="COMMENTS"></span>Comments

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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstream\stream%5D:%20SRB_OPEN_STREAM%20%20RELEASE:%20%2811/22/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




