---
title: ENCAPIPARAM\_BITRATE\_MODE
description: ENCAPIPARAM\_BITRATE\_MODE
ms.assetid: d7e82483-bee3-44bd-9066-c2877130a1f9
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
ms.localizationpriority: medium
---

# ENCAPIPARAM\_BITRATE\_MODE


## <span id="ddk_encapiparam_bitrate_mode_ks"></span><span id="DDK_ENCAPIPARAM_BITRATE_MODE_KS"></span>


The ENCAPIPARAM\_BITRATE property is used to describe the encoding mode of the device.

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
<td><p>LONG</p></td>
</tr>
</tbody>
</table>

 

The property value (operation data) is a VT\_I4 value specified in the **PropertyItem.Values** member of the [**KSPROPERTY\_SET**](https://msdn.microsoft.com/library/windows/hardware/ff565617) structure with a discrete list of supported values out of the [**VIDEOENCODER\_BITRATE\_MODE**](https://msdn.microsoft.com/library/windows/hardware/ff568695) enumeration.

### <span id="comments"></span><span id="COMMENTS"></span>Comments

For a sample of how to use this property, see [Encoder Code Examples](https://msdn.microsoft.com/library/windows/hardware/ff559532).

The minidriver is required to either provide a static **PropertyItem.Values** description in the property item or handle a basic support query and fill the values in. The minidriver must also specify the defaults for this property.

### <span id="requirements"></span><span id="REQUIREMENTS"></span>Requirements

**Headers:** Declared in *ksmedia.h*. Include *ksmedia.h*.

### <span id="see_also"></span><span id="SEE_ALSO"></span>See Also

[**KSPROPERTY**](https://msdn.microsoft.com/library/windows/hardware/ff564262), [**VIDEOENCODER\_BITRATE\_MODE**](https://msdn.microsoft.com/library/windows/hardware/ff568695)

 

 





