---
title: SRB\_GET\_STREAM\_INFO
description: SRB\_GET\_STREAM\_INFO
keywords: ["SRB_GET_STREAM_INFO Streaming Media Devices"]
topic_type:
- apiref
api_name:
- SRB_GET_STREAM_INFO
api_type:
- NA
ms.date: 11/28/2017
---

# SRB\_GET\_STREAM\_INFO


## <span id="ddk_srb_get_stream_info_ks"></span><span id="DDK_SRB_GET_STREAM_INFO_KS"></span>


The class driver sends this request to obtain a description of the device and the streams it supports.

### <span id="return_value"></span><span id="RETURN_VALUE"></span>Return Value

The minidriver should set one of the following as the status in the SRB:

<span id="STATUS_SUCCESS"></span><span id="status_success"></span>STATUS\_SUCCESS  
Indicates successful completion of the command.

<span id="STATUS_IO_DEVICE_ERROR"></span><span id="status_io_device_error"></span>STATUS\_IO\_DEVICE\_ERROR  
Indicates that a hardware failure occurred.

### Comments

The class driver passes a buffer in *pSrb*-&gt;**CommandData.StreamBuffer** of the size specified by the minidriver in response to the class driver's [**SRB\_INITIALIZE\_DEVICE**](srb-initialize-device.md) request. The *pSrb* pointer points to a [**HW\_STREAM\_REQUEST\_BLOCK**](/windows-hardware/drivers/ddi/strmini/ns-strmini-_hw_stream_request_block) structure. Also see [**PORT\_CONFIGURATION\_INFORMATION**](/windows-hardware/drivers/ddi/strmini/ns-strmini-_port_configuration_information).

The minidriver fills **CommandData.StreamBuffer** with an [**HW\_STREAM\_DESCRIPTOR**](/windows-hardware/drivers/ddi/strmini/ns-strmini-_hw_stream_descriptor) that describes the device and the streams it supports. The size of this buffer is indicated by the minidriver in the **StreamDescriptorSize** field in the [**PORT\_CONFIGURATION\_INFORMATION**](/windows-hardware/drivers/ddi/strmini/ns-strmini-_port_configuration_information) structure.

The class driver normally issues this request only once. The minidriver may force the class driver to reissue this request, to update its description of the supported streams, by calling [StreamClassReenumerateStreams](/windows-hardware/drivers/ddi/strmini/nf-strmini-streamclassreenumeratestreams).

**When the SRB\_GET\_STREAM\_INFO command is received by the minidriver, the minidriver should:**

1.  Retrieve the pointers for the stream header and the stream information data structures. For example:

    ```cpp
     PHW_STREAM_HEADER pstrhdr =
      (PHW_STREAM_HEADER)&(pSrb->CommandData.StreamBuffer->StreamHeader);
     PHW_STREAM_INFORMATION pstrinfo =
      (PHW_STREAM_INFORMATION)&(pSrb->CommandData.StreamBuffer->StreamInfo);
     
    ```

2.  Verify that the buffer is large enough to hold the returned data.

3.  Write the information to the buffer.
