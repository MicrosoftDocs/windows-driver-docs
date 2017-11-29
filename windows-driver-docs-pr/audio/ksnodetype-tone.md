---
title: KSNODETYPE\_TONE
description: KSNODETYPE\_TONE
ms.assetid: d9d55db0-8305-403f-8d0c-56c2cd736912
keywords: ["KSNODETYPE_TONE Audio Devices"]
topic_type:
- apiref
api_name:
- KSNODETYPE_TONE
api_type:
- NA
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# KSNODETYPE\_TONE


## <span id="ddk_ksnodetype_tone_ks"></span><span id="DDK_KSNODETYPE_TONE_KS"></span>


The KSNODETYPE\_TONE node represents a tone control. The tone control has one input stream and one output stream; the two streams have the same data format. It can attenuate the amount of bass, treble, or mid-frequencies of the output stream. In addition, it can optionally support a bass boost or gain.

A KSNODETYPE\_TONE node should support at least one of the following properties:

[**KSPROPERTY\_AUDIO\_BASS**](ksproperty-audio-bass.md)

[**KSPROPERTY\_AUDIO\_MID**](ksproperty-audio-mid.md)

[**KSPROPERTY\_AUDIO\_TREBLE**](ksproperty-audio-treble.md)

[**KSPROPERTY\_AUDIO\_BASS\_BOOST**](ksproperty-audio-bass-boost.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[audio\audio]:%20KSNODETYPE_TONE%20%20RELEASE:%20%2811/22/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




