---
title: KSPROPERTY\_AUDIO\_POSITION
description: The KSPROPERTY\_AUDIO\_POSITION property specifies the current positions of the play and write cursors in the sound buffer for the pin's audio stream.
ms.assetid: 859990bc-18c0-429a-afb6-07b5adc98630
keywords: ["KSPROPERTY_AUDIO_POSITION Audio Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_AUDIO_POSITION
api_location:
- Ksmedia.h
api_type:
- HeaderDef
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# KSPROPERTY\_AUDIO\_POSITION


The KSPROPERTY\_AUDIO\_POSITION property specifies the current positions of the play and write cursors in the sound buffer for the pin's audio stream.

## <span id="ddk_ksproperty_audio_position_ks"></span><span id="DDK_KSPROPERTY_AUDIO_POSITION_KS"></span>


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
<td align="left"><p>Pin</p></td>
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff564262" data-raw-source="[&lt;strong&gt;KSPROPERTY&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff564262)"><strong>KSPROPERTY</strong></a></p></td>
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff537091" data-raw-source="[&lt;strong&gt;KSAUDIO_POSITION&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff537091)"><strong>KSAUDIO_POSITION</strong></a></p></td>
</tr>
</tbody>
</table>

 

The property value (operation data) is a structure of type KSAUDIO\_POSITION that specifies a render stream's play and write positions or a capture stream's record and read positions.

### <span id="Return_Value"></span><span id="return_value"></span><span id="RETURN_VALUE"></span>Return Value

A KSPROPERTY\_AUDIO\_POSITION property request returns STATUS\_SUCCESS to indicate that it has completed successfully. Otherwise, the request returns an appropriate error status code.

Remarks
-------

DirectSound uses the KSPROPERTY\_AUDIO\_POSITION property to implement the **IDirectSoundBuffer::GetCurrentPosition** and **IDirectSoundBuffer::SetCurrentPosition** methods. The Windows multimedia functions **waveInGetPosition** and **waveOutGetPosition** also use this property. For more information about DirectSound and the Windows multimedia functions, see the Microsoft Windows SDK documentation.

WaveCyclic and WavePci miniport drivers do not need to implement property handlers for KSPROPERTY\_AUDIO\_POSITION because the WaveCyclic and WavePci port drivers handle this property on behalf of miniport drivers. To obtain the play position in a render stream or record position in a capture stream, the property handler in the port driver calls the miniport driver's [**IMiniportWaveCyclicStream::GetPosition**](https://msdn.microsoft.com/library/windows/hardware/ff536716) or [**IMiniportWavePciStream::GetPosition**](https://msdn.microsoft.com/library/windows/hardware/ff536727) method.

For more information, see [Audio Position Property](https://msdn.microsoft.com/library/windows/hardware/ff536211).

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


[**KSPROPERTY**](https://msdn.microsoft.com/library/windows/hardware/ff564262)

[**KSAUDIO\_POSITION**](https://msdn.microsoft.com/library/windows/hardware/ff537091)

[**IMiniportWaveCyclicStream::GetPosition**](https://msdn.microsoft.com/library/windows/hardware/ff536716)

[**IMiniportWavePciStream::GetPosition**](https://msdn.microsoft.com/library/windows/hardware/ff536727)

 

 






