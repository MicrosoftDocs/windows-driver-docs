---
title: Mapping WIA Properties with the Same IDs but Different Names
description: Mapping WIA Properties with the Same IDs but Different Names
ms.assetid: 0321db59-74a1-4294-bbaf-ec0b9317464b
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Mapping WIA Properties with the Same IDs but Different Names


There are Windows XP properties that have the same property IDs but different property names than their Windows Vista counterparts. The following is a table of these Windows XP root properties and the FLATBED and FEEDER (ADF) properties that they are translated to in Windows Vista.

<table>
<colgroup>
<col width="25%" />
<col width="25%" />
<col width="25%" />
<col width="25%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p><strong>Windows XP property</strong></p></td>
<td><p><strong>Windows XP</strong></p>
<p><strong>item / context</strong></p></td>
<td><p><strong>Windows Vista property</strong></p></td>
<td><p><strong>Windows Vista</strong> <strong>item</strong></p></td>
</tr>
<tr class="even">
<td><p>WIA_DPS_DOCUMENT_HANDLING_SELECT</p>
<p>Read/Write access See note: d</p></td>
<td><p>Root</p>
<p>See note: c</p></td>
<td><p>WIA_IPS_DOCUMENT_HANDLING_SELECT</p>
<p>Read/Write access See note: d</p></td>
<td><p>FEEDER</p>
<p>See note: a</p></td>
</tr>
<tr class="odd">
<td><p>WIA_DPS_SHEET_FEEDER_REGISTRATION</p>
<p>Read-only access</p></td>
<td><p>Root / FEEDER</p>
<p>See note: a</p></td>
<td><p>WIA_IPS_SHEET_FEEDER_REGISTRATION</p>
<p>Read-only access</p></td>
<td><p>FEEDER</p>
<p>See note: a</p></td>
</tr>
<tr class="even">
<td><p>WIA_DPS_OPTICAL_XRES</p>
<p>Read-only access</p></td>
<td><p>Root / FLATBED</p>
<p>See note: b</p></td>
<td><p>WIA_IPS_OPTICAL_XRES</p>
<p>Read-only access</p></td>
<td><p>FLATBED</p>
<p>See note: b</p></td>
</tr>
<tr class="odd">
<td><p>WIA_DPS_OPTICAL_XRES</p>
<p>Read-only access</p></td>
<td><p>Root / FEEDER</p>
<p>See note: a</p></td>
<td><p>WIA_IPS_OPTICAL_XRES</p>
<p>Read-only access</p></td>
<td><p>FEEDER</p>
<p>See note: a</p></td>
</tr>
<tr class="even">
<td><p>WIA_DPS_OPTICAL_YRES</p>
<p>Read-only access</p></td>
<td><p>Root / FLATBED</p>
<p>See note: b</p></td>
<td><p>WIA_IPS_OPTICAL_YRES</p>
<p>Read-only access</p></td>
<td><p>FLATBED</p>
<p>See note: b</p></td>
</tr>
<tr class="odd">
<td><p>WIA_DPS_OPTICAL_YRES</p>
<p>Read-only access</p></td>
<td><p>Root / FEEDER</p>
<p>See note: a</p></td>
<td><p>WIA_IPS_OPTICAL_YRES</p>
<p>Read-only access</p></td>
<td><p>FEEDER</p>
<p>See note: a</p></td>
</tr>
<tr class="even">
<td><p>WIA_DPS_PAGES</p>
<p>Read/Write access</p></td>
<td><p>Root / FEEDER</p>
<p>See note: a</p></td>
<td><p>WIA_IPS_PAGES</p>
<p>Read/Write access</p></td>
<td><p>FEEDER</p>
<p>See note: a</p></td>
</tr>
<tr class="odd">
<td><p>WIA_DPS_PAGE_SIZE</p>
<p>Read/Write access See note:e</p></td>
<td><p>Root / FEEDER</p>
<p>See note: a</p></td>
<td><p>WIA_IPS_PAGE_SIZE</p>
<p>Read/Write access See note:e</p></td>
<td><p>FEEDER</p>
<p>See note: a</p></td>
</tr>
<tr class="even">
<td><p>WIA_DPS_PAGE_WIDTH</p>
<p>Read-only access</p></td>
<td><p>Root / FEEDER</p>
<p>See note: a</p></td>
<td><p>WIA_IPS_PAGE_WIDTH</p>
<p>Read-only access</p></td>
<td><p>FEEDER</p>
<p>See note: a</p></td>
</tr>
<tr class="odd">
<td><p>WIA_DPS_PAGE_HEIGHT</p>
<p>Read-only access</p></td>
<td><p>Root / FEEDER</p>
<p>See note: a</p></td>
<td><p>WIA_IPS_PAGE_WIDTH</p>
<p>Read-only access</p></td>
<td><p>FEEDER</p>
<p>See note: a</p></td>
</tr>
<tr class="even">
<td><p>WIA_DPS_PREVIEW</p>
<p>Read/Write access</p></td>
<td><p>Root / FLATBED</p>
<p>See note: b</p></td>
<td><p>WIA_IPS_PREVIEW</p>
<p>Read-only access</p></td>
<td><p>FLATBED</p>
<p>See note: b</p></td>
</tr>
<tr class="odd">
<td><p>WIA_DPS_PREVIEW</p>
<p>Read/Write access</p></td>
<td><p>Root / FEEDER</p>
<p>See note: a</p></td>
<td><p>WIA_IPS_PREVIEW</p>
<p>Read/Write access</p></td>
<td><p>FEEDER</p>
<p>See note: a</p></td>
</tr>
<tr class="even">
<td><p>WIA_DPS_SHOW_PREVIEW_CONTROL</p>
<p>Read-only access</p></td>
<td><p>Root / FLATBED</p>
<p>See note: c</p></td>
<td><p>WIA_IPS_SHOW_PREVIEW_CONTROL</p>
<p>Read-only access</p></td>
<td><p>FLATBED</p>
<p>See note: c</p></td>
</tr>
<tr class="odd">
<td><p>WIA_DPS_SHOW_PREVIEW_CONTROL</p>
<p>Read-only access</p></td>
<td><p>Root / FEEDER</p>
<p>See note: a</p></td>
<td><p>WIA_IPS_SHOW_PREVIEW_CONTROL</p>
<p>Read-only access</p></td>
<td><p>FEEDER</p>
<p>See note: a</p></td>
</tr>
</tbody>
</table>

 

<a href="" id="note-a-"></a>Note a:  
FEEDER item (ADF) or FEEDER context on the Windows XP root or child item (WIA\_DPS\_DOCUMENT\_HANDLING\_SELECT is set to FEEDER)

<a href="" id="note-b-"></a>Note b:  
FLATBED item or FLATBED context on the Windows XP root or child item (WIA\_DPS\_DOCUMENT\_HANDLING\_SELECT is set to FLATBED)

<a href="" id="note-c-"></a>Note c:  
Root item, no context specified for Windows XP

<a href="" id="note-d-"></a>Note d:  
For Windows XP to Windows Vista translation only:

BACK\_FIRST

BACK\_ONLY

DUPLEX

FRONT\_FIRST

FRONT\_ONLY

FRONT\_ONLY is the default if this property is not implemented.

Note e:
Translate all values, not just the legacy ones (WIA\_PAGE\_CUSTOM, WIA\_PAGE\_A4, WIA\_PAGE\_LETTER)

Note that the Windows XP root item must be configured into the appropriate FLATBED/FEEDER context set (through WIA\_DPS\_DOCUMENT\_HANDLING\_SELECT) before accessing context-dependent property (both for read and write access).

 

 




