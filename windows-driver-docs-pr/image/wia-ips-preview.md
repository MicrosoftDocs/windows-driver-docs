---
title: WIA\_IPS\_PREVIEW
description: The WIA\_IPS\_PREVIEW property indicates the preview mode for a device.
ms.assetid: 06caadc7-2a65-4c54-8d63-4aa1c17186de
keywords: ["WIA_IPS_PREVIEW Imaging Devices"]
topic_type:
- apiref
api_name:
- WIA_IPS_PREVIEW
api_location:
- Wiadef.h
api_type:
- HeaderDef
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# WIA\_IPS\_PREVIEW


The WIA\_IPS\_PREVIEW property indicates the preview mode for a device.

Property Type: VT\_I4

Valid Values: WIA\_PROP\_LIST

Access Rights: Read/write

Remarks
-------

An application sets WIA\_IPS\_PREVIEW to place a device into a preview mode.

The following table describes the constants that are valid with WIA\_IPS\_PREVIEW.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Value</th>
<th>Definition</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>WIA_FINAL_SCAN</p></td>
<td><p>The application will perform a final scan.</p></td>
</tr>
<tr class="even">
<td><p>WIA_PREVIEW_SCAN</p></td>
<td><p>The application will perform a preview scan.</p></td>
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
<td><p>Available in Windows Vista and later operating systems. For Windows XP, use the WIA_DPS_PREVIEW property instead.</p></td>
</tr>
<tr class="even">
<td><p>Header</p></td>
<td>Wiadef.h (include Wiadef.h)</td>
</tr>
</tbody>
</table>

## See also


[**WIA\_DPS\_PREVIEW**](wia-dps-preview.md)

 

 






