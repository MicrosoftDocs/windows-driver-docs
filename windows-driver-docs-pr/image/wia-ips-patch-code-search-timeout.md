---
title: WIA\_IPS\_PATCH\_CODE\_SEARCH\_TIMEOUT
description: The WIA\_IPS\_PATCH\_CODE\_SEARCH\_TIMEOUT property describes the maximum time to search for patch codes on a document page.
ms.assetid: D7DD05B2-43CA-484F-8207-4ED9C307D3AA
keywords: ["WIA_IPS_PATCH_CODE_SEARCH_TIMEOUT Imaging Devices"]
topic_type:
- apiref
api_name:
- WIA_IPS_PATCH_CODE_SEARCH_TIMEOUT
api_location:
- Wiadef.h
api_type:
- HeaderDef
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# WIA\_IPS\_PATCH\_CODE\_SEARCH\_TIMEOUT


The **WIA\_IPS\_PATCH\_CODE\_SEARCH\_TIMEOUT** property describes the maximum time to search for patch codes on a document page.




Property Type: VT\_I4

Valid Values: WIA\_PROP\_RANGE

Access Rights: Read/Write

Remarks
-------

The time unit is not specified (it can be milliseconds or tenths of a second for example) but the application can choose values in the minimum – maximum range reported by the WIA minidriver.

This property is required for all Patch Code Reader items. The property can be implemented to support a range containing one single value (meaning the application cannot change this timeout)

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

 

 





