---
title: Topology Nodes
description: Topology Nodes
keywords:
- topology nodes WDK audio
- nodes WDK audio , topology
- MIXERCONTROL structure
- tone nodes WDK audio
- translating nodes WDK audio
- supermix nodes WDK audio
- bass property WDK audio
- treble property WDK audio
- bass boost property WDK audio
- mid-frequency property WDK audio
ms.date: 04/20/2017
---

# Topology Nodes


## <span id="topology_nodes"></span><span id="TOPOLOGY_NODES"></span>


Audio applications can access mixer controls through the Microsoft Windows multimedia function [**mixerGetLineControls**](/previous-versions/dd757302(v=vs.85)). This function retrieves an array of one or more MIXERCONTROL structures, each of which describes the state and metrics of a single control node on an audio line. The **dwControlType** member of the MIXERCONTROL structure is set to an enumeration value that specifies the type of the control. A number of mixer-control types have been specified for audio VxDs, but only a subset of these controls is available for WDM audio drivers.

WDMAud translates some but not all topology nodes into corresponding mixer-line controls. The topology-node types that are listed in the following table have counterparts that are mixer-line controls.

<table>
<colgroup>
<col width="33%" />
<col width="33%" />
<col width="33%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Node Type</th>
<th align="left">Topology-Node Type Name</th>
<th align="left">Mixer-Control Type Name</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>AGC</p></td>
<td align="left"><p><a href="/windows-hardware/drivers/audio/ksnodetype-agc" data-raw-source="[&lt;strong&gt;KSNODETYPE_AGC&lt;/strong&gt;](./ksnodetype-agc.md)"><strong>KSNODETYPE_AGC</strong></a></p></td>
<td align="left"><p>MIXERCONTROL_CONTROLTYPE_ONOFF</p></td>
</tr>
<tr class="even">
<td align="left"><p>Loudness</p></td>
<td align="left"><p><a href="/windows-hardware/drivers/audio/ksnodetype-loudness" data-raw-source="[&lt;strong&gt;KSNODETYPE_LOUDNESS&lt;/strong&gt;](./ksnodetype-loudness.md)"><strong>KSNODETYPE_LOUDNESS</strong></a></p></td>
<td align="left"><p>MIXERCONTROL_CONTROLTYPE_LOUDNESS</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Mute</p></td>
<td align="left"><p><a href="/windows-hardware/drivers/audio/ksnodetype-mute" data-raw-source="[&lt;strong&gt;KSNODETYPE_MUTE&lt;/strong&gt;](./ksnodetype-mute.md)"><strong>KSNODETYPE_MUTE</strong></a></p></td>
<td align="left"><p>MIXERCONTROL_CONTROLTYPE_MUTE</p></td>
</tr>
<tr class="even">
<td align="left"><p>Tone (multiple)</p></td>
<td align="left"><p><a href="/windows-hardware/drivers/audio/ksnodetype-tone" data-raw-source="[&lt;strong&gt;KSNODETYPE_TONE&lt;/strong&gt;](./ksnodetype-tone.md)"><strong>KSNODETYPE_TONE</strong></a></p></td>
<td align="left"><p>MIXERCONTROL_CONTROLTYPE_ONOFF (if KSPROPERTY_AUDIO_BASS_BOOST is supported)</p>
<p>MIXERCONTROL_CONTROLTYPE_BASS (if KSPROPERTY_AUDIO_BASS is supported)</p>
<p>MIXERCONTROL_CONTROLTYPE_TREBLE (if KSPROPERTY_AUDIO_TREBLE is supported)</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Volume</p></td>
<td align="left"><p><a href="/windows-hardware/drivers/audio/ksnodetype-volume" data-raw-source="[&lt;strong&gt;KSNODETYPE_VOLUME&lt;/strong&gt;](./ksnodetype-volume.md)"><strong>KSNODETYPE_VOLUME</strong></a></p></td>
<td align="left"><p>MIXERCONTROL_CONTROLTYPE_VOLUME</p></td>
</tr>
<tr class="even">
<td align="left"><p>Peakmeter</p></td>
<td align="left"><p><a href="/windows-hardware/drivers/audio/ksnodetype-peakmeter" data-raw-source="[&lt;strong&gt;KSNODETYPE_PEAKMETER&lt;/strong&gt;](./ksnodetype-peakmeter.md)"><strong>KSNODETYPE_PEAKMETER</strong></a></p></td>
<td align="left"><p>MIXERCONTROL_CONTROLTYPE_PEAKMETER</p></td>
</tr>
<tr class="odd">
<td align="left"><p>MUX</p></td>
<td align="left"><p><a href="/windows-hardware/drivers/audio/ksnodetype-mux" data-raw-source="[&lt;strong&gt;KSNODETYPE_MUX&lt;/strong&gt;](./ksnodetype-mux.md)"><strong>KSNODETYPE_MUX</strong></a></p></td>
<td align="left"><p>MIXERCONTROL_CONTROLTYPE_MUX</p></td>
</tr>
<tr class="even">
<td align="left"><p>Stereo wide</p></td>
<td align="left"><p><a href="/windows-hardware/drivers/audio/ksnodetype-stereo-wide" data-raw-source="[&lt;strong&gt;KSNODETYPE_STEREO_WIDE&lt;/strong&gt;](./ksnodetype-stereo-wide.md)"><strong>KSNODETYPE_STEREO_WIDE</strong></a></p></td>
<td align="left"><p>MIXERCONTROL_CONTROLTYPE_FADER</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Chorus</p></td>
<td align="left"><p><a href="/windows-hardware/drivers/audio/ksnodetype-chorus" data-raw-source="[&lt;strong&gt;KSNODETYPE_CHORUS&lt;/strong&gt;](./ksnodetype-chorus.md)"><strong>KSNODETYPE_CHORUS</strong></a></p></td>
<td align="left"><p>MIXERCONTROL_CONTROLTYPE_FADER</p></td>
</tr>
<tr class="even">
<td align="left"><p>Reverb</p></td>
<td align="left"><p><a href="/windows-hardware/drivers/audio/ksnodetype-reverb" data-raw-source="[&lt;strong&gt;KSNODETYPE_REVERB&lt;/strong&gt;](./ksnodetype-reverb.md)"><strong>KSNODETYPE_REVERB</strong></a></p></td>
<td align="left"><p>MIXERCONTROL_CONTROLTYPE_FADER</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Supermix (multiple)</p></td>
<td align="left"><p><a href="/windows-hardware/drivers/audio/ksnodetype-supermix" data-raw-source="[&lt;strong&gt;KSNODETYPE_SUPERMIX&lt;/strong&gt;](./ksnodetype-supermix.md)"><strong>KSNODETYPE_SUPERMIX</strong></a></p></td>
<td align="left"><p>MIXERCONTROL_CONTROLTYPE_MUTE (if KSPROPERTY_AUDIO_MUTE is supported in the supermix node)</p>
<p>MIXERCONTROL_CONTROLTYPE_VOLUME (see comments in text)</p></td>
</tr>
</tbody>
</table>

 

Topology-node types that are missing from the preceding table are not translated into mixer-line controls, and mixer-line controls that are missing from the table are not supported by WDM audio drivers.

Note that MIXERCONTROL\_CONTROLTYPE\_CUSTOM is missing from the table. This means that WDM audio drivers do not support custom mixer controls.

A [**tone node**](./ksnodetype-tone.md) supports four properties: [**bass**](./ksproperty-audio-bass.md), [**treble**](./ksproperty-audio-treble.md), [**mid-frequency**](./ksproperty-audio-mid.md), and [**bass boost**](./ksproperty-audio-bass-boost.md). The mid-frequency property has no mixer-line counterpart, but the other three properties do. For each tone node discovered in the topology, a query is made for each of the supported properties:

[**KSPROPERTY\_AUDIO\_BASS**](./ksproperty-audio-bass.md)

[**KSPROPERTY\_AUDIO\_TREBLE**](./ksproperty-audio-treble.md)

[**KSPROPERTY\_AUDIO\_BASS\_BOOST**](./ksproperty-audio-bass-boost.md)

Each property query that succeeds generates a mixer-line control. Due to naming issues, a single tone node should support only a single property. If a device supports both bass and treble, for example, it should have two tone nodes so that the nodes can have different names.

A [**supermix node**](./ksnodetype-supermix.md) supports up to two controls: mute and volume. A supermix node can be used as a mute control when it satisfies at least one of these two conditions for every entry in the supermix node's [**capabilities table**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-ksaudio_mixcap_table):

-   The entry supports the mute property, as specified by the **Capabilities**.**Mute** flag.

-   The entry is fully attenuated (-infinity decibels attenuation) and cannot be turned up, which is specified by both **Capabilities**.**Minimum** and **Capabilities**.**Maximum** having the value LONG\_MIN (0x80000000).

A supermix node can be used as a volume control when every entry in the supermix capabilities table has a nonzero range. All other controls are translated one-to-one. When a recognized node is encountered, the mixer-line driver queries the respective property for that node.

To check for stereo or mono support, the left channel is queried, followed by the right channel, and finally, if both of these fail, the master channel (-1) is tried. If none of these queries succeeds, no control is generated for that node. Note that the MUX node is not queried for each channel. Instead, a single query to retrieve the current MUX selection is performed.

The name of the control is returned as a string when the node is queried for its [**KSPROPERTY\_TOPOLOGY\_NAME**](../stream/ksproperty-topology-name.md) property. If a node generates more than one control, all controls share the same name.

