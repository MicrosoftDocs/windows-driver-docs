---
title: KSNODETYPE\_MUX
description: KSNODETYPE\_MUX
keywords: ["KSNODETYPE_MUX Audio Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- KSNODETYPE_MUX
api_type:
- NA
ms.date: 03/06/2023
---


# KSNODETYPE\_MUX


## <span id="ddk_ksnodetype_mux_ks"></span><span id="DDK_KSNODETYPE_MUX_KS"></span>


The KSNODETYPE\_MUX node represents a multiplexer (MUX). The MUX has multiple input streams and one output stream, all with the same data format. Only one input stream at a time is routed to the output stream.

A KSNODETYPE\_MUX node should support the following required property:

[**KSPROPERTY\_AUDIO\_MUX\_SOURCE**](ksproperty-audio-mux-source.md)

 

 





