---
title: WIA\_DPS\_VERTICAL\_BED\_REGISTRATION
description: The WIA\_DPS\_VERTICAL\_BED\_REGISTRATION property contains the registration, or vertical alignment and edge detection, for documents that are placed on the flatbed of a scanner. The WIA minidriver creates and maintains this property.
ms.assetid: 58c1bfb2-1f61-4910-ac6d-189aa203c370
keywords: ["WIA_DPS_VERTICAL_BED_REGISTRATION Imaging Devices"]
topic_type:
- apiref
api_name:
- WIA_DPS_VERTICAL_BED_REGISTRATION
api_location:
- Wiadef.h
api_type:
- HeaderDef
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# WIA\_DPS\_VERTICAL\_BED\_REGISTRATION


The WIA\_DPS\_VERTICAL\_BED\_REGISTRATION property contains the registration, or vertical alignment and edge detection, for documents that are placed on the flatbed of a scanner. The WIA minidriver creates and maintains this property.

## <span id="ddk_wia_dps_vertical_bed_registration_si"></span><span id="DDK_WIA_DPS_VERTICAL_BED_REGISTRATION_SI"></span>


Property Type: VT\_I4

Valid Values: WIA\_PROP\_NONE

Access Rights: Read-only

Remarks
-------

The following table describes the constants that are valid with the WIA\_DPS\_VERTICAL\_BED\_REGISTRATION property.

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
<td><p>BOTTOM_JUSTIFIED</p></td>
<td><p>The paper is bottom-aligned.</p></td>
</tr>
<tr class="even">
<td><p>CENTERED</p></td>
<td><p>The paper is centered.</p></td>
</tr>
<tr class="odd">
<td><p>TOP_JUSTIFIED</p></td>
<td><p>The paper is top-aligned.</p></td>
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
<td><p>Obsolete in Windows Vista and later operating systems and should no longer be used. However, this property is still defined in Windows Vista for compatibility with applications and devices designed for Windows Server 2003, Windows XP, and previous versions of Windows.</p></td>
</tr>
<tr class="even">
<td><p>Header</p></td>
<td>Wiadef.h (include Wiadef.h)</td>
</tr>
</tbody>
</table>

## See also


[**WIA\_DPS\_HORIZONTAL\_BED\_REGISTRATION**](wia-dps-horizontal-bed-registration.md)

 

 






