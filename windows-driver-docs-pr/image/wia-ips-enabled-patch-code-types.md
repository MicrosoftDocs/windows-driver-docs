---
title: WIA\_IPS\_ENABLED\_PATCH\_CODE\_TYPES
description: The WIA\_IPS\_ENABLED\_PATCH\_CODE\_TYPES property is used to select the enabled patch codes for which the Patch Code Reader will search in the current session.
ms.assetid: 278C93EF-661E-41B2-8882-DF05A2FB9723
keywords: ["WIA_IPS_ENABLED_PATCH_CODE_TYPES Imaging Devices"]
topic_type:
- apiref
api_name:
- WIA_IPS_ENABLED_PATCH_CODE_TYPES
api_location:
- Wiadef.h
api_type:
- HeaderDef
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# WIA\_IPS\_ENABLED\_PATCH\_CODE\_TYPES


The **WIA\_IPS\_ENABLED\_PATCH\_CODE\_TYPES** property is used to select the enabled patch codes for which the Patch Code Reader will search in the current session. These patch codes can be some or all the values that the WIA minidriver reports for [**WIA\_IPS\_SUPPORTED\_PATCH\_CODE\_TYPES**](wia-ips-supported-patch-code-types.md). The order of the values in the array specifies the priority order in which the respective patch codes are to be searched.




Property Type: VT\_I4 | VT\_VECTOR

Valid Values: WIA\_PROP\_NONE (single 'array'/vector value)

Access Rights: Read/Write

Remarks
-------

The valid values for the **WIA\_IPS\_ENABLED\_PATCH\_CODE\_TYPES** property are the same WIA\_PATCH\_CODE\_ values that are defined for the [**WIA\_IPS\_SUPPORTED\_PATCH\_CODE\_TYPES**](wia-ips-supported-patch-code-types.md) property.

This property is required for all Patch Code Reader items.

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

 

 





