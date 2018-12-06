---
title: WIA\_IPS\_SCAN\_AHEAD\_CAPACITY
description: The WIA\_IPS\_SCAN\_AHEAD\_CAPACITY describes the maximum number of pages that the scanner can scan ahead (and store in the internal scanner memory buffer) at the current scan job settings (the current document size, scan resolution, data type, file format, compression, and so on). The WIA minidriver creates and maintains this property.
ms.assetid: 7A80964D-B0A4-4D6B-A320-4DE0A700E1A9
keywords: ["WIA_IPS_SCAN_AHEAD_CAPACITY Imaging Devices"]
topic_type:
- apiref
api_name:
- WIA_IPS_SCAN_AHEAD_CAPACITY
api_location:
- Wiadef.h
api_type:
- HeaderDef
ms.date: 05/22/2018
ms.localizationpriority: medium
---

# WIA\_IPS\_SCAN\_AHEAD\_CAPACITY


The **WIA\_IPS\_SCAN\_AHEAD\_CAPACITY** describes the maximum number of pages that the scanner can scan ahead (and store in the internal scanner memory buffer) at the current scan job settings (the current document size, scan resolution, data type, file format, compression, and so on). The WIA minidriver creates and maintains this property.




Property Type: VT\_UI4

Valid Values: WIA\_PROP\_NONE

Access Rights: Read/Write

Remarks
-------

When the [**WIA\_IPS\_SCAN\_AHEAD**](wia-ips-scan-ahead.md) property is supported, this property is valid only for the Feeder item (WIA\_CATEGORY\_FEEDER), and is optional.

A value of 0 means "undefined/unknown number of pages."

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

 

 





