---
title: WIA\_IPS\_COLOR\_DROP\_RED
description: The WIA\_IPS\_COLOR\_DROP\_RED property is used to configure the amount of color drop-out for the Red color channel (R in RGB), as a percentage in a range from 0 (no dropout) to 100 (full channel dropout).
ms.assetid: B241154C-0F4F-4800-A8CD-30831F1AB25B
keywords: ["WIA_IPS_COLOR_DROP_RED Imaging Devices"]
topic_type:
- apiref
api_name:
- WIA_IPS_COLOR_DROP_RED
api_location:
- Wiadef.h
api_type:
- HeaderDef
ms.date: 05/22/2018
ms.localizationpriority: medium
---

# WIA\_IPS\_COLOR\_DROP\_RED


The **WIA\_IPS\_COLOR\_DROP\_RED** property is used to configure the amount of color drop-out for the Red color channel (R in RGB), as a percentage in a range from 0% (no dropout) to 100% (full channel dropout). The WIA minidriver creates and maintains this property.



Property Type: VT\_I4 | VT\_VECTOR

Valid Values: WIA\_PROP\_NONE

Access Rights: Read/Write

Remarks
-------

When the [**WIA\_IPS\_COLOR\_DROP**](wia-ips-color-drop.md) property is supported, this property is valid for all programmable image data source items, including Flatbed (WIA\_CATEGORY\_FLATBED) and Feeder (WIA\_CATEGORY\_FEEDER) and is required. Valid values for this property are between 0 and 100, inclusive.

Requirements
------------

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Header</p></td>
<td>Wiadef.h (include Wiadef.h)</td>
</tr>
</tbody>
</table>

 

 





