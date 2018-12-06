---
title: KSPROPERTY\_DIRECTSOUND3DLISTENER\_ROLLOFFFACTOR
description: The KSPROPERTY\_DIRECTSOUND3DLISTENER\_ROLLOFFFACTOR property specifies the rolloff factor for a 3D listener.
ms.assetid: 3eef80ef-921b-4364-b31d-14a62f305f5d
keywords: ["KSPROPERTY_DIRECTSOUND3DLISTENER_ROLLOFFFACTOR Audio Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_DIRECTSOUND3DLISTENER_ROLLOFFFACTOR
api_location:
- Ksmedia.h
api_type:
- HeaderDef
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# KSPROPERTY\_DIRECTSOUND3DLISTENER\_ROLLOFFFACTOR


The KSPROPERTY\_DIRECTSOUND3DLISTENER\_ROLLOFFFACTOR property specifies the rolloff factor for a 3D listener.

## <span id="ddk_ksproperty_directsound3dlistener_rollofffactor_ks"></span><span id="DDK_KSPROPERTY_DIRECTSOUND3DLISTENER_ROLLOFFFACTOR_KS"></span>


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
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff537143" data-raw-source="[&lt;strong&gt;KSNODEPROPERTY&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff537143)"><strong>KSNODEPROPERTY</strong></a></p></td>
<td align="left"><p>FLOAT</p></td>
</tr>
</tbody>
</table>

 

The property value (operation data) is of type FLOAT and specifies the rolloff factor. The rolloff factor can range from DS3D\_MINROLLOFFFACTOR to DS3D\_MAXROLLOFFFACTOR, which are defined as 0.0 and 10.0 respectively. The default rolloff factor is DS3D\_DEFAULTROLLOFFFACTOR, which is defined as 1.0.

### <span id="Return_Value"></span><span id="return_value"></span><span id="RETURN_VALUE"></span>Return Value

A KSPROPERTY\_DIRECTSOUND3DLISTENER\_ROLLOFFFACTOR property request returns STATUS\_SUCCESS to indicate that it has completed successfully. Otherwise, the request returns an appropriate error status code.

Remarks
-------

Rolloff is the amount of attenuation that is applied to sounds, based on the listener's distance from the sound source. A rolloff factor of zero means that no attenuation is applied to a sound regardless of its distance from the listener. Factors larger than 1 exaggerate the real-world attenuation of sound with distance.

DirectSound uses this property to implement the **IDirectSound3DListener::GetRolloffFactor** and **IDirectSound3DListener::SetRolloffFactor** methods, which are described in the Microsoft Windows SDK documentation.

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

 

 






