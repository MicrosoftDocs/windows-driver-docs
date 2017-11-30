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
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
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

### <span id="comments"></span><span id="COMMENTS"></span>Comments

The class driver sets the **CommandData**.**MasterClockHandle** member pointed to by *pSrb* to the handle for the clock object that represents the master clock. The *pSrb* pointer points to a [**HW\_STREAM\_REQUEST\_BLOCK**](https://msdn.microsoft.com/library/windows/hardware/ff559702) structure.

A stream may query the time value of the master clock by passing the master clock handle to [**StreamClassQueryMasterClock**](https://msdn.microsoft.com/library/windows/hardware/ff568249) or [**StreamClassQueryMasterClockSync**](https://msdn.microsoft.com/library/windows/hardware/ff568251).

Until the minidriver receives a SRB\_INDICATE\_MASTER\_CLOCK for a particular stream, it can assume that the stream is free running. If the handle passed in this SRB for a subordinate pin is the same as the handle passed to the minidriver in [**SRB\_OPEN\_MASTER\_CLOCK**](srb-open-master-clock.md), the minidriver can read the time directly from the master clock because it controls the master and the subordinate.

The minidriver should retain the **CommandData.MasterClockHandle** field in the SRB that points to the handle for the master clock. If this handle is zero, it indicates to the minidriver that this stream is now free running and cannot be subordinate to a master clock.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstream\stream%5D:%20SRB_INDICATE_MASTER_CLOCK%20%20RELEASE:%20%2811/22/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




