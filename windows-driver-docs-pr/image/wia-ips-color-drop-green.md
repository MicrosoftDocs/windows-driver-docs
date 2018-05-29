---
title: WIA\_IPS\_COLOR\_DROP\_GREEN
description: The WIA\_IPS\_COLOR\_DROP\_GREEN property is used to configure the amount of color drop-out for the Green color channel (G in RGB), as a percentage in a range from 0 (no dropout) to 100 (full channel dropout).
ms.assetid: 601BB830-034C-4A60-9F21-A1EBC45FDA8F
keywords: ["WIA_IPS_COLOR_DROP_GREEN Imaging Devices"]
topic_type:
- apiref
api_name:
- WIA_IPS_COLOR_DROP_GREEN
api_location:
- Wiadef.h
api_type:
- HeaderDef
ms.author: windowsdriverdev
ms.date: 05/22/2018
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# WIA\_IPS\_COLOR\_DROP\_GREEN


The **WIA\_IPS\_COLOR\_DROP\_GREEN** property is used to configure the amount of color drop-out for the Green color channel (G in RGB), as a percentage in a range from 0% (no dropout) to 100% (full channel dropout). The WIA minidriver creates and maintains this property.



Property Type: VT\_I4 | VT\_VECTOR & WIA\_PROP\_NONE

Valid Values: WIA\_PROP\_RANGE

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

 

 





