---
title: SRB\_READ\_DATA
description: SRB\_READ\_DATA
MS-HAID:
- 'strclass-srbs\_d5c585dd-b9ee-456d-a2b5-03e9206ff3ba.xml'
- 'stream.srb\_read\_data'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: b59d705d-5215-42ee-85cf-369a2e69f99b
keywords: ["SRB_READ_DATA Streaming Media Devices"]
topic_type:
- apiref
api_name:
- SRB_READ_DATA
api_type:
- NA
---

# SRB\_READ\_DATA


## <span id="ddk_srb_read_data_ks"></span><span id="DDK_SRB_READ_DATA_KS"></span>


The class driver has received a read request for the minidriver.

### <span id="return_value"></span><span id="RETURN_VALUE"></span>Return Value

The minidriver can set one of the following as the status in the SRB, or it can pass additional error codes to indicate error situations such as memory errors and bad parameters. The class driver checks only for STATUS\_SUCCESS.

<span id="STATUS_SUCCESS"></span><span id="status_success"></span>STATUS\_SUCCESS  
Indicates successful completion of the command.

<span id="STATUS_NOT_IMPLEMENTED"></span><span id="status_not_implemented"></span>STATUS\_NOT\_IMPLEMENTED  
Indicates that the function is not supported by the minidriver.

<span id="STATUS_IO_DEVICE_ERROR"></span><span id="status_io_device_error"></span>STATUS\_IO\_DEVICE\_ERROR  
Indicates that a hardware failure occurred.

### <span id="comments"></span><span id="COMMENTS"></span>Comments

The value of *pSrb*-&gt;**CommandData**.**DataBufferArray** points to an array of [**KSSTREAM\_HEADER**](https://msdn.microsoft.com/library/windows/hardware/ff567138) structures, which together describe the data buffer. The *pSrb* pointer points to a [**HW\_STREAM\_REQUEST\_BLOCK**](https://msdn.microsoft.com/library/windows/hardware/ff559702) structure. *pSrb*-&gt;**CommandData**.**NumberOfBuffers** specifies the size of the array.

**When the SRB\_READ\_DATA command is received by the minidriver, the responding minidriver routine should:**

1.  Check to determine the current stream state. The minidriver should only accept read requests when in either the Pause or Run state. If the stream is stopped, it should immediately complete and return the SRB.

2.  Place the SRB in the queue.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstream\stream%5D:%20SRB_READ_DATA%20%20RELEASE:%20%2811/22/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




