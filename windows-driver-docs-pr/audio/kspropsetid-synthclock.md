---
title: KSPROPSETID\_SynthClock
description: KSPROPSETID\_SynthClock
ms.assetid: 8baad0d2-ea86-4d27-8fb0-03cdd9e978f0
keywords: ["KSPROPSETID_SynthClock"]
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
<td align="left"><p>[<strong>KSPROPERTY</strong>](https://msdn.microsoft.com/library/windows/hardware/ff564262)</p></td>
<td align="left"><p>ULONGLONG</p></td>
</tr>
</tbody>
</table>

 

The property value (operation data) is of type ULONGLONG and represents the master clock time. This time is specified in 100-nanosecond units.

### <span id="Return_Value"></span><span id="return_value"></span><span id="RETURN_VALUE"></span>Return Value

A KSPROPERTY\_SYNTH\_MASTERCLOCK property request returns STATUS\_SUCCESS to indicate that it has completed successfully. Otherwise, the request returns an appropriate error status code.

For more information, see [Master Clocks](https://msdn.microsoft.com/library/windows/hardware/ff567717).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[audio\audio]:%20KSPROPSETID_SynthClock%20%20RELEASE:%20%2811/22/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




