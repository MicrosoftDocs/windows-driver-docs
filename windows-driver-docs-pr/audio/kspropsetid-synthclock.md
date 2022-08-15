---
title: KSPROPSETID\_SynthClock
description: KSPROPSETID\_SynthClock
keywords: ["KSPROPSETID_SynthClock"]
ms.date: 11/28/2017
---

# KSPROPSETID\_SynthClock


## <span id="ddk_kspropsetid_synthclock_ks"></span><span id="DDK_KSPROPSETID_SYNTHCLOCK_KS"></span>


The `KSPROPSETID_SynthClock` property set is used to get the master clock time for a DirectMusic synthesizer. This set contains a single property of a DirectMusic filter object. The DMus port driver implements the handler for this property.

For more information, see [Master Clocks](../stream/master-clocks.md) and [Synthesizer Timing](./synthesizer-timing.md).

Property items in this set are specified by KSPROPERTY\_SYNTHCLOCK enumeration values, as defined in header file Dmusprop.h.

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
<td align="left"><p><a href="/windows-hardware/drivers/stream/ksproperty-structure" data-raw-source="[&lt;strong&gt;KSPROPERTY&lt;/strong&gt;](../stream/ksproperty-structure.md)"><strong>KSPROPERTY</strong></a></p></td>
<td align="left"><p>ULONGLONG</p></td>
</tr>
</tbody>
</table>

 

The property value (operation data) is of type ULONGLONG and represents the master clock time. This time is specified in 100-nanosecond units.

### <span id="Return_Value"></span><span id="return_value"></span><span id="RETURN_VALUE"></span>Return Value

A KSPROPERTY\_SYNTH\_MASTERCLOCK property request returns STATUS\_SUCCESS to indicate that it has completed successfully. Otherwise, the request returns an appropriate error status code.

For more information, see [Master Clocks](../stream/master-clocks.md).
