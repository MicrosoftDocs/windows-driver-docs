---
title: SRB_SET_DEVICE_PROPERTY
description: SRB\_SET\_DEVICE\_PROPERTY
keywords: ["SRB_SET_DEVICE_PROPERTY Streaming Media Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- SRB_SET_DEVICE_PROPERTY
api_type:
- NA
ms.date: 11/28/2017
---

# SRB\_SET\_DEVICE\_PROPERTY


## <span id="ddk_srb_set_device_property_ks"></span><span id="DDK_SRB_SET_DEVICE_PROPERTY_KS"></span>


The class driver sends this request to query the minidriver for the data necessary to complete a property set request on a minidriver-defined property.

### <span id="return_value"></span><span id="RETURN_VALUE"></span>Return Value

The minidriver should set one of the following as the status in the SRB:

<span id="STATUS_SUCCESS"></span><span id="status_success"></span>STATUS\_SUCCESS  
Indicates successful completion of the command.

<span id="STATUS_NOT_IMPLEMENTED"></span><span id="status_not_implemented"></span>STATUS\_NOT\_IMPLEMENTED  
Indicates that the function is not supported by the minidriver.

<span id="STATUS_IO_DEVICE_ERROR"></span><span id="status_io_device_error"></span>STATUS\_IO\_DEVICE\_ERROR  
Indicates that a hardware failure occurred.

### Comments

The class driver passes the parameters of the operation in the *pSrb*-&gt;**CommandData**.**PropertyInfo** buffer, a structure of the form [**STREAM\_PROPERTY\_DESCRIPTOR**](/windows-hardware/drivers/ddi/strmini/ns-strmini-_stream_property_descriptor). The *pSrb* pointer points to a [**HW\_STREAM\_REQUEST\_BLOCK**](/windows-hardware/drivers/ddi/strmini/ns-strmini-_hw_stream_request_block) structure. The **Property** member of STREAM\_PROPERTY\_DESCRIPTOR describes the property in question, while the **PropertyInfo** member specifies a buffer from which to copy the property data. If the buffer is too small, the minidriver should set the **Status** member pointed to by *pSrb* to STATUS\_BUFFER\_OVERFLOW.

For more information about property sets, see [KS Properties](./ks-properties.md).

## See also


[**STREAM\_PROPERTY\_DESCRIPTOR**](/windows-hardware/drivers/ddi/strmini/ns-strmini-_stream_property_descriptor)

 

