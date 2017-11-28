---
title: SRB\_GET\_STREAM\_INFO
description: SRB\_GET\_STREAM\_INFO
ms.assetid: ff5412ee-6e4f-43f4-a90d-4a2bdfa5d4ae
keywords: ["SRB_GET_STREAM_INFO Streaming Media Devices"]
topic_type:
- apiref
api_name:
- SRB_GET_STREAM_INFO
api_type:
- NA
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

### <span id="comments"></span><span id="COMMENTS"></span>Comments

The class driver passes a buffer in *pSrb*-&gt;**CommandData.StreamBuffer** of the size specified by the minidriver in response to the class driver's [**SRB\_INITIALIZE\_DEVICE**](srb-initialize-device.md) request. The *pSrb* pointer points to a [**HW\_STREAM\_REQUEST\_BLOCK**](https://msdn.microsoft.com/library/windows/hardware/ff559702) structure. Also see [**PORT\_CONFIGURATION\_INFORMATION**](https://msdn.microsoft.com/library/windows/hardware/ff567785).

The minidriver fills **CommandData.StreamBuffer** with an [**HW\_STREAM\_DESCRIPTOR**](https://msdn.microsoft.com/library/windows/hardware/ff559686) that describes the device and the streams it supports. The size of this buffer is indicated by the minidriver in the **StreamDescriptorSize** field in the [**PORT\_CONFIGURATION\_INFORMATION**](https://msdn.microsoft.com/library/windows/hardware/ff567785) structure.

The class driver normally issues this request only once. The minidriver may force the class driver to reissue this request, to update its description of the supported streams, by calling [StreamClassReenumerateStreams](https://msdn.microsoft.com/library/windows/hardware/ff568256).

**When the SRB\_GET\_STREAM\_INFO command is received by the minidriver, the minidriver should:**

1.  Retrieve the pointers for the stream header and the stream information data structures. For example:
    ```
     PHW_STREAM_HEADER pstrhdr =
      (PHW_STREAM_HEADER)&amp;(pSrb->CommandData.StreamBuffer->StreamHeader);
     PHW_STREAM_INFORMATION pstrinfo =
      (PHW_STREAM_INFORMATION)&amp;(pSrb->CommandData.StreamBuffer->StreamInfo);
     
    ```

2.  Verify that the buffer is large enough to hold the returned data.

3.  Write the information to the buffer.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstream\stream%5D:%20SRB_GET_STREAM_INFO%20%20RELEASE:%20%2811/22/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




