---
title: SRB\_CHANGE\_POWER\_STATE
description: SRB\_CHANGE\_POWER\_STATE
ms.assetid: 61a3e390-1ba2-44e0-b364-e86b10937cd6
keywords: ["SRB_CHANGE_POWER_STATE Streaming Media Devices"]
topic_type:
- apiref
api_name:
- SRB_CHANGE_POWER_STATE
api_type:
- NA
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# SRB\_CHANGE\_POWER\_STATE


## <span id="ddk_srb_change_power_state_ks"></span><span id="DDK_SRB_CHANGE_POWER_STATE_KS"></span>


The class driver sends this request to signal to the minidriver that it should reset its power state. *pSrb*-&gt;**DeviceState** specifies the new power state. See [**HW\_STREAM\_REQUEST\_BLOCK**](https://msdn.microsoft.com/library/windows/hardware/ff559702).

### <span id="return_value"></span><span id="RETURN_VALUE"></span>Return Value

The minidriver should set one of the following as the status in the SRB:

<span id="STATUS_SUCCESS"></span><span id="status_success"></span>STATUS\_SUCCESS  
Indicates successful completion of the command.

<span id="STATUS_NOT_IMPLEMENTED"></span><span id="status_not_implemented"></span>STATUS\_NOT\_IMPLEMENTED  
Indicates that the function is not supported by the minidriver.

<span id="STATUS_IO_DEVICE_ERROR"></span><span id="status_io_device_error"></span>STATUS\_IO\_DEVICE\_ERROR  
Indicates that a hardware failure occurred and low power cannot be invoked.

### Comments

If the minidriver needs to save or restore device-specific data it should do so when processing an SRB\_CHANGE\_POWER\_STATE request.

For more information about power states, see [Managing Power for Individual Devices](https://msdn.microsoft.com/library/windows/hardware/ff554397).

 

 





