---
title: Topology Nodes
description: Topology Nodes
ms.assetid: 39827413-2b6b-4925-97bb-e0f3e3428b13
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
ms.localizationpriority: medium
---

# Topology Nodes


## <span id="topology_nodes"></span><span id="TOPOLOGY_NODES"></span>


Audio applications can access mixer controls through the Microsoft Windows multimedia function [**mixerGetLineControls**](https://msdn.microsoft.com/library/windows/desktop/dd757302). This function retrieves an array of one or more MIXERCONTROL structures, each of which describes the state and metrics of a single control node on an audio line. The **dwControlType** member of the MIXERCONTROL structure is set to an enumeration value that specifies the type of the control. A number of mixer-control types have been specified for audio VxDs, but only a subset of these controls is available for WDM audio drivers.

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
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff537154" data-raw-source="[&lt;strong&gt;KSNODETYPE_AGC&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff537154)"><strong>KSNODETYPE_AGC</strong></a></p></td>
<td align="left"><p>MIXERCONTROL_CONTROLTYPE_ONOFF</p></td>
</tr>
<tr class="even">
<td align="left"><p>Loudness</p></td>
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff537174" data-raw-source="[&lt;strong&gt;KSNODETYPE_LOUDNESS&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff537174)"><strong>KSNODETYPE_LOUDNESS</strong></a></p></td>
<td align="left"><p>MIXERCONTROL_CONTROLTYPE_LOUDNESS</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Mute</p></td>
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff537178" data-raw-source="[&lt;strong&gt;KSNODETYPE_MUTE&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff537178)"><strong>KSNODETYPE_MUTE</strong></a></p></td>
<td align="left"><p>MIXERCONTROL_CONTROLTYPE_MUTE</p></td>
</tr>
<tr class="even">
<td align="left"><p>Tone (multiple)</p></td>
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff537205" data-raw-source="[&lt;strong&gt;KSNODETYPE_TONE&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff537205)"><strong>KSNODETYPE_TONE</strong></a></p></td>
<td align="left"><p>MIXERCONTROL_CONTROLTYPE_ONOFF (if KSPROPERTY_AUDIO_BASS_BOOST is supported)</p>
<p>MIXERCONTROL_CONTROLTYPE_BASS (if KSPROPERTY_AUDIO_BASS is supported)</p>
<p>MIXERCONTROL_CONTROLTYPE_TREBLE (if KSPROPERTY_AUDIO_TREBLE is supported)</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Volume</p></td>
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff537208" data-raw-source="[&lt;strong&gt;KSNODETYPE_VOLUME&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff537208)"><strong>KSNODETYPE_VOLUME</strong></a></p></td>
<td align="left"><p>MIXERCONTROL_CONTROLTYPE_VOLUME</p></td>
</tr>
<tr class="even">
<td align="left"><p>Peakmeter</p></td>
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff537183" data-raw-source="[&lt;strong&gt;KSNODETYPE_PEAKMETER&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff537183)"><strong>KSNODETYPE_PEAKMETER</strong></a></p></td>
<td align="left"><p>MIXERCONTROL_CONTROLTYPE_PEAKMETER</p></td>
</tr>
<tr class="odd">
<td align="left"><p>MUX</p></td>
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff537180" data-raw-source="[&lt;strong&gt;KSNODETYPE_MUX&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff537180)"><strong>KSNODETYPE_MUX</strong></a></p></td>
<td align="left"><p>MIXERCONTROL_CONTROLTYPE_MUX</p></td>
</tr>
<tr class="even">
<td align="left"><p>Stereo wide</p></td>
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff537194" data-raw-source="[&lt;strong&gt;KSNODETYPE_STEREO_WIDE&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff537194)"><strong>KSNODETYPE_STEREO_WIDE</strong></a></p></td>
<td align="left"><p>MIXERCONTROL_CONTROLTYPE_FADER</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Chorus</p></td>
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff537156" data-raw-source="[&lt;strong&gt;KSNODETYPE_CHORUS&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff537156)"><strong>KSNODETYPE_CHORUS</strong></a></p></td>
<td align="left"><p>MIXERCONTROL_CONTROLTYPE_FADER</p></td>
</tr>
<tr class="even">
<td align="left"><p>Reverb</p></td>
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff537189" data-raw-source="[&lt;strong&gt;KSNODETYPE_REVERB&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff537189)"><strong>KSNODETYPE_REVERB</strong></a></p></td>
<td align="left"><p>MIXERCONTROL_CONTROLTYPE_FADER</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Supermix (multiple)</p></td>
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff537198" data-raw-source="[&lt;strong&gt;KSNODETYPE_SUPERMIX&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff537198)"><strong>KSNODETYPE_SUPERMIX</strong></a></p></td>
<td align="left"><p>MIXERCONTROL_CONTROLTYPE_MUTE (if KSPROPERTY_AUDIO_MUTE is supported in the supermix node)</p>
<p>MIXERCONTROL_CONTROLTYPE_VOLUME (see comments in text)</p></td>
</tr>
</tbody>
</table>

 

Topology-node types that are missing from the preceding table are not translated into mixer-line controls, and mixer-line controls that are missing from the table are not supported by WDM audio drivers.

Note that MIXERCONTROL\_CONTROLTYPE\_CUSTOM is missing from the table. This means that WDM audio drivers do not support custom mixer controls.

A [**tone node**](https://msdn.microsoft.com/library/windows/hardware/ff537205) supports four properties: [**bass**](https://msdn.microsoft.com/library/windows/hardware/ff537242), [**treble**](https://msdn.microsoft.com/library/windows/hardware/ff537308), [**mid-frequency**](https://msdn.microsoft.com/library/windows/hardware/ff537290), and [**bass boost**](https://msdn.microsoft.com/library/windows/hardware/ff537245). The mid-frequency property has no mixer-line counterpart, but the other three properties do. For each tone node discovered in the topology, a query is made for each of the supported properties:

[**KSPROPERTY\_AUDIO\_BASS**](https://msdn.microsoft.com/library/windows/hardware/ff537242)

[**KSPROPERTY\_AUDIO\_TREBLE**](https://msdn.microsoft.com/library/windows/hardware/ff537308)

[**KSPROPERTY\_AUDIO\_BASS\_BOOST**](https://msdn.microsoft.com/library/windows/hardware/ff537245)

Each property query that succeeds generates a mixer-line control. Due to naming issues, a single tone node should support only a single property. If a device supports both bass and treble, for example, it should have two tone nodes so that the nodes can have different names.

A [**supermix node**](https://msdn.microsoft.com/library/windows/hardware/ff537198) supports up to two controls: mute and volume. A supermix node can be used as a mute control when it satisfies at least one of these two conditions for every entry in the supermix node's [**capabilities table**](https://msdn.microsoft.com/library/windows/hardware/ff537088):

-   The entry supports the mute property, as specified by the **Capabilities**.**Mute** flag.

-   The entry is fully attenuated (-infinity decibels attenuation) and cannot be turned up, which is specified by both **Capabilities**.**Minimum** and **Capabilities**.**Maximum** having the value LONG\_MIN (0x80000000).

A supermix node can be used as a volume control when every entry in the supermix capabilities table has a nonzero range. All other controls are translated one-to-one. When a recognized node is encountered, the mixer-line driver queries the respective property for that node.

To check for stereo or mono support, the left channel is queried, followed by the right channel, and finally, if both of these fail, the master channel (-1) is tried. If none of these queries succeeds, no control is generated for that node. Note that the MUX node is not queried for each channel. Instead, a single query to retrieve the current MUX selection is performed.

The name of the control is returned as a string when the node is queried for its [**KSPROPERTY\_TOPOLOGY\_NAME**](https://msdn.microsoft.com/library/windows/hardware/ff565809) property. If a node generates more than one control, all controls share the same name.

 

 




