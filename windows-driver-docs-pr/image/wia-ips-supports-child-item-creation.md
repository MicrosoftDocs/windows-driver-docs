---
title: WIA\_IPS\_SUPPORTS\_CHILD\_ITEM\_CREATION
description: The WIA\_IPS\_SUPPORTS\_CHILD\_ITEM\_CREATION property indicates if a device supports the creation of child items.
ms.assetid: 77358889-d2c4-410f-b553-2dae2f7b27e3
keywords: ["WIA_IPS_SUPPORTS_CHILD_ITEM_CREATION Imaging Devices"]
topic_type:
- apiref
api_name:
- WIA_IPS_SUPPORTS_CHILD_ITEM_CREATION
api_location:
- Wiadef.h
api_type:
- HeaderDef
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# WIA\_IPS\_SUPPORTS\_CHILD\_ITEM\_CREATION


The WIA\_IPS\_SUPPORTS\_CHILD\_ITEM\_CREATION property indicates if a device supports the creation of child items. The WIA minidriver creates and maintains this property

Property Type: VT\_I4

Valid Values: WIA\_PROP\_NONE

Access Rights: Read-only

Remarks
-------

Items that support the [**WIA\_IPS\_SEGMENTATION**](wia-ips-segmentation.md) property and the WIA\_USE\_SEGMENTATION\_FILTER value must also support the WIA\_IPS\_SUPPORTS\_CHILD\_ITEM\_CREATION property and have it set to **TRUE**.

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
<td><p>Available in Windows Vista and later operating systems.</p></td>
</tr>
<tr class="even">
<td><p>Header</p></td>
<td>Wiadef.h (include Wiadef.h)</td>
</tr>
</tbody>
</table>

## See also


[**WIA\_IPS\_SEGMENTATION**](wia-ips-segmentation.md)

 

 






