---
title: SRB\_OPEN\_MASTER\_CLOCK
description: SRB\_OPEN\_MASTER\_CLOCK
ms.assetid: 1ccad1bc-27e7-4038-b341-389240051fb8
keywords: ["SRB_OPEN_MASTER_CLOCK Streaming Media Devices"]
topic_type:
- apiref
api_name:
- SRB_OPEN_MASTER_CLOCK
api_type:
- NA
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# SRB\_OPEN\_MASTER\_CLOCK


## <span id="ddk_srb_open_master_clock_ks"></span><span id="DDK_SRB_OPEN_MASTER_CLOCK_KS"></span>


The class driver issues this request to indicate to a stream that it now serves as the master clock for the minidriver.

### <span id="return_value"></span><span id="RETURN_VALUE"></span>Return Value

The minidriver should set one of the following as the status in the SRB:

<span id="STATUS_SUCCESS"></span><span id="status_success"></span>STATUS\_SUCCESS  
Indicates successful completion of the command.

<span id="STATUS_NOT_IMPLEMENTED"></span><span id="status_not_implemented"></span>STATUS\_NOT\_IMPLEMENTED  
Indicates that the function is not supported by the minidriver.

<span id="STATUS_IO_DEVICE_ERROR"></span><span id="status_io_device_error"></span>STATUS\_IO\_DEVICE\_ERROR  
Indicates that a hardware failure occurred.

### Comments

The class driver sets the **CommandData**.**MasterClockHandle** member pointed to by *pSrb* to the handle for the clock object it creates to represent the master clock. The *pSrb* pointer points to a [**HW\_STREAM\_REQUEST\_BLOCK**](https://msdn.microsoft.com/library/windows/hardware/ff559702) structure.

The minidriver should retain the **CommandData.MasterClockHandle** field value in the SRB that points to the handle of the master clock.

 

 





