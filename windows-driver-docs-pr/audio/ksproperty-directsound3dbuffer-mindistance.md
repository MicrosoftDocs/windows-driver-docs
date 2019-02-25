---
title: KSPROPERTY\_DIRECTSOUND3DBUFFER\_MINDISTANCE
description: The KSPROPERTY\_DIRECTSOUND3DBUFFER\_MINDISTANCE property specifies the minimum distance for a 3D sound buffer.
ms.assetid: 998e591d-7c23-4857-908c-4e90918c9a94
keywords: ["KSPROPERTY_DIRECTSOUND3DBUFFER_MINDISTANCE Audio Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_DIRECTSOUND3DBUFFER_MINDISTANCE
api_location:
- Ksmedia.h
api_type:
- HeaderDef
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# KSPROPERTY\_DIRECTSOUND3DBUFFER\_MINDISTANCE


The KSPROPERTY\_DIRECTSOUND3DBUFFER\_MINDISTANCE property specifies the minimum distance for a 3D sound buffer.

## <span id="ddk_ksproperty_directsound3dbuffer_mindistance_ks"></span><span id="DDK_KSPROPERTY_DIRECTSOUND3DBUFFER_MINDISTANCE_KS"></span>


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

 

The property value (operation data) is of type FLOAT and specifies the minimum distance. For information about distance units, see [**KSPROPERTY\_DIRECTSOUND3DLISTENER\_DISTANCEFACTOR**](ksproperty-directsound3dlistener-distancefactor.md).

### <span id="Return_Value"></span><span id="return_value"></span><span id="RETURN_VALUE"></span>Return Value

A KSPROPERTY\_DIRECTSOUND3DBUFFER\_MINDISTANCE property request returns STATUS\_SUCCESS to indicate that it has completed successfully. Otherwise, the request returns an appropriate error status code.

Remarks
-------

At a distance less than the minimum distance from a sound source, the sound volume no longer increases as the distance decreases. For more information about the minimum distance for a DirectSound 3D buffer, see the following in the Microsoft Windows SDK documentation:

-   The **flMinDistance** member of the DS3DBUFFER structure.

-   The **IDirectSound3DBuffer::GetMinDistance** and **IDirectSound3DBuffer::SetMinDistance** methods.

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

[**KSPROPERTY\_DIRECTSOUND3DLISTENER\_DISTANCEFACTOR**](ksproperty-directsound3dlistener-distancefactor.md)

 

 






