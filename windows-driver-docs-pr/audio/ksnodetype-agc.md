---
title: KSNODETYPE\_AGC
description: KSNODETYPE\_AGC
ms.assetid: 54d6bb6a-9c15-4020-bc6e-92b24878e1fd
keywords: ["KSNODETYPE_AGC Audio Devices"]
topic_type:
- apiref
api_name:
- KSNODETYPE_AGC
api_type:
- NA
---

# KSNODETYPE\_AGC


## <span id="ddk_ksnodetype_agc_ks"></span><span id="DDK_KSNODETYPE_AGC_KS"></span>


The KSNODETYPE\_AGC node represents an automatic gain control (AGC). An AGC node has one input stream and one output stream, and each of the two streams has the same data format. The node automatically adjusts the amount of attenuation or gain applied to the input stream to achieve maximum dynamic range without clipping the signal.

A KSNODETYPE\_AGC node should support the following property:

[**KSPROPERTY\_AUDIO\_AGC**](ksproperty-audio-agc.md)

A KSNODETYPE\_AGC node can also support the following optional properties:

[**KSPROPERTY\_TOPOLOGYNODE\_ENABLE**](ksproperty-topologynode-enable.md)

[**KSPROPERTY\_TOPOLOGYNODE\_RESET**](ksproperty-topologynode-reset.md)

The KSPROPERTY\_TOPOLOGYNODE\_ENABLE property is used to both enable and disable the node. When disabled, the node operates in pass-through mode (that is, it allows the input stream to pass through to the output without modification).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[audio\audio]:%20KSNODETYPE_AGC%20%20RELEASE:%20%2811/22/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




