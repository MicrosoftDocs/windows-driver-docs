---
title: Seventh Picture Decoding Configuration
description: Seventh Picture Decoding Configuration
keywords:
- compressed picture decoding set WDK DirectX VA
- picture decoding set WDK DirectX VA
ms.date: 04/20/2017
---

# Seventh Picture Decoding Configuration


## <span id="ddk_seventh_picture_decoding_configuration_gg"></span><span id="DDK_SEVENTH_PICTURE_DECODING_CONFIGURATION_GG"></span>


The seventh configuration in this set is defined only for the [MPEG2\_C](mpeg2-c.md) and [MPEG2\_D](mpeg2-d.md) restricted profiles indicated in the [**DXVA\_ConnectMode**](/windows-hardware/drivers/ddi/dxva/ns-dxva-_dxva_connectmode) structure. No other restricted profiles include this configuration in their minimal interoperability set.

This configuration (which is not a preferred configuration) is defined the same way as the [first picture decoding configuration](first-picture-decoding-configuration.md) with the following exceptions.

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
<td align="left"><p><strong>bConfigResidDiffHost</strong></p></td>
<td align="left"><p>Zero</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>bConfigResidDiffAccelerator</strong></p></td>
<td align="left"><p>1</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>bConfig4GroupedCoefs</strong></p></td>
<td align="left"><p>1</p></td>
</tr>
</tbody>
</table>

 

 

