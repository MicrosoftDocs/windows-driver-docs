---
title: WIA\_DPS\_VERTICAL\_BED\_SIZE
description: The WIA\_DPS\_VERTICAL\_BED\_SIZE property contains the physical vertical dimensions of a scanner's flatbed, in thousandths of an inch (.001). The WIA minidriver creates and maintains this property.
ms.assetid: c4e02364-4785-45f4-8e43-056582bb6d1a
keywords: ["WIA_DPS_VERTICAL_BED_SIZE Imaging Devices"]
topic_type:
- apiref
api_name:
- WIA_DPS_VERTICAL_BED_SIZE
api_location:
- Wiadef.h
api_type:
- HeaderDef
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# WIA\_DPS\_VERTICAL\_BED\_SIZE


The WIA\_DPS\_VERTICAL\_BED\_SIZE property contains the physical vertical dimensions of a scanner's flatbed, in thousandths of an inch (.001). The WIA minidriver creates and maintains this property.

## <span id="ddk_wia_dps_vertical_bed_size_si"></span><span id="DDK_WIA_DPS_VERTICAL_BED_SIZE_SI"></span>


Property Type: VT\_I4

Valid Values: WIA\_PROP\_NONE

Access Rights: Read-only

Requirements
------------

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Version</p></td>
<td><p>Beginning with Windows Vista, the WIA_DPS_VERTICAL_BED_SIZE property is still available at the root level of the WIA driver. But this property has been replaced with the WIA_IPS_MAX_VERTICAL_SIZE property, and you should consider it to be optional.</p></td>
</tr>
<tr class="even">
<td><p>Header</p></td>
<td>Wiadef.h (include Wiadef.h)</td>
</tr>
</tbody>
</table>

## See also


[**WIA\_DPS\_HORIZONTAL\_BED\_SIZE**](wia-dps-horizontal-bed-size.md)

[**WIA\_IPS\_MAX\_VERTICAL\_SIZE**](wia-ips-max-vertical-size.md)

 

 






