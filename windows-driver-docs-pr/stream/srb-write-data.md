---
title: SRB\_WRITE\_DATA
description: SRB\_WRITE\_DATA
ms.assetid: f7867185-3f1b-4c83-b23a-5b2b4ce6e484
keywords: ["SRB_WRITE_DATA Streaming Media Devices"]
topic_type:
- apiref
api_name:
- SRB_WRITE_DATA
api_type:
- NA
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# SRB\_WRITE\_DATA


## <span id="ddk_srb_write_data_ks"></span><span id="DDK_SRB_WRITE_DATA_KS"></span>


The class driver has received a write request for the minidriver. The value of *pSrb*-&gt;**CommandData**.**DataBufferArray** points to an array of [**KSSTREAM\_HEADER**](https://msdn.microsoft.com/library/windows/hardware/ff567138) structures, which together describe the data buffer. The value of *pSrb*-&gt;**CommandData**.**NumberOfBuffers** specifies the size of the array. The *pSrb* pointer points to a [**HW\_STREAM\_REQUEST\_BLOCK**](https://msdn.microsoft.com/library/windows/hardware/ff559702) structure.

### <span id="return_value"></span><span id="RETURN_VALUE"></span>Return Value

The minidriver can set one of the following as status in the SRB, or it can pass additional error codes to indicate error situations such as memory errors and bad parameters. The class driver is concerned only with STATUS\_SUCCESS.

<span id="STATUS_SUCCESS"></span><span id="status_success"></span>STATUS\_SUCCESS  
Indicates successful completion of the command.

<span id="STATUS_NOT_IMPLEMENTED"></span><span id="status_not_implemented"></span>STATUS\_NOT\_IMPLEMENTED  
Indicates that the function is not supported by the minidriver.

<span id="STATUS_IO_DEVICE_ERROR"></span><span id="status_io_device_error"></span>STATUS\_IO\_DEVICE\_ERROR  
Indicates that a hardware failure occurred.

## <span id="see_also"></span>See also


[**SRB\_SET\_STREAM\_STATE**](srb-set-stream-state.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstream\stream%5D:%20SRB_WRITE_DATA%20%20RELEASE:%20%2811/22/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





