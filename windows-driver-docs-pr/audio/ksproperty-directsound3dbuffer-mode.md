---
title: KSPROPERTY\_DIRECTSOUND3DBUFFER\_MODE
description: The KSPROPERTY\_DIRECTSOUND3DBUFFER\_MODE property specifies the processing mode of a 3D sound buffer.
ms.assetid: a3b15544-c534-47ea-a02e-5c8f9ccee414
keywords: ["KSPROPERTY_DIRECTSOUND3DBUFFER_MODE Audio Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_DIRECTSOUND3DBUFFER_MODE
api_location:
- Ksmedia.h
api_type:
- HeaderDef
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# KSPROPERTY\_DIRECTSOUND3DBUFFER\_MODE


The KSPROPERTY\_DIRECTSOUND3DBUFFER\_MODE property specifies the processing mode of a 3D sound buffer.

## <span id="ddk_ksproperty_directsound3dbuffer_mode_ks"></span><span id="DDK_KSPROPERTY_DIRECTSOUND3DBUFFER_MODE_KS"></span>


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
<td align="left"><p>ULONG</p></td>
</tr>
</tbody>
</table>

 

The property value (operation data) is of type ULONG and specifies the sound buffer's processing mode. The mode can have one of the following values, which are defined in header file Dsound.h:

-   DS3DMODE\_NORMAL

-   DS3DMODE\_HEADRELATIVE

-   DS3DMODE\_DISABLE

The meaning of these parameters is explained in the Microsoft Windows SDK documentation.

### <span id="Return_Value"></span><span id="return_value"></span><span id="RETURN_VALUE"></span>Return Value

A KSPROPERTY\_DIRECTSOUND3DBUFFER\_MODE property request returns STATUS\_SUCCESS to indicate that it has completed successfully. Otherwise, the request returns an appropriate error status code.

Remarks
-------

For additional information about the processing mode for a DirectSound 3D buffer, see the following in the Windows SDK documentation:

-   The **dwMode** member of the DS3DBUFFER structure.

-   The **IDirectSound3DBuffer::GetMode** and **IDirectSound3DBuffer::SetMode** methods.

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

 

 






