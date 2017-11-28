---
title: WIA\_DPS\_DOCUMENT\_HANDLING\_STATUS
description: The WIA\_DPS\_DOCUMENT\_HANDLING\_STATUS property contains the current state of a scanner's installed flatbed, document feeder, or duplexer.
ms.assetid: b95c64ee-b06c-4786-87d3-d8a0f91dcba2
keywords: ["WIA_DPS_DOCUMENT_HANDLING_STATUS Imaging Devices"]
topic_type:
- apiref
api_name:
- WIA_DPS_DOCUMENT_HANDLING_STATUS
api_location:
- Wiadef.h
api_type:
- HeaderDef
---

# WIA\_DPS\_DOCUMENT\_HANDLING\_STATUS


The WIA\_DPS\_DOCUMENT\_HANDLING\_STATUS property contains the current state of a scanner's installed flatbed, document feeder, or duplexer.

## <span id="ddk_wia_dps_document_handling_status_si"></span><span id="DDK_WIA_DPS_DOCUMENT_HANDLING_STATUS_SI"></span>


Property Type: VT\_I4

Valid Values: WIA\_PROP\_NONE

Access Rights: Read-only

Remarks
-------

An application reads the WIA\_DPS\_DOCUMENT\_HANDLING\_STATUS property to determine whether a scanner device is ready to use. Reading this property is an ideal way to check whether paper is in the feeder before a user acquires an image. The WIA minidriver creates and maintains this property.

The following table describes the constants that are valid with Windows 8 and later versions of Windows.

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
<td><p>IMPRINTER_READY</p></td>
<td><p>The imprinter capabilities of an imprinter/endorser are enabled and ready for use.</p></td>
</tr>
<tr class="even">
<td><p>ENDORSER_READY</p></td>
<td><p>The endorser capabilities of an imprinter/endorser are enabled and ready for use.</p></td>
</tr>
<tr class="odd">
<td><p>BARCODE_READER_READY</p></td>
<td><p>The barcode reader is enabled and ready for use.</p></td>
</tr>
<tr class="even">
<td><p>PATCH_CODE_READER_READY</p></td>
<td><p>The patch code reader is enabled and ready for use.</p></td>
</tr>
<tr class="odd">
<td><p>MICR_READER_READY</p></td>
<td><p>The MICR reader is enabled and ready for use.</p></td>
</tr>
</tbody>
</table>

 

The following table describes the constants that are valid with both Windows Vista and Windows XP.

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
<td><p>DUP_READY</p></td>
<td><p>The duplexer is enabled and ready to use.</p></td>
</tr>
<tr class="even">
<td><p>FEED_READY</p></td>
<td><p>The document feeder has a page loaded and is ready for use.</p></td>
</tr>
<tr class="odd">
<td><p>FLAT_COVER_UP</p></td>
<td><p>The flatbed cover is up.</p></td>
</tr>
<tr class="even">
<td><p>FLAT_READY</p></td>
<td><p>The flatbed is ready for use.</p></td>
</tr>
<tr class="odd">
<td><p>PAPER_JAM</p></td>
<td><p>A document is stuck in the document feeder.</p></td>
</tr>
<tr class="even">
<td><p>PATH_COVER_UP</p></td>
<td><p>The paper path is covered and is preventing proper operation.</p></td>
</tr>
</tbody>
</table>

 

The following table describes the constants that are valid with Windows Vista only.

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
<td><p>FILM_TPA_READY</p></td>
<td><p>A transparency adapter is installed and ready for use.</p></td>
</tr>
<tr class="even">
<td><p>STORAGE_READY</p></td>
<td><p>A storage device is installed and ready for use.</p></td>
</tr>
<tr class="odd">
<td><p>STORAGE_FULL</p></td>
<td><p>The storage is full; no upload operations are possible.</p></td>
</tr>
<tr class="even">
<td><p>MULTIPLE_FEED</p></td>
<td><p>A multiple feed occurred; this type of feed usually occurs with a PAPER_JAM value.</p></td>
</tr>
<tr class="odd">
<td><p>DEVICE_ATTENTION</p></td>
<td><p>There is an error that requires user intervention on the scanner.</p></td>
</tr>
<tr class="even">
<td><p>LAMP_ERR</p></td>
<td><p>The scanner has a problem with the lamp and is not ready.</p></td>
</tr>
</tbody>
</table>

 

**Note**   There are no custom-defined base definitions. You cannot create custom extensions for status flag values. If you need custom status reporting, you should define a custom property.

 

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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20WIA_DPS_DOCUMENT_HANDLING_STATUS%20%20RELEASE:%20%2811/13/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




