---
title: SRB_GET_DATA_FORMAT
description: SRB\_GET\_DATA\_FORMAT
ms.date: 11/28/2017
---

# SRB\_GET\_DATA\_FORMAT


## <span id="ddk_srb_get_data_format_ks"></span><span id="DDK_SRB_GET_DATA_FORMAT_KS"></span>


The class driver issues this request to query the data format for the stream. The minidriver should set *pSrb*-&gt;**CommandData** to the current data format for the stream.

For more information about data formats, see the [Stream Class Minidriver Design Guide](./streaming-minidrivers2.md).

 

