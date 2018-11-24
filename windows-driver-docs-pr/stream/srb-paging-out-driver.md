---
title: SRB\_PAGING\_OUT\_DRIVER
description: SRB\_PAGING\_OUT\_DRIVER
ms.assetid: 9bcb9f07-6fea-427b-9ae8-afdc6aec540f
keywords: ["SRB_PAGING_OUT_DRIVER Streaming Media Devices"]
topic_type:
- apiref
api_name:
- SRB_PAGING_OUT_DRIVER
api_type:
- NA
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# SRB\_PAGING\_OUT\_DRIVER


## <span id="ddk_srb_paging_out_driver_ks"></span><span id="DDK_SRB_PAGING_OUT_DRIVER_KS"></span>


The class driver sends this request to signal that it is about to page out the minidriver.

### <span id="return_value"></span><span id="RETURN_VALUE"></span>Return Value

The minidriver should set one of the following as the status in the SRB:

<span id="STATUS_SUCCESS"></span><span id="status_success"></span>STATUS\_SUCCESS  
Indicates successful completion of the command.

### Comments

The class driver only attempts to page out the minidriver if it has no open streams or devices. Though it is unlikely that a minidriver would have pending callbacks in this state, the minidriver should cancel any outstanding callbacks upon receipt of this SRB. The minidriver should disable adapter interrupts and then return STATUS\_SUCCESS.

The class driver pages out the minidriver only if the minidriver turns on this feature. The minidriver enables this feature by setting the registry variable PageOutWhenUnopened to 1 in the device's INF file. See the sample streaming minidriver's INFs for more information.

 

 





