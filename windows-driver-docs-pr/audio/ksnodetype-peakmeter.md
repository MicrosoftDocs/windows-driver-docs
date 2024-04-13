---
title: KSNODETYPE\_PEAKMETER
description: KSNODETYPE\_PEAKMETER
keywords: ["KSNODETYPE_PEAKMETER Audio Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- KSNODETYPE_PEAKMETER
api_type:
- NA
ms.date: 04/21/2020
---

# KSNODETYPE\_PEAKMETER

## <span id="ddk_ksnodetype_peakmeter_ks"></span><span id="DDK_KSNODETYPE_PEAKMETER_KS"></span>

The **KSNODETYPE\_PEAKMETER** node represents a hardware peakmeter. A KS peakmeter node has one input pin and one output pin, and the two pins share the same data format.

A KS peakmeter internally logs the maximum value of the audio signal since the last time the peakmeter was reset to zero. The peakmeter automatically resets itself to zero after an IOCTL\_KS\_PROPERTY request to get a [**KSPROPERTY\_AUDIO\_PEAKMETER2**](ksproperty-audio-peakmeter2.md) property.

A peakmeter requires hardware support. A software peakmeter is not feasible, and this is because the adapter driver does not have access to signals that are present on line-in, microphone, or other inputs that are mixed with the playback channel.

Microsoft recommends making a peakmeter node the final node through which a stream passes within a filter. On a render stream, an audio adapter usually connects a peakmeter node after a master output [**KSNODETYPE\_MUTE**](ksnodetype-mute.md) node or a [**KSNODETYPE\_VOLUME**](ksnodetype-volume.md) node. The same approach applies to a capture stream or any other streams for which the filter incorporates a peakmeter node.

An audio adapter should name a peakmeter node KSAUDFNAME\_PEAKMETER.

A peakmeter node should provide a property handler for the property flags (see [**KSPROPERTY**](../stream/ksproperty-structure.md)) that appear in the following table.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Flag Name</th>
<th align="left">Meaning</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>KSPROPERTY_TYPE_GET</p></td>
<td align="left"><p>Returns the current value of the hardware peakmeter.</p></td>
</tr>
<tr class="even">
<td align="left"><p>KSPROPERTY_TYPE_BASICSUPPORT</p></td>
<td align="left"><p>
For KSPROPERTY_AUDIO_PEAKMETER - Returns a data range of 0x8000 to 0x7fff, which is the data range of 16-bit digital audio. The upper 16 bits must be set to zero, to allow the operating system to receive a positive value. Note that KSPROPERTY_AUDIO_PEAKMETER is deprecated and KSPROPERTY_AUDIO_PEAKMETER2 should be used instead.</p>
<p>For KSPROPERTY_AUDIO_PEAKMETER2 - Returns a data range of LONG_MIN to LONG_MAX.</p>
</td>
</tr>
</tbody>
</table>

The property handler should verify input parameters and left and right channel information.

A peakmeter node should also support the properties in the following table.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Property Name</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p><a href="ksproperty-audio-peakmeter2.md" data-raw-source="[&lt;strong&gt;KSPROPERTY_AUDIO_PEAKMETER2&lt;/strong&gt;](ksproperty-audio-peakmeter2.md)"><strong>KSPROPERTY_AUDIO_PEAKMETER2</strong></a></p></td>
<td align="left"><p>Represents the peakmeter control.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="ksproperty-audio-cpu-resources.md" data-raw-source="[&lt;strong&gt;KSPROPERTY_AUDIO_CPU_RESOURCES&lt;/strong&gt;](ksproperty-audio-cpu-resources.md)"><strong>KSPROPERTY_AUDIO_CPU_RESOURCES</strong></a></p></td>
<td align="left"><p>Indicates whether the specified node's functionality makes use of the host CPU.</p></td>
</tr>
</tbody>
</table>
