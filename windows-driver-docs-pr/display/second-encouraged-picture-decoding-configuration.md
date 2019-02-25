---
title: Second Encouraged Picture Decoding Configuration
description: Second Encouraged Picture Decoding Configuration
ms.assetid: 9e259768-4588-4a5b-b01b-fca0021cd966
keywords:
- compressed picture decoding set WDK DirectX VA
- picture decoding set WDK DirectX VA
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Second Encouraged Picture Decoding Configuration


## <span id="ddk_second_encouraged_picture_decoding_configuration_gg"></span><span id="DDK_SECOND_ENCOURAGED_PICTURE_DECODING_CONFIGURATION_GG"></span>


The second encouraged configuration provides improved support of off-host IDCT acceleration. Accelerators that implement the first configuration in this set should support the second one. Implementing support for both configurations provides flexibility in the manner in which their acceleration capabilities can be used.

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
<td align="left"><p><strong>bConfigMBcontrolRasterOrder</strong></p></td>
<td align="left"><p>Zero</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>bConfigResidDiffHost</strong></p></td>
<td align="left"><p>Zero</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>bConfigResidDiffAccelerator</strong></p></td>
<td align="left"><p>1</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>bConfigHostInverseScan</strong></p></td>
<td align="left"><p>1</p></td>
</tr>
</tbody>
</table>

 

 

 





