---
title: KSNODETYPE\_NOISE\_SUPPRESS
description: KSNODETYPE\_NOISE\_SUPPRESS
ms.assetid: 416504e2-38eb-4cfd-ae20-6f1f44a82abd
keywords: ["KSNODETYPE_NOISE_SUPPRESS Audio Devices"]
topic_type:
- apiref
api_name:
- KSNODETYPE_NOISE_SUPPRESS
api_type:
- NA
---

# KSNODETYPE\_NOISE\_SUPPRESS


## <span id="ddk_ksnodetype_noise_suppress_ks"></span><span id="DDK_KSNODETYPE_NOISE_SUPPRESS_KS"></span>


The KSNODETYPE\_NOISE\_SUPPRESS node represents a noise-suppression (NS) control. An NS node has connections for one input stream and one output stream. Both streams have the same format.

When a filter containing an NS node is created or the node is reset, the node is initially configured to operate in pass-through mode.

An NS node can be incorporated into an AEC (acoustic echo cancellation) filter to support full-duplex DirectSound applications. For more information, see [DirectSound Capture Effects](https://msdn.microsoft.com/library/windows/hardware/ff536327).

A KSNODETYPE\_NOISE\_SUPPRESS node in an AEC filter should support the following properties in order to enable hardware acceleration:

[**KSPROPERTY\_AUDIO\_CPU\_RESOURCES**](ksproperty-audio-cpu-resources.md)

[**KSPROPERTY\_AUDIO\_ALGORITHM\_INSTANCE**](ksproperty-audio-algorithm-instance.md)

[**KSPROPERTY\_TOPOLOGYNODE\_ENABLE**](ksproperty-topologynode-enable.md)

[**KSPROPERTY\_TOPOLOGYNODE\_RESET**](ksproperty-topologynode-reset.md)

The KSPROPERTY\_TOPOLOGYNODE\_ENABLE property is used to both enable and disable the node. When disabled, the node operates in pass-through mode (that is, it allows the input stream to pass through to the output without modification).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[audio\audio]:%20KSNODETYPE_NOISE_SUPPRESS%20%20RELEASE:%20%2811/22/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




