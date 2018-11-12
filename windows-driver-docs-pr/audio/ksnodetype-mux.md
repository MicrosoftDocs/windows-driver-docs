---
title: KSNODETYPE\_MUX
description: KSNODETYPE\_MUX
ms.assetid: c22054fe-7ede-4694-8ae1-6e18e1270185
keywords: ["KSNODETYPE_MUX Audio Devices"]
topic_type:
- apiref
api_name:
- KSNODETYPE_MUX
api_type:
- NA
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# KSNODETYPE\_MUX


## <span id="ddk_ksnodetype_mux_ks"></span><span id="DDK_KSNODETYPE_MUX_KS"></span>


The KSNODETYPE\_MUX node represents a multiplexer (MUX). The MUX has multiple input streams and one output stream, all with the same data format. Only one input stream at a time is routed to the output stream.

A KSNODETYPE\_MUX node should support the following required property:

[**KSPROPERTY\_AUDIO\_MUX\_SOURCE**](ksproperty-audio-mux-source.md)

 

 





