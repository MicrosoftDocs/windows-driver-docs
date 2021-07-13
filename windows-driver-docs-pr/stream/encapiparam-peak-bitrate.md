---
title: ENCAPIPARAM\_PEAK\_BITRATE
description: ENCAPIPARAM\_PEAK\_BITRATE
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# ENCAPIPARAM\_PEAK\_BITRATE


## <span id="ddk_encapiparam_peak_bitrate_ks"></span><span id="DDK_ENCAPIPARAM_PEAK_BITRATE_KS"></span>


The ENCAPIPARAM\_BITRATE property is used to describe the supported peak bit rate (bits per second) range of the device.

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
<td><p>ULONG</p></td>
</tr>
</tbody>
</table>

 

The property value (operation data) is a VT\_UI4 stepped range of peak bit rates of the device, specified in the **PropertyItem.Values** member of [**KSPROPERTY\_SET**](/windows-hardware/drivers/ddi/ks/ns-ks-ksproperty_set) structure.

### Comments

The minidriver is required to either provide a static **PropertyItem.Values** description in the property item or handle a basic support query and fill the values in. The minidriver must also specify the defaults for this property.

### Requirements

**Headers:** Declared in *ksmedia.h*. Include *ksmedia.h*.

### See Also

[**KSPROPERTY**](ksproperty-structure.md), [**VIDEOENCODER\_BITRATE\_MODE**](/windows-hardware/drivers/ddi/ksmedia/ne-ksmedia-videoencoder_bitrate_mode)

 

