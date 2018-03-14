---
title: SRB\_GET\_STREAM\_STATE
description: SRB\_GET\_STREAM\_STATE
ms.assetid: ea868e5e-0724-4064-bccb-85d5b6e93d89
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# SRB\_GET\_STREAM\_STATE


## <span id="ddk_srb_get_stream_state_ks"></span><span id="DDK_SRB_GET_STREAM_STATE_KS"></span>


The class driver sends this request to get the stream state for this stream. The minidriver enters the stream state in *pSrb*-&gt;**CommandData**.**StreamState**. See [**KSPROPERTY\_CONNECTION\_STATE**](ksproperty-connection-state.md) for a description of stream states.

 

 





