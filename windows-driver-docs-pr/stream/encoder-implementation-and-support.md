---
title: Encoder Implementation and Support
description: Encoder Implementation and Support
ms.assetid: 6ba97ff8-815b-490f-920b-6ede4f730e98
keywords:
- encoder devices WDK AVStream
- AVStream WDK , encoder devices
- uncompressed data streams WDK AVStream
- encoded streams WDK AVStream
- audio encoder devices WDK AVStream
- video encoder devices WDK AVStream
- property sets WDK encoder
- ENCAPIPARAM_BITRATE_MODE
- ENCAPIPARAM_BITRATE
- ENCAPIPARAM_PEAK_BITRATE
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Encoder Implementation and Support


In Windows XP Service Pack 1, Microsoft defined three kernel streaming property sets and one enumeration in *ksmedia.h* to support video-only encoder devices. Each property set contains a single property. In other words, each property receives its own property set. If your driver makes *get*-property or *Set*-property calls, then specify the property set's GUID (as defined in *ksmedia.h*) in the **Set** member of the [**KSPROPERTY**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ks/ns-ks-ksidentifier) structure and zero in the **Id** member when you set up the call:

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Property Set</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><a href="https://msdn.microsoft.com/library/windows/hardware/ff559520" data-raw-source="[ENCAPIPARAM_BITRATE](https://msdn.microsoft.com/library/windows/hardware/ff559520)">ENCAPIPARAM_BITRATE</a></td>
<td><p>Implement this property set to specify the encoding bit rates supported by the encoder device. See <a href="encoder-code-examples.md" data-raw-source="[Encoder Code Examples](encoder-code-examples.md)">Encoder Code Examples</a> for more details.</p></td>
</tr>
<tr class="even">
<td><a href="https://msdn.microsoft.com/library/windows/hardware/ff559524" data-raw-source="[ENCAPIPARAM_BITRATE_MODE](https://msdn.microsoft.com/library/windows/hardware/ff559524)">ENCAPIPARAM_BITRATE_MODE</a></td>
<td><p>Implement this property set to specify the encoding modes supported by the device. This property set uses the <a href="https://msdn.microsoft.com/library/windows/hardware/ff568695" data-raw-source="[&lt;strong&gt;VIDEOENCODER_BITRATE_MODE&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff568695)"><strong>VIDEOENCODER_BITRATE_MODE</strong></a> enumeration to specify the supported modes. See <a href="encoder-code-examples.md" data-raw-source="[Encoder Code Examples](encoder-code-examples.md)">Encoder Code Examples</a> for more details.</p></td>
</tr>
<tr class="odd">
<td><a href="https://msdn.microsoft.com/library/windows/hardware/ff559529" data-raw-source="[ENCAPIPARAM_PEAK_BITRATE](https://msdn.microsoft.com/library/windows/hardware/ff559529)">ENCAPIPARAM_PEAK_BITRATE</a></td>
<td><p>Implement this property set to specify the maximum encoding bit rate of the device.</p></td>
</tr>
</tbody>
</table>

 

Clients access these properties by deriving the **IVideoEncoder** COM interface from the **IEncoderAPI** COM interface (described in the Windows Software Development Kit (SDK) documentation).

A minidriver must specify default values for each of the ENCAPIPARAM\_*Xxx* properties. The topic [Encoder Code Examples](encoder-code-examples.md) demonstrates how to specify default property values. During the development and debugging of an encoder filter, the current property page can be triggered from a minidriver supporting the ENCAPIPARAM\_BITRATE property set.

In DirectX 9.0, six additional property sets and one event set were defined in *ksmedia.h* to provide better support for a wider variety of encoders, including audio-only encoders. As with ENCAPIPARAM\_*Xxx* properties, each property receives its own property set:

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Property Set</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><a href="https://msdn.microsoft.com/library/windows/hardware/ff557705" data-raw-source="[CODECAPI_VIDEO_ENCODER](https://msdn.microsoft.com/library/windows/hardware/ff557705)">CODECAPI_VIDEO_ENCODER</a></td>
<td><p>If your device supports encoding video streams (including auxiliary audio such as TV audio) then implement support for this property set.</p></td>
</tr>
<tr class="even">
<td><a href="https://msdn.microsoft.com/library/windows/hardware/ff557693" data-raw-source="[CODECAPI_AUDIO_ENCODER](https://msdn.microsoft.com/library/windows/hardware/ff557693)">CODECAPI_AUDIO_ENCODER</a></td>
<td><p>If your device is an audio-only encoder, then implement support for this property set instead of CODECAPI_VIDEO_ENCODER.</p></td>
</tr>
<tr class="odd">
<td><a href="https://msdn.microsoft.com/library/windows/hardware/ff557702" data-raw-source="[CODECAPI_SETALLDEFAULTS](https://msdn.microsoft.com/library/windows/hardware/ff557702)">CODECAPI_SETALLDEFAULTS</a></td>
<td><p>Implement this property set to reset all the encoder device&#39;s internal settings, such as encoding bit rate and encoding mode to their default values.</p></td>
</tr>
<tr class="even">
<td><a href="https://msdn.microsoft.com/library/windows/hardware/ff557691" data-raw-source="[CODECAPI_ALLSETTINGS](https://msdn.microsoft.com/library/windows/hardware/ff557691)">CODECAPI_ALLSETTINGS</a></td>
<td><p>Implement this property set to communicate the current settings of the encoder device. This property set is used for communication to and from clients.</p></td>
</tr>
<tr class="odd">
<td><a href="https://msdn.microsoft.com/library/windows/hardware/ff557703" data-raw-source="[CODECAPI_SUPPORTSEVENTS](https://msdn.microsoft.com/library/windows/hardware/ff557703)">CODECAPI_SUPPORTSEVENTS</a></td>
<td><p>If your device supports events from user mode--such as to change the encoding mode, bit rate, or other settings--then implement this property set. If you implement this property set, then you must also implement support for the CODECAPI_CHANGELISTS event.</p></td>
</tr>
<tr class="even">
<td><a href="https://msdn.microsoft.com/library/windows/hardware/ff557700" data-raw-source="[CODECAPI_CURRENTCHANGELIST](https://msdn.microsoft.com/library/windows/hardware/ff557700)">CODECAPI_CURRENTCHANGELIST</a></td>
<td><p>Implement this property set to determine which encoder parameters were changed in a previous call to set one or more encoder properties.</p></td>
</tr>
</tbody>
</table>

 

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Event Set</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff557696" data-raw-source="[CODECAPI_CHANGELISTS](https://msdn.microsoft.com/library/windows/hardware/ff557696)">CODECAPI_CHANGELISTS</a></p></td>
<td><p>If the device supports responding to user-mode events through the CODECAPI_SUPPORTSEVENTS property set, then implement this event set to return a list of encoder settings that have changed as the result of a client&#39;s prior <em>Set</em>-property call to either CODECAPI_SETALLDEFAULTS or CODECAPI_ALLSETTINGS.</p></td>
</tr>
</tbody>
</table>

 

Clients access these properties through the **ICodecAPI** COM interface (described in the Windows SDK documentation). See [Encoder Installation and Registration](encoder-installation-and-registration.md) for more information about the COM interfaces, including how to specify which interface KsProxy should expose.

A minidriver should implement support for basic *get*-property queries. The topic [Encoder Code Examples](encoder-code-examples.md) demonstrates how to support *get*-property queries.

When developing an encoder filter, move encoding functionality into a separate filter from a video capture filter. Define your own private mediums so that graph builders can properly connect encoder and capture filters. If your hardware is capable of bus mastering non-encoded content, then you may also expose public mediums. If you implement both public and private mediums, then list the private mediums first because it reduces graph building time; to find the correct filter when building a filter graph.

For more information about the issues and reasons to separate encoding functionality into its own filter, see the [Designing Video Capture Boards for Use with the Microsoft ActiveX Video Control](http://go.microsoft.com/fwlink/p/?linkid=204793) paper on the Microsoft website. For more information about using mediums and multiple instances of a filter (in separate filter graphs) see [Mediums and Categories](mediums-and-categories.md).

 

 




