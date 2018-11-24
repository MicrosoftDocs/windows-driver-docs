---
title: KSPROPERTY\_AUDIO\_ALGORITHM\_INSTANCE
description: The KSPROPERTY\_AUDIO\_ALGORITHM\_INSTANCE property specifies the digital signal processing (DSP) algorithm that is used to achieve the third-party effect that the node applies to the audio data stream.
ms.assetid: 8c27f856-de46-42a2-9f1f-e0cef1ee0f6e
keywords: ["KSPROPERTY_AUDIO_ALGORITHM_INSTANCE Audio Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_AUDIO_ALGORITHM_INSTANCE
api_location:
- Ksmedia.h
api_type:
- HeaderDef
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# KSPROPERTY\_AUDIO\_ALGORITHM\_INSTANCE


The KSPROPERTY\_AUDIO\_ALGORITHM\_INSTANCE property specifies the digital signal processing (DSP) algorithm that is used to achieve the third-party effect that the node applies to the audio data stream. The effects that are defined for this property include acoustic echo cancellation and noise suppression.

## <span id="ddk_ksproperty_audio_algorithm_instance_ks"></span><span id="DDK_KSPROPERTY_AUDIO_ALGORITHM_INSTANCE_KS"></span>


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
<td align="left"><p>Filter</p></td>
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff537143" data-raw-source="[&lt;strong&gt;KSNODEPROPERTY&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff537143)"><strong>KSNODEPROPERTY</strong></a></p></td>
<td align="left"><p>GUID</p></td>
</tr>
</tbody>
</table>

 

The property value (operation data) is a GUID that identifies the effect that the pin applies to its data stream. This value can be one of the following GUIDs from header file Ksmedia.h:

<span id="KSALGORITHMINSTANCE_SYSTEM_AGC"></span><span id="ksalgorithminstance_system_agc"></span>KSALGORITHMINSTANCE\_SYSTEM\_AGC  
Reserved for future use

<span id="KSALGORITHMINSTANCE_SYSTEM_ACOUSTIC_ECHO_CANCEL"></span><span id="ksalgorithminstance_system_acoustic_echo_cancel"></span>KSALGORITHMINSTANCE\_SYSTEM\_ACOUSTIC\_ECHO\_CANCEL  
System default acoustic echo cancellation algorithm

<span id="KSALGORITHMINSTANCE_SYSTEM_MICROPHONE_ARRAY_PROCESSOR"></span><span id="ksalgorithminstance_system_microphone_array_processor"></span>KSALGORITHMINSTANCE\_SYSTEM\_MICROPHONE\_ARRAY\_PROCESSOR  
Reserved for future use

<span id="KSALGORITHMINSTANCE_SYSTEM_NOISE_SUPPRESS"></span><span id="ksalgorithminstance_system_noise_suppress"></span>KSALGORITHMINSTANCE\_SYSTEM\_NOISE\_SUPPRESS  
System default noise suppression algorithm

### <span id="Return_Value"></span><span id="return_value"></span><span id="RETURN_VALUE"></span>Return Value

A KSPROPERTY\_AUDIO\_ALGORITHM\_INSTANCE property request returns STATUS\_SUCCESS to indicate that it has completed successfully. Otherwise, the request returns an appropriate error status code.

Remarks
-------

This property is used to control the DSP algorithm that is performed by an AEC node ([**KSNODETYPE\_ACOUSTIC\_ECHO\_CANCEL**](ksnodetype-acoustic-echo-cancel.md)) or noise suppression node ([**KSNODETYPE\_NOISE\_SUPPRESS**](ksnodetype-noise-suppress.md)).

The algorithm-instance GUID matches the value in the **guidDSCFXInstance** member of a DSCEFFECTDESC structure that a caller passes to the **IDirectSoundCapture::CreateCaptureBuffer** method or **DirectSoundFullDuplexCreate** function. For more information, see the Microsoft Windows SDK documentation.

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

## <span id="see_also"></span>See also


[**KSNODEPROPERTY**](https://msdn.microsoft.com/library/windows/hardware/ff537143)

[**KSNODETYPE\_ACOUSTIC\_ECHO\_CANCEL**](ksnodetype-acoustic-echo-cancel.md)

[**KSNODETYPE\_NOISE\_SUPPRESS**](ksnodetype-noise-suppress.md)

 

 






