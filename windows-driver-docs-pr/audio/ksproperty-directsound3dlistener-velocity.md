---
title: KSPROPERTY\_DIRECTSOUND3DLISTENER\_VELOCITY
description: The KSPROPERTY\_DIRECTSOUND3DLISTENER\_VELOCITY property specifies the velocity vector of a 3D listener.
ms.assetid: 654a8cd1-c8ad-4d65-9d14-7602d269bcff
keywords: ["KSPROPERTY_DIRECTSOUND3DLISTENER_VELOCITY Audio Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_DIRECTSOUND3DLISTENER_VELOCITY
api_location:
- Ksmedia.h
api_type:
- HeaderDef
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# KSPROPERTY\_DIRECTSOUND3DLISTENER\_VELOCITY


The KSPROPERTY\_DIRECTSOUND3DLISTENER\_VELOCITY property specifies the velocity vector of a 3D listener.

## <span id="ddk_ksproperty_directsound3dlistener_velocity_ks"></span><span id="DDK_KSPROPERTY_DIRECTSOUND3DLISTENER_VELOCITY_KS"></span>


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
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff536367" data-raw-source="[&lt;strong&gt;DS3DVECTOR&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff536367)"><strong>DS3DVECTOR</strong></a></p></td>
</tr>
</tbody>
</table>

 

The property value (operation data) is a structure of type DS3DVECTOR that specifies the velocity vector. Velocity is expressed in distance units per second. The default distance unit is a meter. The distance unit can be changed by sending a [**KSPROPERTY\_DIRECTSOUND3DLISTENER\_DISTANCEFACTOR**](ksproperty-directsound3dlistener-distancefactor.md)set-property request.

### <span id="Return_Value"></span><span id="return_value"></span><span id="RETURN_VALUE"></span>Return Value

A KSPROPERTY\_DIRECTSOUND3DLISTENER\_VELOCITY property request returns STATUS\_SUCCESS to indicate that it has completed successfully. Otherwise, the request returns an appropriate error status code.

Remarks
-------

DirectSound uses this property to implement the **IDirectSound3DListener::GetVelocity** and **IDirectSound3DListener::SetVelocity** methods, which are described in the Microsoft Windows SDK documentation.

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

[**DS3DVECTOR**](https://msdn.microsoft.com/library/windows/hardware/ff536367)

 

 






