---
title: KSPROPERTY\_AUDIO\_POSITIONEX
description: The KSPROPERTY\_AUDIO\_POSITIONEX property provides the caller with the stream position and the associated timestamp information for a kernel streaming (KS)-based audio driver.
ms.assetid: 660b1ee9-7c52-4d95-8df9-b1c0dce320e3
keywords: ["KSPROPERTY_AUDIO_POSITIONEX Audio Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_AUDIO_POSITIONEX
api_location:
- Ksmedia.h
api_type:
- HeaderDef
---

# KSPROPERTY\_AUDIO\_POSITIONEX


The KSPROPERTY\_AUDIO\_POSITIONEX property provides the caller with the stream position and the associated timestamp information for a kernel streaming (KS)-based audio driver.

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
<th align="left">Get</th>
<th align="left">Set</th>
<th align="left">Target</th>
<th align="left">Property descriptor type</th>
<th align="left">Property value type</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>Yes</p></td>
<td align="left"><p>No</p></td>
<td align="left"><p>Pin</p></td>
<td align="left"><p>[<strong>KSPROPERTY</strong>](https://msdn.microsoft.com/library/windows/hardware/ff564262)</p></td>
<td align="left"><p>[<strong>KSAUDIO_POSITIONEX</strong>](https://msdn.microsoft.com/library/windows/hardware/ff537092)</p></td>
</tr>
</tbody>
</table>

 

The property value (operation data) is a structure of type KSAUDIO\_POSITIONEX that receives the position information from the property handler. The position information that is specified by the KSAUDIO\_POSITIONEX structure is the position information for the pin that was selected by the caller.

### <span id="Return_Value"></span><span id="return_value"></span><span id="RETURN_VALUE"></span>Return Value

The KSPROPERTY\_AUDIO\_POSITIONEX property request returns S\_OK if the call was successful. Otherwise, it returns the appropriate HRESULT error code.

Remarks
-------

Typically, audio applications must monitor the current position of an audio stream. This position is specified as a byte offset from the beginning of the stream. There are two possible interpretations of the stream position information:

-   In the case of a rendering stream, the stream position is the byte offset of the audio frame that is currently playing through the digital-to-analog converters (DACs).

-   In the case of a capture stream, the stream position is the byte offset of the audio frame that is currently being recorded through the analog-to-digital converters (ADCs).

A driver that supports the KSPROPERTY\_AUDIO\_POSITIONEX property generates a timestamp window for the stream position value. The timestamp window is the interval between the timestamp that is sampled before stream position is determined and the timestamp that is taken after the stream position is determined. The caller then determines whether it can use the timestamp window.

Requirements
------------

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p>Version</p></td>
<td align="left"><p>Available in Windows Vista and later versions of Windows.</p></td>
</tr>
<tr class="even">
<td align="left"><p>Header</p></td>
<td align="left">Ksmedia.h (include Ksmedia.h)</td>
</tr>
</tbody>
</table>

## <span id="see_also"></span>See also


[**KSAUDIO\_POSITIONEX**](https://msdn.microsoft.com/library/windows/hardware/ff537092)

[**KSPROPERTY**](https://msdn.microsoft.com/library/windows/hardware/ff564262)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[audio\audio]:%20KSPROPERTY_AUDIO_POSITIONEX%20%20RELEASE:%20%2811/22/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





