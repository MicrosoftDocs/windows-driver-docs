---
title: CODECAPI\_CURRENTCHANGELIST
description: CODECAPI\_CURRENTCHANGELIST
ms.assetid: f783857f-d1a1-417f-8f69-198b6f328a69
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# CODECAPI\_CURRENTCHANGELIST


## <span id="ddk_codecapi_currentchangelist_ks"></span><span id="DDK_CODECAPI_CURRENTCHANGELIST_KS"></span>


The CODECAPI\_CURRENTCHANGELIST property is used to indicate which parameters changed in a previous property "set" call, such as [CODECAPI\_ALLSETTINGS](codecapi-allsettings.md) and [CODECAPI\_SETALLDEFAULTS](codecapi-setalldefaults.md).

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
<td><p>Array of GUIDs</p></td>
</tr>
</tbody>
</table>

 

The property value (operation data) is an array of GUIDs.

### Comments

On a property get call:

If an application makes a property get call with a nonzero buffer size, the minidriver returns STATUS\_BUFFER\_TOO\_SMALL if the supplied buffer is too small for the data block. If there are no items to return, the minidrivers returns STATUS\_SUCCESS. Otherwise a list of GUIDs is returned (that is, where the sizeof(GUID) bytes equals 16 bytes). The returned size is the length of the list in bytes (that is, the number of GUIDS \* sizeof(GUID)).

On a property set call:

The current list of changed GUIDs is reset.

### Requirements

**Headers:** Declared in *ksmedia.h*. Include *ksmedia.h*.

### See Also

[**KSPROPERTY**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ks/ns-ks-ksidentifier), [CODECAPI\_ALLSETTINGS](codecapi-allsettings.md), [CODECAPI\_SETALLDEFAULTS](codecapi-setalldefaults.md)

 

 





