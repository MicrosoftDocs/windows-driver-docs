---
title: KSPROPERTY\_BDA\_RF\_TUNER\_FREQUENCY\_MULTIPLIER
description: Clients use KSPROPERTY\_BDA\_RF\_TUNER\_FREQUENCY\_MULTIPLIER along with KSPROPERTY\_BDA\_RF\_TUNER\_FREQUENCY to control the frequency setting of the tuner node.
ms.assetid: bca395b5-3993-42c0-880d-eb38d3b933bb
keywords: ["KSPROPERTY_BDA_RF_TUNER_FREQUENCY_MULTIPLIER Streaming Media Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_BDA_RF_TUNER_FREQUENCY_MULTIPLIER
api_location:
- Bdamedia.h
api_type:
- HeaderDef
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# KSPROPERTY\_BDA\_RF\_TUNER\_FREQUENCY\_MULTIPLIER


Clients use KSPROPERTY\_BDA\_RF\_TUNER\_FREQUENCY\_MULTIPLIER along with KSPROPERTY\_BDA\_RF\_TUNER\_FREQUENCY to control the frequency setting of the tuner node.

## <span id="ddk_ksproperty_bda_rf_tuner_frequency_multiplier_ks"></span><span id="DDK_KSPROPERTY_BDA_RF_TUNER_FREQUENCY_MULTIPLIER_KS"></span>


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

The **NodeId** member of KSP\_NODE specifies the identifier of the tuner node.

The property value specifies the frequency multiplier to set.

If the KSPROPERTY\_BDA\_RF\_TUNER\_FREQUENCY\_MULTIPLIER property specified a multiplier of BDA\_FREQUENCY\_MULTIPLIER\_NOT\_SET (−1) or BDA\_FREQUENCY\_MULTIPLIER\_NOT\_DEFINED (0), then the KSPROPERTY\_BDA\_RF\_TUNER\_FREQUENCY property specifies the frequency in kilohertz (kHz). In addition, if the minidriver's set handler ([*KStrSetPropertyHandler*](https://msdn.microsoft.com/library/windows/hardware/ff567200)) for the frequency multiplier property is not called, the minidriver must determine that the supplied frequency is expressed in units of kHz (1Hz x 1000). In effect, the default multiplier value is 1000. For more information, see [Accessing Frequency Properties of a BDA Tuner Node](https://msdn.microsoft.com/library/windows/hardware/ff554072).

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

[**KSPROPERTY\_BDA\_RF\_TUNER\_FREQUENCY**](ksproperty-bda-rf-tuner-frequency.md)

 

 






