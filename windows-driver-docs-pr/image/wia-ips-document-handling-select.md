---
title: WIA\_IPS\_DOCUMENT\_HANDLING\_SELECT
description: The WIA\_IPS\_DOCUMENT\_HANDLING\_SELECT property contains the current scanner acquisition source and mode.
ms.assetid: f148e91f-847c-4db2-8459-9f52892cd703
keywords: ["WIA_IPS_DOCUMENT_HANDLING_SELECT Imaging Devices"]
topic_type:
- apiref
api_name:
- WIA_IPS_DOCUMENT_HANDLING_SELECT
api_location:
- Wiadef.h
api_type:
- HeaderDef
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# WIA\_IPS\_DOCUMENT\_HANDLING\_SELECT


The WIA\_IPS\_DOCUMENT\_HANDLING\_SELECT property contains the current scanner acquisition source and mode.

Property Type: VT\_I4

Valid Values: WIA\_PROP\_FLAG

Access Rights: Read/write

Remarks
-------

An application reads the WIA\_IPS\_DOCUMENT\_HANDLING\_SELECT property to determine the current acquisition source of a scanner, or the application writes this property to set the source and mode of the scanner. In addition, applications use this property to enable and disable duplexer functionality. The WIA minidriver creates and maintains this property.

The following table describes a constant that is valid with Windows Vista and later only.

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
<td><p>ADVANCED_DUPLEX</p></td>
<td><p>Scan by using individual configuration settings for each child feeder item (WIA_CATEGORY_FEEDER_FRONT and WIA_CATEGORY_FEEDER_BACK). This flag cannot be set together with DUPLEX.</p>
<p>A device that supports different scan settings for the front and back items should implement the optional ADF front and back items and it should support both DUPLEX and ADVANCED_DUPLEX.</p></td>
</tr>
</tbody>
</table>

 

The following table describes the constants that are valid with Windows Vista and Windows XP.

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
<td><p>BACK_FIRST</p></td>
<td><p>Scan the back of the document first. This value is valid only when DUPLEX is set.</p></td>
</tr>
<tr class="even">
<td><p>BACK_ONLY</p></td>
<td><p>Scan the back <em>only</em>. This value is valid only when DUPLEX is set.</p></td>
</tr>
<tr class="odd">
<td><p>DUPLEX</p></td>
<td><p>Scan by using duplexer operations.</p></td>
</tr>
<tr class="even">
<td><p>FRONT_FIRST</p></td>
<td><p>Scan the front of the document first. This value is valid only when DUPLEX is set.</p></td>
</tr>
<tr class="odd">
<td><p>FRONT_ONLY</p></td>
<td><p>Scan the front <em>only</em>.</p></td>
</tr>
</tbody>
</table>

 

The values DUPLEX and FRONT\_ONLY are mutually exclusive--set one or the other, but not both.

A WIA 2.0 minidriver must set the initial value of this property to its default value, FRONT\_ONLY. Failure to observe this requirement might make the minidriver incompatible with the WIA 1.0 common scan dialog and with some WIA 1.0 applications.

The following table describes the constants that are valid with Windows XP but are obsolete with Windows Vista and later.

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
<td><p>AUTO_ADVANCE</p></td>
<td><p>Enable automatic feeding of the next document after a scan.</p></td>
</tr>
<tr class="even">
<td><p>FEEDER</p></td>
<td><p>Scan by using the document feeder.</p></td>
</tr>
<tr class="odd">
<td><p>FLATBED</p></td>
<td><p>Scan by using the flatbed.</p></td>
</tr>
<tr class="even">
<td><p>NEXT_PAGE</p></td>
<td><p>Scan the next page of the document.</p></td>
</tr>
<tr class="odd">
<td><p>PREFEED</p></td>
<td><p>Enable pre-feed mode. Position the next document while scanning.</p></td>
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
<td><p>Version</p></td>
<td><p>Available in Windows Vista and later operating systems. For Windows XP, use the identical WIA_DPS_DOCUMENT_HANDLING_SELECT property.</p></td>
</tr>
<tr class="even">
<td><p>Header</p></td>
<td>Wiadef.h (include Wiadef.h)</td>
</tr>
</tbody>
</table>

## See also


[**WIA\_DPS\_DOCUMENT\_HANDLING\_SELECT**](wia-dps-document-handling-select.md)

 

 






