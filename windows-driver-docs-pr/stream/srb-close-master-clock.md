---
title: SRB_CLOSE_MASTER_CLOCK
description: SRB\_CLOSE\_MASTER\_CLOCK
keywords: ["SRB_CLOSE_MASTER_CLOCK Streaming Media Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- SRB_CLOSE_MASTER_CLOCK
api_type:
- NA
ms.date: 11/28/2017
---

# SRB\_CLOSE\_MASTER\_CLOCK


## <span id="ddk_srb_close_master_clock_ks"></span><span id="DDK_SRB_CLOSE_MASTER_CLOCK_KS"></span>


The class driver issues this request to indicate to a stream that it is no longer the master clock for the minidriver.

### <span id="return_value"></span><span id="RETURN_VALUE"></span>Return Value

The minidriver should set one of the following as the status in the SRB:

<span id="STATUS_SUCCESS"></span><span id="status_success"></span>STATUS\_SUCCESS  
Indicates successful completion of the command.

<span id="STATUS_NOT_IMPLEMENTED"></span><span id="status_not_implemented"></span>STATUS\_NOT\_IMPLEMENTED  
Indicates that the function is not supported by the minidriver.

<span id="STATUS_IO_DEVICE_ERROR"></span><span id="status_io_device_error"></span>STATUS\_IO\_DEVICE\_ERROR  
Indicates that a hardware failure occurred.

 

 





