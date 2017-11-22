---
title: KSNODETYPE\_VOLUME
description: KSNODETYPE\_VOLUME
ms.assetid: 4776ea69-6492-428e-97ce-dd8842f22c16
keywords: ["KSNODETYPE_VOLUME Audio Devices"]
topic_type:
- apiref
api_name:
- KSNODETYPE_VOLUME
api_type:
- NA
---

# KSNODETYPE\_VOLUME


## <span id="ddk_ksnodetype_volume_ks"></span><span id="DDK_KSNODETYPE_VOLUME_KS"></span>


The KSNODETYPE\_VOLUME node represents a volume (gain or attenuation) control. The volume control has one input stream and one output stream; each of the two streams has the same data format. It can apply attenuation (reduction in volume) or gain (increase in volume) to the stream. In addition, it can optionally support inverting the signal.

For information about multichannel volume nodes, see [Exposing Multichannel Nodes](https://msdn.microsoft.com/library/windows/hardware/ff536380).

A KSNODETYPE\_VOLUME node should support the following required property:

[**KSPROPERTY\_AUDIO\_VOLUMELEVEL**](ksproperty-audio-volumelevel.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[audio\audio]:%20KSNODETYPE_VOLUME%20%20RELEASE:%20%2811/22/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




