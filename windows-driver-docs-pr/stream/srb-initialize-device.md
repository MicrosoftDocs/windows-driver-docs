---
title: SRB\_INITIALIZE\_DEVICE
description: SRB\_INITIALIZE\_DEVICE
ms.assetid: a4e35253-43d8-4d11-8a5b-72a9863f6677
keywords: ["SRB_INITIALIZE_DEVICE Streaming Media Devices"]
topic_type:
- apiref
api_name:
- SRB_INITIALIZE_DEVICE
api_type:
- NA
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# SRB\_INITIALIZE\_DEVICE


## <span id="ddk_srb_initialize_device_ks"></span><span id="DDK_SRB_INITIALIZE_DEVICE_KS"></span>


The class driver sends this request when it begins initializing the minidriver's hardware.

### <span id="return_value"></span><span id="RETURN_VALUE"></span>Return Value

The minidriver should set one of the following as the status in the SRB:

<span id="STATUS_SUCCESS"></span><span id="status_success"></span>STATUS\_SUCCESS  
Indicates that a host adapter was found and the configuration information was successfully determined.

<span id="STATUS_IO_DEVICE_ERROR"></span><span id="status_io_device_error"></span>STATUS\_IO\_DEVICE\_ERROR  
Indicates that a host adapter was found, but there was an error in obtaining the configuration information. If possible, the error should be logged.

<span id="STATUS_NO_SUCH_DEVICE"></span><span id="status_no_such_device"></span>STATUS\_NO\_SUCH\_DEVICE  
Indicates that the supplied configuration information was invalid.

### <span id="comments"></span><span id="COMMENTS"></span>Comments

The class driver passes a pointer to a PORT\_CONFIGURATION\_INFORMATION structure in *pSrb*-&gt;**CommandData.ConfigInfo**. The *pSrb* pointer points to a [**HW\_STREAM\_REQUEST\_BLOCK**](https://msdn.microsoft.com/library/windows/hardware/ff559702) structure. The class driver fills out most fields in *pSrb*-&gt;**CommandData.ConfigInfo** with information that it gets about the device from the operating system. Under most circumstances, the minidriver only needs to fill in the **StreamDescriptorSize** member of **ConfigInfo** with the size of its [**HW\_STREAM\_DESCRIPTOR**](https://msdn.microsoft.com/library/windows/hardware/ff559686) structure.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstream\stream%5D:%20SRB_INITIALIZE_DEVICE%20%20RELEASE:%20%2811/22/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




