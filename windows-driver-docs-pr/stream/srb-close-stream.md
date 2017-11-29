---
title: SRB\_CLOSE\_STREAM
description: SRB\_CLOSE\_STREAM
ms.assetid: e118ddd7-fe0e-4834-9ae6-19eef0348b2c
keywords: ["SRB_CLOSE_STREAM Streaming Media Devices"]
topic_type:
- apiref
api_name:
- SRB_CLOSE_STREAM
api_type:
- NA
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# SRB\_CLOSE\_STREAM


## <span id="ddk_srb_close_stream_ks"></span><span id="DDK_SRB_CLOSE_STREAM_KS"></span>


The class driver sends this request to close a stream.

### <span id="return_value"></span><span id="RETURN_VALUE"></span>Return Value

The minidriver should set one of the following as the status in the SRB:

<span id="STATUS_SUCCESS"></span><span id="status_success"></span>STATUS\_SUCCESS  
Indicates successful completion of the command.

<span id="STATUS_NOT_IMPLEMENTED"></span><span id="status_not_implemented"></span>STATUS\_NOT\_IMPLEMENTED  
Indicates that the function is not supported by the minidriver.

<span id="STATUS_IO_DEVICE_ERROR"></span><span id="status_io_device_error"></span>STATUS\_IO\_DEVICE\_ERROR  
Indicates that a hardware failure occurred.

### <span id="comments"></span><span id="COMMENTS"></span>Comments

The class driver provides a [**HW\_STREAM\_OBJECT**](https://msdn.microsoft.com/library/windows/hardware/ff559697) buffer in *pSrb*-&gt;**StreamObject**, with *pSrb*-&gt;**StreamObject**-&gt;**StreamNumber** set to the number of the stream to be closed. The *pSrb* pointer points to a [**HW\_STREAM\_REQUEST\_BLOCK**](https://msdn.microsoft.com/library/windows/hardware/ff559702) structure. **StreamNumber** corresponds to the offset of the stream within the [**HW\_STREAM\_DESCRIPTOR**](https://msdn.microsoft.com/library/windows/hardware/ff559686) structure that the minidriver provides in response to a [**SRB\_GET\_STREAM\_INFO**](srb-get-stream-info.md) request.

If the minidriver successfully closes the stream, the minidriver returns STATUS\_SUCCESS. Otherwise, it returns an appropriate error status.

**When the SRB\_CLOSE\_STREAM command is received by the minidriver, the responding minidriver routine should:**

1.  Free any resources allocated by the minidriver when the stream was opened.

2.  Stop referencing the clock if a clock was used for the stream.

3.  Reset the stream state to Stop.

Note that a stream could be closed arbitrarily while streaming if an associated user-mode application crashes. Therefore, you must release all outstanding resources for the stream, complete all pending SRBs for the stream, and put the stream back into a quiescent state.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstream\stream%5D:%20SRB_CLOSE_STREAM%20%20RELEASE:%20%2811/22/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




