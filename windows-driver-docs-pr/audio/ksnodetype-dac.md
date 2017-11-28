---
title: KSNODETYPE\_DAC
description: KSNODETYPE\_DAC
ms.assetid: 70b30425-cffc-49e1-aa8b-8f5734bd196e
keywords: ["KSNODETYPE_DAC Audio Devices"]
topic_type:
- apiref
api_name:
- KSNODETYPE_DAC
api_type:
- NA
---

# KSNODETYPE\_DAC


## <span id="ddk_ksnodetype_dac_ks"></span><span id="DDK_KSNODETYPE_DAC_KS"></span>


The KSNODETYPE\_DAC node represents a digital-to-analog converter (DAC). The DAC node has one input stream and one output stream.

A good, general rule is that an audio driver should expose only one DAC node in its topology. Because DirectSound assumes that a driver's topology contains only a single DAC node, it sends speaker-configuration property requests to the first DAC node that it discovers, but not to any others. In fact, a topology can safely contain more than one DAC node, but only if all the DAC nodes represent the same physical control. In this case, setting a property on any one of the DAC nodes has the effect of setting the same property on all the DAC nodes. Some audio drivers might need to use multiple DAC nodes to work around a problem in Windows Me/98, Windows 2000, and Windows XP: If a miniport driver provides more than one wave-rendering pin factory and has a topology that mixes the streams from these pins together through a SUM node that feeds a DAC node, wdmaud.drv (the mixer-line driver) incorrectly reports a separate wave volume control for each of the pin factories. It should generate only a single wave volume control. To fix this problem, a work-around solution is to insert a DAC node into the data path from each of the pin factories.

A KSNODETYPE\_DAC node can support the following optional properties:

[**KSPROPERTY\_AUDIO\_CHANNEL\_CONFIG**](ksproperty-audio-channel-config.md)

[**KSPROPERTY\_AUDIO\_DYNAMIC\_SAMPLING\_RATE**](ksproperty-audio-dynamic-sampling-rate.md)

[**KSPROPERTY\_AUDIO\_SAMPLING\_RATE**](ksproperty-audio-sampling-rate.md)

[**KSPROPERTY\_AUDIO\_STEREO\_SPEAKER\_GEOMETRY**](ksproperty-audio-stereo-speaker-geometry.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[audio\audio]:%20KSNODETYPE_DAC%20%20RELEASE:%20%2811/22/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




