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
ms.date: 11/28/2017
ms.localizationpriority: medium
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

### Comments

The class driver provides a [**HW\_STREAM\_OBJECT**](https://msdn.microsoft.com/library/windows/hardware/ff559697) buffer in *pSrb*-&gt;**StreamObject**, with *pSrb*-&gt;**StreamObject**-&gt;**StreamNumber** set to the number of the stream to be closed. The *pSrb* pointer points to a [**HW\_STREAM\_REQUEST\_BLOCK**](https://msdn.microsoft.com/library/windows/hardware/ff559702) structure. **StreamNumber** corresponds to the offset of the stream within the [**HW\_STREAM\_DESCRIPTOR**](https://msdn.microsoft.com/library/windows/hardware/ff559686) structure that the minidriver provides in response to a [**SRB\_GET\_STREAM\_INFO**](srb-get-stream-info.md) request.

If the minidriver successfully closes the stream, the minidriver returns STATUS\_SUCCESS. Otherwise, it returns an appropriate error status.

**When the SRB\_CLOSE\_STREAM command is received by the minidriver, the responding minidriver routine should:**

1.  Free any resources allocated by the minidriver when the stream was opened.

2.  Stop referencing the clock if a clock was used for the stream.

3.  Reset the stream state to Stop.

Note that a stream could be closed arbitrarily while streaming if an associated user-mode application crashes. Therefore, you must release all outstanding resources for the stream, complete all pending SRBs for the stream, and put the stream back into a quiescent state.

 

 





