---
title: SRB\_GET\_DEVICE\_PROPERTY
description: SRB\_GET\_DEVICE\_PROPERTY
ms.assetid: 2a0a3b8a-7252-4ba5-a1a5-ffef0f0f5715
keywords: ["SRB_GET_DEVICE_PROPERTY Streaming Media Devices"]
topic_type:
- apiref
api_name:
- SRB_GET_DEVICE_PROPERTY
api_type:
- NA
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# SRB\_GET\_DEVICE\_PROPERTY


## <span id="ddk_srb_get_device_property_ks"></span><span id="DDK_SRB_GET_DEVICE_PROPERTY_KS"></span>


The class driver sends this request to query the minidriver for the data necessary to complete a property get request on a minidriver-defined property.

### <span id="return_value"></span><span id="RETURN_VALUE"></span>Return Value

The minidriver should set one of the following as the status in the SRB:

<span id="STATUS_SUCCESS"></span><span id="status_success"></span>STATUS\_SUCCESS  
Indicates successful completion of the command.

<span id="STATUS_NOT_IMPLEMENTED"></span><span id="status_not_implemented"></span>STATUS\_NOT\_IMPLEMENTED  
Indicates that the function is not supported by the minidriver.

<span id="STATUS_IO_DEVICE_ERROR"></span><span id="status_io_device_error"></span>STATUS\_IO\_DEVICE\_ERROR  
Indicates that a hardware failure occurred.

### Comments

The class driver passes the parameters of the operation in the *pSrb*-&gt;**CommandData.PropertyInfo** buffer, a structure of the form [**STREAM\_PROPERTY\_DESCRIPTOR**](https://msdn.microsoft.com/library/windows/hardware/ff568442). The *pSrb* pointer points to a [**HW\_STREAM\_REQUEST\_BLOCK**](https://msdn.microsoft.com/library/windows/hardware/ff559702) structure. The **Property** member of STREAM\_PROPERTY\_DESCRIPTOR describes the property in question, while the **PropertyInfo** member specifies a buffer to copy the property data into. If the buffer is too small, the minidriver should set the **Status** member of *pSrb* to STATUS\_BUFFER\_OVERFLOW.

For more information about property sets, see [KS Properties](https://msdn.microsoft.com/library/windows/hardware/ff567671).

## See also


[**STREAM\_PROPERTY\_DESCRIPTOR**](https://msdn.microsoft.com/library/windows/hardware/ff568442)

 

 






