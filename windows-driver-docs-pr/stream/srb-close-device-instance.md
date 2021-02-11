---
title: SRB\_CLOSE\_DEVICE\_INSTANCE
description: SRB\_CLOSE\_DEVICE\_INSTANCE
keywords: ["SRB_CLOSE_DEVICE_INSTANCE Streaming Media Devices"]
topic_type:
- apiref
api_name:
- SRB_CLOSE_DEVICE_INSTANCE
api_type:
- NA
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# SRB\_CLOSE\_DEVICE\_INSTANCE


## <span id="ddk_srb_close_device_instance_ks"></span><span id="DDK_SRB_CLOSE_DEVICE_INSTANCE_KS"></span>


The class driver sends this request to close a previously opened instance of the adapter.

### <span id="return_value"></span><span id="RETURN_VALUE"></span>Return Value

The minidriver should set one of the following as the status in the SRB:

<span id="STATUS_SUCCESS"></span><span id="status_success"></span>STATUS\_SUCCESS  
Indicates successful completion of the command.

<span id="STATUS_NOT_IMPLEMENTED"></span><span id="status_not_implemented"></span>STATUS\_NOT\_IMPLEMENTED  
Indicates that the function is not supported by the minidriver.

<span id="STATUS_IO_DEVICE_ERROR"></span><span id="status_io_device_error"></span>STATUS\_IO\_DEVICE\_ERROR  
Indicates that a hardware failure occurred.

### Comments

Most adapters do not support multiple instances, so in those cases the **FilterInstanceExtensionSize** field in the [**HW\_INITIALIZATION\_DATA**](/windows-hardware/drivers/ddi/strmini/ns-strmini-_hw_initialization_data) structure should be set to zero and should never receive this command.

 

