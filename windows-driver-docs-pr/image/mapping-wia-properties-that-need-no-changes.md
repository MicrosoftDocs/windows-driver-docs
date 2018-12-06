---
title: Mapping WIA Properties That Need No Changes
description: Mapping WIA Properties That Need No Changes
ms.assetid: ceb0fe83-9803-4ba5-9a9f-7c722389db0b
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Mapping WIA Properties That Need No Changes


There are Windows XP properties that have the same property IDs and property names as their Windows Vista counterparts. These properties are translated with appropriate Windows XP context selection only; there are no other changes. The following is a table of these Windows XP root properties and the FLATBED and FEEDER (ADF) properties that they are translated to in Windows Vista.

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
<td><p><strong>Windows XP item / context</strong></p></td>
<td><p><strong>Windows Vista property</strong></p></td>
<td><p><strong>Windows Vista</strong> <strong>item</strong></p></td>
</tr>
<tr class="even">
<td><p>WIA_IPS_CUR_INTENT</p>
<p>Read/Write access</p></td>
<td><p>Child / FLATBED</p>
<p>See note: b</p></td>
<td><p>WIA_IPS_CUR_INTENT</p>
<p>Read/Write access</p></td>
<td><p>FLATBED</p>
<p>See note: b</p></td>
</tr>
<tr class="odd">
<td><p>WIA_IPS_CUR_INTENT</p>
<p>Read/Write access</p></td>
<td><p>Child / FEEDER</p>
<p>See note: a</p></td>
<td><p>WIA_IPS_CUR_INTENT</p>
<p>Read/Write access</p></td>
<td><p>FEEDER</p>
<p>See note: a</p></td>
</tr>
<tr class="even">
<td><p>WIA_IPS_XRES</p>
<p>Read/Write access</p></td>
<td><p>Child / FLATBED</p>
<p>See note: b</p></td>
<td><p>WIA_IPS_XRES</p>
<p>Read/Write access</p></td>
<td><p>FLATBED</p>
<p>See note: b</p></td>
</tr>
<tr class="odd">
<td><p>WIA_IPS_XRES</p>
<p>Read/Write access</p></td>
<td><p>Child / FEEDER</p>
<p>See note: a</p></td>
<td><p>WIA_IPS_XRES</p>
<p>Read/Write access</p></td>
<td><p>FEEDER</p>
<p>See note: a</p></td>
</tr>
<tr class="even">
<td><p>WIA_IPS_YRES</p>
<p>Read/Write access</p></td>
<td><p>Child / FLATBED</p>
<p>See note: b</p></td>
<td><p>WIA_IPS_YRES</p>
<p>Read/Write access</p></td>
<td><p>FLATBED</p>
<p>See note: b</p></td>
</tr>
<tr class="odd">
<td><p>WIA_IPS_YRES</p>
<p>Read/Write access</p></td>
<td><p>Child / FEEDER</p>
<p>See note: a</p></td>
<td><p>WIA_IPS_YRES</p>
<p>Read/Write access</p></td>
<td><p>FEEDER</p>
<p>See note: a</p></td>
</tr>
<tr class="even">
<td><p>WIA_IPS_XPOS</p>
<p>Read/Write access</p></td>
<td><p>Child / FLATBED</p>
<p>See note: b</p></td>
<td><p>WIA_IPS_XPOS</p>
<p>Read/Write access</p></td>
<td><p>FLATBED</p>
<p>See note: b</p></td>
</tr>
<tr class="odd">
<td><p>WIA_IPS_XPOS</p>
<p>Read/Write access</p></td>
<td><p>Child / FEEDER</p>
<p>See note: a</p></td>
<td><p>WIA_IPS_XPOS</p>
<p>Read/Write access</p></td>
<td><p>FEEDER</p>
<p>See note: a</p></td>
</tr>
<tr class="even">
<td><p>WIA_IPS_YPOS</p>
<p>Read/Write access</p></td>
<td><p>Child / FLATBED</p>
<p>See note: b</p></td>
<td><p>WIA_IPS_YPOS</p>
<p>Read/Write access</p></td>
<td><p>FLATBED</p>
<p>See note: b</p></td>
</tr>
<tr class="odd">
<td><p>WIA_IPS_YPOS</p>
<p>Read/Write access</p></td>
<td><p>Child / FEEDER</p>
<p>See note: a</p></td>
<td><p>WIA_IPS_YPOS</p>
<p>Read/Write access</p></td>
<td><p>FEEDER</p>
<p>See note: a</p></td>
</tr>
<tr class="even">
<td><p>WIA_IPS_XEXTENT</p>
<p>Read/Write access</p></td>
<td><p>Child / FLATBED</p>
<p>See note: b</p></td>
<td><p>WIA_IPS_XEXTENT</p>
<p>Read/Write access</p></td>
<td><p>FLATBED</p>
<p>See note: b</p></td>
</tr>
<tr class="odd">
<td><p>WIA_IPS_XEXTENT</p>
<p>Read/Write access</p></td>
<td><p>Child / FEEDER</p>
<p>See note: a</p></td>
<td><p>WIA_IPS_XEXTENT</p>
<p>Read/Write access</p></td>
<td><p>FEEDER</p>
<p>See note: a</p></td>
</tr>
<tr class="even">
<td><p>WIA_IPS_YEXTENT</p>
<p>Read/Write access</p></td>
<td><p>Child / FLATBED</p>
<p>See note: b</p></td>
<td><p>WIA_IPS_YEXTENT</p>
<p>Read/Write access</p></td>
<td><p>FLATBED</p>
<p>See note: b</p></td>
</tr>
<tr class="odd">
<td><p>WIA_IPS_YEXTENT</p>
<p>Read/Write access</p></td>
<td><p>Child / FEEDER</p>
<p>See note: a</p></td>
<td><p>WIA_IPS_YEXTENT</p>
<p>Read/Write access</p></td>
<td><p>FEEDER</p>
<p>See note: a</p></td>
</tr>
<tr class="even">
<td><p>WIA_IPS_PHOTOMETRIC_INTERP</p>
<p>Read/Write access</p></td>
<td><p>Child / FLATBED</p>
<p>See note: b</p></td>
<td><p>WIA_IPS_PHOTOMETRIC_INTERP</p>
<p>Read/Write access</p></td>
<td><p>FLATBED</p>
<p>See note: b</p></td>
</tr>
<tr class="odd">
<td><p>WIA_IPS_PHOTOMETRIC_INTERP</p>
<p>Read/Write access</p></td>
<td><p>Child / FEEDER</p>
<p>See note: a</p></td>
<td><p>WIA_IPS_PHOTOMETRIC_INTERP</p>
<p>Read/Write access</p></td>
<td><p>FEEDER</p>
<p>See note: a</p></td>
</tr>
<tr class="even">
<td><p>WIA_IPS_BRIGHTNESS</p>
<p>Read/Write access</p></td>
<td><p>Child / FLATBED</p>
<p>See note: b</p></td>
<td><p>WIA_IPS_BRIGHTNESS</p>
<p>Read/Write access</p></td>
<td><p>FLATBED</p>
<p>See note: b</p></td>
</tr>
<tr class="odd">
<td><p>WIA_IPS_BRIGHTNESS</p>
<p>Read/Write access</p></td>
<td><p>Child / FEEDER</p>
<p>See note: a</p></td>
<td><p>WIA_IPS_BRIGHTNESS</p>
<p>Read/Write access</p></td>
<td><p>FEEDER</p>
<p>See note: a</p></td>
</tr>
<tr class="even">
<td><p>WIA_IPS_CONTRAST</p>
<p>Read/Write access</p></td>
<td><p>Child / FLATBED</p>
<p>See note: b</p></td>
<td><p>WIA_IPS_CONTRAST</p>
<p>Read/Write access</p></td>
<td><p>FLATBED</p>
<p>See note: b</p></td>
</tr>
<tr class="odd">
<td><p>WIA_IPS_CONTRAST</p>
<p>Read/Write access</p></td>
<td><p>Child / FEEDER</p>
<p>See note: a</p></td>
<td><p>WIA_IPS_CONTRAST</p>
<p>Read/Write access</p></td>
<td><p>FEEDER</p>
<p>See note: a</p></td>
</tr>
<tr class="even">
<td><p>WIA_IPS_ORIENTATION</p>
<p>Read/Write access</p></td>
<td><p>Child / FLATBED</p>
<p>See note: b</p></td>
<td><p>WIA_IPS_ORIENTATION</p>
<p>Read/Write access</p></td>
<td><p>FLATBED</p>
<p>See note: b</p></td>
</tr>
<tr class="odd">
<td><p>WIA_IPS_ORIENTATION</p>
<p>Read/Write access</p></td>
<td><p>Child / FEEDER</p>
<p>See note: a</p></td>
<td><p>WIA_IPS_ORIENTATION</p>
<p>Read/Write access</p></td>
<td><p>FEEDER</p>
<p>See note: a</p></td>
</tr>
<tr class="even">
<td><p>WIA_IPS_ROTATION</p>
<p>Read/Write access</p></td>
<td><p>Child / FLATBED</p>
<p>See note: b</p></td>
<td><p>WIA_IPS_ROTATION</p>
<p>Read/Write access</p></td>
<td><p>FLATBED</p>
<p>See note: b</p></td>
</tr>
<tr class="odd">
<td><p>WIA_IPS_ROTATION</p>
<p>Read/Write access</p></td>
<td><p>Child / FEEDER</p>
<p>See note: a</p></td>
<td><p>WIA_IPS_ROTATION</p>
<p>Read/Write access</p></td>
<td><p>FEEDER</p>
<p>See note: a</p></td>
</tr>
<tr class="even">
<td><p>WIA_IPS_THRESHOLD</p>
<p>Read/Write access</p></td>
<td><p>Child / FLATBED</p>
<p>See note: b</p></td>
<td><p>WIA_IPS_THRESHOLD</p>
<p>Read/Write access</p></td>
<td><p>FLATBED</p>
<p>See note: b</p></td>
</tr>
<tr class="odd">
<td><p>WIA_IPS_THRESHOLD</p>
<p>Read/Write access</p></td>
<td><p>Child / FEEDER</p>
<p>See note: a</p></td>
<td><p>WIA_IPS_THRESHOLD</p>
<p>Read/Write access</p></td>
<td><p>FEEDER</p>
<p>See note: a</p></td>
</tr>
<tr class="even">
<td><p>WIA_IPS_WARM_UP_TIME</p>
<p>Read-only access</p></td>
<td><p>Child / FLATBED</p>
<p>See note: b</p></td>
<td><p>WIA_IPS_WARM_UP_TIME</p>
<p>Read-only access</p></td>
<td><p>FLATBED</p>
<p>See note: b</p></td>
</tr>
<tr class="odd">
<td><p>WIA_IPS_WARM_UP_TIME</p>
<p>Read-only access</p></td>
<td><p>Child / FEEDER</p>
<p>See note: a</p></td>
<td><p>WIA_IPS_WARM_UP_TIME</p>
<p>Read-only access</p></td>
<td><p>FEEDER</p>
<p>See note: a</p></td>
</tr>
</tbody>
</table>

 

<a href="" id="note-a-"></a>Note a:  
FEEDER item (ADF) or FEEDER context on the Windows XP root or child item (WIA\_DPS\_DOCUMENT\_HANDLING\_SELECT is set to FEEDER).

<a href="" id="note-b-"></a>Note b:  
FLATBED item or FLATBED context on the Windows XP root or child item (WIA\_DPS\_DOCUMENT\_HANDLING\_SELECT is set to FLATBED).

 

 




