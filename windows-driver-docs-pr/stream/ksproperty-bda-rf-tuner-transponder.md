---
title: KSPROPERTY\_BDA\_RF\_TUNER\_TRANSPONDER
description: Clients use KSPROPERTY\_BDA\_RF\_TUNER\_TRANSPONDER to inform the tuner node of the appropriate transponder number.
ms.assetid: 00445260-a317-4341-baab-d1391f6748e4
keywords: ["KSPROPERTY_BDA_RF_TUNER_TRANSPONDER Streaming Media Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_BDA_RF_TUNER_TRANSPONDER
api_location:
- Bdamedia.h
api_type:
- HeaderDef
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# KSPROPERTY\_BDA\_RF\_TUNER\_TRANSPONDER


Clients use KSPROPERTY\_BDA\_RF\_TUNER\_TRANSPONDER to inform the tuner node of the appropriate transponder number.

## <span id="ddk_ksproperty_bda_rf_tuner_transponder_ks"></span><span id="DDK_KSPROPERTY_BDA_RF_TUNER_TRANSPONDER_KS"></span>


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

The property value specifies the transponder number to set.

Some tuning spaces have all of the information about how to acquire a frequency imbedded in hardware. These tuning spaces specify a transponder number. This property informs the tuner node of this transponder number. The tuner hardware can then automatically determine the tuning characteristics needed to acquire the intermediate frequency. In this case, the other properties in the KSPROPSETID\_BdaFrequencyFilter property set are set to −1.

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

 

 






