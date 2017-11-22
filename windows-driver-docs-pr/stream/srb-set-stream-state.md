---
title: SRB\_SET\_STREAM\_STATE
description: SRB\_SET\_STREAM\_STATE
MS-HAID:
- 'strclass-srbs\_3909096d-3edb-463f-ad46-160400b2ca44.xml'
- 'stream.srb\_set\_stream\_state'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 8dd1237c-3b3e-4207-96b8-22311968c3a0
keywords: ["SRB_SET_STREAM_STATE Streaming Media Devices"]
topic_type:
- apiref
api_name:
- SRB_SET_STREAM_STATE
api_type:
- NA
---

# SRB\_SET\_STREAM\_STATE


## <span id="ddk_srb_set_stream_state_ks"></span><span id="DDK_SRB_SET_STREAM_STATE_KS"></span>


The class driver sends this request to set the stream state for this stream.

### <span id="return_value"></span><span id="RETURN_VALUE"></span>Return Value

The minidriver should set one of the following as the status in the SRB:

<span id="STATUS_SUCCESS"></span><span id="status_success"></span>STATUS\_SUCCESS  
Indicates successful completion of the command.

<span id="STATUS_NOT_IMPLEMENTED"></span><span id="status_not_implemented"></span>STATUS\_NOT\_IMPLEMENTED  
Indicates that the function is not supported by the minidriver.

<span id="STATUS_IO_DEVICE_ERROR"></span><span id="status_io_device_error"></span>STATUS\_IO\_DEVICE\_ERROR  
Indicates that a hardware failure occurred.

### <span id="comments"></span><span id="COMMENTS"></span>Comments

The class driver specifies the new stream state in *pSrb*-&gt;**CommandData**.**StreamState**. The *pSrb* pointer points to a [**HW\_STREAM\_REQUEST\_BLOCK**](https://msdn.microsoft.com/library/windows/hardware/ff559702) structure. See [**KSPROPERTY\_CONNECTION\_STATE**](ksproperty-connection-state.md) for a description of stream states.

The minidriver should set the stream to the specified state and return STATUS\_SUCCESS if successful. An appropriate error code should be returned if the operation fails.

## <span id="see_also"></span>See also


[SRB\_GET\_STREAM\_STATE](srb-get-stream-state.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstream\stream%5D:%20SRB_SET_STREAM_STATE%20%20RELEASE:%20%2811/22/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





