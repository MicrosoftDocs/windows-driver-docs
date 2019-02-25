---
title: SRB\_WRITE\_DATA
description: SRB\_WRITE\_DATA
ms.assetid: f7867185-3f1b-4c83-b23a-5b2b4ce6e484
keywords: ["SRB_WRITE_DATA Streaming Media Devices"]
topic_type:
- apiref
api_name:
- SRB_WRITE_DATA
api_type:
- NA
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# SRB\_WRITE\_DATA


## <span id="ddk_srb_write_data_ks"></span><span id="DDK_SRB_WRITE_DATA_KS"></span>


The class driver has received a write request for the minidriver. The value of *pSrb*-&gt;**CommandData**.**DataBufferArray** points to an array of [**KSSTREAM\_HEADER**](https://msdn.microsoft.com/library/windows/hardware/ff567138) structures, which together describe the data buffer. The value of *pSrb*-&gt;**CommandData**.**NumberOfBuffers** specifies the size of the array. The *pSrb* pointer points to a [**HW\_STREAM\_REQUEST\_BLOCK**](https://msdn.microsoft.com/library/windows/hardware/ff559702) structure.

### <span id="return_value"></span><span id="RETURN_VALUE"></span>Return Value

The minidriver can set one of the following as status in the SRB, or it can pass additional error codes to indicate error situations such as memory errors and bad parameters. The class driver is concerned only with STATUS\_SUCCESS.

<span id="STATUS_SUCCESS"></span><span id="status_success"></span>STATUS\_SUCCESS  
Indicates successful completion of the command.

<span id="STATUS_NOT_IMPLEMENTED"></span><span id="status_not_implemented"></span>STATUS\_NOT\_IMPLEMENTED  
Indicates that the function is not supported by the minidriver.

<span id="STATUS_IO_DEVICE_ERROR"></span><span id="status_io_device_error"></span>STATUS\_IO\_DEVICE\_ERROR  
Indicates that a hardware failure occurred.

## See also


[**SRB\_SET\_STREAM\_STATE**](srb-set-stream-state.md)

 

 






