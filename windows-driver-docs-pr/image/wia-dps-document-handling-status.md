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
ms.date: 11/28/2017
ms.localizationpriority: medium
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

 

 





