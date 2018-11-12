---
title: KSPROPERTY\_BDA\_LNB\_LOF\_HIGH\_BAND
description: Clients use KSPROPERTY\_BDA\_LNB\_LOF\_HIGH\_BAND to inform the RF tuner node about the local oscillator frequency (LOF) that is used by the low-noise block (LNB) device for shifting the frequency of incoming high-band RF signals.
ms.assetid: 77ee5ad8-330e-47a6-8fdb-6a4f9b3eef1d
keywords: ["KSPROPERTY_BDA_LNB_LOF_HIGH_BAND Streaming Media Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_BDA_LNB_LOF_HIGH_BAND
api_location:
- Bdamedia.h
api_type:
- HeaderDef
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# KSPROPERTY\_BDA\_LNB\_LOF\_HIGH\_BAND


Clients use KSPROPERTY\_BDA\_LNB\_LOF\_HIGH\_BAND to inform the RF tuner node about the local oscillator frequency (LOF) that is used by the low-noise block (LNB) device for shifting the frequency of incoming high-band RF signals.

## <span id="ddk_ksproperty_bda_lnb_lof_high_band_ks"></span><span id="DDK_KSPROPERTY_BDA_LNB_LOF_HIGH_BAND_KS"></span>


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
<td><p>ULONG</p></td>
</tr>
</tbody>
</table>

 

Remarks
-------

The **NodeId** member of KSP\_NODE specifies the identifier of the RF tuner node.

The property value specifies the LOF that is used by the LNB for high-band signals.

The LNB gathers the RF signal reflected by the satellite dish, shifts the frequency of the RF signal down by the high-band LOF amount, and sends the resulting signal to the RF tuner.

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


[**KSP\_NODE**](https://msdn.microsoft.com/library/windows/hardware/ff566720)

 

 






