---
title: SRB\_OPEN\_DEVICE\_INSTANCE
description: SRB\_OPEN\_DEVICE\_INSTANCE
ms.assetid: 71f57abd-7875-4c7a-bbb3-c5c45c9a83ab
keywords: ["SRB_OPEN_DEVICE_INSTANCE Streaming Media Devices"]
topic_type:
- apiref
api_name:
- SRB_OPEN_DEVICE_INSTANCE
api_type:
- NA
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# SRB\_OPEN\_DEVICE\_INSTANCE


## <span id="ddk_srb_open_device_instance_ks"></span><span id="DDK_SRB_OPEN_DEVICE_INSTANCE_KS"></span>


The class driver sends this request to open an instance of the adapter.

### <span id="return_value"></span><span id="RETURN_VALUE"></span>Return Value

The minidriver should set one of the following as the status in the SRB:

<span id="STATUS_SUCCESS"></span><span id="status_success"></span>STATUS\_SUCCESS  
Indicates successful completion of the command.

<span id="STATUS_NOT_IMPLEMENTED"></span><span id="status_not_implemented"></span>STATUS\_NOT\_IMPLEMENTED  
Indicates that the function is not supported by the minidriver.

<span id="STATUS_TOO_MANY_NODES"></span><span id="status_too_many_nodes"></span>STATUS\_TOO\_MANY\_NODES  
Indicates that there are not enough resources to open this stream.

<span id="STATUS_IO_DEVICE_ERROR"></span><span id="status_io_device_error"></span>STATUS\_IO\_DEVICE\_ERROR  
Indicates that a hardware failure occurred.

### Comments

If the minidriver supports multiple instances of a device, this command is sent by the class driver each time a new instance of the adapter is opened. As an example, consider a DSP decoder that can allocate *n* number of instances of the streams specified. The **HwInstanceExtension** field in the SRB should then be set to the minidriver's per-instance workspace by the class driver.

Most adapters do not support multiple instances, so in those cases the **FilterInstanceExtensionSize** field in the **HW\_INITIALIZATION\_DATA** structure should be set to zero and should never receive this command.

## See also


[**SRB\_CLOSE\_DEVICE\_INSTANCE**](srb-close-device-instance.md)

 

 






