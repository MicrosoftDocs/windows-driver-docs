---
title: KSPROPERTY\_AUDIOENGINE\_VOLUMELEVEL
description: The KSPROPERTY\_AUDIOENGINE\_VOLUMELEVEL property specifies the volume level of a channel in a given stream.
ms.assetid: E10E2ADC-BD76-4871-85DA-19385A0D77EE
keywords: ["KSPROPERTY_AUDIOENGINE_VOLUMELEVEL Audio Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_AUDIOENGINE_VOLUMELEVEL
api_location:
- Ksmedia.h
api_type:
- HeaderDef
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# KSPROPERTY\_AUDIOENGINE\_VOLUMELEVEL


The **KSPROPERTY\_AUDIOENGINE\_VOLUMELEVEL** property specifies the volume level of a channel in a given stream.

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
<td align="left"><p>Yes</p></td>
<td align="left"><p>Node via Pin instance</p></td>
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff537145" data-raw-source="[&lt;strong&gt;KSNODEPROPERTY_AUDIO_CHANNEL&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff537145)"><strong>KSNODEPROPERTY_AUDIO_CHANNEL</strong></a></p></td>
<td align="left"><p>LONG (for a Get request) and <a href="https://msdn.microsoft.com/library/windows/hardware/hh831854" data-raw-source="[&lt;strong&gt;KSAUDIOENGINE_VOLUMELEVEL&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/hh831854)"><strong>KSAUDIOENGINE_VOLUMELEVEL</strong></a> (for a Set request).</p></td>
</tr>
</tbody>
</table>

 

For a Get request, the property value is of type LONG, and it specifies the volume level of a channel in a given a stream. Volume-level values use the following scale and can be bounded by the minimum and maximum values supplied in the Basic Support response for this property:

-2147483648 (0x80000000 in hexadecimal, or LONG\_MIN) is -Infinity decibels (attenuation),

-2147483647 (0x80000001 in hexadecimal, or LONG\_MIN + 1) is -32767.99998474 decibels (attenuation), and

+2147483647 (0x7FFFFFFF in hexadecimal, or LONG\_MAX) is +32767.99998474 decibels (gain).

&gt; \[!Note\]
&gt;  The decibel range is represented by integer values from -2147483648 to +2147483647, where this scale has a resolution of 1/65536 decibel.

 

For a Set request, the property value is of type **KSAUDIOENGINE\_VOLUMELEVEL**, and it specifies the desired volume level of a channel in a given stream, as well as a curve type and curve duration to be applied as the volume level is set. If a value is specified beyond the range of the filter, the request to set this property will still be successful. But the actual value that was applied to the filter can only be determined by a subsequent Get call to this property.

### <span id="Return_Value"></span><span id="return_value"></span><span id="RETURN_VALUE"></span>Return Value

The [**KSPROPERTY\_AUDIOENGINE\_SUPPORTEDDEVICEFORMATS**](ksproperty-audioengine-supporteddeviceformats.md) property request returns **STATUS\_SUCCESS** to indicate that it has completed successfully. Otherwise, the request returns an appropriate error status code.

Remarks
-------

The property descriptor for **KSPROPERTY\_AUDIOENGINE\_VOLUMELEVEL** specifies a channel number. If the stream that passes through the audio engine node contains *n* channels, the channels are numbered 0 through *n-1*. Also note that a channel value of 0xFFFFFFFF indicates that the request applies to all channels. If a property request is made while the stream is not in a running state, the volume level is immediately set to the requested level. If the stream leaves the run state while a volume level ramp is in progress, the volume level of the stream is immediately set to the target level of the current fade. If a new property request is made while an existing volume level ramp is in progress, the new ramp request must begin from the current volume level - the level that the volume had reached when the new request arrived.

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
<td align="left"><p>Windows 8</p></td>
</tr>
<tr class="even">
<td align="left"><p>Header</p></td>
<td align="left">Ksmedia.h</td>
</tr>
</tbody>
</table>

## <span id="see_also"></span>See also


[**KSAUDIOENGINE\_VOLUMELEVEL**](https://msdn.microsoft.com/library/windows/hardware/hh831854)

[**KSNODEPROPERTY\_AUDIO\_CHANNEL**](https://msdn.microsoft.com/library/windows/hardware/ff537145)

[**KSPROPERTY\_AUDIOENGINE**](ksproperty-audioengine.md)

[**KSPROPERTY\_AUDIOENGINE\_SUPPORTEDDEVICEFORMATS**](ksproperty-audioengine-supporteddeviceformats.md)

 

 






