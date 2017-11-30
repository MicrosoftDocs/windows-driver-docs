---
title: WIA\_IPA\_PROP\_STREAM\_COMPAT\_ID
description: The WIA\_IPA\_PROP\_STREAM\_COMPAT\_ID property specifies a class identifier (CLSID) that represents a set of device property values.
ms.assetid: e0701a7a-45e8-4096-8f20-2ed7d3113181
keywords: ["WIA_IPA_PROP_STREAM_COMPAT_ID Imaging Devices"]
topic_type:
- apiref
api_name:
- WIA_IPA_PROP_STREAM_COMPAT_ID
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

# WIA\_IPA\_PROP\_STREAM\_COMPAT\_ID


The WIA\_IPA\_PROP\_STREAM\_COMPAT\_ID property specifies a class identifier (CLSID) that represents a set of device property values.

## <span id="ddk_wia_ipa_prop_stream_compat_id_si"></span><span id="DDK_WIA_IPA_PROP_STREAM_COMPAT_ID_SI"></span>


Property Type: VT\_CLSID

Valid Values: WIA\_PROP\_LIST

Access Rights: Read-only

Remarks
-------

If a device driver implements the WIA\_IPA\_PROP\_STREAM\_COMPAT\_ID property, applications use this property to determine whether the device supports a set of values.

The following table describes the constants that are valid with WIA\_IPA\_PROP\_STREAM\_COMPAT\_ID.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Format</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>WiaImgFmt_BMP</p></td>
<td><p>Microsoft Windows bitmap with a header file</p></td>
</tr>
<tr class="even">
<td><p>WiaImgFmt_EMF</p></td>
<td><p>Extended Windows metafile</p></td>
</tr>
<tr class="odd">
<td><p>WiaImgFmt_EXIF</p></td>
<td><p>Exchangeable File Format</p></td>
</tr>
<tr class="even">
<td><p>WiaImgFmt_FLASHPIX</p></td>
<td><p>FlashPix format</p></td>
</tr>
<tr class="odd">
<td><p>WiaImgFmt_GIF</p></td>
<td><p>GIF image format</p></td>
</tr>
<tr class="even">
<td><p>WiaImgFmt_ICO</p></td>
<td><p>Windows icon file format</p></td>
</tr>
<tr class="odd">
<td><p>WiaImgFmt_JPEG</p></td>
<td><p>JPEG compressed format</p></td>
</tr>
<tr class="even">
<td><p>WiaImgFmt_PHOTOCD</p></td>
<td><p>Eastman Kodak file format</p></td>
</tr>
<tr class="odd">
<td><p>WiaImgFmt_PNG</p></td>
<td><p>W3C PNG format</p></td>
</tr>
<tr class="even">
<td><p>WiaImgFmt_MEMORYBMP</p></td>
<td><p>Windows bitmap without a header file</p></td>
</tr>
<tr class="odd">
<td><p>WiaImgFmt_TIFF</p></td>
<td><p>Tag Image File Format</p></td>
</tr>
<tr class="even">
<td><p>WiaImgFmt_WMF</p></td>
<td><p>Windows metafile</p></td>
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
<td><p>Header</p></td>
<td>Wiadef.h (include Wiadef.h)</td>
</tr>
</tbody>
</table>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20WIA_IPA_PROP_STREAM_COMPAT_ID%20%20RELEASE:%20%2811/13/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




