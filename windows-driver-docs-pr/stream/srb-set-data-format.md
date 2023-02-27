---
title: SRB\_SET\_DATA\_FORMAT
description: SRB\_SET\_DATA\_FORMAT
keywords: ["SRB_SET_DATA_FORMAT Streaming Media Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- SRB_SET_DATA_FORMAT
api_type:
- NA
ms.date: 11/28/2017
---

# SRB\_SET\_DATA\_FORMAT


## <span id="ddk_srb_set_data_format_ks"></span><span id="DDK_SRB_SET_DATA_FORMAT_KS"></span>


The class driver issues this request to set the data format for the stream.

### <span id="return_value"></span><span id="RETURN_VALUE"></span>Return Value

<span id="STATUS_SUCCESS"></span><span id="status_success"></span>STATUS\_SUCCESS  
Indicates successful completion of the command.

<span id="STATUS_NOT_SUPPORTED"></span><span id="status_not_supported"></span>STATUS\_NOT\_SUPPORTED  
Indicates that the minidriver does not support the requested data format.

### Comments

The class driver passes the new data format in the **CommandData**.**OpenFormat** member of the *pSrb* pointer. (This pointer points to a [**HW\_STREAM\_REQUEST\_BLOCK**](/windows-hardware/drivers/ddi/strmini/ns-strmini-_hw_stream_request_block) structure.)

For more information about data formats, see the [Stream Class Minidriver Design Guide](./streaming-minidrivers2.md). Also see [Data Range Intersections in AVStream](./data-range-intersections-in-avstream.md).

 

