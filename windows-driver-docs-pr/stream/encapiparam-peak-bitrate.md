---
title: ENCAPIPARAM\_PEAK\_BITRATE
description: ENCAPIPARAM\_PEAK\_BITRATE
ms.assetid: 444a20e0-f3af-4dbc-9272-44e992e059e8
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

 

The property value (operation data) is a VT\_UI4 stepped range of peak bit rates of the device, specified in the **PropertyItem.Values** member of [**KSPROPERTY\_SET**](https://msdn.microsoft.com/library/windows/hardware/ff565617) structure.

### Comments

The minidriver is required to either provide a static **PropertyItem.Values** description in the property item or handle a basic support query and fill the values in. The minidriver must also specify the defaults for this property.

### Requirements

**Headers:** Declared in *ksmedia.h*. Include *ksmedia.h*.

### See Also

[**KSPROPERTY**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ks/ns-ks-ksidentifier), [**VIDEOENCODER\_BITRATE\_MODE**](https://msdn.microsoft.com/library/windows/hardware/ff568695)

 

 





