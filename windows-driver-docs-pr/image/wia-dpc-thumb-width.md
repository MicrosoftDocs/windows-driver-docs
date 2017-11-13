---
title: WIA\_DPC\_THUMB\_WIDTH
description: The WIA\_DPC\_THUMB\_WIDTH property defines the width, in pixels, of a thumbnail image to use for newly captured images.
MS-HAID:
- 'WIA\_PropTable\_9e4f93e0-30b7-42af-8026-633e8a09d045.xml'
- 'image.wia\_dpc\_thumb\_width'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 01136695-9bef-4d47-89df-fb1d14465bef
keywords: ["WIA_DPC_THUMB_WIDTH Imaging Devices"]
topic_type:
- apiref
api_name:
- WIA_DPC_THUMB_WIDTH
api_location:
- Wiadef.h
api_type:
- HeaderDef
---

# WIA\_DPC\_THUMB\_WIDTH


The WIA\_DPC\_THUMB\_WIDTH property defines the width, in pixels, of a thumbnail image to use for newly captured images.

## <span id="ddk_wia_dpc_thumb_width_si"></span><span id="DDK_WIA_DPC_THUMB_WIDTH_SI"></span>


Property Type: VT\_I4

Valid Values: WIA\_PROP\_NONE, or WIA\_PROP\_LIST

Access Rights: Read-only or read/write

Remarks
-------

An application reads the WIA\_DPC\_THUMB\_WIDTH value to get an estimated size for displaying thumbnail images in its user interface.

If the value or WIA\_DPC\_THUMB\_WIDTH is WIA\_PROP\_NONE, the access rights must be read-only. If the value is WIA\_PROP\_LIST, the access rights must be read/write.

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


[**WIA\_DPC\_THUMB\_HEIGHT**](wia-dpc-thumb-height.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20WIA_DPC_THUMB_WIDTH%20%20RELEASE:%20%2811/13/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





