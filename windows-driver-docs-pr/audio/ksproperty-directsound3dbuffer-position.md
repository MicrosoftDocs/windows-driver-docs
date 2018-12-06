---
title: KSPROPERTY\_DIRECTSOUND3DBUFFER\_POSITION
description: The KSPROPERTY\_DIRECTSOUND3DBUFFER\_POSITION property specifies the position of a 3D sound buffer.
ms.assetid: 727ffb54-f020-473f-8631-1300da0f312c
keywords: ["KSPROPERTY_DIRECTSOUND3DBUFFER_POSITION Audio Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_DIRECTSOUND3DBUFFER_POSITION
api_location:
- Ksmedia.h
api_type:
- HeaderDef
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# KSPROPERTY\_DIRECTSOUND3DBUFFER\_POSITION


The KSPROPERTY\_DIRECTSOUND3DBUFFER\_POSITION property specifies the position of a 3D sound buffer.

## <span id="ddk_ksproperty_directsound3dbuffer_position_ks"></span><span id="DDK_KSPROPERTY_DIRECTSOUND3DBUFFER_POSITION_KS"></span>


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

 

The property value (operation data) is a structure of type DS3DVECTOR that specifies the buffer position. For information about position units, see [**KSPROPERTY\_DIRECTSOUND3DLISTENER\_DISTANCEFACTOR**](ksproperty-directsound3dlistener-distancefactor.md).

### <span id="Return_Value"></span><span id="return_value"></span><span id="RETURN_VALUE"></span>Return Value

A KSPROPERTY\_DIRECTSOUND3DBUFFER\_POSITION property request returns STATUS\_SUCCESS to indicate that it has completed successfully. Otherwise, the request returns an appropriate error status code.

Remarks
-------

For more information about the position of a DirectSound 3D buffer, see the following in the Microsoft Windows SDK documentation:

-   The **vPosition** member of the DS3DBUFFER structure.

-   The **IDirectSound3DBuffer::GetPosition** and **IDirectSound3DBuffer::SetPosition** methods.

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

[**KSPROPERTY\_DIRECTSOUND3DLISTENER\_DISTANCEFACTOR**](ksproperty-directsound3dlistener-distancefactor.md)

 

 






