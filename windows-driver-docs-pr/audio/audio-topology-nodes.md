---
title: Audio Topology Nodes
description: Audio Topology Nodes
ms.assetid: d999955b-d620-41c9-b42d-6870ce1d4b93
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[audio\audio]:%20Audio%20Topology%20Nodes%20%20RELEASE:%20%2811/22/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




