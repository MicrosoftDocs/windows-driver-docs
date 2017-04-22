---
title: GFX Data Format Requirements
description: GFX Data Format Requirements
ms.assetid: 34a02463-231f-46c5-b6c1-b3592adb3739
keywords:
- GFX filters WDK audio , data formats
- stream formats WDK audio , GFX filters
- formats WDK audio , GFX filters
- data formats WDK audio , GFX filters
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# GFX Data Format Requirements


## <span id="gfx_data_format_requirements"></span><span id="GFX_DATA_FORMAT_REQUIREMENTS"></span>


A GFX filter's input and output pins should support a 48-kHz, 16-bit stereo data format. (In other words, the filter should expose data ranges for the input and output pins that use this format.) If either pin is connected to a stream with this data format, the other pin should also be able to connect to a stream with the same format. Additionally, when one pin is connected, the other pin should be able to connect at the same sample rate as the pin that is currently connected unless the GFX filter contains a sample rate converter (SRC) node.

These requirements apply to all GFX filters regardless of whether they are intended to be used for capture or rendering.

A GFX filter that processes a rendering stream might need to change to a different stream data format on the fly. For more information, see [How KMixer Handles Set-Format Requests](how-kmixer-handles-set-format-requests.md).

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[audio\audio]:%20GFX%20Data%20Format%20Requirements%20%20RELEASE:%20%287/18/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


