---
title: WIA\_IPS\_MAXIMUM\_PATCH\_CODE\_SEARCH\_RETRIES
description: The WIA\_IPS\_MAXIMUM\_PATCH\_CODE\_SEARCH\_RETRIES property describes the maximum number of retries the reader attempts if no patch code can be found when patch code detection is enabled.
ms.assetid: F6CBEC7E-B44D-4524-9F75-8CBF413FCAF6
keywords: ["WIA_IPS_MAXIMUM_PATCH_CODE_SEARCH_RETRIES Imaging Devices"]
topic_type:
- apiref
api_name:
- WIA_IPS_MAXIMUM_PATCH_CODE_SEARCH_RETRIES
api_location:
- Wiadef.h
api_type:
- HeaderDef
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# WIA\_IPS\_MAXIMUM\_PATCH\_CODE\_SEARCH\_RETRIES


The **WIA\_IPS\_MAXIMUM\_PATCH\_CODE\_SEARCH\_RETRIES** property describes the maximum number of retries the reader attempts if no patch code can be found when patch code detection is enabled.




Property Type: VT\_I4

Valid Values: WIA\_PROP\_RANGE

Access Rights: Read/Write

Remarks
-------

This property is required for all Patch Code Reader items. The property can be implemented to support a range containing one single value, including 0 (no retries).

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

 

 





