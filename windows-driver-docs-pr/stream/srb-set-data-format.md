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
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# SRB\_SET\_DATA\_FORMAT


## <span id="ddk_srb_set_data_format_ks"></span><span id="DDK_SRB_SET_DATA_FORMAT_KS"></span>


The class driver issues this request to set the data format for the stream.

### <span id="return_value"></span><span id="RETURN_VALUE"></span>Return Value

<span id="STATUS_SUCCESS"></span><span id="status_success"></span>STATUS\_SUCCESS  
Indicates successful completion of the command.

<span id="STATUS_NOT_SUPPORTED"></span><span id="status_not_supported"></span>STATUS\_NOT\_SUPPORTED  
Indicates that the minidriver does not support the requested data format.

### Comments

The class driver passes the new data format in the **CommandData**.**OpenFormat** member of the *pSrb* pointer. (This pointer points to a [**HW\_STREAM\_REQUEST\_BLOCK**](https://msdn.microsoft.com/library/windows/hardware/ff559702) structure.)

For more information about data formats, see the [Stream Class Minidriver Design Guide](https://msdn.microsoft.com/library/windows/hardware/ff568277). Also see [Data Range Intersections in AVStream](https://msdn.microsoft.com/library/windows/hardware/ff558680).

 

 





