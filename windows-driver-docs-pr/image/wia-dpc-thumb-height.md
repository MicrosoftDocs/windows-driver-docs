---
title: WIA\_DPC\_THUMB\_HEIGHT
description: The WIA\_DPC\_THUMB\_HEIGHT property defines the height, in pixels, of a thumbnail image to use for newly captured images.
ms.assetid: bc4ad063-7287-461e-a31b-d4b6628372b6
keywords: ["WIA_DPC_THUMB_HEIGHT Imaging Devices"]
topic_type:
- apiref
api_name:
- WIA_DPC_THUMB_HEIGHT
api_location:
- Wiadef.h
api_type:
- HeaderDef
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# WIA\_DPC\_THUMB\_HEIGHT


The WIA\_DPC\_THUMB\_HEIGHT property defines the height, in pixels, of a thumbnail image to use for newly captured images.

## <span id="ddk_wia_dpc_thumb_height_si"></span><span id="DDK_WIA_DPC_THUMB_HEIGHT_SI"></span>


Property Type: VT\_I4

Valid Values: WIA\_PROP\_NONE or WIA\_PROP\_LIST

Access Rights: Read-only or read/write

Remarks
-------

An application reads the WIA\_DPC\_THUMB\_HEIGHT value to get an estimated size for displaying thumbnail images in its user interface.

If the value or WIA\_DPC\_THUMB\_HEIGHT is WIA\_PROP\_NONE, the access rights must be read-only. If the value is WIA\_PROP\_LIST, the access rights must be read/write.

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


[**WIA\_DPC\_THUMB\_WIDTH**](wia-dpc-thumb-width.md)

 

 






