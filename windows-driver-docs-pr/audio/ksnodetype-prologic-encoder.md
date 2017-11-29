---
title: KSNODETYPE\_PROLOGIC\_ENCODER
description: KSNODETYPE\_PROLOGIC\_ENCODER
ms.assetid: cca6fe1d-20f8-4112-956b-a1b33b48a4ff
keywords: ["KSNODETYPE_PROLOGIC_ENCODER Audio Devices"]
topic_type:
- apiref
api_name:
- KSNODETYPE_PROLOGIC_ENCODER
api_type:
- NA
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# KSNODETYPE\_PROLOGIC\_ENCODER


## <span id="ddk_ksnodetype_prologic_encoder_ks"></span><span id="DDK_KSNODETYPE_PROLOGIC_ENCODER_KS"></span>


The KSNODETYPE\_PROLOGIC\_ENCODER node represents a Dolby Surround Pro Logic encoder. The node accepts a four-channel input stream with channels for left, right, center, and back speakers. The node encodes the input stream as a surround-encoded stereo output stream.

The functionality of the KSNODETYPE\_PROLOGIC\_ENCODER node is complementary to the [**KSNODETYPE\_PROLOGIC\_DECODER**](ksnodetype-prologic-decoder.md) node, which takes a surround-encoded stereo input stream and decodes it into a four-channel stream with channels for left, right, center, and back speakers.

In Microsoft Windows XP and later, the [KMixer system driver](https://msdn.microsoft.com/library/windows/hardware/ff537039#kmixer-system-driver) has a KSNODETYPE\_PROLOGIC\_ENCODER node.

A KSNODETYPE\_PROLOGIC\_ENCODER node should support the [**KSPROPERTY\_AUDIO\_SURROUND\_ENCODE**](ksproperty-audio-surround-encode.md) property, which is used to enable and disable the node.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[audio\audio]:%20KSNODETYPE_PROLOGIC_ENCODER%20%20RELEASE:%20%2811/22/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




