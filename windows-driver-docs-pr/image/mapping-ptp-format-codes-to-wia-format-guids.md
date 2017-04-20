---
title: Mapping PTP Format Codes to WIA Format GUIDs
author: windows-driver-content
description: Mapping PTP Format Codes to WIA Format GUIDs
ms.assetid: a69269c0-1474-4de5-9a08-94902ef1f089
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Mapping PTP Format Codes to WIA Format GUIDs


## <a href="" id="ddk-mapping-ptp-format-codes-to-wia-format-guids-si"></a>


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
<td><p>See [Mapping PTP Associations to WIA Folders](mapping-ptp-associations-to-wia-folders.md).</p></td>
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

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20Mapping%20PTP%20Format%20Codes%20to%20WIA%20Format%20GUIDs%20%20RELEASE:%20%288/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


