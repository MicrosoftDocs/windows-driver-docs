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
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
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
<td align="left"><p>[<strong>KSNODETYPE_AGC</strong>](https://msdn.microsoft.com/library/windows/hardware/ff537154)</p></td>
<td align="left"><p>MIXERCONTROL_CONTROLTYPE_ONOFF</p></td>
</tr>
<tr class="even">
<td align="left"><p>Loudness</p></td>
<td align="left"><p>[<strong>KSNODETYPE_LOUDNESS</strong>](https://msdn.microsoft.com/library/windows/hardware/ff537174)</p></td>
<td align="left"><p>MIXERCONTROL_CONTROLTYPE_LOUDNESS</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Mute</p></td>
<td align="left"><p>[<strong>KSNODETYPE_MUTE</strong>](https://msdn.microsoft.com/library/windows/hardware/ff537178)</p></td>
<td align="left"><p>MIXERCONTROL_CONTROLTYPE_MUTE</p></td>
</tr>
<tr class="even">
<td align="left"><p>Tone (multiple)</p></td>
<td align="left"><p>[<strong>KSNODETYPE_TONE</strong>](https://msdn.microsoft.com/library/windows/hardware/ff537205)</p></td>
<td align="left"><p>MIXERCONTROL_CONTROLTYPE_ONOFF (if KSPROPERTY_AUDIO_BASS_BOOST is supported)</p>
<p>MIXERCONTROL_CONTROLTYPE_BASS (if KSPROPERTY_AUDIO_BASS is supported)</p>
<p>MIXERCONTROL_CONTROLTYPE_TREBLE (if KSPROPERTY_AUDIO_TREBLE is supported)</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Volume</p></td>
<td align="left"><p>[<strong>KSNODETYPE_VOLUME</strong>](https://msdn.microsoft.com/library/windows/hardware/ff537208)</p></td>
<td align="left"><p>MIXERCONTROL_CONTROLTYPE_VOLUME</p></td>
</tr>
<tr class="even">
<td align="left"><p>Peakmeter</p></td>
<td align="left"><p>[<strong>KSNODETYPE_PEAKMETER</strong>](https://msdn.microsoft.com/library/windows/hardware/ff537183)</p></td>
<td align="left"><p>MIXERCONTROL_CONTROLTYPE_PEAKMETER</p></td>
</tr>
<tr class="odd">
<td align="left"><p>MUX</p></td>
<td align="left"><p>[<strong>KSNODETYPE_MUX</strong>](https://msdn.microsoft.com/library/windows/hardware/ff537180)</p></td>
<td align="left"><p>MIXERCONTROL_CONTROLTYPE_MUX</p></td>
</tr>
<tr class="even">
<td align="left"><p>Stereo wide</p></td>
<td align="left"><p>[<strong>KSNODETYPE_STEREO_WIDE</strong>](https://msdn.microsoft.com/library/windows/hardware/ff537194)</p></td>
<td align="left"><p>MIXERCONTROL_CONTROLTYPE_FADER</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Chorus</p></td>
<td align="left"><p>[<strong>KSNODETYPE_CHORUS</strong>](https://msdn.microsoft.com/library/windows/hardware/ff537156)</p></td>
<td align="left"><p>MIXERCONTROL_CONTROLTYPE_FADER</p></td>
</tr>
<tr class="even">
<td align="left"><p>Reverb</p></td>
<td align="left"><p>[<strong>KSNODETYPE_REVERB</strong>](https://msdn.microsoft.com/library/windows/hardware/ff537189)</p></td>
<td align="left"><p>MIXERCONTROL_CONTROLTYPE_FADER</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Supermix (multiple)</p></td>
<td align="left"><p>[<strong>KSNODETYPE_SUPERMIX</strong>](https://msdn.microsoft.com/library/windows/hardware/ff537198)</p></td>
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

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[audio\audio]:%20Topology%20Nodes%20%20RELEASE:%20%287/18/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


