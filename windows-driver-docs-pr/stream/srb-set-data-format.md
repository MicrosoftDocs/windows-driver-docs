---
title: SRB\_SET\_DATA\_FORMAT
description: SRB\_SET\_DATA\_FORMAT
ms.assetid: a111ab92-a0a0-464e-ac13-f5be33ecd064
keywords: ["SRB_SET_DATA_FORMAT Streaming Media Devices"]
topic_type:
- apiref
api_name:
- SRB_SET_DATA_FORMAT
api_type:
- NA
---

# SRB\_SET\_DATA\_FORMAT


## <span id="ddk_srb_set_data_format_ks"></span><span id="DDK_SRB_SET_DATA_FORMAT_KS"></span>


The class driver issues this request to set the data format for the stream.

### <span id="return_value"></span><span id="RETURN_VALUE"></span>Return Value

<span id="STATUS_SUCCESS"></span><span id="status_success"></span>STATUS\_SUCCESS  
Indicates successful completion of the command.

<span id="STATUS_NOT_SUPPORTED"></span><span id="status_not_supported"></span>STATUS\_NOT\_SUPPORTED  
Indicates that the minidriver does not support the requested data format.

### <span id="comments"></span><span id="COMMENTS"></span>Comments

The class driver passes the new data format in the **CommandData**.**OpenFormat** member of the *pSrb* pointer. (This pointer points to a [**HW\_STREAM\_REQUEST\_BLOCK**](https://msdn.microsoft.com/library/windows/hardware/ff559702) structure.)

For more information about data formats, see the [Stream Class Minidriver Design Guide](https://msdn.microsoft.com/library/windows/hardware/ff568277). Also see [Data Range Intersections in AVStream](https://msdn.microsoft.com/library/windows/hardware/ff558680).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstream\stream%5D:%20SRB_SET_DATA_FORMAT%20%20RELEASE:%20%2811/22/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




