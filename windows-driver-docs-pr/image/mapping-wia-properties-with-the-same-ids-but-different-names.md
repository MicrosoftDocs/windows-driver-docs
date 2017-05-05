---
title: Mapping WIA Properties with the Same IDs but Different Names
author: windows-driver-content
description: Mapping WIA Properties with the Same IDs but Different Names
ms.assetid: 0321db59-74a1-4294-bbaf-ec0b9317464b
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
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

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20Mapping%20WIA%20Properties%20with%20the%20Same%20IDs%20but%20Different%20Names%20%20RELEASE:%20%288/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


