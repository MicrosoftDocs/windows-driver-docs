---
title: KSPROPERTY\_BDA\_RF\_TUNER\_RANGE
description: Clients use KSPROPERTY\_BDA\_RF\_TUNER\_RANGE to control the tuner range, that is, the domain on which to find a particular carrier frequency.
ms.assetid: 2f2aa515-3f3c-419f-a817-0d597466ec85
keywords: ["KSPROPERTY_BDA_RF_TUNER_RANGE Streaming Media Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_BDA_RF_TUNER_RANGE
api_location:
- Bdamedia.h
api_type:
- HeaderDef
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# KSPROPERTY\_BDA\_RF\_TUNER\_RANGE


Clients use KSPROPERTY\_BDA\_RF\_TUNER\_RANGE to control the tuner range, that is, the domain on which to find a particular carrier frequency.

## <span id="ddk_ksproperty_bda_rf_tuner_range_ks"></span><span id="DDK_KSPROPERTY_BDA_RF_TUNER_RANGE_KS"></span>


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

The property value specifies the tuner range to set.

Specifying the KSPROPERTY\_BDA\_RF\_TUNER\_RANGE property with:

-   BDA\_RANGE\_NOT\_SET (−1) indicates that the tuner range is not set.

-   BDA\_RANGE\_NOT\_DEFINED (0) indicates that the tuner range is not defined.

Some tuners control an external device, such as a multiswitch, that defines the domain on which to find a particular carrier frequency. This property sets the tuner range either to −1, meaning that tuner range is not used for the particular tuning space, or to a value that is specific to the tuning space.

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

 

 






