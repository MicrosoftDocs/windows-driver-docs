---
title: KSPROPERTY\_DIRECTSOUND3DBUFFER\_CONEANGLES
description: The KSPROPERTY\_DIRECTSOUND3DBUFFER\_CONEANGLES property specifies the inside and outside cone angles of the sound projection cone for a 3D sound buffer.
ms.assetid: a3978aaf-218c-4021-abf0-e426eacf52c7
keywords: ["KSPROPERTY_DIRECTSOUND3DBUFFER_CONEANGLES Audio Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_DIRECTSOUND3DBUFFER_CONEANGLES
api_location:
- Ksmedia.h
api_type:
- HeaderDef
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# KSPROPERTY\_DIRECTSOUND3DBUFFER\_CONEANGLES


The KSPROPERTY\_DIRECTSOUND3DBUFFER\_CONEANGLES property specifies the inside and outside cone angles of the sound projection cone for a 3D sound buffer.

## <span id="ddk_ksproperty_directsound3dbuffer_coneangles_ks"></span><span id="DDK_KSPROPERTY_DIRECTSOUND3DBUFFER_CONEANGLES_KS"></span>


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
<td align="left"><a href="https://msdn.microsoft.com/library/windows/hardware/ff537143" data-raw-source="[&lt;strong&gt;KSNODEPROPERTY&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff537143)"><strong>KSNODEPROPERTY</strong></a></td>
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff537103" data-raw-source="[&lt;strong&gt;KSDS3D_BUFFER_CONE_ANGLES&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff537103)"><strong>KSDS3D_BUFFER_CONE_ANGLES</strong></a></p></td>
</tr>
</tbody>
</table>

 

The property value (operation data) is a structure of type KSDS3D\_BUFFER\_CONE\_ANGLES that specifies the inside and outside cone angles.

### <span id="Return_Value"></span><span id="return_value"></span><span id="RETURN_VALUE"></span>Return Value

A KSPROPERTY\_DIRECTSOUND3DBUFFER\_CONEANGLES property request returns STATUS\_SUCCESS to indicate that it has completed successfully. Otherwise, the request returns an appropriate error status code.

Remarks
-------

For more information about the inside and outside cone angles of the sound projection cone for a DirectSound 3D buffer, see the following in the Microsoft Windows SDK documentation:

-   The **dwInsideConeAngle** and **dwOutsideConeAngle** members of the DS3DBUFFER structure.

-   The **IDirectSound3DBuffer::GetConeAngles** and **IDirectSound3DBuffer::SetConeAngles** methods.

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

[**KSDS3D\_BUFFER\_CONE\_ANGLES**](https://msdn.microsoft.com/library/windows/hardware/ff537103)

 

 






