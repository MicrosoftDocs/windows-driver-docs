---
title: KSPROPERTY\_BDA\_SIGNAL\_QUALITY
description: Clients use KSPROPERTY\_BDA\_SIGNAL\_QUALITY to determine the amount of data successfully extracted from the signal as a percent.
ms.assetid: 8967400d-3a10-475a-997a-d756837c3438
keywords: ["KSPROPERTY_BDA_SIGNAL_QUALITY Streaming Media Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_BDA_SIGNAL_QUALITY
api_location:
- Bdamedia.h
api_type:
- HeaderDef
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# KSPROPERTY\_BDA\_SIGNAL\_QUALITY


Clients use KSPROPERTY\_BDA\_SIGNAL\_QUALITY to determine the amount of data successfully extracted from the signal as a percent.

## <span id="ddk_ksproperty_bda_signal_quality_ks"></span><span id="DDK_KSPROPERTY_BDA_SIGNAL_QUALITY_KS"></span>


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

The returned value specifies the data that is extracted from the signal as a percent.

The demodulation node typically reports signal quality, which is a representation of how much of the original data could be extracted from the signal.

In the case of analog signals, this percentage can be computed by examining the timing of horizontal sync (HSync) and vertical sync (VSync) as well as by looking at information contained in horizontal-blanking (HBlanking) and vertical-blanking (VBlanking) intervals.

In the case of digital signals, this percentage can be computed by examining packet cyclic redundancy checks (CRC) and forward error correction (FEC) confidence values as follows:

-   100 percent is ideal.

-   95 percent shows very little (almost unnoticeable) artifacts when rendered.

-   90 percent contains few enough artifacts as to be easily viewable.

-   80 percent is the minimum level to be viewable.

-   60 percent is the minimum level to expect data services, including receiving an electronic program guide (EPG), to work.

-   20 percent indicates that the demodulator is aware that a properly modulated signal exists but cannot produce enough data to be useful.

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

 

 






