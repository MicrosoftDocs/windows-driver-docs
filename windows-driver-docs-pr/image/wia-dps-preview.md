---
title: WIA\_DPS\_PREVIEW
description: The WIA\_DPS\_PREVIEW property indicates the preview mode for a device. An application sets this property to place the device into a preview mode.
ms.assetid: 410f58c0-479c-44ab-8126-a5dec79b713b
keywords: ["WIA_DPS_PREVIEW Imaging Devices"]
topic_type:
- apiref
api_name:
- WIA_DPS_PREVIEW
api_location:
- Wiadef.h
api_type:
- HeaderDef
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# WIA\_DPS\_PREVIEW


The WIA\_DPS\_PREVIEW property indicates the preview mode for a device. An application sets this property to place the device into a preview mode.

## <span id="ddk_wia_dps_preview_si"></span><span id="DDK_WIA_DPS_PREVIEW_SI"></span>


Property Type: VT\_I4

Valid Values: WIA\_PROP\_LIST

Access Rights: Read/write

Remarks
-------

The following table describes the constants that are valid with the WIA\_DPS\_PREVIEW property.

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
<td><p>Available for Microsoft Windows XP. For Windows Vista and later, use the identical WIA_IPS_PREVIEW property.</p></td>
</tr>
<tr class="even">
<td><p>Header</p></td>
<td>Wiadef.h (include Wiadef.h)</td>
</tr>
</tbody>
</table>

## See also


[**WIA\_IPS\_PREVIEW**](wia-ips-preview.md)

 

 






