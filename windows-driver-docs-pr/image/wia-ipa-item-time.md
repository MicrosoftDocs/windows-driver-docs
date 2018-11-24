---
title: WIA\_IPA\_ITEM\_TIME
description: The WIA\_IPA\_ITEM\_TIME property contains the time that an image was originally captured.
ms.assetid: 30e29169-7a1a-412e-858a-a467d6f1b44e
keywords: ["WIA_IPA_ITEM_TIME Imaging Devices"]
topic_type:
- apiref
api_name:
- WIA_IPA_ITEM_TIME
api_location:
- Wiadef.h
api_type:
- HeaderDef
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# WIA\_IPA\_ITEM\_TIME


The WIA\_IPA\_ITEM\_TIME property contains the time that an image was originally captured.

## <span id="ddk_wia_ipa_item_time_si"></span><span id="DDK_WIA_IPA_ITEM_TIME_SI"></span>


Property Type: VT\_UI2 | VT\_VECTOR

Valid Values: WIA\_PROP\_NONE

Access Rights: Read/write or read-only

Remarks
-------

The WIA minidriver creates and maintains the WIA\_IPA\_ITEM\_TIME property. This property should be reported as a vector of eight WORD values in the form of a SYSTEMTIME structure (which is described in the Microsoft Windows SDK documentation).

Requirements
------------

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Header</p></td>
<td>Wiadef.h (include Wiadef.h)</td>
</tr>
</tbody>
</table>

 

 





