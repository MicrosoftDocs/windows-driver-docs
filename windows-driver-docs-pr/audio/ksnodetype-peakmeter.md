---
title: KSNODETYPE\_PEAKMETER
description: KSNODETYPE\_PEAKMETER
ms.assetid: 11c886eb-dd63-44dd-9bca-dd19a8dd6948
keywords: ["KSNODETYPE_PEAKMETER Audio Devices"]
topic_type:
- apiref
api_name:
- KSNODETYPE_PEAKMETER
api_type:
- NA
---

# KSNODETYPE\_PEAKMETER


## <span id="ddk_ksnodetype_peakmeter_ks"></span><span id="DDK_KSNODETYPE_PEAKMETER_KS"></span>


The KSNODETYPE\_PEAKMETER node represents a hardware peakmeter. A KS peakmeter node has one input pin and one output pin, and the two pins share the same data format.

A KS peakmeter internally logs the maximum value of the audio signal since the last time the peakmeter was reset to zero. The peakmeter automatically resets itself to zero after an IOCTL\_KS\_PROPERTY request to get a [**KSPROPERTY\_AUDIO\_PEAKMETER**](ksproperty-audio-peakmeter.md) property.

A peakmeter requires hardware support. A software peakmeter is not feasible, and this is because the adapter driver does not have access to signals that are present on line-in, microphone, or other inputs that are mixed with the playback channel.

Microsoft recommends making a peakmeter node the final node through which a stream passes within a filter. On a render stream, an audio adapter usually connects a peakmeter node after a master output [**KSNODETYPE\_MUTE**](ksnodetype-mute.md) node or a [**KSNODETYPE\_VOLUME**](ksnodetype-volume.md) node. The same approach applies to a capture stream or any other streams for which the filter incorporates a peakmeter node.

An audio adapter should name a peakmeter node KSAUDFNAME\_PEAKMETER.

A peakmeter node should provide a property handler for the property flags (see [**KSPROPERTY**](https://msdn.microsoft.com/library/windows/hardware/ff564262)) that appear in the following table.

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
<td align="left"><p>Returns a data range of -32768 to 32767, which is the data range of 16-bit digital audio.</p></td>
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
<td align="left"><p>[<strong>KSPROPERTY_AUDIO_PEAKMETER</strong>](ksproperty-audio-peakmeter.md)</p></td>
<td align="left"><p>Represents the peakmeter control.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>KSPROPERTY_AUDIO_CPU_RESOURCES</strong>](ksproperty-audio-cpu-resources.md)</p></td>
<td align="left"><p>Indicates whether the specified node's functionality makes use of the host CPU.</p></td>
</tr>
</tbody>
</table>

 

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[audio\audio]:%20KSNODETYPE_PEAKMETER%20%20RELEASE:%20%2811/22/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




