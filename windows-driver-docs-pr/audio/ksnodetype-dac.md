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
ms.date: 11/28/2017
ms.localizationpriority: medium
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

 

 





