---
title: WIA\_IPS\_OVER\_SCAN\_TOP
description: The WIA\_IPS\_OVER\_SCAN\_TOP property along with WIA\_IPS\_OVER\_SCAN\_BOTTOM, WIA\_IPS\_OVER\_SCAN\_LEFT, and WIA\_IPS\_OVER\_SCAN\_RIGHT are used to configure the amount of over scanning, in thousandths of an inch (0.001 \ 0034;) units, relative to the physical document.
ms.assetid: 7957BBB4-C4E6-4704-A64D-F2F318ABDF61
keywords: ["WIA_IPS_OVER_SCAN_TOP Imaging Devices"]
topic_type:
- apiref
api_name:
- WIA_IPS_OVER_SCAN_TOP
api_location:
- Wiadef.h
api_type:
- HeaderDef
ms.date: 05/22/2018
ms.localizationpriority: medium
---

# WIA\_IPS\_OVER\_SCAN\_TOP


The **WIA\_IPS\_OVER\_SCAN\_TOP** property along with [**WIA\_IPS\_OVER\_SCAN\_BOTTOM**](wia-ips-over-scan-bottom.md), [**WIA\_IPS\_OVER\_SCAN\_LEFT**](wia-ips-over-scan-left.md), and [**WIA\_IPS\_OVER\_SCAN\_RIGHT**](wia-ips-over-scan-right.md) are used to configure the amount of over scanning, in thousandths of an inch (0.001") units, relative to the physical document. The WIA minidriver creates and maintains this property.




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

 

 





