---
title: WIA\_DPS\_HORIZONTAL\_SHEET\_FEED\_SIZE
description: The WIA\_DPS\_HORIZONTAL\_SHEET\_FEED\_SIZE property contains the physical horizontal dimensions of scanner's document feeder, in thousandths of an inch (.001). The WIA minidriver creates and maintains this property.
ms.assetid: e5c43028-5f2f-4e06-8f74-acd7cbb84755
keywords: ["WIA_DPS_HORIZONTAL_SHEET_FEED_SIZE Imaging Devices"]
topic_type:
- apiref
api_name:
- WIA_DPS_HORIZONTAL_SHEET_FEED_SIZE
api_location:
- Wiadef.h
api_type:
- HeaderDef
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# WIA\_DPS\_HORIZONTAL\_SHEET\_FEED\_SIZE


The WIA\_DPS\_HORIZONTAL\_SHEET\_FEED\_SIZE property contains the physical horizontal dimensions of scanner's document feeder, in thousandths of an inch (.001). The WIA minidriver creates and maintains this property.

## <span id="ddk_wia_dps_horizontal_sheet_feed_size_si"></span><span id="DDK_WIA_DPS_HORIZONTAL_SHEET_FEED_SIZE_SI"></span>


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
<td><p>Beginning with Windows Vista, the WIA_DPS_HORIZONTAL_SHEET_FEED_SIZE property is still available at the root level of the WIA driver, but it has been replaced by the WIA_IPS_MAX_HORIZONTAL_SIZE property, so you should consider it optional.</p></td>
</tr>
<tr class="even">
<td><p>Header</p></td>
<td>Wiadef.h (include Wiadef.h)</td>
</tr>
</tbody>
</table>

## See also


[**WIA\_DPS\_VERTICAL\_SHEET\_FEED\_SIZE**](wia-dps-vertical-sheet-feed-size.md)

[**WIA\_IPS\_MAX\_HORIZONTAL\_SIZE**](wia-ips-max-horizontal-size.md)

 

 






