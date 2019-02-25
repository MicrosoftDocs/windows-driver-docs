---
title: KSPROPERTY\_AUDIO\_3D\_INTERFACE
description: The KSPROPERTY\_AUDIO\_3D\_INTERFACE property specifies the 3D algorithm to use to process the data in the sound buffer.
ms.assetid: 76c56e61-23ef-43ad-b66b-2412fd247b6e
keywords: ["KSPROPERTY_AUDIO_3D_INTERFACE Audio Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_AUDIO_3D_INTERFACE
api_location:
- Ksmedia.h
api_type:
- HeaderDef
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# KSPROPERTY\_AUDIO\_3D\_INTERFACE


The KSPROPERTY\_AUDIO\_3D\_INTERFACE property specifies the 3D algorithm to use to process the data in the sound buffer.

## <span id="ddk_ksproperty_audio_3d_interface_ks"></span><span id="DDK_KSPROPERTY_AUDIO_3D_INTERFACE_KS"></span>


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
<td align="left"><p>GUID</p></td>
</tr>
</tbody>
</table>

 

The property value (operation data) is a GUID that specifies a 3D algorithm. This value can be one of the following GUIDs from header file Dsound.h:

-   DS3DALG\_DEFAULT

-   DS3DALG\_NO\_VIRTUALIZATION

-   DS3DALG\_HRTF\_FULL

-   DS3DALG\_HRTF\_LIGHT

For more information about these GUIDs, see the description of the **guid3dAlgorithm** member of the DSBUFFERDESC structure in the Microsoft Windows SDK documentation.

### <span id="Return_Value"></span><span id="return_value"></span><span id="RETURN_VALUE"></span>Return Value

A KSPROPERTY\_AUDIO\_3D\_INTERFACE property request returns STATUS\_SUCCESS to indicate that it has completed successfully. Otherwise, the request returns an appropriate error status code.

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

[**KSNODETYPE\_3D\_EFFECTS**](ksnodetype-3d-effects.md)

 

 






