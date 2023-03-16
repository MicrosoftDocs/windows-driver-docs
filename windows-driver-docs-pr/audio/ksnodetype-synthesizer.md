---
title: KSNODETYPE\_SYNTHESIZER
description: KSNODETYPE\_SYNTHESIZER
keywords: ["KSNODETYPE_SYNTHESIZER Audio Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- KSNODETYPE_SYNTHESIZER
api_type:
- NA
ms.date: 03/06/2023
---


# KSNODETYPE\_SYNTHESIZER


## <span id="ddk_ksnodetype_synthesizer_ks"></span><span id="DDK_KSNODETYPE_SYNTHESIZER_KS"></span>


The KSNODETYPE\_SYNTHESIZER node represents a MIDI synthesizer. A synth node takes as input a MIDI stream and outputs one of the following:

-   A wave stream

-   An analog audio signal

-   Raw MIDI

The DMusUART audio sample driver in the Microsoft Windows Driver Kit (WDK) is an example of a miniport driver that outputs raw MIDI to an external synthesizer and contains a synth node (on its DirectMusic pin).

A synth node should support the following required properties:

[**KSPROPERTY\_SYNTH\_CAPS**](/previous-versions/ff537389(v=vs.85))

[**KSPROPERTY\_SYNTH\_PORTPARAMETERS**](/previous-versions/ff537405(v=vs.85))

A synth node that supports multiple channel groups should also support the following property:

[**KSPROPERTY\_SYNTH\_CHANNELGROUPS**](/previous-versions/ff537390(v=vs.85))

If the node does not support this property, the number of channel groups defaults to 1.

A synth node can also support the following optional [KSPROPSETID\_Synth](kspropsetid-synth.md) and [KSPROPSETID\_Synth\_Dls](kspropsetid-synth-dls.md) properties:

[**KSPROPERTY\_SYNTH\_LATENCYCLOCK**](/previous-versions/ff537402(v=vs.85))

[**KSPROPERTY\_SYNTH\_MASTERCLOCK**](/previous-versions/ff537403(v=vs.85))

[**KSPROPERTY\_SYNTH\_RUNNINGSTATS**](/previous-versions/ff537406(v=vs.85))

[**KSPROPERTY\_SYNTH\_VOICEPRIORITY**](/previous-versions/ff537407(v=vs.85))

[**KSPROPERTY\_SYNTH\_VOLUME**](/previous-versions/ff537409(v=vs.85))

[**KSPROPERTY\_SYNTH\_VOLUMEBOOST**](/previous-versions/ff537410(v=vs.85))

[**KSPROPERTY\_SYNTH\_DLS\_APPEND**](/previous-versions/ff537392(v=vs.85))

[**KSPROPERTY\_SYNTH\_DLS\_COMPACT**](/previous-versions/ff537394(v=vs.85))

[**KSPROPERTY\_SYNTH\_DLS\_DOWNLOAD**](/previous-versions/ff537396(v=vs.85))

[**KSPROPERTY\_SYNTH\_DLS\_UNLOAD**](/previous-versions/ff537398(v=vs.85))

[**KSPROPERTY\_SYNTH\_DLS\_WAVEFORMAT**](/previous-versions/ff537400(v=vs.85))

 

