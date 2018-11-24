---
title: First Encouraged Picture Decoding Configuration
description: First Encouraged Picture Decoding Configuration
ms.assetid: ad1c20a6-e070-4df0-91cd-6c2bd728e311
keywords:
- compressed picture decoding set WDK DirectX VA
- picture decoding set WDK DirectX VA
ms.date: 04/20/2017
ms.localizationpriority: medium
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

 

 

 





