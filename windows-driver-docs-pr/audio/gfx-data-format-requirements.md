---
title: GFX Data Format Requirements
description: GFX Data Format Requirements
ms.assetid: 34a02463-231f-46c5-b6c1-b3592adb3739
keywords:
- GFX filters WDK audio , data formats
- stream formats WDK audio , GFX filters
- formats WDK audio , GFX filters
- data formats WDK audio , GFX filters
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# GFX Data Format Requirements


## <span id="gfx_data_format_requirements"></span><span id="GFX_DATA_FORMAT_REQUIREMENTS"></span>


A GFX filter's input and output pins should support a 48-kHz, 16-bit stereo data format. (In other words, the filter should expose data ranges for the input and output pins that use this format.) If either pin is connected to a stream with this data format, the other pin should also be able to connect to a stream with the same format. Additionally, when one pin is connected, the other pin should be able to connect at the same sample rate as the pin that is currently connected unless the GFX filter contains a sample rate converter (SRC) node.

These requirements apply to all GFX filters regardless of whether they are intended to be used for capture or rendering.

A GFX filter that processes a rendering stream might need to change to a different stream data format on the fly. For more information, see [How KMixer Handles Set-Format Requests](how-kmixer-handles-set-format-requests.md).

 

 




