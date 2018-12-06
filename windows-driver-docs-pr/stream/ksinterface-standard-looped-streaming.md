---
title: KSINTERFACE\_STANDARD\_LOOPED\_STREAMING
description: KSINTERFACE\_STANDARD\_LOOPED\_STREAMING
ms.assetid: c12e7085-fa13-48d3-b4ed-ea0a708f026b
keywords: ["KSINTERFACE_STANDARD_LOOPED_STREAMING Streaming Media Devices"]
topic_type:
- apiref
api_name:
- KSINTERFACE_STANDARD_LOOPED_STREAMING
api_type:
- NA
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# KSINTERFACE\_STANDARD\_LOOPED\_STREAMING


## <span id="ddk_ksinterface_standard_looped_streaming_ks"></span><span id="DDK_KSINTERFACE_STANDARD_LOOPED_STREAMING_KS"></span>


The KSINTERFACE\_STANDARD\_LOOPED\_STREAMING interface is used by clients of DSound. At release time of Windows XP, Kmixer and Portcls are the only KS Audio filters that support this interface.

If a pin supports KSINTERFACE\_STANDARD\_LOOPED\_STREAMING, the relevant filter does not complete buffers until the pin is placed into the *Stop* state. The filter processes data by continuously looping around the data in the single buffer submitted to the filter.

### See Also

[KSINTERFACESETID\_Standard](ksinterfacesetid-standard.md), [**KSPIN\_INTERFACE**](https://msdn.microsoft.com/library/windows/hardware/ff563537), [**KSPIN\_DESCRIPTOR**](https://msdn.microsoft.com/library/windows/hardware/ff563533)

 

 





