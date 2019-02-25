---
title: CODECAPI\_ALLSETTINGS
description: CODECAPI\_ALLSETTINGS
ms.assetid: 0ae11200-af21-476a-89a8-515bd98920a0
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# CODECAPI\_ALLSETTINGS


## <span id="ddk_codecapi_allsettings_ks"></span><span id="DDK_CODECAPI_ALLSETTINGS_KS"></span>


The CODECAPI\_ALLSETTINGS property is used to pass back and forth a minidriver-generated block of data.

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
<td><p>PVOID</p></td>
</tr>
</tbody>
</table>

 

The property value (operation data) is of type PVOID, which is a pointer to a user-mode buffer for the minidriver-generated block of data.

### Comments

On a property get call:

If an application makes a property get call with a zero length buffer, the minidriver must return STATUS\_BUFFER\_OVERFLOW and specify the required buffer size in the **Irp-&gt;IoStatus.Information** field. If the length buffer is nonzero, the minidriver must return STATUS\_BUFFER\_TOO\_SMALL if the supplied buffer is too small for the data block, otherwise the minidriver packs its settings into a data block that can be restored later.

It is the minidriver's responsibility to add data integrity checks to the data, such as a unique GUID to indicate the minidriver generated the data, a cyclic redundancy check (CRC), and a header length.

The data returned should be lightweight and contain only information required to reconstruct the current settings.

Applications will use this property for multilevel undos, stored with their projects, etc.

On a property set call:

The minidriver must verify the data's integrity and check that the data block size is under the maximum data size (for example, reject anything over a certain size). It must also verify the CRC and the header length. The minidriver must also cache any changes to be propagated for [CODECAPI\_CURRENTCHANGELIST](codecapi-currentchangelist.md).

### Requirements

**Headers:** Declared in *ksmedia.h*. Include *ksmedia.h*.

### See Also

[**KSPROPERTY**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ks/ns-ks-ksidentifier), [CODECAPI\_CURRENTCHANGELIST](codecapi-currentchangelist.md)

 

 





