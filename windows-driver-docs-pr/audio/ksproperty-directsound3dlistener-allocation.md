---
title: KSPROPERTY\_DIRECTSOUND3DLISTENER\_ALLOCATION
description: The KSPROPERTY\_DIRECTSOUND3DLISTENER\_ALLOCATION property is used to tell the driver when to allocate and free the storage for its listener data.
keywords: ["KSPROPERTY_DIRECTSOUND3DLISTENER_ALLOCATION Audio Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- KSPROPERTY_DIRECTSOUND3DLISTENER_ALLOCATION
api_location:
- Ksmedia.h
api_type:
- HeaderDef
ms.date: 03/06/2023
---


# KSPROPERTY\_DIRECTSOUND3DLISTENER\_ALLOCATION


The KSPROPERTY\_DIRECTSOUND3DLISTENER\_ALLOCATION property is used to tell the driver when to allocate and free the storage for its listener data. Storage is allocated when the listener is created, and freed when the listener is deleted. This property can also be used to query the driver whether listener data is currently allocated.

## <span id="ddk_ksproperty_directsound3dlistener_allocation_ks"></span><span id="DDK_KSPROPERTY_DIRECTSOUND3DLISTENER_ALLOCATION_KS"></span>


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
<td align="left"><p>BOOL</p></td>
</tr>
</tbody>
</table>

 

The property value (operation data) is of type BOOL. For a set-property request, this value specifies whether the driver should allocate or free the storage for its listener data:

-   A value of **TRUE** directs the driver to allocate storage for its listener data.

-   A value of **FALSE** tells the driver to free the listener data.

For a get-property request, a value of **TRUE** or **FALSE** indicates whether the driver currently holds a storage allocation for listener data.

### <span id="Return_Value"></span><span id="return_value"></span><span id="RETURN_VALUE"></span>Return Value

A KSPROPERTY\_DIRECTSOUND3DLISTENER\_ALLOCATION property request returns STATUS\_SUCCESS to indicate that it has completed successfully. Otherwise, the request returns an appropriate error status code.

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

