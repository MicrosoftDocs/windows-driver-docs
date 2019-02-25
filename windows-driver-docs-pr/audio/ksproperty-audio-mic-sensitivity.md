---
title: KSPROPERTY\_AUDIO\_MIC\_SENSITIVITY
description: The KSPROPERTY\_AUDIO\_MIC\_SENSITIVITY property specifies the microphone sensitivity in decibels relative to full scale (dBFS) units.
ms.assetid: FE62AAA5-E022-459F-817B-3661535FA9BD
keywords: ["KSPROPERTY_AUDIO_MIC_SENSITIVITY Audio Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_AUDIO_MIC_SENSITIVITY
api_location:
- Ksmedia.h
api_type:
- HeaderDef
ms.date: 05/10/2018
ms.localizationpriority: medium
---

# KSPROPERTY\_AUDIO\_MIC\_SENSITIVITY

The KSPROPERTY\_AUDIO\_MIC\_SENSITIVITY property specifies the microphone sensitivity in decibels relative to full scale (dBFS) units.

> [!NOTE]
> KSPROPERTY\_AUDIO\_MIC\_SENSITIVITY is deprecated starting with Windows 10 Version 1803. 
> Use [KSPROPERTY\_AUDIO\_MIC\_SENSITIVITY2](ksproperty-audio-mic-sensitivity2.md) instead.

### <span id="Usage_Summary_Table"></span><span id="usage_summary_table"></span><span id="USAGE_SUMMARY_TABLE"></span>Usage Summary Table



<table>
<colgroup>
<col width="20%" />
<col width="20%" />
<col width="20%" />
<col width="20%" />
<col width="20%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p>Get</p></td>
<td align="left"><p>Set</p></td>
<td align="left"><p>Target</p></td>
<td align="left"><p>Property descriptor type</p></td>
<td align="left"><p>Property value type</p></td>
</tr>
<tr class="even">
<td align="left"><p>Yes</p></td>
<td align="left"><p>No</p></td>
<td align="left"><p>Pin Instance</p></td>
<td align="left"><a href="https://msdn.microsoft.com/library/windows/hardware/ff566722" data-raw-source="[&lt;strong&gt;KSP_PIN&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff566722)"><strong>KSP_PIN</strong></a></td>
<td align="left">LONG</td>
</tr>
</tbody>
</table>

 

The property value (operation data) is of type LONG and contains sensitivity information in decibels relative to dBFS units. The sensitivity value uses the following scale. The value uses fixed point decimal representation. The data is stored as a 16.16 fixed point value. The upper 16 bits are used for the whole number of the value and the lower 16 bits are used for the fractional portion of the value.

### <span id="Return_Value"></span><span id="return_value"></span><span id="RETURN_VALUE"></span>Return Value

A KSPROPERTY\_AUDIO\_MIC\_SENSITIVITY property request returns a STATUS\_SUCCESS upon successful completion of the request. Otherwise, the request returns an appropriate error status code.

Remarks
-------

The audio driver can obtain microphone sensitivity for each microphone. This property allows this information to be retrieved from driver.

For Windows 10 voice recognition experiences such as Cortana to accurately detect and analyze user’s voice on various devices with different microphones, the OS needs to know certain characteristics of the input signal. Based on that information, the OS can calculate effective sensitivity and apply appropriate gain to enhance input signal. For more information, see [Voice Activation](https://msdn.microsoft.com/library/windows/hardware/mt593238).

KSPROPERTY\_AUDIO\_MIC\_SENSITIVITY is available beginning with Windows 10, version 1607.

Requirements
------------

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p>Header</p></td>
<td align="left">Ksmedia.h (include Ksmedia.h)</td>
</tr>
</tbody>
</table>

 

 





