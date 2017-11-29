---
title: WIA\_IPA\_COMPRESSION
description: The WIA\_IPA\_COMPRESSION property contains the current compression type that is used. The WIA minidriver creates and maintains this property.
ms.assetid: 6853dc51-bde0-4548-92f6-678b55cf6275
keywords: ["WIA_IPA_COMPRESSION Imaging Devices"]
topic_type:
- apiref
api_name:
- WIA_IPA_COMPRESSION
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

# WIA\_IPA\_COMPRESSION


The WIA\_IPA\_COMPRESSION property contains the current compression type that is used. The WIA minidriver creates and maintains this property.

## <span id="ddk_wia_ipa_compression_si"></span><span id="DDK_WIA_IPA_COMPRESSION_SI"></span>


Property Type: VT\_I4

Valid Values: WIA\_PROP\_LIST

Access Rights: Read/write (image acquisitions); read-only (image storage)

Remarks
-------

An application reads the WIA\_IPA\_COMPRESSION property to determine the image compression type, or the application sets this property to configure the compression setting.

The following table describes the constants that are valid with WIA\_IPA\_COMPRESSION.

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
<td><p>WIA_COMPRESSION_BI_RLE4</p></td>
<td><p>RLE 4 compression</p></td>
</tr>
<tr class="even">
<td><p>WIA_COMPRESSION_BI_RLE8</p></td>
<td><p>RLE 8 compression</p></td>
</tr>
<tr class="odd">
<td><p>WIA_COMPRESSION_G3</p></td>
<td><p>Group 3 compression</p></td>
</tr>
<tr class="even">
<td><p>WIA_COMPRESSION_G4</p></td>
<td><p>Group 4 compression</p></td>
</tr>
<tr class="odd">
<td><p>WIA_COMPRESSION_JBIG*</p></td>
<td><p>IS 11544 (ITU-T T.82) compression</p></td>
</tr>
<tr class="even">
<td><p>WIA_COMPRESSION_JPEG</p></td>
<td><p>JPEG compression</p></td>
</tr>
<tr class="odd">
<td><p>WIA_COMPRESSION_JPEG2K*</p></td>
<td><p>JPEG 2000 compression</p></td>
</tr>
<tr class="even">
<td><p>WIA_COMPRESSION_NONE</p></td>
<td><p>No compression</p></td>
</tr>
<tr class="odd">
<td><p>WIA_COMPRESSION_PNG*</p></td>
<td><p>W3C PNG compression</p></td>
</tr>
</tbody>
</table>

 

Values that are marked with an asterisk (\*) are for Windows Vista and later operating systems only.

**Note**   When the file format is WiaImgFmt\_XPS or WiaImgFmt\_PDFA, WIA\_COMPRESSION\_NONE means "not defined"; the device cannot choose the internal compression (if any) for images that are stored in these two document formats.

 

All WIA 2.0 minidrivers must set the initial value of this property to its default value, which is WIA\_COMPRESSION\_NONE.

The access rights of the WIA\_IPA\_COMPRESSION property are read/write for all image acquisitions but read-only for stored image items.

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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20WIA_IPA_COMPRESSION%20%20RELEASE:%20%2811/13/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




