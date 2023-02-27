---
title: SRB\_INITIALIZATION\_COMPLETE
description: SRB\_INITIALIZATION\_COMPLETE
keywords: ["SRB_INITIALIZATION_COMPLETE Streaming Media Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- SRB_INITIALIZATION_COMPLETE
api_type:
- NA
ms.date: 11/28/2017
---

# SRB\_INITIALIZATION\_COMPLETE


## <span id="ddk_srb_initialization_complete_ks"></span><span id="DDK_SRB_INITIALIZATION_COMPLETE_KS"></span>


The class driver sends this request to signal the minidriver that it has completed its initialization.

### Comments

Once the minidriver completes this request, the class driver can begin to send [**SRB\_OPEN\_STREAM**](srb-open-stream.md) requests.

When this SRB is received by the minidriver, the minidriver should create any necessary Registry entries. For example, a DirectShow filter might register a TV tuner or Crossbar for use with the FilterGraph using the [**StreamClassRegisterFilterWithNoKSPins**](/windows-hardware/drivers/ddi/strmini/nf-strmini-streamclassregisterfilterwithnokspins) routine.

 

