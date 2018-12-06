---
title: KSPROPERTY\_BDA\_LNB\_SWITCH\_FREQUENCY
description: Clients use KSPROPERTY\_BDA\_LNB\_SWITCH\_FREQUENCY to inform the RF tuner node about the frequency of incoming RF signals at which the tuner should inform the low-noise block (LNB) device to switch from using low-band local oscillator frequency (LOF) to using high-band LOF or vice versa when the LNB shifts the frequency of RF signals.
ms.assetid: a448bad1-40dc-4596-bc18-9522144e33a7
keywords: ["KSPROPERTY_BDA_LNB_SWITCH_FREQUENCY Streaming Media Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_BDA_LNB_SWITCH_FREQUENCY
api_location:
- Bdamedia.h
api_type:
- HeaderDef
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# KSPROPERTY\_BDA\_LNB\_SWITCH\_FREQUENCY


Clients use KSPROPERTY\_BDA\_LNB\_SWITCH\_FREQUENCY to inform the RF tuner node about the frequency of incoming RF signals at which the tuner should inform the low-noise block (LNB) device to switch from using low-band local oscillator frequency (LOF) to using high-band LOF or vice versa when the LNB shifts the frequency of RF signals.

## <span id="ddk_ksproperty_bda_lnb_switch_frequency_ks"></span><span id="DDK_KSPROPERTY_BDA_LNB_SWITCH_FREQUENCY_KS"></span>


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

The property value specifies the frequency of incoming RF signals at which the LNB should switch from using low-band LOF to using high-band LOF.

If a client sends a KSPROPERTY\_BDA\_RF\_TUNER\_FREQUENCY request to tune an RF tuner to a specific frequency and this frequency is greater than or equal to the switch frequency specified using KSPROPERTY\_BDA\_LNB\_SWITCH\_FREQUENCY, then the RF tuner should send a command to the LNB to switch to the high-band LOF. The RF tuner should then expect that the LNB device shifts the frequency of the incoming RF signal by the high-band LOF amount, which was specified using KSPROPERTY\_BDA\_LNB\_LOF\_HIGH\_BAND.

Likewise, if a client sends a KSPROPERTY\_BDA\_RF\_TUNER\_FREQUENCY request to tune an RF tuner to a specific frequency and this frequency is less than the switch frequency, then the RF tuner should send a command to the LNB to switch to the low-band LOF. The RF tuner should then expect that the LNB device shifts the frequency of the incoming RF signal by the low-band LOF amount, which was specified using KSPROPERTY\_BDA\_LNB\_LOF\_LOW\_BAND.

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

[**KSPROPERTY\_BDA\_LNB\_LOF\_HIGH\_BAND**](ksproperty-bda-lnb-lof-high-band.md)

[**KSPROPERTY\_BDA\_LNB\_LOF\_LOW\_BAND**](ksproperty-bda-lnb-lof-low-band.md)

[**KSPROPERTY\_BDA\_RF\_TUNER\_FREQUENCY**](ksproperty-bda-rf-tuner-frequency.md)

 

 






