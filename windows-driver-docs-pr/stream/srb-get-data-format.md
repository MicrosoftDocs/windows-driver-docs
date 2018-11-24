---
title: SRB\_GET\_DATA\_FORMAT
description: SRB\_GET\_DATA\_FORMAT
ms.assetid: 6346d719-395d-4847-af80-6c65e15af250
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# SRB\_GET\_DATA\_FORMAT


## <span id="ddk_srb_get_data_format_ks"></span><span id="DDK_SRB_GET_DATA_FORMAT_KS"></span>


The class driver issues this request to query the data format for the stream. The minidriver should set *pSrb*-&gt;**CommandData** to the current data format for the stream.

For more information about data formats, see the [Stream Class Minidriver Design Guide](https://msdn.microsoft.com/library/windows/hardware/ff568277).

 

 





