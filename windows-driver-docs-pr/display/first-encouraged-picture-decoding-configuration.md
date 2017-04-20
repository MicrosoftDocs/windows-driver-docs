---
title: First Encouraged Picture Decoding Configuration
description: First Encouraged Picture Decoding Configuration
ms.assetid: ad1c20a6-e070-4df0-91cd-6c2bd728e311
keywords:
- compressed picture decoding set WDK DirectX VA
- picture decoding set WDK DirectX VA
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# First Encouraged Picture Decoding Configuration


## <span id="ddk_first_encouraged_picture_decoding_configuration_gg"></span><span id="DDK_FIRST_ENCOURAGED_PICTURE_DECODING_CONFIGURATION_GG"></span>


The first encouraged configuration is for improved support of off-host bitstream processing acceleration.

This configuration is defined the same way as the [first picture decoding configuration](first-picture-decoding-configuration.md) with the following exceptions.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Member</th>
<th align="left">Value</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p><strong>bConfigBitstreamRaw</strong></p></td>
<td align="left"><p>1</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>bConfigMBcontrolRasterOrder</strong></p></td>
<td align="left"><p>Zero</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>bConfigResidDiffHost</strong></p></td>
<td align="left"><p>Zero</p></td>
</tr>
</tbody>
</table>

 

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20First%20Encouraged%20Picture%20Decoding%20Configuration%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




