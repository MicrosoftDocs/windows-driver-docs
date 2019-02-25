---
title: SRB\_READ\_DATA
description: SRB\_READ\_DATA
ms.assetid: b59d705d-5215-42ee-85cf-369a2e69f99b
keywords: ["SRB_READ_DATA Streaming Media Devices"]
topic_type:
- apiref
api_name:
- SRB_READ_DATA
api_type:
- NA
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# SRB\_READ\_DATA


## <span id="ddk_srb_read_data_ks"></span><span id="DDK_SRB_READ_DATA_KS"></span>


The class driver has received a read request for the minidriver.

### <span id="return_value"></span><span id="RETURN_VALUE"></span>Return Value

The minidriver can set one of the following as the status in the SRB, or it can pass additional error codes to indicate error situations such as memory errors and bad parameters. The class driver checks only for STATUS\_SUCCESS.

<span id="STATUS_SUCCESS"></span><span id="status_success"></span>STATUS\_SUCCESS  
Indicates successful completion of the command.

<span id="STATUS_NOT_IMPLEMENTED"></span><span id="status_not_implemented"></span>STATUS\_NOT\_IMPLEMENTED  
Indicates that the function is not supported by the minidriver.

<span id="STATUS_IO_DEVICE_ERROR"></span><span id="status_io_device_error"></span>STATUS\_IO\_DEVICE\_ERROR  
Indicates that a hardware failure occurred.

### Comments

The value of *pSrb*-&gt;**CommandData**.**DataBufferArray** points to an array of [**KSSTREAM\_HEADER**](https://msdn.microsoft.com/library/windows/hardware/ff567138) structures, which together describe the data buffer. The *pSrb* pointer points to a [**HW\_STREAM\_REQUEST\_BLOCK**](https://msdn.microsoft.com/library/windows/hardware/ff559702) structure. *pSrb*-&gt;**CommandData**.**NumberOfBuffers** specifies the size of the array.

**When the SRB\_READ\_DATA command is received by the minidriver, the responding minidriver routine should:**

1.  Check to determine the current stream state. The minidriver should only accept read requests when in either the Pause or Run state. If the stream is stopped, it should immediately complete and return the SRB.

2.  Place the SRB in the queue.

 

 





