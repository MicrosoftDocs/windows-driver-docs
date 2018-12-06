---
title: WIA\_DPC\_FOCUS\_MODE
description: The WIA\_DPC\_FOCUS\_MODE property defines the current focus mode setting for a camera device.
ms.assetid: d651c9f7-97ca-4fa5-bc52-2af1f7c2e241
keywords: ["WIA_DPC_FOCUS_MODE Imaging Devices"]
topic_type:
- apiref
api_name:
- WIA_DPC_FOCUS_MODE
api_location:
- Wiadef.h
api_type:
- HeaderDef
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# WIA\_DPC\_FOCUS\_MODE


The WIA\_DPC\_FOCUS\_MODE property defines the current focus mode setting for a camera device.

## <span id="ddk_wia_dpc_focus_mode_si"></span><span id="DDK_WIA_DPC_FOCUS_MODE_SI"></span>


Property Type: VT\_I4

Valid Values: WIA\_PROP\_LIST

Access Rights: Read/write

Remarks
-------

A device driver enumerates the supported values of the WIA\_DPC\_FOCUS\_MODE property, and an application writes this property to set the focus mode for the camera device.

The following table describes the constants that are valid with the WIA\_DPC\_FOCUS\_MODE property.

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
<td><p>FOCUSMODE_AUTO</p></td>
<td><p>The camera device is configured to focus automatically.</p></td>
</tr>
<tr class="even">
<td><p>FOCUSMODE_MACROAUTO</p></td>
<td><p>The camera device is configured to focus automatically by using short-range macro settings.</p></td>
</tr>
<tr class="odd">
<td><p>FOCUSMODE_MANUAL</p></td>
<td><p>The camera device is configured to allow a user to focus manually.</p></td>
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

 

 





