---
title: KSPROPERTY\_DIRECTSOUND3DBUFFER\_MAXDISTANCE
description: The KSPROPERTY\_DIRECTSOUND3DBUFFER\_MAXDISTANCE property specifies the maximum distance for a 3D sound buffer.
ms.assetid: efa69fe3-834a-42be-a578-f284b07b93c4
keywords: ["KSPROPERTY_DIRECTSOUND3DBUFFER_MAXDISTANCE Audio Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_DIRECTSOUND3DBUFFER_MAXDISTANCE
api_location:
- Ksmedia.h
api_type:
- HeaderDef
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# KSPROPERTY\_DIRECTSOUND3DBUFFER\_MAXDISTANCE


The KSPROPERTY\_DIRECTSOUND3DBUFFER\_MAXDISTANCE property specifies the maximum distance for a 3D sound buffer.

## <span id="ddk_ksproperty_directsound3dbuffer_maxdistance_ks"></span><span id="DDK_KSPROPERTY_DIRECTSOUND3DBUFFER_MAXDISTANCE_KS"></span>


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
<td align="left">[<strong>KSNODEPROPERTY</strong>](https://msdn.microsoft.com/library/windows/hardware/ff537143)</td>
<td align="left"><p>FLOAT</p></td>
</tr>
</tbody>
</table>

 

The property value (operation data) is of type FLOAT and specifies the maximum distance. For information about distance units, see [**KSPROPERTY\_DIRECTSOUND3DLISTENER\_DISTANCEFACTOR**](ksproperty-directsound3dlistener-distancefactor.md).

### <span id="Return_Value"></span><span id="return_value"></span><span id="RETURN_VALUE"></span>Return Value

A KSPROPERTY\_DIRECTSOUND3DBUFFER\_MAXDISTANCE property request returns STATUS\_SUCCESS to indicate that it has completed successfully. Otherwise, the request returns an appropriate error status code.

Remarks
-------

At a distance that exceeds the maximum distance from a sound source, the sound from that source is reduced to silence. For more information about the maximum distance for a DirectSound 3D buffer, see the following in the Microsoft Windows SDK documentation:

-   The **flMaxDistance** member of the DS3DBUFFER structure.

-   The **IDirectSound3DBuffer::GetMaxDistance** and **IDirectSound3DBuffer::SetMaxDistance** methods.

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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[audio\audio]:%20KSPROPERTY_DIRECTSOUND3DBUFFER_MAXDISTANCE%20%20RELEASE:%20%2811/22/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





