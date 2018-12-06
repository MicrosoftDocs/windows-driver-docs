---
title: Mapping WIA Properties with Different IDs and Names
description: Mapping WIA Properties with Different IDs and Names
ms.assetid: e3a352fc-c817-466e-bd04-0ec8b029d500
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Mapping WIA Properties with Different IDs and Names


There are Windows XP properties that have different property IDs and different property names from their Windows Vista counterparts. The following is a table of these Windows XP root properties and the FLATBED and FEEDER (ADF) properties that they are translated to in Windows Vista.

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
<p><strong>item/context</strong></p></td>
<td><p><strong>Windows Vista property</strong></p></td>
<td><p><strong>Windows Vista</strong> <strong>item</strong></p></td>
</tr>
<tr class="even">
<td><p>WIA_DPS_HORIZONTAL_BED_SIZE</p>
<p>Read-only access</p></td>
<td><p>Root</p>
<p>See note: a</p></td>
<td><p>WIA_IPS_MAX_HORIZONTAL_SIZE</p>
<p>Read-only access</p></td>
<td><p>FLATBED</p>
<p>See note: b</p></td>
</tr>
<tr class="odd">
<td><p>WIA_DPS_VERTICAL_BED_SIZE</p>
<p>Read-only access</p></td>
<td><p>Root</p>
<p>See note: a</p></td>
<td><p>WIA_IPS_MAX_VERTICAL_SIZE</p>
<p>Read-only access</p></td>
<td><p>FLATBED</p>
<p>See note: b</p></td>
</tr>
<tr class="even">
<td><p>WIA_DPS_HORIZONTAL_SHEET_FEED_SIZE</p>
<p>Read-only access</p></td>
<td><p>Root</p>
<p>See note: a</p></td>
<td><p>WIA_IPS_MAX_HORIZONTAL_SIZE</p>
<p>Read-only access</p></td>
<td><p>FEEDER</p>
<p>See note: c</p></td>
</tr>
<tr class="odd">
<td><p>WIA_DPS_VERTICAL_SHEET_FEED_SIZE</p>
<p>Read-only access</p></td>
<td><p>Root</p>
<p>See note: a</p></td>
<td><p>WIA_IPS_MAX_HORIZONTAL_SIZE</p>
<p>Read-only access</p></td>
<td><p>FEEDER</p>
<p>See note: c</p></td>
</tr>
<tr class="even">
<td><p>WIA_DPS_MIN_HORIZONTAL_SHEET_FEED_SIZE</p>
<p>Read-only access</p></td>
<td><p>Root</p>
<p>See note: a</p></td>
<td><p>WIA_IPS_MIN_HORIZONTAL_SIZE</p>
<p>Read-only access</p></td>
<td><p>FEEDER</p>
<p>See note: c</p></td>
</tr>
<tr class="odd">
<td><p>WIA_DPS_MIN_VERTICAL_SHEET_FEED_SIZE</p>
<p>Read-only access</p></td>
<td><p>Root</p>
<p>See note: a</p></td>
<td><p>WIA_IPS_MIN_VERTICAL_SIZE</p>
<p>Read-only access</p></td>
<td><p>FEEDER</p>
<p>See note: c</p></td>
</tr>
<tr class="even">
<td><p>Generic value: 1</p></td>
<td><p>NA</p></td>
<td><p>WIA_IPS_MIN_HORIZONTAL_SIZE</p>
<p>Read-only access</p></td>
<td><p>FLATBED</p>
<p>See note: c</p></td>
</tr>
<tr class="odd">
<td><p>Generic value: 1</p></td>
<td><p>NA</p></td>
<td><p>WIA_IPS_MIN_VERTICAL_SIZE</p>
<p>Read-only access</p></td>
<td><p>FLATBED</p>
<p>See note: c</p></td>
</tr>
</tbody>
</table>

 

<a href="" id="note-a-"></a>Note a:  
Root item, no context specified for Windows XP

<a href="" id="note-b-"></a>Note b:  
FLATBED item or FLATBED context on the Windows XP root or child item (WIA\_DPS\_DOCUMENT\_HANDLING\_SELECT is set to FLATBED)

<a href="" id="note-c-"></a>Note c:  
FEEDER item (ADF) or FEEDER context on the Windows XP root or child item (WIA\_DPS\_DOCUMENT\_HANDLING\_SELECT is set to FEEDER)

 

 




