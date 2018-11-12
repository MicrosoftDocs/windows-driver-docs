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
ms.date: 11/28/2017
ms.localizationpriority: medium
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
<td><p>WIA_COMPRESSION_JBIG<em></p></td>
<td><p>IS 11544 (ITU-T T.82) compression</p></td>
</tr>
<tr class="even">
<td><p>WIA_COMPRESSION_JPEG</p></td>
<td><p>JPEG compression</p></td>
</tr>
<tr class="odd">
<td><p>WIA_COMPRESSION_JPEG2K</em></p></td>
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

 

 





