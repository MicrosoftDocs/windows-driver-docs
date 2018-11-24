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
ms.date: 11/28/2017
ms.localizationpriority: medium
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

### Comments

The class driver passes a pointer to a PORT\_CONFIGURATION\_INFORMATION structure in *pSrb*-&gt;**CommandData.ConfigInfo**. The *pSrb* pointer points to a [**HW\_STREAM\_REQUEST\_BLOCK**](https://msdn.microsoft.com/library/windows/hardware/ff559702) structure. The class driver fills out most fields in *pSrb*-&gt;**CommandData.ConfigInfo** with information that it gets about the device from the operating system. Under most circumstances, the minidriver only needs to fill in the **StreamDescriptorSize** member of **ConfigInfo** with the size of its [**HW\_STREAM\_DESCRIPTOR**](https://msdn.microsoft.com/library/windows/hardware/ff559686) structure.

 

 





