---
title: CODECAPI\_SETALLDEFAULTS
description: CODECAPI\_SETALLDEFAULTS
ms.assetid: 6a50a75f-cbc5-487f-b2cd-34e89eb127a0
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# CODECAPI\_SETALLDEFAULTS


## <span id="ddk_codecapi_setalldefaults_ks"></span><span id="DDK_CODECAPI_SETALLDEFAULTS_KS"></span>


The CODECAPI\_SETALLDEFAULTS property is used to reset all the internal settings of the minidriver to their default configurations.

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
<td><p>No</p></td>
<td><p>Yes</p></td>
<td><p>Filter</p></td>
<td><p>KSPROPERTY</p></td>
<td><p>n/a</p></td>
</tr>
</tbody>
</table>

 

A set to this property set is a trigger that the device should reset all of its settings to their defaults.

### <span id="comments"></span><span id="COMMENTS"></span>Comments

The minidriver should cache its entire list of changed parameters for [CODECAPI\_CURRENTCHANGELIST](codecapi-currentchangelist.md) when this property is set.

### <span id="requirements"></span><span id="REQUIREMENTS"></span>Requirements

**Headers:** Declared in *ksmedia.h*. Include *ksmedia.h*.

### <span id="see_also"></span><span id="SEE_ALSO"></span>See Also

[**KSPROPERTY**](https://msdn.microsoft.com/library/windows/hardware/ff564262)

 

 





