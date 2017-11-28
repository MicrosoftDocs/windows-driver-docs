---
title: SRB\_PROPOSE\_DATA\_FORMAT
description: SRB\_PROPOSE\_DATA\_FORMAT
ms.assetid: a15ec7cc-7351-4a63-ad35-e59610205913
keywords: ["SRB_PROPOSE_DATA_FORMAT Streaming Media Devices"]
topic_type:
- apiref
api_name:
- SRB_PROPOSE_DATA_FORMAT
api_type:
- NA
---

# SRB\_PROPOSE\_DATA\_FORMAT


## <span id="ddk_srb_propose_data_format_ks"></span><span id="DDK_SRB_PROPOSE_DATA_FORMAT_KS"></span>


The class driver issues this request to determine if the stream supports a given data format.

### <span id="return_value"></span><span id="RETURN_VALUE"></span>Return Value

The minidriver should set one of the following as the status in the SRB:

<span id="STATUS_SUCCESS"></span><span id="status_success"></span>STATUS\_SUCCESS  
Indicates successful completion of the command.

<span id="STATUS_NOT_IMPLEMENTED"></span><span id="status_not_implemented"></span>STATUS\_NOT\_IMPLEMENTED  
Indicates that the function is not supported by the minidriver.

<span id="STATUS_NOT_SUPPORTED"></span><span id="status_not_supported"></span>STATUS\_NOT\_SUPPORTED  
Indicates that the proposed format is not supported by the minidriver.

<span id="STATUS_IO_DEVICE_ERROR"></span><span id="status_io_device_error"></span>STATUS\_IO\_DEVICE\_ERROR  
Indicates that a hardware failure occurred.

### <span id="comments"></span><span id="COMMENTS"></span>Comments

When the class driver receives a [**KSPROPERTY\_CONNECTION\_PROPOSEDATAFORMAT**](ksproperty-connection-proposedataformat.md) request, it uses this SRB code to determine whether the proposed format is supported. The class driver passes the proposed data format in the **CommandData**.**OpenFormat** member pointed to by *pSrb*. The *pSrb* pointer points to a [**HW\_STREAM\_REQUEST\_BLOCK**](https://msdn.microsoft.com/library/windows/hardware/ff559702) structure.

If the minidriver does not support the data format, it sets *pSrb*-&gt;**Status** to STATUS\_NOT\_SUPPORTED. If the minidriver is able to switch the stream to the specified format, it sets this field to STATUS\_SUCCESS.

If the minidriver is able to accept the new format, the class driver at some later time may send the minidriver a format change, which is indicated by the **OptionsFlags** member in a [**KSSTREAM\_HEADER**](https://msdn.microsoft.com/library/windows/hardware/ff567138) structure.

## <span id="see_also"></span>See also


[**SRB\_SET\_DATA\_FORMAT**](srb-set-data-format.md)

[SRB\_GET\_DATA\_FORMAT](srb-get-data-format.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstream\stream%5D:%20SRB_PROPOSE_DATA_FORMAT%20%20RELEASE:%20%2811/22/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





