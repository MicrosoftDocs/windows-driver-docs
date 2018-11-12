---
title: WIA\_DPC\_FOCUS\_DISTANCE
description: The WIA\_DPC\_FOCUS\_DISTANCE property contains the distance, in millimeters, between the image-capturing plane of a digital camera and the point of focus.
ms.assetid: 0f12fbdf-2c40-4b8b-9a22-ee35aa8cbc3f
keywords: ["WIA_DPC_FOCUS_DISTANCE Imaging Devices"]
topic_type:
- apiref
api_name:
- WIA_DPC_FOCUS_DISTANCE
api_location:
- Wiadef.h
api_type:
- HeaderDef
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# WIA\_DPC\_FOCUS\_DISTANCE


The WIA\_DPC\_FOCUS\_DISTANCE property contains the distance, in millimeters, between the image-capturing plane of a digital camera and the point of focus.

## <span id="ddk_wia_dpc_focus_distance_si"></span><span id="DDK_WIA_DPC_FOCUS_DISTANCE_SI"></span>


Property Type: VT\_I4

Valid Values: WIA\_PROP\_RANGE or WIA\_PROP\_LIST

Access Rights: Read/write

Remarks
-------

A value of 0xFFFF for the WIA\_DPC\_FOCUS\_DISTANCE property corresponds to a setting that is greater than 655 meters.

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

 

 





