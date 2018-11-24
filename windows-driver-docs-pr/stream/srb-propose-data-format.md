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
ms.date: 11/28/2017
ms.localizationpriority: medium
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

### Comments

When the class driver receives a [**KSPROPERTY\_CONNECTION\_PROPOSEDATAFORMAT**](ksproperty-connection-proposedataformat.md) request, it uses this SRB code to determine whether the proposed format is supported. The class driver passes the proposed data format in the **CommandData**.**OpenFormat** member pointed to by *pSrb*. The *pSrb* pointer points to a [**HW\_STREAM\_REQUEST\_BLOCK**](https://msdn.microsoft.com/library/windows/hardware/ff559702) structure.

If the minidriver does not support the data format, it sets *pSrb*-&gt;**Status** to STATUS\_NOT\_SUPPORTED. If the minidriver is able to switch the stream to the specified format, it sets this field to STATUS\_SUCCESS.

If the minidriver is able to accept the new format, the class driver at some later time may send the minidriver a format change, which is indicated by the **OptionsFlags** member in a [**KSSTREAM\_HEADER**](https://msdn.microsoft.com/library/windows/hardware/ff567138) structure.

## See also


[**SRB\_SET\_DATA\_FORMAT**](srb-set-data-format.md)

[SRB\_GET\_DATA\_FORMAT](srb-get-data-format.md)

 

 






