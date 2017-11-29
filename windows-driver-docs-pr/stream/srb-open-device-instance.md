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
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
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

### <span id="comments"></span><span id="COMMENTS"></span>Comments

If the minidriver supports multiple instances of a device, this command is sent by the class driver each time a new instance of the adapter is opened. As an example, consider a DSP decoder that can allocate *n* number of instances of the streams specified. The **HwInstanceExtension** field in the SRB should then be set to the minidriver's per-instance workspace by the class driver.

Most adapters do not support multiple instances, so in those cases the **FilterInstanceExtensionSize** field in the **HW\_INITIALIZATION\_DATA** structure should be set to zero and should never receive this command.

## <span id="see_also"></span>See also


[**SRB\_CLOSE\_DEVICE\_INSTANCE**](srb-close-device-instance.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstream\stream%5D:%20SRB_OPEN_DEVICE_INSTANCE%20%20RELEASE:%20%2811/22/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





