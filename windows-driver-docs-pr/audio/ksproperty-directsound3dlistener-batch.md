---
title: KSPROPERTY\_DIRECTSOUND3DLISTENER\_BATCH
description: The KSPROPERTY\_DIRECTSOUND3DLISTENER\_BATCH property specifies the batch-mode setting for a 3D listener.
ms.assetid: 370191f8-e5a2-40f0-a979-c14cf7f44756
keywords: ["KSPROPERTY_DIRECTSOUND3DLISTENER_BATCH Audio Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_DIRECTSOUND3DLISTENER_BATCH
api_location:
- Ksmedia.h
api_type:
- HeaderDef
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# KSPROPERTY\_DIRECTSOUND3DLISTENER\_BATCH


The KSPROPERTY\_DIRECTSOUND3DLISTENER\_BATCH property specifies the batch-mode setting for a 3D listener.

## <span id="ddk_ksproperty_directsound3dlistener_batch_ks"></span><span id="DDK_KSPROPERTY_DIRECTSOUND3DLISTENER_BATCH_KS"></span>


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
<td align="left"><p>BOOL</p></td>
</tr>
</tbody>
</table>

 

The property value (operation data) is of type BOOL and specifies the batch-mode setting:

-   When the value of this property is **TRUE**, the miniport driver should cache all changes to the listener properties and all associated buffer properties.

-   When the value is **FALSE**, changes to the listener properties and buffer properties take effect immediately.

### <span id="Return_Value"></span><span id="return_value"></span><span id="RETURN_VALUE"></span>Return Value

A KSPROPERTY\_DIRECTSOUND3DLISTENER\_BATCH property request returns STATUS\_SUCCESS to indicate that it has completed successfully. Otherwise, the request returns an appropriate error status code.

Remarks
-------

When this property transitions from **TRUE** to **FALSE** the miniport driver should put all cached properties into effect immediately. If possible, any cached properties should be put into effect simultaneously.

For more information about batch-mode settings for 3D listeners, see the description of the **IDirectSound3DListener::CommitDeferredSettings** method in the Microsoft Windows SDK documentation.

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

 

 






