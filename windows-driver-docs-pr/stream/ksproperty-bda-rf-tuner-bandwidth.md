---
title: KSPROPERTY\_BDA\_RF\_TUNER\_BANDWIDTH
description: Clients use KSPROPERTY\_BDA\_RF\_TUNER\_BANDWIDTH to control the bandwidth setting of the tuner node.
ms.assetid: 34feb05d-c1dc-4ce1-86bf-d7d33920befd
keywords: ["KSPROPERTY_BDA_RF_TUNER_BANDWIDTH Streaming Media Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_BDA_RF_TUNER_BANDWIDTH
api_location:
- Bdamedia.h
api_type:
- HeaderDef
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# KSPROPERTY\_BDA\_RF\_TUNER\_BANDWIDTH


Clients use KSPROPERTY\_BDA\_RF\_TUNER\_BANDWIDTH to control the bandwidth setting of the tuner node.

## <span id="ddk_ksproperty_bda_rf_tuner_bandwidth_ks"></span><span id="DDK_KSPROPERTY_BDA_RF_TUNER_BANDWIDTH_KS"></span>


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

The property value specifies the bandwidth to set. Bandwidth is the range of frequencies used to transmit a signal or group of interrelated signals. In other words, the amount of information that can be transmitted at one time.

Specifying the KSPROPERTY\_BDA\_RF\_TUNER\_BANDWIDTH property with:

-   BDA\_CHAN\_BANDWITH\_NOT\_SET (−1) indicates that the bandwidth is not set.

-   BDA\_CHAN\_BANDWITH\_NOT\_DEFINED (0) indicates that the bandwidth is not defined.

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

 

 






