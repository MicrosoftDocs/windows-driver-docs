---
title: KSPROPERTY\_DIRECTSOUND3DLISTENER\_ORIENTATION
description: The KSPROPERTY\_DIRECTSOUND3DLISTENER\_ORIENTATION property specifies the orientation of a 3D listener.
ms.assetid: 324b0def-e989-4dd1-9266-17d018dd512c
keywords: ["KSPROPERTY_DIRECTSOUND3DLISTENER_ORIENTATION Audio Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_DIRECTSOUND3DLISTENER_ORIENTATION
api_location:
- Ksmedia.h
api_type:
- HeaderDef
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# KSPROPERTY\_DIRECTSOUND3DLISTENER\_ORIENTATION


The KSPROPERTY\_DIRECTSOUND3DLISTENER\_ORIENTATION property specifies the orientation of a 3D listener.

## <span id="ddk_ksproperty_directsound3dlistener_orientation_ks"></span><span id="DDK_KSPROPERTY_DIRECTSOUND3DLISTENER_ORIENTATION_KS"></span>


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
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff537119" data-raw-source="[&lt;strong&gt;KSDS3D_LISTENER_ORIENTATION&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff537119)"><strong>KSDS3D_LISTENER_ORIENTATION</strong></a></p></td>
</tr>
</tbody>
</table>

 

The property value (operation data) is a structure of type KSDS3D\_LISTENER\_ORIENTATION that specifies the listener's orientation.

### <span id="Return_Value"></span><span id="return_value"></span><span id="RETURN_VALUE"></span>Return Value

A KSPROPERTY\_DIRECTSOUND3DLISTENER\_ORIENTATION property request returns STATUS\_SUCCESS to indicate that it has completed successfully. Otherwise, the request returns an appropriate error status code.

Remarks
-------

DirectSound uses this property to implement the **IDirectSound3DListener::GetOrientation** and **IDirectSound3DListener::SetOrientation** methods, which are described in the Microsoft Windows SDK documentation.

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

[**KSDS3D\_LISTENER\_ORIENTATION**](https://msdn.microsoft.com/library/windows/hardware/ff537119)

 

 






