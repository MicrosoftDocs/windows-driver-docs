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
---

# KSNODETYPE\_DELAY


## <span id="ddk_ksnodetype_delay_ks"></span><span id="DDK_KSNODETYPE_DELAY_KS"></span>


The KSNODETYPE\_DELAY node represents a delay control. The delay control has one input stream and one output stream, and these two streams share the same data format. The delay control causes the output stream to lag behind the input stream by some specified amount of time.

A KSNODETYPE\_DELAY node should support the following required property:

[**KSPROPERTY\_AUDIO\_DELAY**](ksproperty-audio-delay.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[audio\audio]:%20KSNODETYPE_DELAY%20%20RELEASE:%20%2811/22/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




