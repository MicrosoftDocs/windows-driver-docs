---
title: CODECAPI\_SUPPORTSEVENTS
description: CODECAPI\_SUPPORTSEVENTS
ms.assetid: feb6d110-9a9c-4e2b-bc19-259f80f3947a
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# CODECAPI\_SUPPORTSEVENTS


## <span id="ddk_codecapi_supportsevents_ks"></span><span id="DDK_CODECAPI_SUPPORTSEVENTS_KS"></span>


The CODECAPI\_SUPPORTSEVENTS property is used to indicate whether the minidriver supports user-mode events. That is, the minidriver implements the [CODECAPI\_CHANGELISTS](codecapi-changelists.md) event.

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
<th>Get</th>
<th>Set</th>
<th>Target</th>
<th>Property descriptor type</th>
<th>Property value type</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>Yes</p></td>
<td><p>Yes</p></td>
<td><p>Filter</p></td>
<td><p>KSPROPERTY</p></td>
<td><p>BOOL</p></td>
</tr>
</tbody>
</table>

 

The property value (operation data) is of type BOOL, which specifies whether the minidriver supports user-mode events. A value of **TRUE** indicates the minidriver provides support. The minidriver should not support this GUID if it does not support the event mechanism.

### Requirements

**Headers:** Declared in *ksmedia.h*. Include *ksmedia.h*.

### See Also

[**KSPROPERTY**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ks/ns-ks-ksidentifier)

 

 





