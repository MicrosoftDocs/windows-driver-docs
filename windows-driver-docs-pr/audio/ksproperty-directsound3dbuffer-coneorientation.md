---
title: KSPROPERTY\_DIRECTSOUND3DBUFFER\_CONEORIENTATION
description: The KSPROPERTY\_DIRECTSOUND3DBUFFER\_CONEORIENTATION property specifies the orientation of the sound-projection cone for a 3D sound buffer.
keywords: ["KSPROPERTY_DIRECTSOUND3DBUFFER_CONEORIENTATION Audio Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- KSPROPERTY_DIRECTSOUND3DBUFFER_CONEORIENTATION
api_location:
- Ksmedia.h
api_type:
- HeaderDef
ms.date: 03/06/2023
---


# KSPROPERTY\_DIRECTSOUND3DBUFFER\_CONEORIENTATION


The KSPROPERTY\_DIRECTSOUND3DBUFFER\_CONEORIENTATION property specifies the orientation of the sound-projection cone for a 3D sound buffer.

## <span id="ddk_ksproperty_directsound3dbuffer_coneorientation_ks"></span><span id="DDK_KSPROPERTY_DIRECTSOUND3DBUFFER_CONEORIENTATION_KS"></span>


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
<td align="left"><a href="/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-ksnodeproperty" data-raw-source="[&lt;strong&gt;KSNODEPROPERTY&lt;/strong&gt;](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-ksnodeproperty)"><strong>KSNODEPROPERTY</strong></a></td>
<td align="left"><p><a href="/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-_ds3dvector" data-raw-source="[&lt;strong&gt;DS3DVECTOR&lt;/strong&gt;](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-_ds3dvector)"><strong>DS3DVECTOR</strong></a></p></td>
</tr>
</tbody>
</table>

 

The property value (operation data) is a structure of type DS3DVECTOR that specifies the orientation of the sound-projection cone.

### <span id="Return_Value"></span><span id="return_value"></span><span id="RETURN_VALUE"></span>Return Value

A KSPROPERTY\_DIRECTSOUND3DBUFFER\_CONEORIENTATION property request returns STATUS\_SUCCESS to indicate that it has completed successfully. Otherwise, the request returns an appropriate error status code.

## Remarks

For more information about the orientation of the sound projection cone for a DirectSound 3D buffer, see the following in the Microsoft Windows SDK documentation:

-   The **vConeOrientation** member of the DS3DBUFFER structure.

-   The **IDirectSound3DBuffer::GetConeOrientation** and **IDirectSound3DBuffer::SetConeOrientation** methods.

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

