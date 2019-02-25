---
title: KSPROPERTY\_BDA\_SIGNAL\_LOCKED
description: Clients use KSPROPERTY\_BDA\_SIGNAL\_LOCKED to determine whether a signal can be locked.
ms.assetid: 98023f83-2e90-4649-8e85-3e7b7f26b01d
keywords: ["KSPROPERTY_BDA_SIGNAL_LOCKED Streaming Media Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_BDA_SIGNAL_LOCKED
api_location:
- Bdamedia.h
api_type:
- HeaderDef
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# KSPROPERTY\_BDA\_SIGNAL\_LOCKED


Clients use KSPROPERTY\_BDA\_SIGNAL\_LOCKED to determine whether a signal can be locked.

## <span id="ddk_ksproperty_bda_signal_locked_ks"></span><span id="DDK_KSPROPERTY_BDA_SIGNAL_LOCKED_KS"></span>


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
<td><p>BOOL</p></td>
</tr>
</tbody>
</table>

 

Remarks
-------

The **NodeId** member of KSP\_NODE specifies the identifier of the control node or is set to −1 to specify a pin.

The returned value indicates whether a signal can be locked. Returns **TRUE** if a signal can be locked and **FALSE** otherwise.

If an RF tuner node returns **TRUE**, a phase-lock-loop (PLL) lock is typically indicated.

If a demodulator node returns **TRUE**, a signal quality of at least 20% is indicated.

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

 

 






