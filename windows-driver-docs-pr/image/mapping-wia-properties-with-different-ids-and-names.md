---
title: Mapping WIA Properties with Different IDs and Names
author: windows-driver-content
description: Mapping WIA Properties with Different IDs and Names
ms.assetid: e3a352fc-c817-466e-bd04-0ec8b029d500
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
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

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20Mapping%20WIA%20Properties%20with%20Different%20IDs%20and%20Names%20%20RELEASE:%20%288/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


