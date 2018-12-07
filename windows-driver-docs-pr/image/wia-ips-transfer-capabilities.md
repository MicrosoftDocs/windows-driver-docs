---
title: WIA\_IPS\_TRANSFER\_CAPABILITIES
description: The WIA\_IPS\_TRANSFER\_CAPABILITIES property indicates if a device can transfer parent and child items together. The WIA minidriver creates and maintains this property.
ms.assetid: 937e3e54-6ad3-46bb-bd00-e0812c64e539
keywords: ["WIA_IPS_TRANSFER_CAPABILITIES Imaging Devices"]
topic_type:
- apiref
api_name:
- WIA_IPS_TRANSFER_CAPABILITIES
api_location:
- Wiadef.h
api_type:
- HeaderDef
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# WIA\_IPS\_TRANSFER\_CAPABILITIES


The WIA\_IPS\_TRANSFER\_CAPABILITIES property indicates if a device can transfer parent and child items together. The WIA minidriver creates and maintains this property.

Property Type: VT\_I4

Valid Values: WIA\_PROP\_NONE

Access Rights: Read-only

Remarks
-------

The following table describes the constant that is valid with the WIA\_IPS\_TRANSFER\_CAPABILITIES property

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Flag</th>
<th>Definition</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>WIA_TRANSFER_CHILDREN_SINGLE_SCAN</p></td>
<td><p>The device can transfer the parent and child items together or the device must make a separate scan for each item and each child item.</p></td>
</tr>
</tbody>
</table>

 

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

 

 





