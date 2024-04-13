---
title: KSPROPERTY\_DIRECTSOUND3DLISTENER\_POSITION
description: The KSPROPERTY\_DIRECTSOUND3DLISTENER\_POSITION property specifies the position of a 3D listener.
keywords: ["KSPROPERTY_DIRECTSOUND3DLISTENER_POSITION Audio Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- KSPROPERTY_DIRECTSOUND3DLISTENER_POSITION
api_location:
- Ksmedia.h
api_type:
- HeaderDef
ms.date: 03/06/2023
---


# KSPROPERTY\_DIRECTSOUND3DLISTENER\_POSITION


The KSPROPERTY\_DIRECTSOUND3DLISTENER\_POSITION property specifies the position of a 3D listener.

## <span id="ddk_ksproperty_directsound3dlistener_position_ks"></span><span id="DDK_KSPROPERTY_DIRECTSOUND3DLISTENER_POSITION_KS"></span>


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
<td align="left"><p><a href="/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-ksnodeproperty" data-raw-source="[&lt;strong&gt;KSNODEPROPERTY&lt;/strong&gt;](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-ksnodeproperty)"><strong>KSNODEPROPERTY</strong></a></p></td>
<td align="left"><p><a href="/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-_ds3dvector" data-raw-source="[&lt;strong&gt;DS3DVECTOR&lt;/strong&gt;](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-_ds3dvector)"><strong>DS3DVECTOR</strong></a></p></td>
</tr>
</tbody>
</table>

 

The property value (operation data) is a structure of type DS3DVECTOR that specifies the listener's position. Position coordinates are expressed in the current distance units. For information about distance units, see [**KSPROPERTY\_DIRECTSOUND3DLISTENER\_DISTANCEFACTOR**](ksproperty-directsound3dlistener-distancefactor.md).

### <span id="Return_Value"></span><span id="return_value"></span><span id="RETURN_VALUE"></span>Return Value

A KSPROPERTY\_DIRECTSOUND3DLISTENER\_POSITION property request returns STATUS\_SUCCESS to indicate that it has completed successfully. Otherwise, the request returns an appropriate error status code.

## Remarks

DirectSound uses this property to implement the **IDirectSound3DListener::GetPosition** and **IDirectSound3DListener::SetPosition** methods, which are described in the Microsoft Windows SDK documentation.

## Requirements

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


[**KSNODEPROPERTY**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-ksnodeproperty)

[**DS3DVECTOR**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-_ds3dvector)

[**KSPROPERTY\_DIRECTSOUND3DLISTENER\_DISTANCEFACTOR**](ksproperty-directsound3dlistener-distancefactor.md)

