---
title: KSPROPERTY\_DIRECTSOUND3DLISTENER\_DISTANCEFACTOR
description: The KSPROPERTY\_DIRECTSOUND3DLISTENER\_DISTANCEFACTOR property specifies the distance factor that should be applied to any distance values.
ms.assetid: 38daa5d8-d70f-4484-bf5a-a9a365296313
keywords: ["KSPROPERTY_DIRECTSOUND3DLISTENER_DISTANCEFACTOR Audio Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_DIRECTSOUND3DLISTENER_DISTANCEFACTOR
api_location:
- Ksmedia.h
api_type:
- HeaderDef
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# KSPROPERTY\_DIRECTSOUND3DLISTENER\_DISTANCEFACTOR


The KSPROPERTY\_DIRECTSOUND3DLISTENER\_DISTANCEFACTOR property specifies the distance factor that should be applied to any distance values.

## <span id="ddk_ksproperty_directsound3dlistener_distancefactor_ks"></span><span id="DDK_KSPROPERTY_DIRECTSOUND3DLISTENER_DISTANCEFACTOR_KS"></span>


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

 

The property value (operation data) is of type FLOAT and specifies the distance factor.

### <span id="Return_Value"></span><span id="return_value"></span><span id="RETURN_VALUE"></span>Return Value

A KSPROPERTY\_DIRECTSOUND3DLISTENER\_DISTANCEFACTOR property request returns STATUS\_SUCCESS to indicate that it has completed successfully. Otherwise, the request returns an appropriate error status code.

Remarks
-------

Distances for KSPROPSETID\_DirectSound3DBuffer and KSPROPSETID\_DirectSound3DListener properties are expressed in units of meters times a distance factor.

By default, the distance factor is 1 and distances are therefore expressed in meters. (Also, the default velocity units are meters per second.)

A client can change the distance units for the **KSPROPSETID\_DirectSound3DBuffer** and **KSPROPSETID\_DirectSound3DListener** properties by sending a KSPROPERTY\_DIRECTSOUND3DLISTENER\_DISTANCEFACTOR set-property request that specifies a different distance factor.

DirectSound uses this property to implement the **IDirectSound3DListener::GetDistanceFactor** and **IDirectSound3DListener::SetDistanceFactor** methods, which are described in the Microsoft Windows SDK documentation.

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

 

 






