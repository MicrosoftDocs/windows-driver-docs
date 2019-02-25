---
title: WIA\_IPS\_SHOW\_PREVIEW\_CONTROL
description: The WIA\_IPS\_SHOW\_PREVIEW\_CONTROL property indicates whether an item needs a preview control displayed to a user. The WIA minidriver creates and maintains this property.
ms.assetid: 50559dc2-8e5b-4dbc-9c39-8c51e0f825dc
keywords: ["WIA_IPS_SHOW_PREVIEW_CONTROL Imaging Devices"]
topic_type:
- apiref
api_name:
- WIA_IPS_SHOW_PREVIEW_CONTROL
api_location:
- Wiadef.h
api_type:
- HeaderDef
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# WIA\_IPS\_SHOW\_PREVIEW\_CONTROL


The WIA\_IPS\_SHOW\_PREVIEW\_CONTROL property indicates whether an item needs a preview control displayed to a user. The WIA minidriver creates and maintains this property.

Property Type: VT\_I4

Valid Values: WIA\_PROP\_NONE

Access Rights: Read-only

Remarks
-------

The following table describes the constants that are valid with WIA\_IPS\_SHOW\_PREVIEW\_CONTROL.

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
<td><p>WIA_DONT_SHOW_PREVIEW_CONTROL</p></td>
<td><p>Do not show a preview control to the user, because this device cannot perform a preview.</p></td>
</tr>
<tr class="even">
<td><p>WIA_SHOW_PREVIEW_CONTROL</p></td>
<td><p>Show a preview control to the user, because this device can perform a preview.</p></td>
</tr>
</tbody>
</table>

 

You can use the WIA\_IPS\_SHOW\_PREVIEW\_CONTROL property to help control devices that cannot preview. For example, some feeder-driven devices cannot reload the paper for a preview scan.

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
<td><p>Available in Windows Vista and later operating systems. For Windows XP, use the WIA_DPS_SHOW_PREVIEW_CONTROL property instead.</p></td>
</tr>
<tr class="even">
<td><p>Header</p></td>
<td>Wiadef.h (include Wiadef.h)</td>
</tr>
</tbody>
</table>

## See also


[**WIA\_DPS\_SHOW\_PREVIEW\_CONTROL**](wia-dps-show-preview-control.md)

 

 






