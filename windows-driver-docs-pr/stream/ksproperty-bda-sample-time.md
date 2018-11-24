---
title: KSPROPERTY\_BDA\_SAMPLE\_TIME
description: Clients use KSPROPERTY\_BDA\_SAMPLE\_TIME to determine the sample time over which signal level and quality are averaged.
ms.assetid: 53252e11-2a18-42d5-aed8-99052a2b0f21
keywords: ["KSPROPERTY_BDA_SAMPLE_TIME Streaming Media Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_BDA_SAMPLE_TIME
api_location:
- Bdamedia.h
api_type:
- HeaderDef
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# KSPROPERTY\_BDA\_SAMPLE\_TIME


Clients use KSPROPERTY\_BDA\_SAMPLE\_TIME to determine the sample time over which signal level and quality are averaged.

## <span id="ddk_ksproperty_bda_sample_time_ks"></span><span id="DDK_KSPROPERTY_BDA_SAMPLE_TIME_KS"></span>


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
<td><p>Pin or Filter</p></td>
<td><p>KSP_NODE</p></td>
<td><p>LONG</p></td>
</tr>
</tbody>
</table>

 

Remarks
-------

The **NodeId** member of KSP\_NODE specifies the identifier of the control node or is set to −1 to specify a pin.

The returned value specifies the sample time in milliseconds.

Each time a client requests a signal statistics property, the node should report the average value for the last n milliseconds where n is the value indicated by KSPROPERTY\_BDA\_SAMPLE\_TIME. If no time value is set or if the driver does not support KSPROPERTY\_BDA\_SAMPLE\_TIME, the driver should default to a sample time of 100 milliseconds.

The driver can report time values for the most recently completed sample period.

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

[**KSPROPERTY\_BDA\_SIGNAL\_QUALITY**](ksproperty-bda-signal-quality.md)

[**KSPROPERTY\_BDA\_SIGNAL\_STRENGTH**](ksproperty-bda-signal-strength.md)

 

 






