---
title: WIA\_DPC\_EFFECT\_MODE
description: The WIA\_DPC\_EFFECT\_MODE property specifies the special image acquisition mode of a camera.
ms.assetid: a874858d-4400-425f-8423-b41bbeb1a925
keywords: ["WIA_DPC_EFFECT_MODE Imaging Devices"]
topic_type:
- apiref
api_name:
- WIA_DPC_EFFECT_MODE
api_location:
- Wiadef.h
api_type:
- HeaderDef
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# WIA\_DPC\_EFFECT\_MODE


The WIA\_DPC\_EFFECT\_MODE property specifies the special image acquisition mode of a camera.

## <span id="ddk_wia_dpc_effect_mode_si"></span><span id="DDK_WIA_DPC_EFFECT_MODE_SI"></span>


Property Type: VT\_I4

Valid Values: WIA\_PROP\_LIST

Access Rights: Read/write

Remarks
-------

The following table describes the constants that are valid with the WIA\_DPC\_EFFECT\_MODE property.

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
<td><p>EFECTMODE_BW</p></td>
<td><p>Capture a grayscale image</p></td>
</tr>
<tr class="even">
<td><p>EFFECTMODE_SEPIA</p></td>
<td><p>Capture a sepia image</p></td>
</tr>
<tr class="odd">
<td><p>EFFECTMODE_STANDARD</p></td>
<td><p>Capture an image in the standard mode for the camera</p></td>
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

 

 





