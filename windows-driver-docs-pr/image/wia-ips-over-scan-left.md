---
title: WIA\_IPS\_OVER\_SCAN\_LEFT
description: The WIA\_IPS\_OVER\_SCAN\_LEFT property along with WIA\_IPS\_OVER\_SCAN\_RIGHT, WIA\_IPS\_OVER\_SCAN\_TOP, and WIA\_IPS\_OVER\_SCAN\_BOTTOM are used to configure the amount of over scanning, in thousandths of an inch (0.001 \ 0034;) units, relative to the physical document.
ms.assetid: D1C2ADF5-A38C-4E30-A377-E62C5B4208A6
keywords: ["WIA_IPS_OVER_SCAN_LEFT Imaging Devices"]
topic_type:
- apiref
api_name:
- WIA_IPS_OVER_SCAN_LEFT
api_location:
- Wiadef.h
api_type:
- HeaderDef
ms.date: 05/22/2018
ms.localizationpriority: medium
---

# WIA\_IPS\_OVER\_SCAN\_LEFT


The **WIA\_IPS\_OVER\_SCAN\_LEFT** property along with [**WIA\_IPS\_OVER\_SCAN\_RIGHT**](wia-ips-over-scan-right.md), [**WIA\_IPS\_OVER\_SCAN\_TOP**](wia-ips-over-scan-top.md), and [**WIA\_IPS\_OVER\_SCAN\_BOTTOM**](wia-ips-over-scan-bottom.md) are used to configure the amount of over scanning, in thousandths of an inch (0.001") units, relative to the physical document. The WIA minidriver creates and maintains this property.




Property Type: VT\_UI4

Valid Values: WIA\_PROP\_RANGE

Access Rights: Read/Write

Remarks
-------

This property is valid for all programmable image data source items, including Flatbed (WIA\_CATEGORY\_FLATBED) and Feeder (WIA\_CATEGORY\_FEEDER) but only when the [**WIA\_IPS\_OVER\_SCAN**](wia-ips-over-scan.md) property is supported. When it is supported, this property is required.

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

 

 





