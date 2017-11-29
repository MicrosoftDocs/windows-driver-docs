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
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
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

### <span id="comments"></span><span id="COMMENTS"></span>Comments

The minidriver should deallocate any resources it allocated, and disable the device's interrupts. (The class driver automatically deallocates any resources it allocated on behalf of the minidriver.)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstream\stream%5D:%20SRB_UNINITIALIZE_DEVICE%20%20RELEASE:%20%2811/22/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




