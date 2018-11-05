---
title: KSPROPERTY\_AUDIO\_MIC\_SNR
description: The KSPROPERTY\_AUDIO\_MIC\_SNR property specifies the microphone signal to noise ratio (SNR) measured in dB units.
ms.assetid: 1DF088D0-7C0D-42B6-B7FA-2E714C70DAA4
keywords: ["KSPROPERTY_AUDIO_MIC_SNR Audio Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_AUDIO_MIC_SNR
api_location:
- Ksmedia.h
api_type:
- HeaderDef
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# KSPROPERTY\_AUDIO\_MIC\_SNR


The KSPROPERTY\_AUDIO\_MIC\_SNR property specifies the microphone signal to noise ratio (SNR) measured in dB units.

### <span id="Usage_Summary_Table"></span><span id="usage_summary_table"></span><span id="USAGE_SUMMARY_TABLE"></span>Usage Summary Table

Usage Summary Table

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

 

The property value (operation data) is of type LONG and contains the SNR information in dB units. The value uses fixed point decimal representation. The data is stored as a 16.16 fixed point value. The upper 16 bits are used for the whole number of the value and the lower 16 bits are used for the fractional portion of the value.

### <span id="Return_Value"></span><span id="return_value"></span><span id="RETURN_VALUE"></span>Return Value

A KSPROPERTY\_AUDIO\_MIC\_SNR property request returns a STATUS\_SUCCESS upon successful completion of the request. Otherwise, the request returns an appropriate error status code.

Remarks
-------

The audio driver can obtain microphone SNR for each microphone. This property allows this information to be retrieved from driver.

For Windows 10 voice recognition experiences such as Cortana to accurately detect and analyze user’s voice on various devices with different microphones, the OS needs to know certain characteristics of the input signal. Based on that information, the OS can calculate effective sensitivity and apply appropriate gain to enhance input signal. For more information, see [Voice Activation](https://msdn.microsoft.com/library/windows/hardware/mt593238).

KSPROPERTY\_AUDIO\_MIC\_SNR is available beginning with Windows 10, version 1607.

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

 

 





