---
title: SRB\_SET\_STREAM\_PROPERTY
description: SRB\_SET\_STREAM\_PROPERTY
ms.assetid: 33a44732-a75c-4394-9839-f3c7d71d01e1
keywords: ["SRB_SET_STREAM_PROPERTY Streaming Media Devices"]
topic_type:
- apiref
api_name:
- SRB_SET_STREAM_PROPERTY
api_type:
- NA
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# SRB\_SET\_STREAM\_PROPERTY


## <span id="ddk_srb_set_stream_property_ks"></span><span id="DDK_SRB_SET_STREAM_PROPERTY_KS"></span>


The class driver sends this request to query the minidriver for the data necessary to complete a property set request on a minidriver-defined property for this stream.

### <span id="return_value"></span><span id="RETURN_VALUE"></span>Return Value

The minidriver should set one of the following as the status in the SRB:

<span id="STATUS_SUCCESS"></span><span id="status_success"></span>STATUS\_SUCCESS  
Indicates successful completion of the command.

<span id="STATUS_NOT_IMPLEMENTED"></span><span id="status_not_implemented"></span>STATUS\_NOT\_IMPLEMENTED  
Indicates that the function is not supported by the minidriver.

<span id="STATUS_IO_DEVICE_ERROR"></span><span id="status_io_device_error"></span>STATUS\_IO\_DEVICE\_ERROR  
Indicates that a hardware failure occurred.

### <span id="comments"></span><span id="COMMENTS"></span>Comments

The class driver passes the parameters of the operation in the *pSrb*-&gt;**CommandData**.**PropertyInfo** buffer, a structure of the form [**STREAM\_PROPERTY\_DESCRIPTOR**](https://msdn.microsoft.com/library/windows/hardware/ff568442). The *pSrb* pointer points to a [**HW\_STREAM\_REQUEST\_BLOCK**](https://msdn.microsoft.com/library/windows/hardware/ff559702) structure.

The **Property** member of STREAM\_PROPERTY\_DESCRIPTOR describes the property in question, while the **PropertyInfo** member specifies a buffer from which to copy the property data. If the buffer is too small, the minidriver should set the **Status** member pointed to by *pSrb* to STATUS\_BUFFER\_OVERFLOW.

## <span id="see_also"></span>See also


[**SRB\_GET\_STREAM\_PROPERTY**](srb-get-stream-property.md)

[**STREAM\_PROPERTY\_DESCRIPTOR**](https://msdn.microsoft.com/library/windows/hardware/ff568442)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstream\stream%5D:%20SRB_SET_STREAM_PROPERTY%20%20RELEASE:%20%2811/22/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





