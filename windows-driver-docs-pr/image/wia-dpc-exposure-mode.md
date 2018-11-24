---
title: WIA\_DPC\_EXPOSURE\_MODE
description: The WIA\_DPC\_EXPOSURE\_MODE property indicates a camera's current exposure mode.
ms.assetid: 30587d4f-5836-4030-9501-7612aaff58ae
keywords: ["WIA_DPC_EXPOSURE_MODE Imaging Devices"]
topic_type:
- apiref
api_name:
- WIA_DPC_EXPOSURE_MODE
api_location:
- Wiadef.h
api_type:
- HeaderDef
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# WIA\_DPC\_EXPOSURE\_MODE


The WIA\_DPC\_EXPOSURE\_MODE property indicates a camera's current exposure mode.

## <span id="ddk_wia_dpc_exposure_mode_si"></span><span id="DDK_WIA_DPC_EXPOSURE_MODE_SI"></span>


Property Type: VT\_I4

Valid Values: WIA\_PROP\_LIST

Access Rights: Read/write

Remarks
-------

An application changes the WIA\_DPC\_EXPOSURE\_MODE property to control the exposure mode of the camera device.

The following table describes the constants that are valid with WIA\_DPC\_EXPOSURE\_MODE.

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
<td><p>EXPOSUREMODE_APERTURE_PRIORITY</p></td>
<td><p>A user manually sets the aperture, and the camera device automatically sets the shutter speed.</p></td>
</tr>
<tr class="even">
<td><p>EXPOSUREMODE_AUTO</p></td>
<td><p>The camera device automatically sets the aperture and shutter speed.</p></td>
</tr>
<tr class="odd">
<td><p>EXPOSUREMODE_MANUAL</p></td>
<td><p>A user manually sets the aperture and shutter speed.</p></td>
</tr>
<tr class="even">
<td><p>EXPOSUREMODE_PROGRAM_ACTION</p></td>
<td><p>The camera device automatically sets the aperture and shutter speed, and it optimizes them for moving subject matter (in other words, scenes that contain fast motion).</p></td>
</tr>
<tr class="odd">
<td><p>EXPOSUREMODE_PROGRAM_CREATIVE</p></td>
<td><p>The camera device automatically sets the aperture and shutter speed, and it optimizes them for still subject matter.</p></td>
</tr>
<tr class="even">
<td><p>EXPOSUREMODE_PORTRAIT</p></td>
<td><p>The camera device automatically sets the aperture and shutter speed, and it optimizes them for portrait photography.</p></td>
</tr>
<tr class="odd">
<td><p>EXPOSUREMODE_SHUTTER_PRIORITY</p></td>
<td><p>A user manually sets the shutter speed, and the camera device automatically sets the aperture.</p></td>
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

 

 





