---
title: SRB\_UNINITIALIZE\_DEVICE
description: SRB\_UNINITIALIZE\_DEVICE
ms.assetid: 2cacb65a-8df3-4649-bc44-1bc7a5c598b9
keywords: ["SRB_UNINITIALIZE_DEVICE Streaming Media Devices"]
topic_type:
- apiref
api_name:
- SRB_UNINITIALIZE_DEVICE
api_type:
- NA
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# SRB\_UNINITIALIZE\_DEVICE


## <span id="ddk_srb_uninitialize_device_ks"></span><span id="DDK_SRB_UNINITIALIZE_DEVICE_KS"></span>


The class driver sends this request to signal the minidriver to disable itself.

### <span id="return_value"></span><span id="RETURN_VALUE"></span>Return Value

The minidriver should set one of the following as the status in the SRB:

<span id="STATUS_SUCCESS"></span><span id="status_success"></span>STATUS\_SUCCESS  
Indicates successful completion of the command.

<span id="STATUS_NOT_IMPLEMENTED"></span><span id="status_not_implemented"></span>STATUS\_NOT\_IMPLEMENTED  
Indicates that the function is not supported by the minidriver.

<span id="STATUS_ADAPTER_HARDWARE_ERROR"></span><span id="status_adapter_hardware_error"></span>STATUS\_ADAPTER\_HARDWARE\_ERROR  
Indicates that the minidriver cannot uninitialize at this time.

### Comments

The minidriver should deallocate any resources it allocated, and disable the device's interrupts. (The class driver automatically deallocates any resources it allocated on behalf of the minidriver.)

 

 





