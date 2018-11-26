---
title: Mapping PTP Format Codes to WIA Format GUIDs
description: Mapping PTP Format Codes to WIA Format GUIDs
ms.assetid: a69269c0-1474-4de5-9a08-94902ef1f089
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Mapping PTP Format Codes to WIA Format GUIDs





The format of an object is exposed through the [**WIA\_IPA\_FORMAT**](https://msdn.microsoft.com/library/windows/hardware/ff551553) property as a GUID. The mapping between PTP format codes and WIA GUIDs is shown in the following table:

<table>
<colgroup>
<col width="33%" />
<col width="33%" />
<col width="33%" />
</colgroup>
<thead>
<tr class="header">
<th>PTP Format Code</th>
<th>Object Type</th>
<th>WIA GUID</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>0x3000</p></td>
<td><p>Undefined</p></td>
<td><p>Not applicable.</p></td>
</tr>
<tr class="even">
<td><p>0x3001</p></td>
<td><p>Association</p></td>
<td><p>See <a href="mapping-ptp-associations-to-wia-folders.md" data-raw-source="[Mapping PTP Associations to WIA Folders](mapping-ptp-associations-to-wia-folders.md)">Mapping PTP Associations to WIA Folders</a>.</p></td>
</tr>
<tr class="odd">
<td><p>0x3002</p></td>
<td><p>Script</p></td>
<td><p>DATAFMT_SCRIPT</p></td>
</tr>
<tr class="even">
<td><p>0x3003</p></td>
<td><p>Executable</p></td>
<td><p>DATAFMT_EXEC</p></td>
</tr>
<tr class="odd">
<td><p>0x3004</p></td>
<td><p>Text</p></td>
<td><p>DATAFMT_UNICODE16</p></td>
</tr>
<tr class="even">
<td><p>0x3005</p></td>
<td><p>HTML</p></td>
<td><p>DATAFMT_HTML</p></td>
</tr>
<tr class="odd">
<td><p>0x3006</p></td>
<td><p>DPOF</p></td>
<td><p>DATAFMT_DPOF</p></td>
</tr>
<tr class="even">
<td><p>0x3007</p></td>
<td><p>AIFF</p></td>
<td><p>AUDFMT_AIFF</p></td>
</tr>
<tr class="odd">
<td><p>0x3008</p></td>
<td><p>WAV</p></td>
<td><p>AUDFMT_WAV</p></td>
</tr>
<tr class="even">
<td><p>0x3009</p></td>
<td><p>MP3</p></td>
<td><p>AUDFMT_MP3</p></td>
</tr>
<tr class="odd">
<td><p>0x300A</p></td>
<td><p>AVI</p></td>
<td><p>VIDFMT_AVI</p></td>
</tr>
<tr class="even">
<td><p>0x300B</p></td>
<td><p>MPEG</p></td>
<td><p>VIDFMT_MPEG</p></td>
</tr>
<tr class="odd">
<td><p>0x300C</p></td>
<td><p>ASF</p></td>
<td><p>VIDFMT_ASF</p></td>
</tr>
<tr class="even">
<td><p>0x3800</p></td>
<td><p>Undefined image</p></td>
<td><p>Not applicable.</p></td>
</tr>
<tr class="odd">
<td><p>0x3801</p></td>
<td><p>EXIF/JPEG</p></td>
<td><p>WiaImgFmt_JPEG</p></td>
</tr>
<tr class="even">
<td><p>0x3802</p></td>
<td><p>TIFF/EP</p></td>
<td><p>WiaImgFmt_TIFF</p></td>
</tr>
<tr class="odd">
<td><p>0x3803</p></td>
<td><p>FlashPix</p></td>
<td><p>WiaImgFmt_FLASHPIX</p></td>
</tr>
<tr class="even">
<td><p>0x3804</p></td>
<td><p>BMP</p></td>
<td><p>WiaImgFmt_BMP</p></td>
</tr>
<tr class="odd">
<td><p>0x3805</p></td>
<td><p>CIFF</p></td>
<td><p>WiaImgFmt_CIFF</p></td>
</tr>
<tr class="even">
<td><p>0x3806</p></td>
<td><p>Undefined (Reserved)</p></td>
<td><p>Not applicable.</p></td>
</tr>
<tr class="odd">
<td><p>0x3807</p></td>
<td><p>GIF</p></td>
<td><p>WiaImgFmt_GIF</p></td>
</tr>
<tr class="even">
<td><p>0x3808</p></td>
<td><p>JFIF</p></td>
<td><p>WiaImgFmt_JPEG</p></td>
</tr>
<tr class="odd">
<td><p>0x3809</p></td>
<td><p>PCD (PhotoCD Image Pac)</p></td>
<td><p>WiaImgFmt_PHOTOCD</p></td>
</tr>
<tr class="even">
<td><p>0x380A</p></td>
<td><p>PICT</p></td>
<td><p>WiaImgFmt_PICT</p></td>
</tr>
<tr class="odd">
<td><p>0x380B</p></td>
<td><p>PNG</p></td>
<td><p>WiaImgFmt_PNG</p></td>
</tr>
<tr class="even">
<td><p>0x380C</p></td>
<td><p>Undefined (Reserved)</p></td>
<td><p>Not applicable.</p></td>
</tr>
<tr class="odd">
<td><p>0x380D</p></td>
<td><p>TIFF</p></td>
<td><p>WiaImgFmt_TIFF</p></td>
</tr>
<tr class="even">
<td><p>0x380E</p></td>
<td><p>TIFF/IT</p></td>
<td><p>WiaImgFmt_TIFF</p></td>
</tr>
<tr class="odd">
<td><p>0x380F</p></td>
<td><p>JPEG2000 Baseline</p></td>
<td><p>WiaImgFmt_JPEG2K</p></td>
</tr>
<tr class="even">
<td><p>0x3810</p></td>
<td><p>JPEG2000 Extended</p></td>
<td><p>WiaImgFmt_JPEG2KX</p></td>
</tr>
</tbody>
</table>

 

(The WiaImgFmt\_XXX GUIDs are defined in *wiadef.h*.)

 

 




