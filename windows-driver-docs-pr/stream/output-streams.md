---
title: Output Streams
author: windows-driver-content
description: Output Streams
ms.assetid: 91be637c-f195-4713-bfb0-b41c0346e390
keywords:
- output streams WDK DVD decoder
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Output Streams


## <a href="" id="ddk-output-streams-ksg"></a>


The following table describes the video port output stream media types used by DVDs:

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Attribute</th>
<th>Value</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>Major Format GUID</p></td>
<td><p>KSDATAFORMAT_TYPE_VIDEO</p></td>
</tr>
<tr class="even">
<td><p>Minor Format GUID</p></td>
<td><p>KSDATAFORMAT_SUBTYPE_VPVideo</p></td>
</tr>
<tr class="odd">
<td><p>Format Block Specifier GUID</p></td>
<td><p>KSDATAFORMAT_SPECIFIER_NULL</p>
<div>
 
</div>
No format block.</td>
</tr>
</tbody>
</table>

 

Kernel-mode interface provides control of video port extensions (VPE) settings. For more information, see [VideoPort Extensions Background](https://msdn.microsoft.com/library/windows/hardware/ff570536).

The following table describes the closed caption (CC) output stream media type used by DVDs:

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Attribute</th>
<th>Value</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>Major Format GUID</p></td>
<td><p>KSDATAFORMAT_TYPE_AUXLine21Data</p></td>
</tr>
<tr class="even">
<td><p>Minor Format GUID</p></td>
<td><p>KSDATAFORMAT_SUBTYPE_Line21_GOPPacket</p></td>
</tr>
<tr class="odd">
<td><p>Format Block Specifier GUID</p></td>
<td><p>KSDATAFORMAT_SPECIFIER_NONE</p>
<div>
 
</div>
No format block.</td>
</tr>
</tbody>
</table>

 

A frame size of 200 (decimal) in the **SampleSize** member of the [**KSDATAFORMAT**](https://msdn.microsoft.com/library/windows/hardware/ff561656) structure must be specified. For more information, see [Closed Captioning Streams](closed-captioning-streams.md).

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstream\stream%5D:%20Output%20Streams%20%20RELEASE:%20%288/23/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


