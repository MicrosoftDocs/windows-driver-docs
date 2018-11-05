---
title: WIA\_IPC\_THUMBNAIL
description: The WIA\_IPC\_THUMBNAIL property contains the 24-bits-per-pixel thumbnail data bits. The WIA minidriver creates and maintains this property.
ms.assetid: 748443a7-cc7f-4291-b987-21462af97c3c
keywords: ["WIA_IPC_THUMBNAIL Imaging Devices"]
topic_type:
- apiref
api_name:
- WIA_IPC_THUMBNAIL
api_location:
- Wiadef.h
api_type:
- HeaderDef
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# WIA\_IPC\_THUMBNAIL


The WIA\_IPC\_THUMBNAIL property contains the 24-bits-per-pixel thumbnail data bits. The WIA minidriver creates and maintains this property.

## <span id="ddk_wia_ipc_thumbnail_si"></span><span id="DDK_WIA_IPC_THUMBNAIL_SI"></span>


Property Type: VT\_UI1 | VT\_VECTOR

Valid Values: WIA\_PROP\_NONE

Access Rights: Read-only

Remarks
-------

The thumbnail data that the WIA\_IPC\_THUMBNAIL property contains must be in uncompressed bitmap data and aligned on 32-bit boundaries. An application reads the values of the [**WIA\_IPC\_THUMBNAIL\_WIDTH**](wia-ipc-thumbnail-width.md) and [**WIA\_IPC\_THUMBNAIL\_HEIGHT**](wia-ipc-thumbnail-height.md) properties and creates a BITMAPINFOHEADER structure (which is described in the Microsoft Windows SDK documentation). The application should be able to read the WIA\_IPC\_THUMBNAIL property (which represents the actual thumbnail image data) and use this property to write the data directly into the newly created bitmap to create the thumbnail image.

WIA\_IPC\_THUMBNAIL is used by WIA minidrivers and applications that are running on Microsoft Windows XP, Windows Me, and later versions of the operating system.

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


[**WIA\_IPC\_THUMBNAIL\_HEIGHT**](wia-ipc-thumbnail-height.md)

[**WIA\_IPC\_THUMBNAIL\_WIDTH**](wia-ipc-thumbnail-width.md)

 

 






