---
title: WIA\_IPS\_BARCODE\_SEARCH\_TIMEOUT
description: The WIA\_IPS\_BARCODE\_SEARCH\_TIMEOUT property describes the maximum time to search for barcodes on a document page.
keywords: ["WIA_IPS_BARCODE_SEARCH_TIMEOUT Imaging Devices"]
topic_type:
- apiref
api_name:
- WIA_IPS_BARCODE_SEARCH_TIMEOUT
api_location:
- Wiadef.h
api_type:
- HeaderDef
ms.date: 05/22/2018
ms.localizationpriority: medium
---

# WIA\_IPS\_BARCODE\_SEARCH\_TIMEOUT


The **WIA\_IPS\_BARCODE\_SEARCH\_TIMEOUT** property describes the maximum time to search for barcodes on a document page.


Property Type: VT\_UI4

Valid Values: WIA\_PROP\_RANGE

Access Rights: Read/Write

## Remarks

The time unit is not specified (it can be milliseconds or tenths of a second, for example) but the application can choose values in the minimum – maximum range reported by the WIA minidriver.

This property is required for all Barcode Reader items. The property can be implemented to support a range that contain one single value (meaning that the application cannot change this timeout).

## Requirements

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

 

 





