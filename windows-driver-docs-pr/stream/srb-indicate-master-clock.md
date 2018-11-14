---
title: SRB\_INDICATE\_MASTER\_CLOCK
description: SRB\_INDICATE\_MASTER\_CLOCK
ms.assetid: 76ce59d2-d33c-4cec-a90e-563a16dc476b
keywords: ["SRB_INDICATE_MASTER_CLOCK Streaming Media Devices"]
topic_type:
- apiref
api_name:
- SRB_INDICATE_MASTER_CLOCK
api_type:
- NA
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# SRB\_INDICATE\_MASTER\_CLOCK


## <span id="ddk_srb_indicate_master_clock_ks"></span><span id="DDK_SRB_INDICATE_MASTER_CLOCK_KS"></span>


The class driver issues this request to indicate to a stream the handle for the clock object that now serves as its master clock, or a zero handle to indicate the stream is free running.

### <span id="return_value"></span><span id="RETURN_VALUE"></span>Return Value

The minidriver should set one of the following as the status in the SRB:

<span id="STATUS_SUCCESS"></span><span id="status_success"></span>STATUS\_SUCCESS  
Indicates successful completion of the command.

<span id="STATUS_NOT_IMPLEMENTED"></span><span id="status_not_implemented"></span>STATUS\_NOT\_IMPLEMENTED  
Indicates that the function is not supported by the minidriver.

<span id="STATUS_IO_DEVICE_ERROR"></span><span id="status_io_device_error"></span>STATUS\_IO\_DEVICE\_ERROR  
Indicates that a hardware failure occurred.

### Comments

The class driver sets the **CommandData**.**MasterClockHandle** member pointed to by *pSrb* to the handle for the clock object that represents the master clock. The *pSrb* pointer points to a [**HW\_STREAM\_REQUEST\_BLOCK**](https://msdn.microsoft.com/library/windows/hardware/ff559702) structure.

A stream may query the time value of the master clock by passing the master clock handle to [**StreamClassQueryMasterClock**](https://msdn.microsoft.com/library/windows/hardware/ff568249) or [**StreamClassQueryMasterClockSync**](https://msdn.microsoft.com/library/windows/hardware/ff568251).

Until the minidriver receives a SRB\_INDICATE\_MASTER\_CLOCK for a particular stream, it can assume that the stream is free running. If the handle passed in this SRB for a subordinate pin is the same as the handle passed to the minidriver in [**SRB\_OPEN\_MASTER\_CLOCK**](srb-open-master-clock.md), the minidriver can read the time directly from the master clock because it controls the master and the subordinate.

The minidriver should retain the **CommandData.MasterClockHandle** field in the SRB that points to the handle for the master clock. If this handle is zero, it indicates to the minidriver that this stream is now free running and cannot be subordinate to a master clock.

 

 





