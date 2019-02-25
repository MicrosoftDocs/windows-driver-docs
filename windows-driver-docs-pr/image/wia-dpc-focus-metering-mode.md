---
title: WIA\_DPC\_FOCUS\_METERING\_MODE
description: The WIA\_DPC\_FOCUS\_METERING\_MODE property specifies the mode that a camera uses to automatically adjust the focus.
ms.assetid: a6a45f46-504b-4dad-a292-496f1ea4d8a0
keywords: ["WIA_DPC_FOCUS_METERING_MODE Imaging Devices"]
topic_type:
- apiref
api_name:
- WIA_DPC_FOCUS_METERING_MODE
api_location:
- Wiadef.h
api_type:
- HeaderDef
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# WIA\_DPC\_FOCUS\_METERING\_MODE


The WIA\_DPC\_FOCUS\_METERING\_MODE property specifies the mode that a camera uses to automatically adjust the focus.

## <span id="ddk_wia_dpc_focus_metering_mode_si"></span><span id="DDK_WIA_DPC_FOCUS_METERING_MODE_SI"></span>


Property Type: VT\_I4

Valid Values: WIA\_PROP\_LIST

Access Rights: Read/write

Remarks
-------

The following table describes the constants that are valid with the WIA\_DPC\_FOCUS\_METERING\_MODE property.

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
<td><p>FOCUSMETERING_CENTERSPOT</p></td>
<td><p>Adjust the focus based on a center spot.</p></td>
</tr>
<tr class="even">
<td><p>FOCUSMETERING_MULTISPOT</p></td>
<td><p>Adjust the focus based on a multispot pattern.</p></td>
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

 

 





