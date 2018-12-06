---
title: KSPROPERTY\_BDA\_INNER\_FEC\_RATE
description: Clients use KSPROPERTY\_BDA\_INNER\_FEC\_RATE to control the binary convolution scheme used for the inner forward error correction (FEC) type of a demodulator node.
ms.assetid: d5bf0ce0-d383-431f-85de-3d00f4831619
keywords: ["KSPROPERTY_BDA_INNER_FEC_RATE Streaming Media Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_BDA_INNER_FEC_RATE
api_location:
- Bdamedia.h
api_type:
- HeaderDef
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# KSPROPERTY\_BDA\_INNER\_FEC\_RATE


Clients use KSPROPERTY\_BDA\_INNER\_FEC\_RATE to control the binary convolution scheme used for the inner forward error correction (FEC) type of a demodulator node.

## <span id="ddk_ksproperty_bda_inner_fec_rate_ks"></span><span id="DDK_KSPROPERTY_BDA_INNER_FEC_RATE_KS"></span>


### Usage Summary Table

<table>
<colgroup>
<col width="20%" />
<col width="20%" />
<col width="20%" />
<col width="20%" />
<col width="20%" />
</colgroup>
<thead>
<tr class="header">
<th>Get</th>
<th>Set</th>
<th>Target</th>
<th>Property descriptor type</th>
<th>Property value type</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>Yes</p></td>
<td><p>Yes</p></td>
<td><p>Filter</p></td>
<td><p>KSP_NODE</p></td>
<td><p>BinaryConvolutionCodeRate</p></td>
</tr>
</tbody>
</table>

 

Remarks
-------

The returned value from the BinaryConvolutionCodeRate enumerated type identifies a binary convolution scheme.

The **NodeId** member of KSP\_NODE specifies the identifier of the demodulator node.

Requirements
------------

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Header</p></td>
<td>Bdamedia.h (include Bdamedia.h)</td>
</tr>
</tbody>
</table>

## See also


[**BinaryConvolutionCodeRate**](https://msdn.microsoft.com/library/windows/hardware/ff556566)

[**KSP\_NODE**](https://msdn.microsoft.com/library/windows/hardware/ff566720)

 

 






