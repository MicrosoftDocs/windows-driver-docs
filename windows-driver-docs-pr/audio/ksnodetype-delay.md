---
title: KSNODETYPE\_DELAY
description: KSNODETYPE\_DELAY
ms.assetid: 50e44c2d-6f56-412e-ab37-cbaeea61754a
keywords: ["KSNODETYPE_DELAY Audio Devices"]
topic_type:
- apiref
api_name:
- KSNODETYPE_DELAY
api_type:
- NA
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# KSNODETYPE\_DELAY


## <span id="ddk_ksnodetype_delay_ks"></span><span id="DDK_KSNODETYPE_DELAY_KS"></span>


The KSNODETYPE\_DELAY node represents a delay control. The delay control has one input stream and one output stream, and these two streams share the same data format. The delay control causes the output stream to lag behind the input stream by some specified amount of time.

A KSNODETYPE\_DELAY node should support the following required property:

[**KSPROPERTY\_AUDIO\_DELAY**](ksproperty-audio-delay.md)

 

 





