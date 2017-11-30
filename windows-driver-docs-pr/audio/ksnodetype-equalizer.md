---
title: KSNODETYPE\_EQUALIZER
description: KSNODETYPE\_EQUALIZER
ms.assetid: 03812936-57ba-4762-b716-858b7f14908f
keywords: ["KSNODETYPE_EQUALIZER Audio Devices"]
topic_type:
- apiref
api_name:
- KSNODETYPE_EQUALIZER
api_type:
- NA
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# KSNODETYPE\_EQUALIZER


## <span id="ddk_ksnodetype_equalizer_ks"></span><span id="DDK_KSNODETYPE_EQUALIZER_KS"></span>


The KSNODETYPE\_EQUALIZER node represents an equalizer with multiple frequency bands. By adjusting the level that the equalization table assigns to each of the frequency bands, an EQ node can control the amount of each frequency band that appears in the node's output stream.

An EQ node has one input stream and one output stream, and the two streams share a common data format.

A KSNODETYPE\_EQUALIZER node should support the following required properties:

[**KSPROPERTY\_AUDIO\_EQ\_LEVEL**](ksproperty-audio-eq-level.md)

[**KSPROPERTY\_AUDIO\_NUM\_EQ\_BANDS**](ksproperty-audio-num-eq-bands.md)

[**KSPROPERTY\_AUDIO\_EQ\_BANDS**](ksproperty-audio-eq-bands.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[audio\audio]:%20KSNODETYPE_EQUALIZER%20%20RELEASE:%20%2811/22/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




