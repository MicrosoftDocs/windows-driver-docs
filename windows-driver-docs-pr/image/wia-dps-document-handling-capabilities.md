---
title: WIA\_DPS\_DOCUMENT\_HANDLING\_CAPABILITIES
description: The WIA\_DPS\_DOCUMENT\_HANDLING\_CAPABILITIES property contains the capabilities of a scanner.
MS-HAID:
- 'WIA\_PropTable\_53c71755-682f-4a6b-8ae2-32754300ce44.xml'
- 'image.wia\_dps\_document\_handling\_capabilities'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 19c9cbd0-19ef-4d44-85f1-25e71f9a92bc
keywords: ["WIA_DPS_DOCUMENT_HANDLING_CAPABILITIES Imaging Devices"]
topic_type:
- apiref
api_name:
- WIA_DPS_DOCUMENT_HANDLING_CAPABILITIES
api_location:
- Wiadef.h
api_type:
- HeaderDef
---

# WIA\_DPS\_DOCUMENT\_HANDLING\_CAPABILITIES


The WIA\_DPS\_DOCUMENT\_HANDLING\_CAPABILITIES property contains the capabilities of a scanner.

## <span id="ddk_wia_dps_document_handling_capabilities_si"></span><span id="DDK_WIA_DPS_DOCUMENT_HANDLING_CAPABILITIES_SI"></span>


Property Type: VT\_I4

Valid Values: WIA\_PROP\_NONE

Access Rights: Read-only

Remarks
-------

An application reads the WIA\_DPS\_DOCUMENT\_HANDLING\_CAPABILITIES property to determine whether a scanner has a flatbed, document feeder, or duplexer installed. You can also use this property to further define the installed features. The WIA minidriver creates and maintains this property.

The following table describes the constants that are valid with Windows 8 only.

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
<td><p>IMPRINTER</p></td>
<td><p>Imprinter</p></td>
</tr>
<tr class="even">
<td><p>ENDORSER</p></td>
<td><p>Endorser</p></td>
</tr>
<tr class="odd">
<td><p>BARCODE_READER</p></td>
<td><p>Barcode Reader</p></td>
</tr>
<tr class="even">
<td><p>PATCH_CODE_READER</p></td>
<td><p>Patch Code Reader</p></td>
</tr>
<tr class="odd">
<td><p>MICR_READER</p></td>
<td><p>MICR Reader</p></td>
</tr>
</tbody>
</table>

 

The following table describes the constants that are valid with Windows 7 only.

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
<td><p>AUTO_SOURCE</p></td>
<td><p>The device supports [auto-configured scanning](https://msdn.microsoft.com/library/windows/hardware/ff539393).</p></td>
</tr>
</tbody>
</table>

 

The following table describes the constants that are valid with Windows 7 and Windows Vista, but not with Windows XP.

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
<td><p>ADVANCED_DUP</p></td>
<td><p>The device supports advanced duplex scan configuration, independently on each document size.</p></td>
</tr>
<tr class="even">
<td><p>DETECT_FILM_TPA</p></td>
<td><p>The scanner can detect when the transparency or film scanning adapter is ready to scan.</p></td>
</tr>
<tr class="odd">
<td><p>DETECT_STOR</p></td>
<td><p>The scanner can detect when there is a document in the internal storage.</p></td>
</tr>
<tr class="even">
<td><p>FILM_TPA</p></td>
<td><p>The scanner has a transparency or film scanning adapter.</p></td>
</tr>
<tr class="odd">
<td><p>STOR</p></td>
<td><p>The scanner is equipped with an internal storage device.</p></td>
</tr>
</tbody>
</table>

 

The following table describes the constants that are valid with Windows 7, Windows Vista, and Windows XP.

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
<td><p>DETECT_FEED</p></td>
<td><p>The scanner can detect a document in the feeder.</p></td>
</tr>
<tr class="even">
<td><p>DETECT_FLAT</p></td>
<td><p>The scanner can detect a document on the flatbed platen.</p></td>
</tr>
<tr class="odd">
<td><p>DETECT_SCAN</p></td>
<td><p>The scanner can detect a document in the feeder only by scanning.</p></td>
</tr>
<tr class="even">
<td><p>DUP</p></td>
<td><p>The scanner has a duplexer.</p></td>
</tr>
<tr class="odd">
<td><p>FEED</p></td>
<td><p>The scanner has a document feeder installed.</p></td>
</tr>
<tr class="even">
<td><p>FLAT</p></td>
<td><p>The scanner has a flatbed platen.</p></td>
</tr>
</tbody>
</table>

 

The following table describes the constants that are valid with Windows XP only; these flags are obsolete for Windows 7 and Windows Vista and should not be used.

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
<td><p>DETECT_DUP</p></td>
<td><p>The scanner can detect a duplex scan request from a user.</p></td>
</tr>
<tr class="even">
<td><p>DETECT_DUP_AVAIL</p></td>
<td><p>The scanner can detect when a duplexer is installed.</p></td>
</tr>
<tr class="odd">
<td><p>DETECT_FEED_AVAIL</p></td>
<td><p>The scanner can detect when a document feeder is installed.</p></td>
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20WIA_DPS_DOCUMENT_HANDLING_CAPABILITIES%20%20RELEASE:%20%2811/13/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




