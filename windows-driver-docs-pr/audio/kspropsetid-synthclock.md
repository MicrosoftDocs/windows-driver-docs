---
title: KSPROPSETID\_SynthClock
description: KSPROPSETID\_SynthClock
ms.assetid: 8baad0d2-ea86-4d27-8fb0-03cdd9e978f0
keywords: ["KSPROPSETID_SynthClock"]
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# KSPROPSETID\_SynthClock


## <span id="ddk_kspropsetid_synthclock_ks"></span><span id="DDK_KSPROPSETID_SYNTHCLOCK_KS"></span>


The `KSPROPSETID_SynthClock` property set is used to get the master clock time for a DirectMusic synthesizer. This set contains a single property of a DirectMusic filter object. The DMus port driver implements the handler for this property.

For more information, see [Master Clocks](https://msdn.microsoft.com/library/windows/hardware/ff567717) and [Synthesizer Timing](https://msdn.microsoft.com/library/windows/hardware/ff538449).

Property items in this set are specified by KSPROPERTY\_SYNTHCLOCK enumeration values, as defined in header file Dmusprop.h.

## <span id="ddk_ksproperty_synth_masterclock_ks"></span><span id="DDK_KSPROPERTY_SYNTH_MASTERCLOCK_KS"></span>


### <span id="Usage_Summary_Table"></span><span id="usage_summary_table"></span><span id="USAGE_SUMMARY_TABLE"></span>Usage Summary Table

The KSPROPERTY\_SYNTH\_MASTERCLOCK property is used to get the master clock time.

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
<th align="left">Get</th>
<th align="left">Set</th>
<th align="left">Target</th>
<th align="left">Property descriptor type</th>
<th align="left">Property value type</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>Yes</p></td>
<td align="left"><p>No</p></td>
<td align="left"><p>Filter</p></td>
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff564262" data-raw-source="[&lt;strong&gt;KSPROPERTY&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff564262)"><strong>KSPROPERTY</strong></a></p></td>
<td align="left"><p>ULONGLONG</p></td>
</tr>
</tbody>
</table>

 

The property value (operation data) is of type ULONGLONG and represents the master clock time. This time is specified in 100-nanosecond units.

### <span id="Return_Value"></span><span id="return_value"></span><span id="RETURN_VALUE"></span>Return Value

A KSPROPERTY\_SYNTH\_MASTERCLOCK property request returns STATUS\_SUCCESS to indicate that it has completed successfully. Otherwise, the request returns an appropriate error status code.

For more information, see [Master Clocks](https://msdn.microsoft.com/library/windows/hardware/ff567717).

 

 





