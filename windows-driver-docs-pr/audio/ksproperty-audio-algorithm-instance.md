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
<td align="left"><p>[<strong>KSNODEPROPERTY</strong>](https://msdn.microsoft.com/library/windows/hardware/ff537143)</p></td>
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[audio\audio]:%20KSPROPERTY_AUDIO_ALGORITHM_INSTANCE%20%20RELEASE:%20%2811/22/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





