---
title: ENCAPIPARAM\_BITRATE
description: ENCAPIPARAM\_BITRATE
ms.assetid: a0fba9b3-7ce3-407d-b53f-fd54a50cbdcb
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# ENCAPIPARAM\_BITRATE


## <span id="ddk_encapiparam_bitrate_ks"></span><span id="DDK_ENCAPIPARAM_BITRATE_KS"></span>


The ENCAPIPARAM\_BITRATE property is used to describe the bit rate (bits per second) supported by the device.

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

 

The property value (operation data) is a VT\_UI4 stepped range of the bit rates supported by the device, specified in the **PropertyItem.Values** member of [**KSPROPERTY\_SET**](https://msdn.microsoft.com/library/windows/hardware/ff565617) structure.

### Comments

For a sample of how to use this property, see [Encoder Code Examples](https://msdn.microsoft.com/library/windows/hardware/ff559532).

The minidriver is required to either provide a static **PropertyItem.Values** description in the property item or handle a basic support query and fill the values in. The minidriver must also specify the defaults for this property.

### Requirements

**Headers:** Declared in *ksmedia.h*. Include *ksmedia.h*.

### See Also

[**KSPROPERTY**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ks/ns-ks-ksidentifier), [**VIDEOENCODER\_BITRATE\_MODE**](https://msdn.microsoft.com/library/windows/hardware/ff568695)

 

 





