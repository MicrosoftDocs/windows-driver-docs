---
title: KSPROPERTY\_STREAM\_FRAMETIME
description: The KSPROPERTY\_STREAM\_FRAMETIME property allows a client to determine the duration of the next frame based on the particular media stream, and use that information to step-frame a sequence.
ms.assetid: 0cc218eb-1f21-4b45-ac48-b3e308bddfaf
keywords: ["KSPROPERTY_STREAM_FRAMETIME Streaming Media Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_STREAM_FRAMETIME
api_location:
- ks.h
api_type:
- HeaderDef
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# KSPROPERTY\_STREAM\_FRAMETIME


The KSPROPERTY\_STREAM\_FRAMETIME property allows a client to determine the duration of the next frame based on the particular media stream, and use that information to step-frame a sequence.

## <span id="ddk_ksproperty_stream_frametime_ks"></span><span id="DDK_KSPROPERTY_STREAM_FRAMETIME_KS"></span>


### <span id="Usage_Summary_Table"></span><span id="usage_summary_table"></span><span id="USAGE_SUMMARY_TABLE"></span>Usage Summary Table

<table>
<colgroup>
<col width="20%" />
<col width="20%" />
<col width="20%" />
<col width="20%" />
<col width="20%" />
</colgroup>
<thead>
<tr class="header">
<th>Get</th>
<th>Set</th>
<th>Target</th>
<th>Property Descriptor Type</th>
<th>Property Value Type</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>Yes</p></td>
<td><p>No</p></td>
<td><p>Pin</p></td>
<td><p>[<strong>KSPROPERTY</strong>](https://msdn.microsoft.com/library/windows/hardware/ff564262)</p></td>
<td><p>[<strong>KSFRAMETIME</strong>](https://msdn.microsoft.com/library/windows/hardware/ff562558)</p></td>
</tr>
</tbody>
</table>

 

Remarks
-------

KSPROPERTY\_STREAM\_FRAMETIME is an optional property that should be implemented if a pin recognizes the specifics of the media type it is transporting.

The property is supported by rendering pins and is used to return the duration of the next frame of data and any flags associated with that frame. A frame is generally the smallest usable unit into which the data can be split. For a video stream, this might be a video frame or a field. For audio, this would be a sample for each channel in the stream. For MIDI, this would be the next MIDI event.

The duration is measured in terms of the presentation time units provided by the pin. This is dependent on the interface and the numerator/denominator pair used in the presentation time. This does not apply to streams that are not oriented toward any specific media type, such as generic file readers.

Requirements
------------

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Header</p></td>
<td>Ks.h (include Ks.h)</td>
</tr>
</tbody>
</table>

## <span id="see_also"></span>See also


[**KSPROPERTY**](https://msdn.microsoft.com/library/windows/hardware/ff564262)

[**KSFRAMETIME**](https://msdn.microsoft.com/library/windows/hardware/ff562558)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstream\stream%5D:%20KSPROPERTY_STREAM_FRAMETIME%20%20RELEASE:%20%2811/22/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





