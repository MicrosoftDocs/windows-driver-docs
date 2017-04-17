---
title: Encoder Implementation and Support
author: windows-driver-content
description: Encoder Implementation and Support
ms.assetid: 6ba97ff8-815b-490f-920b-6ede4f730e98
keywords: ["encoder devices WDK AVStream", "AVStream WDK , encoder devices", "uncompressed data streams WDK AVStream", "encoded streams WDK AVStream", "audio encoder devices WDK AVStream", "video encoder devices WDK AVStream", "property sets WDK encoder", "ENCAPIPARAM_BITRATE_MODE", "ENCAPIPARAM_BITRATE", "ENCAPIPARAM_PEAK_BITRATE"]
---

# Encoder Implementation and Support


In Windows XP Service Pack 1, Microsoft defined three kernel streaming property sets and one enumeration in *ksmedia.h* to support video-only encoder devices. Each property set contains a single property. In other words, each property receives its own property set. If your driver makes *get*-property or *Set*-property calls, then specify the property set's GUID (as defined in *ksmedia.h*) in the **Set** member of the [**KSPROPERTY**](https://msdn.microsoft.com/library/windows/hardware/ff564262) structure and zero in the **Id** member when you set up the call:

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
<td>[ENCAPIPARAM_BITRATE](https://msdn.microsoft.com/library/windows/hardware/ff559520)</td>
<td><p>Implement this property set to specify the encoding bit rates supported by the encoder device. See [Encoder Code Examples](encoder-code-examples.md) for more details.</p></td>
</tr>
<tr class="even">
<td>[ENCAPIPARAM_BITRATE_MODE](https://msdn.microsoft.com/library/windows/hardware/ff559524)</td>
<td><p>Implement this property set to specify the encoding modes supported by the device. This property set uses the [<strong>VIDEOENCODER_BITRATE_MODE</strong>](https://msdn.microsoft.com/library/windows/hardware/ff568695) enumeration to specify the supported modes. See [Encoder Code Examples](encoder-code-examples.md) for more details.</p></td>
</tr>
<tr class="odd">
<td>[ENCAPIPARAM_PEAK_BITRATE](https://msdn.microsoft.com/library/windows/hardware/ff559529)</td>
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
<td>[CODECAPI_VIDEO_ENCODER](https://msdn.microsoft.com/library/windows/hardware/ff557705)</td>
<td><p>If your device supports encoding video streams (including auxiliary audio such as TV audio) then implement support for this property set.</p></td>
</tr>
<tr class="even">
<td>[CODECAPI_AUDIO_ENCODER](https://msdn.microsoft.com/library/windows/hardware/ff557693)</td>
<td><p>If your device is an audio-only encoder, then implement support for this property set instead of CODECAPI_VIDEO_ENCODER.</p></td>
</tr>
<tr class="odd">
<td>[CODECAPI_SETALLDEFAULTS](https://msdn.microsoft.com/library/windows/hardware/ff557702)</td>
<td><p>Implement this property set to reset all the encoder device's internal settings, such as encoding bit rate and encoding mode to their default values.</p></td>
</tr>
<tr class="even">
<td>[CODECAPI_ALLSETTINGS](https://msdn.microsoft.com/library/windows/hardware/ff557691)</td>
<td><p>Implement this property set to communicate the current settings of the encoder device. This property set is used for communication to and from clients.</p></td>
</tr>
<tr class="odd">
<td>[CODECAPI_SUPPORTSEVENTS](https://msdn.microsoft.com/library/windows/hardware/ff557703)</td>
<td><p>If your device supports events from user mode--such as to change the encoding mode, bit rate, or other settings--then implement this property set. If you implement this property set, then you must also implement support for the CODECAPI_CHANGELISTS event.</p></td>
</tr>
<tr class="even">
<td>[CODECAPI_CURRENTCHANGELIST](https://msdn.microsoft.com/library/windows/hardware/ff557700)</td>
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
<td><p>[CODECAPI_CHANGELISTS](https://msdn.microsoft.com/library/windows/hardware/ff557696)</p></td>
<td><p>If the device supports responding to user-mode events through the CODECAPI_SUPPORTSEVENTS property set, then implement this event set to return a list of encoder settings that have changed as the result of a client's prior <em>Set</em>-property call to either CODECAPI_SETALLDEFAULTS or CODECAPI_ALLSETTINGS.</p></td>
</tr>
</tbody>
</table>

 

Clients access these properties through the **ICodecAPI** COM interface (described in the Windows SDK documentation). See [Encoder Installation and Registration](encoder-installation-and-registration.md) for more information about the COM interfaces, including how to specify which interface KsProxy should expose.

A minidriver should implement support for basic *get*-property queries. The topic [Encoder Code Examples](encoder-code-examples.md) demonstrates how to support *get*-property queries.

When developing an encoder filter, move encoding functionality into a separate filter from a video capture filter. Define your own private mediums so that graph builders can properly connect encoder and capture filters. If your hardware is capable of bus mastering non-encoded content, then you may also expose public mediums. If you implement both public and private mediums, then list the private mediums first because it reduces graph building time; to find the correct filter when building a filter graph.

For more information about the issues and reasons to separate encoding functionality into its own filter, see the [Designing Video Capture Boards for Use with the Microsoft ActiveX Video Control](http://go.microsoft.com/fwlink/p/?linkid=204793) paper on the Microsoft website. For more information about using mediums and multiple instances of a filter (in separate filter graphs) see [Mediums and Categories](mediums-and-categories.md).

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstream\stream%5D:%20Encoder%20Implementation%20and%20Support%20%20RELEASE:%20%288/23/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


