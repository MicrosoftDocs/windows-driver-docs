---
title: Mapping WIA Properties with the Same IDs and Names
description: Mapping WIA Properties with the Same IDs and Names
ms.assetid: 40a1094d-50fa-42b6-9976-ec6b05fdc384
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Mapping WIA Properties with the Same IDs and Names


There are Windows XP properties that have the same property IDs and property names as their Windows Vista counterparts. The following is a table of these Windows XP root properties and the FLATBED and FEEDER (ADF) properties that they are translated to in Windows Vista.

<table>
<colgroup>
<col width="25%" />
<col width="25%" />
<col width="25%" />
<col width="25%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p><strong>Windows XP Property</strong></p></td>
<td><p><strong>Windows XP</strong></p>
<p><strong>Item / Context</strong></p></td>
<td><p><strong>Windows Vista Property</strong></p></td>
<td><p><strong>Windows Vista Item</strong></p></td>
</tr>
<tr class="even">
<td><p>WIA_IPA_ITEM_NAME</p>
<p>Read-only access See note: d</p></td>
<td><p>Root</p>
<p>See note: c</p></td>
<td><p>WIA_IPA_ITEM_NAME</p>
<p>Read-only access See note: d</p></td>
<td><p>Root</p>
<p>See note: c</p></td>
</tr>
<tr class="odd">
<td><p>WIA_IPA_ITEM_NAME</p>
<p>or Generic: &quot;FLATBED&quot;</p>
<p>Read-only access See notes: d and e</p></td>
<td><p>Child / FLATBED</p>
<p>See note: b</p></td>
<td><p>WIA_IPA_ITEM_NAME</p>
<p>Read-only access See notes: d and e</p></td>
<td><p>FLATBED</p>
<p>See note: b</p></td>
</tr>
<tr class="even">
<td><p>WIA_IPA_ITEM_NAME</p>
<p>or Generic: &quot;FEEDER&quot;</p>
<p>Read-only access See notes: d and e</p></td>
<td><p>Child / FEEDER</p>
<p>See note: a</p></td>
<td><p>WIA_IPA_ITEM_NAME</p>
<p>Read-only access See notes: d and e</p></td>
<td><p>FEEDER</p>
<p>See note: a</p></td>
</tr>
<tr class="odd">
<td><p>WIA_IPA_FULL_ITEM_NAME</p>
<p>Read-only access See note: d</p></td>
<td><p>Root</p>
<p>See note: c</p></td>
<td><p>WIA_IPA_FULL_ITEM_NAME</p>
<p>Read-only access See note: d</p></td>
<td><p>Root</p>
<p>See note: c</p></td>
</tr>
<tr class="even">
<td><p>WIA_IPA_FULL_ITEM_NAME</p>
<p>or Generic: &quot;\Root\FLATBED&quot;</p>
<p>Read-only access See notes: d and e</p></td>
<td><p>Child / FLATBED</p>
<p>See note: b</p></td>
<td><p>WIA_IPA_FULL_ITEM_NAME</p>
<p>Read-only access</p></td>
<td><p>FLATBED</p>
<p>See note: b</p></td>
</tr>
<tr class="odd">
<td><p>WIA_IPA_FULL_ITEM_NAME</p>
<p>or Generic: &quot;\Root\FEEDER&quot;</p>
<p>Read-only access</p></td>
<td><p>Child / FEEDER</p>
<p>See note: a</p></td>
<td><p>WIA_IPA_FULL_ITEM_NAME</p>
<p>Read-only access See notes: d and e</p></td>
<td><p>FEEDER</p>
<p>See note: a</p></td>
</tr>
<tr class="even">
<td><p>WIA_IPA_ITEM_TIME</p>
<p>Read-only access</p></td>
<td><p>Child / FLATBED</p>
<p>See note: b</p></td>
<td><p>WIA_IPA_ITEM_TIME</p>
<p>Read-only access</p></td>
<td><p>FLATBED</p>
<p>See note: b</p></td>
</tr>
<tr class="odd">
<td><p>WIA_IPA_ITEM_TIME</p>
<p>Read-only access</p></td>
<td><p>Child / FEEDER</p>
<p>See note: a</p></td>
<td><p>WIA_IPA_ITEM_TIME</p>
<p>Read-only access</p></td>
<td><p>FEEDER</p>
<p>See note: a</p></td>
</tr>
<tr class="even">
<td><p>WIA_IPA_ITEM_FLAGS</p>
<p>Read-only access See notes: d and e</p></td>
<td><p>Root</p>
<p>See note: c</p></td>
<td><p>WIA_IPA_ITEM_FLAGS</p>
<p>Read-only access See notes: d and e</p></td>
<td><p>Root</p>
<p>See note: c</p></td>
</tr>
<tr class="odd">
<td><p>WIA_IPA_ITEM_FLAGS</p>
<p>Read-only access See notes: d and e</p></td>
<td><p>Child / FLATBED</p>
<p>See note: b</p></td>
<td><p>WIA_IPA_ITEM_FLAGS</p>
<p>Read-only access See notes: d and e</p></td>
<td><p>FLATBED</p>
<p>See note: b</p></td>
</tr>
<tr class="even">
<td><p>WIA_IPA_ITEM_FLAGS</p>
<p>Read-only access See notes: d and e</p></td>
<td><p>Child / FEEDER</p>
<p>See note: a</p></td>
<td><p>WIA_IPA_ITEM_FLAGS</p>
<p>Read-only access See notes: d and e</p></td>
<td><p>FEEDER</p>
<p>See note: a</p></td>
</tr>
<tr class="odd">
<td><p>WIA_IPA_ACCESS_RIGHTS</p>
<p>Read-only access</p></td>
<td><p>Root</p>
<p>See note: c</p></td>
<td><p>WIA_IPA_ACCESS_RIGHTS</p>
<p>Read-only access</p></td>
<td><p>Root</p>
<p>See note: c</p></td>
</tr>
<tr class="even">
<td><p>WIA_IPA_ACCESS_RIGHTS</p>
<p>Read-only access</p></td>
<td><p>Child / FLATBED</p>
<p>See note: b</p></td>
<td><p>WIA_IPA_ACCESS_RIGHTS</p>
<p>Read-only access</p></td>
<td><p>FLATBED</p>
<p>See note: b</p></td>
</tr>
<tr class="odd">
<td><p>WIA_IPA_ACCESS_RIGHTS</p>
<p>Read-only access</p></td>
<td><p>Child / FEEDER</p>
<p>See note: a</p></td>
<td><p>WIA_IPA_ACCESS_RIGHTS</p>
<p>Read-only access</p></td>
<td><p>FEEDER</p>
<p>See note: a</p></td>
</tr>
<tr class="even">
<td><p>WIA_IPA_DATATYPE</p>
<p>See note: b</p></td>
<td><p>Child / FLATBED</p>
<p>See note: b</p></td>
<td><p>WIA_IPA_DATATYPE</p>
<p>Read/Write access</p></td>
<td><p>FLATBED</p>
<p>See note: b</p></td>
</tr>
<tr class="odd">
<td><p>WIA_IPA_DATATYPE</p>
<p>Read/Write access</p></td>
<td><p>Child / FEEDER</p>
<p>See note: a</p></td>
<td><p>WIA_IPA_DATATYPE</p>
<p>Read/Write access</p></td>
<td><p>FEEDER</p>
<p>See note: a</p></td>
</tr>
<tr class="even">
<td><p>WIA_IPA_DEPTH</p>
<p>Read/Write access</p></td>
<td><p>Child / FLATBED</p>
<p>See note: b</p></td>
<td><p>WIA_IPA_DEPTH</p>
<p>Read/Write access</p></td>
<td><p>FLATBED</p>
<p>See note: b</p></td>
</tr>
<tr class="odd">
<td><p>WIA_IPA_DEPTH</p>
<p>Read/Write access</p></td>
<td><p>Child / FEEDER</p>
<p>See note: a</p></td>
<td><p>WIA_IPA_DEPTH</p>
<p>Read/Write access</p></td>
<td><p>FEEDER</p>
<p>See note: a</p></td>
</tr>
<tr class="even">
<td><p>WIA_IPA_PREFERRED_FORMAT</p>
<p>Read-only access See note: f</p></td>
<td><p>Child / FLATBED</p>
<p>See note: b</p></td>
<td><p>WIA_IPA_PREFERRED_FORMAT</p>
<p>Read-only access See note: f</p></td>
<td><p>FLATBED</p>
<p>See note: b</p></td>
</tr>
<tr class="odd">
<td><p>WIA_IPA_PREFERRED_FORMAT</p>
<p>Read-only access See note: f</p></td>
<td><p>Child / FEEDER</p>
<p>See note: a</p></td>
<td><p>WIA_IPA_PREFERRED_FORMAT</p>
<p>Read-only access See note: f</p></td>
<td><p>FEEDER</p>
<p>See note: a</p></td>
</tr>
<tr class="even">
<td><p>WIA_IPA_FORMAT</p>
<p>Read/Write access See notes: h and i</p></td>
<td><p>Child / FLATBED</p>
<p>See note: b</p></td>
<td><p>WIA_IPA_FORMAT</p>
<p>Read/Write access See notes: h and i</p></td>
<td><p>FLATBED</p>
<p>See note: b</p></td>
</tr>
<tr class="odd">
<td><p>WIA_IPA_FORMAT</p>
<p>Read/Write access See notes: h and i</p></td>
<td><p>Child / FEEDER</p>
<p>See note: a</p></td>
<td><p>WIA_IPA_FORMAT</p>
<p>Read/Write access See notes: h and i</p></td>
<td><p>FEEDER</p>
<p>See note: a</p></td>
</tr>
<tr class="even">
<td><p>WIA_IPA_COMPRESSION</p>
<p>Read/Write access</p></td>
<td><p>Child / FLATBED</p>
<p>See note: b</p></td>
<td><p>WIA_IPA_COMPRESSION</p>
<p>Read/Write access</p></td>
<td><p>FLATBED</p>
<p>See note: b</p></td>
</tr>
<tr class="odd">
<td><p>WIA_IPA_COMPRESSION</p>
<p>Read/Write access</p></td>
<td><p>Child / FEEDER</p>
<p>See note: a</p></td>
<td><p>WIA_IPA_COMPRESSION</p>
<p>Read/Write access</p></td>
<td><p>FEEDER</p>
<p>See note: a</p></td>
</tr>
<tr class="even">
<td><p>WIA_IPA_TYMED</p>
<p>Read/Write access See notes: h, i and k</p></td>
<td><p>Child / FLATBED</p>
<p>See note: b</p></td>
<td><p>WIA_IPA_TYMED</p>
<p>Read/Write access See notes: h, i and k</p></td>
<td><p>FLATBED</p>
<p>See note: b</p></td>
</tr>
<tr class="odd">
<td><p>WIA_IPA_TYMED</p>
<p>Read/Write access See notes: h and i</p></td>
<td><p>Child / FEEDER</p>
<p>See note: a</p></td>
<td><p>WIA_IPA_TYMED</p>
<p>Read/Write access See notes: h and i</p></td>
<td><p>FEEDER</p>
<p>See note: a</p></td>
</tr>
<tr class="even">
<td><p>WIA_IPA_CHANNELS_PER_PIXEL</p>
<p>Read-only access</p></td>
<td><p>Child / FLATBED</p>
<p>See note: b</p></td>
<td><p>WIA_IPA_CHANNELS_PER_PIXEL</p>
<p>Read-only access</p></td>
<td><p>FLATBED</p>
<p>See note: b</p></td>
</tr>
<tr class="odd">
<td><p>WIA_IPA_CHANNELS_PER_PIXEL</p>
<p>Read-only access</p></td>
<td><p>Child / FEEDER</p>
<p>See note: a</p></td>
<td><p>WIA_IPA_CHANNELS_PER_PIXEL</p>
<p>Read-only access</p></td>
<td><p>FEEDER</p>
<p>See note: a</p></td>
</tr>
<tr class="even">
<td><p>WIA_IPA_BITS_PER_CHANNEL</p>
<p>Read-only access</p></td>
<td><p>Child / FLATBED</p>
<p>See note: b</p></td>
<td><p>WIA_IPA_BITS_PER_CHANNEL</p>
<p>Read-only access</p></td>
<td><p>FLATBED</p>
<p>See note: b</p></td>
</tr>
<tr class="odd">
<td><p>WIA_IPA_BITS_PER_CHANNEL</p>
<p>Read-only access</p></td>
<td><p>Child / FEEDER</p>
<p>See note: a</p></td>
<td><p>WIA_IPA_BITS_PER_CHANNEL</p>
<p>Read-only access</p></td>
<td><p>FEEDER</p>
<p>See note: a</p></td>
</tr>
<tr class="even">
<td><p>WIA_IPA_ITEM_SIZE</p>
<p>Read-only access</p></td>
<td><p>Child / FLATBED</p>
<p>See note: b</p></td>
<td><p>WIA_IPA_ITEM_SIZE</p>
<p>Read-only access</p></td>
<td><p>FLATBED</p>
<p>See note: b</p></td>
</tr>
<tr class="odd">
<td><p>WIA_IPA_ITEM_SIZE</p>
<p>Read-only access</p></td>
<td><p>Child / FEEDER</p>
<p>See note: a</p></td>
<td><p>WIA_IPA_ITEM_SIZE</p>
<p>Read-only access</p></td>
<td><p>FEEDER</p>
<p>See note: a</p></td>
</tr>
<tr class="even">
<td><p>WIA_IPA_ICM_PROFILE_NAME</p>
<p>Read/Write access</p></td>
<td><p>Child / FLATBED</p>
<p>See note: b</p></td>
<td><p>WIA_IPA_ICM_PROFILE_NAME</p>
<p>Read/Write access</p></td>
<td><p>FLATBED</p>
<p>See note: b</p></td>
</tr>
<tr class="odd">
<td><p>WIA_IPA_ICM_PROFILE_NAME</p>
<p>Read/Write access</p></td>
<td><p>Child / FEEDER</p>
<p>See note: c</p></td>
<td><p>WIA_IPA_ICM_PROFILE_NAME</p>
<p>Read/Write access</p></td>
<td><p>FEEDER</p>
<p>See note: a</p></td>
</tr>
<tr class="even">
<td><p>WIA_IPA_FILENAME_EXTENSION</p>
<p>Read-only access</p></td>
<td><p>Child / FLATBED</p>
<p>See note: b</p></td>
<td><p>WIA_IPA_FILENAME_EXTENSION</p>
<p>Read-only access</p></td>
<td><p>FLATBED</p>
<p>See note: b</p></td>
</tr>
<tr class="odd">
<td><p>WIA_IPA_FILENAME_EXTENSION</p>
<p>Read-only access</p></td>
<td><p>Child / FEEDER</p>
<p>See note: a</p></td>
<td><p>WIA_IPA_FILENAME_EXTENSION</p>
<p>Read-only access</p></td>
<td><p>FEEDER</p>
<p>See note: a</p></td>
</tr>
<tr class="even">
<td><p>WIA_IPA_SUPPRESS_PROPERTY_PAGE</p>
<p>Read-only access</p></td>
<td><p>Child / FLATBED</p>
<p>See note: b</p></td>
<td><p>WIA_IPA_SUPPRESS_PROPERTY_PAGE</p>
<p>Read-only access</p></td>
<td><p>FLATBED</p>
<p>See note: b</p></td>
</tr>
<tr class="odd">
<td><p>WIA_IPA_SUPPRESS_PROPERTY_PAGE</p>
<p>Read-only access</p></td>
<td><p>Child / FEEDER</p>
<p>See note: a</p></td>
<td><p>WIA_IPA_SUPPRESS_PROPERTY_PAGE</p>
<p>Read-only access</p></td>
<td><p>FEEDER</p></td>
</tr>
<tr class="even">
<td><p>Generic: WIA_CATEGORY_ROOT</p></td>
<td><p>Root</p>
<p>See note: c</p></td>
<td><p>WIA_IPA_ITEM_CATEGORY</p>
<p>Read-only access See note: f</p></td>
<td><p>Root</p></td>
</tr>
<tr class="odd">
<td><p>Generic: WIA_CATEGORY_FLATBED</p></td>
<td><p>Child / FLATBED</p>
<p>See note: b</p></td>
<td><p>WIA_IPA_ITEM_CATEGORY</p>
<p>Read-only access See note: f</p></td>
<td><p>FLATBED</p>
<p>See note: b</p></td>
</tr>
<tr class="even">
<td><p>Generic: WIA_CATEGORY_FEEDER</p></td>
<td><p>Child / FEEDER</p>
<p>See note: a</p></td>
<td><p>WIA_IPA_ITEM_CATEGORY</p>
<p>Read-only access See note: f</p></td>
<td><p>FEEDER</p>
<p>See note: a</p></td>
</tr>
<tr class="odd">
<td><p>WIA_DPS_DOCUMENT_HANDLING_CAPABILITIES</p>
<p>Read-only access See note: l</p></td>
<td><p>Root</p>
<p>See note: c</p></td>
<td><p>WIA_DPS_DOCUMENT_HANDLING_CAPABILITIES</p>
<p>Read-only access See note: l</p></td>
<td><p>Root</p>
<p>See note: c</p></td>
</tr>
<tr class="even">
<td><p>WIA_IPA_BUFFER_SIZE</p>
<p>Read-only access See note: l</p></td>
<td><p>Child / FLATBED</p>
<p>See note: b</p></td>
<td><p>WIA_IPA_BUFFER_SIZE</p>
<p>Read-only access See note: l</p></td>
<td><p>FLATBED</p>
<p>See note: b</p></td>
</tr>
<tr class="odd">
<td><p>WIA_IPA_BUFFER_SIZE</p>
<p>Read-only access See note: l</p></td>
<td><p>Child / FEEDER</p>
<p>See note: a</p></td>
<td><p>WIA_IPA_BUFFER_SIZE</p>
<p>Read-only access See note: l</p></td>
<td><p>FEEDER</p>
<p>See note: a</p></td>
</tr>
<tr class="even">
<td><p>WIA_IPA_MIN_BUFFER_SIZE</p>
<p>Read-only access See note: l</p></td>
<td><p>Child / FLATBED</p>
<p>See note: b</p></td>
<td><p>WIA_IPA_MIN_BUFFER_SIZE</p>
<p>Read-only access See note: l</p></td>
<td><p>FLATBED</p>
<p>See note: b</p></td>
</tr>
<tr class="odd">
<td><p>WIA_IPA_MIN_BUFFER_SIZE</p>
<p>Read-only access See note: l</p></td>
<td><p>Child / FEEDER</p>
<p>See note: a</p></td>
<td><p>WIA_IPA_MIN_BUFFER_SIZE</p>
<p>Read-only access See note: l</p></td>
<td><p>FEEDER</p>
<p>See note: a</p></td>
</tr>
<tr class="even">
<td><p>WIA_IPA_PIXELS_PER_LINE</p>
<p>Read-only access See note: m</p></td>
<td><p>Child / FLATBED</p>
<p>See note: b</p></td>
<td><p>WIA_IPA_PIXELS_PER_LINE</p>
<p>Read-only access See note: m</p></td>
<td><p>FLATBED</p>
<p>See note: b</p></td>
</tr>
<tr class="odd">
<td><p>WIA_IPA_PIXELS_PER_LINE</p>
<p>Read-only access See note: m</p></td>
<td><p>Child / FEEDER</p>
<p>See note: a</p></td>
<td><p>WIA_IPA_PIXELS_PER_LINE</p>
<p>Read-only access See note: m</p></td>
<td><p>FEEDER</p>
<p>See note: a</p></td>
</tr>
<tr class="even">
<td><p>WIA_IPA_NUMBER_OF_LINES</p>
<p>Read-only access See note: m</p></td>
<td><p>Child / FLATBED</p>
<p>See note: b</p></td>
<td><p>WIA_IPA_NUMBER_OF_LINES</p>
<p>Read-only access See note: m</p></td>
<td><p>FLATBED</p>
<p>See note: b</p></td>
</tr>
<tr class="odd">
<td><p>WIA_IPA_NUMBER_OF_LINES</p>
<p>Read-only access See note: m</p></td>
<td><p>Child / FEEDER</p>
<p>See note: a</p></td>
<td><p>WIA_IPA_NUMBER_OF_LINES</p>
<p>Read-only access See note: m</p></td>
<td><p>FEEDER</p>
<p>See note: a</p></td>
</tr>
<tr class="even">
<td><p>WIA_IPA_BYTES_PER_LINE</p>
<p>Read-only access See note: m</p></td>
<td><p>Child / FLATBED</p>
<p>See note: b</p></td>
<td><p>WIA_IPA_BYTES_PER_LINE</p>
<p>Read-only access See note: m</p></td>
<td><p>FLATBED</p>
<p>See note: b</p></td>
</tr>
<tr class="odd">
<td><p>WIA_IPA_BYTES_PER_LINE</p>
<p>Read-only access See note: m</p></td>
<td><p>Child / FEEDER</p>
<p>See note: a</p></td>
<td><p>WIA_IPA_BYTES_PER_LINE</p>
<p>Read-only access See note: m</p></td>
<td><p>FEEDER</p>
<p>See note: a</p></td>
</tr>
<tr class="even">
<td><p>WIA_IPA_PLANAR</p>
<p>Read-only access</p></td>
<td><p>Child / FLATBED</p>
<p>See note: b</p></td>
<td><p>WIA_IPA_PLANAR</p>
<p>Read-only access</p></td>
<td><p>FLATBED</p>
<p>See note: b</p></td>
</tr>
<tr class="odd">
<td><p>WIA_IPA_PLANAR</p>
<p>Read-only access</p></td>
<td><p>Child / FEEDER</p>
<p>See note: a</p></td>
<td><p>WIA_IPA_PLANAR</p>
<p>Read-only access</p></td>
<td><p>FEEDER</p>
<p>See note: a</p></td>
</tr>
<tr class="even">
<td><p>WIA_DPS_MAX_SCAN_TIME</p>
<p>Read-only access</p></td>
<td><p>Root</p>
<p>See note: c</p></td>
<td><p>WIA_DPS_MAX_SCAN_TIME</p>
<p>Read-only access</p></td>
<td><p>Root</p>
<p>See note: c</p></td>
</tr>
</tbody>
</table>

 

<a href="" id="note-a-"></a>Note a:  
FEEDER item (ADF) or FEEDER context on the Windows XP root or child item (WIA\_DPS\_DOCUMENT\_HANDLING\_SELECT is set to FEEDER).

<a href="" id="note-b-"></a>Note b:  
FLATBED item or FLATBED context on the Windows XP root or child item (WIA\_DPS\_DOCUMENT\_HANDLING\_SELECT is set to FLATBED).

<a href="" id="note-c-"></a>Note c:  
Root item, no context specified for Windows XP.

<a href="" id="note-d-"></a>Note d:  
Managed by the WIA service.

<a href="" id="note-e-"></a>Note e:  
Customized for application's application item tree (A-AIT).

<a href="" id="note-f-"></a>Note f:  
Add to A-AIT even when not supported on driver's application item tree (D-AIT). Set to **WiaImgFmt\_BMP**.

<a href="" id="note-g-"></a>Note g:  
For Windows Vista to Windows XP translation, add **WiaImgFmt\_MEMORYBMP** to be used with [TYMED\_CALLBACK](understanding-tymed.md).

<a href="" id="note-h-"></a>Note h:  
For Windows Vista to Windows XP translation, add TYMED\_CALLBACK and **WiaImgFmt\_MEMORYBMP**. For Windows XP to Windows Vista translation, only [TYMED\_FILE](understanding-tymed.md) and TYMED\_MULTIPAGE\_FILE are translated.

<a href="" id="note-i-"></a>Note i:  
For Windows XP to Windows Vista translation, translate only:

TYMED\_FILE

TYMED\_MULTIPAGE\_FILE

Note j:
For Windows XP to Windows Vista translation, translate only:

DUP

FEED

FLAT

DETECT\_FEED

DETECT\_FLAT

DETECT\_SCAN

Note k:
Add to A-AIT even when not supported on D-AIT. Set to TYMED\_FILE.

Note l:
Add to A-AIT even when not supported on D-AIT.

Note m:
Optional for Windows Vista for all transfer-enabled devices. If these properties are implemented, the legacy applications can get estimate on the number of pixels per line, number of bytes required for each scan line, and total number of scan lines in the image. These values are not accurate because the image processing filter might modify the actual values that these properties represent.

If these properties are not supplied by the Windows Vista driver, the compatibility layer in WIA service will add these properties. When these properties are added by WIA service, they will be updated using properties: WIA\_IPA\_DEPTH, WIA\_IPS\_XEXTENT, and WIA\_IPS\_YEXTENT.

**Note**   When possible, applications should always parse the image header data to get accurate information on the image. They should not rely on this property since it is not accurate.

 

 

 




