---
title: KSNODETYPE\_PROLOGIC\_DECODER
description: KSNODETYPE\_PROLOGIC\_DECODER
ms.assetid: 905ff503-1aff-4490-bd6f-f6bec8e7c3d6
keywords: ["KSNODETYPE_PROLOGIC_DECODER Audio Devices"]
topic_type:
- apiref
api_name:
- KSNODETYPE_PROLOGIC_DECODER
api_type:
- NA
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# KSNODETYPE\_PROLOGIC\_DECODER


## <span id="ddk_ksnodetype_prologic_decoder_ks"></span><span id="DDK_KSNODETYPE_PROLOGIC_DECODER_KS"></span>


The KSNODETYPE\_PROLOGIC\_DECODER node represents a Dolby Surround Pro Logic decoder. The decoder control has one stereo input stream and one output stream with one to four channels. In the four-channel output format, the channels are mapped to left, right, center, and back speaker. In the three-channel output format, the channels are mapped to left, right, and back speakers.

The functionality of the KSNODETYPE\_PROLOGIC\_DECODER node is complementary to the [**KSNODETYPE\_PROLOGIC\_ENCODER**](ksnodetype-prologic-encoder.md) node, which converts a four-channel input stream to a surround-encoded stereo output stream.

A KSNODETYPE\_PROLOGIC\_DECODER node should support the following required properties:

[**KSPROPERTY\_AUDIO\_CHANNEL\_CONFIG**](ksproperty-audio-channel-config.md)

[**KSPROPERTY\_TOPOLOGYNODE\_ENABLE**](ksproperty-topologynode-enable.md)

[**KSPROPERTY\_TOPOLOGYNODE\_RESET**](ksproperty-topologynode-reset.md)

The KSPROPERTY\_AUDIO\_CHANNEL\_CONFIG property sets and gets the channel configuration of the node's output stream.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[audio\audio]:%20KSNODETYPE_PROLOGIC_DECODER%20%20RELEASE:%20%2811/22/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




