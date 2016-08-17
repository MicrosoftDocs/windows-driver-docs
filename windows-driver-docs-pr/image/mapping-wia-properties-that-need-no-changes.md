---
title: Mapping WIA Properties That Need No Changes
description: Mapping WIA Properties That Need No Changes
MS-HAID:
- 'WIA\_Fundamentals\_aeb28af3-0b7e-408a-b03b-b5f1a756776f.xml'
- 'image.mapping\_wia\_properties\_that\_need\_no\_changes'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: ceb0fe83-9803-4ba5-9a9f-7c722389db0b
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20Mapping%20WIA%20Properties%20That%20Need%20No%20Changes%20%20RELEASE:%20%288/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




