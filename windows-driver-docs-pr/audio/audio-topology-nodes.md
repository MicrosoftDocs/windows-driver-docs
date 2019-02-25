---
title: Audio Topology Nodes
description: Audio Topology Nodes
ms.assetid: d999955b-d620-41c9-b42d-6870ce1d4b93
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# Audio Topology Nodes


## <span id="ddk_audio_topology_nodes_ks"></span><span id="DDK_AUDIO_TOPOLOGY_NODES_KS"></span>


The WDM audio driver framework defines a standard set of topology nodes for audio devices. A miniport driver describes the device's audio topology by specifying a set of nodes and the connections between the nodes. The [SysAudio system driver](https://msdn.microsoft.com/library/windows/hardware/ff537039#sysaudio-system-driver) uses this information to construct the audio filter graphs that it presents to client applications.

Each data path in the topology begins or ends at a pin and passes through some number of nodes, which can be thought of as beads strung along the data path. Each node in the data path is identified by a node ID (essentially an index) that uniquely identifies that node within the data path. Two pin instances could have nodes with the same ID, but the combination of pin instance and node ID uniquely identifies each node within the audio topology.

A topology node supports a set of node properties. Node properties differ from pin properties by the inclusion of a node ID identifying the internal node that the property belongs to. To send a get- or set-property request to a particular node, the client specifies the target node ID in addition to the target pin instance. When the pin's property handler receives the request, it looks at the node ID and directs the request to the handler for that node.

The following list contains the more commonly used audio topology node types:

[**KSNODETYPE\_3D\_EFFECTS**](ksnodetype-3d-effects.md)

[**KSNODETYPE\_ACOUSTIC\_ECHO\_CANCEL**](ksnodetype-acoustic-echo-cancel.md)

[**KSNODETYPE\_ADC**](ksnodetype-adc.md)

[**KSNODETYPE\_AGC**](ksnodetype-agc.md)

[**KSNODETYPE\_AUDIO\_ENGINE**](ksnodetype-audio-engine.md)

[**KSNODETYPE\_AUDIO\_KEYWORDDETECTOR**](ksnodetype-audio-keyworddetector.md)

[**KSNODETYPE\_CHORUS**](ksnodetype-chorus.md)

[**KSNODETYPE\_DAC**](ksnodetype-dac.md)

[**KSNODETYPE\_DELAY**](ksnodetype-delay.md)

[**KSNODETYPE\_DEMUX**](ksnodetype-demux.md)

[**KSNODETYPE\_DEV\_SPECIFIC**](ksnodetype-dev-specific.md)

[**KSNODETYPE\_DMSYNTH**](ksnodetype-dmsynth.md)

[**KSNODETYPE\_DMSYNTH\_CAPS**](ksnodetype-dmsynth-caps.md)

[**KSNODETYPE\_DRM\_DESCRAMBLE**](ksnodetype-drm-descramble.md)

[**KSNODETYPE\_EQUALIZER**](ksnodetype-equalizer.md)

[**KSNODETYPE\_FM\_RX**](ksnodetype-fm-rx.md)

[**KSNODETYPE\_LOUDNESS**](ksnodetype-loudness.md)

[**KSNODETYPE\_MICROPHONE\_ARRAY\_PROCESSOR**](ksnodetype-microphone-array-processor.md)

[**KSNODETYPE\_MUTE**](ksnodetype-mute.md)

[**KSNODETYPE\_MUX**](ksnodetype-mux.md)

[**KSNODETYPE\_NOISE\_SUPPRESS**](ksnodetype-noise-suppress.md)

[**KSNODETYPE\_PEAKMETER**](ksnodetype-peakmeter.md)

[**KSNODETYPE\_PROLOGIC\_DECODER**](ksnodetype-prologic-decoder.md)

[**KSNODETYPE\_PROLOGIC\_ENCODER**](ksnodetype-prologic-encoder.md)

[**KSNODETYPE\_REVERB**](ksnodetype-reverb.md)

[**KSNODETYPE\_SRC**](ksnodetype-src.md)

[**KSNODETYPE\_STEREO\_ENHANCE**](ksnodetype-stereo-enhance.md)

[**KSNODETYPE\_STEREO\_WIDE**](ksnodetype-stereo-wide.md)

[**KSNODETYPE\_SUM**](ksnodetype-sum.md)

[**KSNODETYPE\_SUPERMIX**](ksnodetype-supermix.md)

[**KSNODETYPE\_SWMIDI**](ksnodetype-swmidi.md)

[**KSNODETYPE\_SWSYNTH**](ksnodetype-swsynth.md)

[**KSNODETYPE\_SYNTHESIZER**](ksnodetype-synthesizer.md)

[**KSNODETYPE\_TELEPHONY\_BIDI**](ksnodetype-telephony-bidi.md)

[**KSNODETYPE\_TONE**](ksnodetype-tone.md)

[**KSNODETYPE\_VOLUME**](ksnodetype-volume.md)

 

 





