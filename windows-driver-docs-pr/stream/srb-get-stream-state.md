---
title: SRB\_GET\_STREAM\_STATE
description: SRB\_GET\_STREAM\_STATE
ms.date: 11/28/2017
---

# SRB\_GET\_STREAM\_STATE


## <span id="ddk_srb_get_stream_state_ks"></span><span id="DDK_SRB_GET_STREAM_STATE_KS"></span>


The class driver sends this request to get the stream state for this stream. The minidriver enters the stream state in *pSrb*-&gt;**CommandData**.**StreamState**. See [**KSPROPERTY\_CONNECTION\_STATE**](ksproperty-connection-state.md) for a description of stream states.

 

 





