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
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
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

## <span id="see_also"></span>See also


[**WIA\_IPC\_THUMBNAIL\_HEIGHT**](wia-ipc-thumbnail-height.md)

[**WIA\_IPC\_THUMBNAIL\_WIDTH**](wia-ipc-thumbnail-width.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20WIA_IPC_THUMBNAIL%20%20RELEASE:%20%2811/13/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





