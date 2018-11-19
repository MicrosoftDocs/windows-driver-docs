---
title: KSNODETYPE\_SYNTHESIZER
description: KSNODETYPE\_SYNTHESIZER
ms.assetid: ef5f5068-c312-4e14-905e-c815d6e9aac2
keywords: ["KSNODETYPE_SYNTHESIZER Audio Devices"]
topic_type:
- apiref
api_name:
- KSNODETYPE_SYNTHESIZER
api_type:
- NA
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# KSNODETYPE\_SYNTHESIZER


## <span id="ddk_ksnodetype_synthesizer_ks"></span><span id="DDK_KSNODETYPE_SYNTHESIZER_KS"></span>


The KSNODETYPE\_SYNTHESIZER node represents a MIDI synthesizer. A synth node takes as input a MIDI stream and outputs one of the following:

-   A wave stream

-   An analog audio signal

-   Raw MIDI

The DMusUART audio sample driver in the Microsoft Windows Driver Kit (WDK) is an example of a miniport driver that outputs raw MIDI to an external synthesizer and contains a synth node (on its DirectMusic pin).

A synth node should support the following required properties:

[**KSPROPERTY\_SYNTH\_CAPS**](https://msdn.microsoft.com/library/windows/hardware/ff537389)

[**KSPROPERTY\_SYNTH\_PORTPARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/ff537405)

A synth node that supports multiple channel groups should also support the following property:

[**KSPROPERTY\_SYNTH\_CHANNELGROUPS**](https://msdn.microsoft.com/library/windows/hardware/ff537390)

If the node does not support this property, the number of channel groups defaults to 1.

A synth node can also support the following optional [KSPROPSETID\_Synth](kspropsetid-synth.md) and [KSPROPSETID\_Synth\_Dls](kspropsetid-synth-dls.md) properties:

[**KSPROPERTY\_SYNTH\_LATENCYCLOCK**](https://msdn.microsoft.com/library/windows/hardware/ff537402)

[**KSPROPERTY\_SYNTH\_MASTERCLOCK**](https://msdn.microsoft.com/library/windows/hardware/ff537403)

[**KSPROPERTY\_SYNTH\_RUNNINGSTATS**](https://msdn.microsoft.com/library/windows/hardware/ff537406)

[**KSPROPERTY\_SYNTH\_VOICEPRIORITY**](https://msdn.microsoft.com/library/windows/hardware/ff537407)

[**KSPROPERTY\_SYNTH\_VOLUME**](https://msdn.microsoft.com/library/windows/hardware/ff537409)

[**KSPROPERTY\_SYNTH\_VOLUMEBOOST**](https://msdn.microsoft.com/library/windows/hardware/ff537410)

[**KSPROPERTY\_SYNTH\_DLS\_APPEND**](https://msdn.microsoft.com/library/windows/hardware/ff537392)

[**KSPROPERTY\_SYNTH\_DLS\_COMPACT**](https://msdn.microsoft.com/library/windows/hardware/ff537394)

[**KSPROPERTY\_SYNTH\_DLS\_DOWNLOAD**](https://msdn.microsoft.com/library/windows/hardware/ff537396)

[**KSPROPERTY\_SYNTH\_DLS\_UNLOAD**](https://msdn.microsoft.com/library/windows/hardware/ff537398)

[**KSPROPERTY\_SYNTH\_DLS\_WAVEFORMAT**](https://msdn.microsoft.com/library/windows/hardware/ff537400)

 

 





