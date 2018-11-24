---
title: SRB\_SET\_STREAM\_STATE
description: SRB\_SET\_STREAM\_STATE
ms.assetid: 8dd1237c-3b3e-4207-96b8-22311968c3a0
keywords: ["SRB_SET_STREAM_STATE Streaming Media Devices"]
topic_type:
- apiref
api_name:
- SRB_SET_STREAM_STATE
api_type:
- NA
ms.date: 11/28/2017
ms.localizationpriority: medium
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

### Comments

The class driver specifies the new stream state in *pSrb*-&gt;**CommandData**.**StreamState**. The *pSrb* pointer points to a [**HW\_STREAM\_REQUEST\_BLOCK**](https://msdn.microsoft.com/library/windows/hardware/ff559702) structure. See [**KSPROPERTY\_CONNECTION\_STATE**](ksproperty-connection-state.md) for a description of stream states.

The minidriver should set the stream to the specified state and return STATUS\_SUCCESS if successful. An appropriate error code should be returned if the operation fails.

## See also


[SRB\_GET\_STREAM\_STATE](srb-get-stream-state.md)

 

 






