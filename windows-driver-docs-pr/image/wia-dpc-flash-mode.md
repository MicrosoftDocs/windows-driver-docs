---
title: WIA\_DPC\_FLASH\_MODE
description: The WIA\_DPC\_FLASH\_MODE property defines the current flash mode setting for a camera device. The device driver enumerates the supported values of this property, and an application writes this property to set the flash mode for the camera device.
ms.assetid: 04c58111-09a7-4cd0-b60b-a65197c0931d
keywords: ["WIA_DPC_FLASH_MODE Imaging Devices"]
topic_type:
- apiref
api_name:
- WIA_DPC_FLASH_MODE
api_location:
- Wiadef.h
api_type:
- HeaderDef
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# WIA\_DPC\_FLASH\_MODE


The WIA\_DPC\_FLASH\_MODE property defines the current flash mode setting for a camera device. The device driver enumerates the supported values of this property, and an application writes this property to set the flash mode for the camera device.

## <span id="ddk_wia_dpc_flash_mode_si"></span><span id="DDK_WIA_DPC_FLASH_MODE_SI"></span>


Property Type: VT\_I4

Valid Values: WIA\_PROP\_LIST

Access Rights: Read/write

Remarks
-------

The following table describes the six that are valid with this property.

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
<td><p>FLASHMODE_AUTO</p></td>
<td><p>The camera device determines the proper flash settings.</p></td>
</tr>
<tr class="even">
<td><p>FLASHMODE_EXTERNALSYNC</p></td>
<td><p>The camera device is configured to synchronize with external flash units.</p></td>
</tr>
<tr class="odd">
<td><p>FLASHMODE_FILL</p></td>
<td><p>The camera device is configured to flash regardless of current lighting conditions.</p></td>
</tr>
<tr class="even">
<td><p>FLASHMODE_OFF</p></td>
<td><p>The camera device is configured <em>not</em> to flash for any picture taken.</p></td>
</tr>
<tr class="odd">
<td><p>FLASHMODE_REDEYE_AUTO</p></td>
<td><p>The camera device determines the proper flash settings by using red-eye reduction, regardless of current lighting conditions.</p></td>
</tr>
<tr class="even">
<td><p>FLASHMODE_REDEYE_FILL</p></td>
<td><p>The camera device is configured to use red-eye reduction and flash regardless of current lighting conditions.</p></td>
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

 

 





