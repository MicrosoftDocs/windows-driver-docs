---
title: KSPROPERTY\_BDA\_LNB\_LOF\_LOW\_BAND
description: Clients use KSPROPERTY\_BDA\_LNB\_LOF\_LOW\_BAND to inform the RF tuner node about the local oscillator frequency (LOF) that is used by the low-noise block (LNB) device for shifting the frequency of incoming low-band RF signals.
ms.assetid: 96880a70-5c3f-4391-a613-a6a90d1605b4
keywords: ["KSPROPERTY_BDA_LNB_LOF_LOW_BAND Streaming Media Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_BDA_LNB_LOF_LOW_BAND
api_location:
- Bdamedia.h
api_type:
- HeaderDef
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# KSPROPERTY\_BDA\_LNB\_LOF\_LOW\_BAND


Clients use KSPROPERTY\_BDA\_LNB\_LOF\_LOW\_BAND to inform the RF tuner node about the local oscillator frequency (LOF) that is used by the low-noise block (LNB) device for shifting the frequency of incoming low-band RF signals.

## <span id="ddk_ksproperty_bda_lnb_lof_low_band_ks"></span><span id="DDK_KSPROPERTY_BDA_LNB_LOF_LOW_BAND_KS"></span>


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

The property value specifies the LOF that is used by the LNB for low-band signals.

The LNB gathers the RF signal reflected by the satellite dish, shifts the frequency of the RF signal down by the low-band LOF amount, and sends the resulting signal to the RF tuner.

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

 

 






